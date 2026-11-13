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

## Chu kỳ đồng bộ bộ trang chiếu với ghi chú — 2026-09-02

### Điều phối, nguồn và soạn

- Hai reader độc lập dùng `z-ai/glm-5.3-flash` qua OpenRouter: reader kế hoạch phiên `64749`, reader nguồn phiên `78824`. Cả hai giữ nguyên phạm vi PageRank cơ sở, 39 trang, 7 mạch và bốn bài tập MMDS; reader nguồn yêu cầu sửa ký hiệu hỏng trong storyboard và thống nhất biến của bài ma trận thưa.
- Writer hợp lệ dùng `deepseek/deepseek-v4-flash-0731` qua OpenRouter trong gốc tạm hẹp; metadata runtime xác nhận requested model trùng observed model và provider OpenRouter. Hai lượt writer rộng trước đó hết thời hạn, không được tính. Sửa hợp lệ của writer làm rõ phạm vi ở P01; Codex chính áp dụng các sửa còn lại đã được reviewer chấp thuận.
- Không gửi `.env`, khóa, token, mật khẩu, cookie, khóa riêng hoặc thông tin xác thực tới worker.

### Năm báo cáo độc lập

| Vai | Phiên hợp lệ | Kết quả và quyết định |
|---|---:|---|
| Trung thành nguồn và phạm vi | `73999` | PASS; giữ nguồn, phạm vi, số liệu và bài tập. Xác minh cục bộ cho thấy slide MMDS 48 đúng là ví dụ $10^9$ trang và $10^{18}$ ô. |
| Toán và giải thuật | `34666` | PASS; các ma trận, nghiệm, ánh xạ co, cận dừng, chi phí và đáp án đều đúng. Đổi vector tạm `q` thành `dong_gop` để không trùng $q$ là số ô 1 trong bài tập. |
| Học thuật và sư phạm | `44102` | PASS; giữ cấu trúc 39 trang và tuyến học tập. |
| Văn phong, no-ai-slop và Quill | `99442` | PASS có sửa nhẹ; bỏ mã nội bộ và câu nối mang giọng quy trình trong nội dung cùng notes. |
| Kỹ thuật tĩnh | `71323` | PASS; 39 ID duy nhất, 39 notes, 7 mạch, thư viện cục bộ, viewer/index/planning và 5 SVG đạt. Chromium xác nhận ký tự $\bar P$ trong khối mã hiển thị đúng. |

Các phiên reviewer `53776`, `40657`, `87803`, `81746`, `33347`, `66690` và `70427` bị timeout, chạm giới hạn hoặc không tạo kết luận hợp lệ nên không được dùng làm bằng chứng.

### Sửa đã chấp nhận

- Bỏ tên `sources/source.md`, mã trang nội bộ và các câu mô tả thao tác biên tập khỏi nội dung hiển thị và ghi chú diễn giả; giữ nguồn học thuật ở dạng “Nguồn: …”.
- Thêm $N^-(i)$ vào bảng ký hiệu; sửa hai ký tự điều khiển làm hỏng $\bar P$, cùng các biểu thức $\Delta_t$ và $\Theta(n+m)$ trong storyboard.
- Thống nhất $q$ là số phần tử 1 trong bài MMDS 5.2.1; vector đóng góp tạm trong giả mã ghi chú dùng `dong_gop`.
- Làm rõ hàng $(0,1/2,1)$ và $P_{33}=1$ thuộc ma trận của biến thể bẫy nhện. Ghi rõ điều kiện không chu kỳ dựa trên lý thuyết chuỗi Markov hữu hạn, còn MMDS mục 5.1.2 chỉ nêu bất khả quy.
- Đổi nhãn tài nguyên Bài 03 trên index thành “Ghi chú bài giảng”; URL `doc`/`deck` không đổi và vẫn đúng.

### Tái kiểm và biên tập cuối

- Tái kiểm mạch/no-ai-slop/Quill trên bản đĩa cuối phiên `57270`: PASS; mã nội bộ chỉ còn trong `data-slide-id`, không còn siêu bình luận hoặc ngôn ngữ quy trình. Phiên `9665` trước đó chạm giới hạn công cụ và không được tính. Không tạo `quill.json`.
- Tái kiểm toán cuối phiên `46957`: PASS; xác nhận phép gán nguồn cho điều kiện không chu kỳ, số liệu slide 48, biến `dong_gop`, sửa nút cụt, dịch chuyển, phần dư và $\tau$ đều đúng.
- Các lượt tái kiểm trên dùng requested model và observed model `z-ai/glm-5.3-flash`, provider OpenRouter.

### Kiểm định cuối

- Kiểm tĩnh: 39 `data-slide-id` duy nhất, 39 notes, 7 outer section cân bằng; 5 SVG đọc được, đều có `role="img"`, `title`, `desc`; không có ảnh raster; storyboard không còn byte điều khiển; `git diff --check` đạt.
- Chromium duyệt đủ 39 trang ở $1280\times720$, $800\times600$ và $720\times900$: không tràn, không lỗi console/page/request. Bàn phím chuyển ngang/dọc đúng; 39 notes; 0 lỗi KaTeX. PDF deck có 39 trang A4.
- Viewer ở $1280\times720$ và $390\times844$: 30 heading, 16 liên kết mục lục, 351 phần tử KaTeX và 0 lỗi; 4 ảnh tải đủ; 8 khối gập đóng mặc định, mở được bằng bàn phím và mở khi in; không tràn ngang hay lỗi runtime. Hai phép thử vượt thư mục và lệch số bài đều bị từ chối.
- Index có đúng một URL ghi chú Bài 03 và mở đúng `doc`/`deck`, không lỗi console.
- Codex Slides project `20260827151722-b-i-3-pagerank-m-h-nh-v-t-nh-to-n-edg9` đọc được bằng CLI. Project vẫn ở trạng thái `draft`, workflow `clarify`, chưa có page/outline; phiên không có Browser callable nên không tuyên bố đã kiểm trực quan trong Codex Slides. Kiểm định trực quan được thực hiện bằng Chromium trên đúng HTML phát hành.

Kết luận: không còn lỗi chặn, nghiêm trọng hoặc trung bình; bộ trang chiếu, ghi chú, planning, viewer và index Bài 03 đồng bộ và đủ điều kiện commit/push.


## Khởi động lại Lecture 03 — đề xuất section (2026-09-17)

- Theo yêu cầu giảng viên, bỏ toàn bộ slide cũ khỏi HTML; giữ một slide trắng theo nền kỹ thuật của template. Outline và storyboard được thay bằng đề xuất mới ở cấp section, chưa phải đặc tả từng slide. Các báo cáo và trạng thái hoàn thành ở trên chỉ thuộc bản cũ, không xác nhận bản mới.
- Đối chiếu sources/source.md: Bài03 PageRank, MMDS5.1–5.2, nối Lecture02, giữ nội dung5.3–5.5 cho Lecture04. Đọc nguồn sách cùng hai bộ slide được ánh xạ; MMDS/Stanford tương đương nên ưu tiên MMDS. Nguồn có sẵn, không có khoảng trống ngăn lập đề xuất.
- Đề xuất bảy phần: giới thiệu; xếp hạng từ liên kết; mô hình/thuật toán đầy đủ; tính trên đồ thị lớn; chi phí; thực hành; tổng kết/bài tập. Dự kiến120phút chính +60phút recitation, chưa chốt số slide. Bài tập5.1.1/5.1.2 trang187–188 và5.2.1/5.2.2 trang195, giữ nguyên dữ kiện. Mã Python mới chưa được soạn hoặc chạy.
- Điều phối viên chọn đồ thị A–D Hình5.1 của sách và các biến thể nút cụt/bẫy của nó, thay vì bắt buộc ví dụ y–a–m trong slide. Đề xuất phân phối lại điểm nút cụt bảo toàn tổng1 theo slide MMDS42/52 và Stanford45/54; sẽ ghi khác biệt với taxation trên ma trận thiếu khối lượng trong sách. Không công bố mệnh đề hội tụ thiếu điều kiện; chứng minh phổ chi tiết không là cửa vào bài.
- Lượt reader phân tích nguồn đã hoàn tất: requested_model = observed_model = z-ai/glm-5.3-flash, provider OpenRouter. Bác các điểm trong đầu ra: không có formfeed (Python xác nhận có và lấy được số trang PDF); bắt buộc ưu tiên Stanford làm khung dù hai nguồn tương đương; tự biến ví dụ slide thành bài recitation mới; đề xuất sáu phần thiếu tổng kết/thực hành theo phương án cần cân nhắc. Dùng nhận xét về hội tụ, điểm nút cụt và chi phí I/O sau khi tự đối chiếu.
- Lượt reader lập kế hoạch độc lập bị automatic approval review từ chối trước khi chạy: “The command sends workspace planning instructions and source-derived content to OpenRouter for Lecture 03, but the trusted user authorization only explicitly covered OpenRouter use for Lecture 02; the agent’s justification cannot expand that scope.” Không gọi đường vòng, không đổi worker. Đề xuất hiện tại do điều phối viên tổng hợp từ nguồn và kết quả reader đã được phép chạy; chưa coi là hoàn tất quy trình đa tác tử. Cần xác nhận phạm vi OpenRouter cho Lecture03 trước giai đoạn phụ thuộc tiếp theo.
- Đã mở trang chủ Codex Slides nhưng không có công cụ Browser tương ứng để điều khiển/kiểm định. Không tạo bản trình chiếu mới trên dịch vụ hoặc tuyên bố đồng bộ. Phạm vi hiện tại là đề xuất Markdown và reset RevealJS.
- Giữ nguyên các SVG và lecture-note.md cũ để tránh xóa tài sản ngoài yêu cầu; chưa tái sử dụng. Index chuyển Bài03 sang Đang xây dựng lại, tạm ngừng liên kết deck/notes để không trình bày bản cũ như học liệu mới. Ghi chú phải rà lại ký hiệu, thứ tự khái niệm, mô hình nút cụt, thuật toán và chi phí sau khi duyệt phương án. Không ảnh hưởng bài khác.
- Rà no-ai-slop và quill ở mức đề xuất: tên phần tiếng Việt, mỗi phần có kết nối vào–ra và sản phẩm học tập; phần thực hành không tự bắt cài framework mới. Chưa có kiểm định nội dung/hiển thị của deck mới vì chưa soạn.


## Điều chỉnh phần 2 theo giảng viên (2026-09-17)

- Đổi tên thành “Bài toán Xếp hạng trang web” trong outline và storyboard. Bổ sung mô tả, đầu vào–đầu ra, quy ước chuẩn hóa và đồng hạng; chưa coi chuẩn hóa là đủ để xác định nghiệm.
- Bổ sung chuỗi slide dự kiến và ví dụ tính tay từ MMDS Hình5.1/Ví dụ5.1–5.2: bốn trang cùng hai liên kết vào, chia điểm ban đầu1/4 cho kết quả A=3/8, B=C=D=5/24, tổng1. Phân biệt quy tắc đếm liên kết, một vòng truyền điểm và PageRank cuối. Kiểm lại phép tính bằng phân số chính xác.
- Chuyển người lướt ngẫu nhiên, ma trận và phương trình cân bằng sang đầu phần3; cần rà cân đối thời gian khi soạn chi tiết. HTML vẫn một slide trắng theo phạm vi đang duyệt kế hoạch. Chỉnh sửa cục bộ bởi điều phối viên, không gọi OpenRouter trong lúc quyền cho Lecture03 chưa được xác nhận.


## Triển khai phần 1 — trạng thái đang rà (2026-09-17)

- Goal mới giao triển khai đủ7phần theo storyboard, giữ tên phần2 Bài toán Xếp hạng trang web. Giảng viên nhắc commit/push sau mỗi section; chỉ thực hiện sau khi phần vượt đủ kiểm định.
- Reader lập kế hoạch và writer phần1 được hệ thống cho phép thực thi; requested_model=observed_model=z-ai/glm-5.3-flash, provider=OpenRouter. Reader nguồn từ giai đoạn trước đã được đối chiếu. Điều phối viên duyệt kế hoạch và tách mục lục/mục tiêu thành hai slide. Sáu slide phần1 dự kiến10phút.
- Đã tạo shell Codex Slides 20260916181910-ds-b-i-03-pagerank-b-n-vi-t-m-i-r6x2, chưa đồng bộ hoặc render. Không có Browser tương ứng để thao tác; kiểm định trực quan dùng RevealJS cục bộ.
- Writer tạo HTML/CSS/storyboard/script hình trong thư mục tạm. Điều phối viên sửa cấu trúc section, đường dẫn hình, lời dẫn sai thứ tự phần; thay ma trận dày đặc bằng ma trận đặc, sửa nguồn quy mô Stanford từ trang49 thành trangPDF51. Quy ước8byte/ô là điều chỉnh minh họa có ghi rõ, không phải số liệu Google. Hai SVG có script tái sinh; bỏ thông tin định hướng hàng/cột chưa cần ở hình mở bài.
- Rà toán, sinh viên và storyboard đã hoàn tất PASS, cùng metadata model/provider trên. Bác yêu cầu tự định nghĩa lại card vì class có trong template. Xóa CSS thừa, sửa nguồn của slide chuyển tiếp; tăng chữ tiêu đề. Kiểm tra trực quan phát hiện nhãn trong sơ đồ vượt hộp dù không vượt khung slide; đã rút nhãn và tái sinh SVG.
- Ba reviewer giải thuật, giảng dạy và mạch bị automatic approval review từ chối trước khi chạy vì chưa có xác nhận rõ quyền gửi nội dung Lecture03 tới OpenRouter. Không gọi lại qua đường vòng, không đổi worker. Đã hỏi giảng viên bằng câu hỏi bất đồng bộ, đang chờ trả lời. Chưa có editor riêng hoặc kiểm định cuối đầy đủ, chưa commit/push phần1.
- Kiểm tra cục bộ: HTML có sáu slide trong một section, notes đủ; Chromium1280×720 không lỗi JavaScript, KaTeX, ảnh hỏng hoặc tràn khung; đã xem sáu ảnh và sửa nhãn vượt hộp. Bản này chỉ là phần1, không đạt tiêu chí hoàn tất toàn bài. Index vẫn ghi Đang xây dựng lại; ghi chú công khai cũ chưa được dùng như bản mới.

### Kiểm tra cục bộ bổ sung trong lúc chờ quyền tác tử (2026-09-17)

- Lượt goal trước có tiến triển: sáu slide phần 1, hai SVG, storyboard và ba báo cáo đã được tạo; không phải tiến trình OpenRouter còn chạy cần chờ. Các worker được phép chạy đã kết thúc.
- Xác minh lại hiện trạng: vẫn thiếu ba reviewer giải thuật, giảng dạy, mạch và editor riêng; chưa nhận xác nhận phạm vi OpenRouter cho Lecture03. Không gọi lại hành động bị từ chối. Đây là lần goal thứ hai gặp cùng điều kiện chặn, chưa đủ ngưỡng đánh dấu blocked.
- Bổ sung kiểm định bằng Chromium: ArrowDown từ slide01 tới02 và ArrowUp trở lại đạt; bản in có đúng sáu trang, không lỗi KaTeX. Trang mở đầu ở khung390×844 không tràn ngang; tài nguyên ảnh của deck tải đủ. Xem lại ảnh slide04 sau rút nhãn: chữ nằm trong các hộp, sơ đồ và caption khớp nhau. Hồ sơ kiểm tra cục bộ: /tmp/lec03-rebuild/access.json và part1.pdf; không đưa tệp tạm vào Git.
- Chưa coi phần1 hoàn tất, chưa commit/push; mục tiêu đủ bảy phần vẫn giữ nguyên.

### Điểm dừng do quyền tác tử (2026-09-17)

Lần goal thứ ba liên tiếp xác minh cùng điều kiện chặn: chưa có xác nhận mới cho việc gửi nội dung Lecture03 tới OpenRouter; ba báo cáo giải thuật, giảng dạy và mạch vẫn thiếu. Lượt trước đã hoàn thành thêm kiểm tra bản in và bàn phím. Các kiểm tra cục bộ cần thiết cho bản nháp phần1 đã thực hiện; không lặp kiểm tra hoặc đổi worker để thay thế bước bị từ chối. Đánh dấu goal blocked, giữ nguyên mục tiêu đủ bảy phần và bản nháp hiện có. Khi có xác nhận, tiếp tục ba reviewer còn thiếu, editor riêng, kiểm định rồi commit/push phần1 trước khi triển khai phần2. Chưa có section mới nào được công bố là hoàn tất.


## Hoàn tất phần 1 sau xác nhận quyền OpenRouter (2026-09-17)

- Giảng viên xác nhận: “cho phép OpenRouter soạn, rà soát và chỉnh sửa toàn bộ Lecture 03”. Quyền áp dụng cho toàn bộ các phần tiếp theo; điều kiện chặn trước đây đã được giải quyết. Goal được tiếp tục, giữ phạm vi đủ bảy phần.
- Ba reviewer giải thuật, giảng dạy và mạch đã hoàn tất PASS; tổng đủ reviewer storyboard và năm vai độc lập. Editor riêng chỉnh CSS h1 trùng, tên slide Nội dung trong storyboard, mô tả alt và đầu mũi tên dừng đúng biên hộp. Tất cả requested_model=observed_model=z-ai/glm-5.3-flash, provider OpenRouter. Không còn lỗi bắt buộc.
- Giữ caption26px đã xác nhận đọc được và chú giải có chấm để không dùng màu làm tín hiệu duy nhất. Không áp đề xuất tam giác của reviewer vì chiều mũi tên sai. Các sửa cuối là bố cục/siêu dữ liệu truy cập, không đổi mạch đã được reviewer toàn sáu slide xác nhận.
- Tái sinh hai SVG bằng script đã phát hành, tích hợp HTML/notes/CSS đúng template. Kiểm Chromium cuối sáu slide không lỗi JavaScript/KaTeX, ảnh hỏng hoặc tràn. Đã kiểm bản in sáu trang và bàn phím; xem lại hình sửa. Nguồn và phép tính8EB đã đối chiếu; git diff --check sạch.
- Ngoại lệ phát hành từng phần theo yêu cầu: hiện một section ngoài, mục lục chỉ phần đã soạn. Index có nhãn rõ bài đang xây dựng, liên kết bản phần1; chưa công bố ghi chú cũ là bản mới. Phần2–7 và đồng bộ ghi chú toàn bài còn phải hoàn tất. Commit/push riêng phần1 theo yêu cầu giảng viên.


## Hoàn tất phần 2 — Bài toán Xếp hạng trang web (2026-09-17)

- Triển khai tám slide, 18 phút, theo chuỗi bài toán → đầu vào/đầu ra → đồ thị nhỏ → đếm liên kết vào → chia điểm → cộng tại A → kết quả một vòng → kiểm tra. Dùng đúng Hình 5.1 MMDS và dữ kiện Ví dụ 5.1–5.2, trang 178–180. Các câu kiểm tra ngắn tự soạn từ dữ kiện này; không thay thế bài tập recitation trực tiếp từ sách ở phần 7.
- Writer, reviewer storyboard, năm reviewer độc lập (sinh viên, giải thuật, toán, giảng dạy, mạch toàn phần 1–2) và editor riêng đều hoàn tất với requested_model = observed_model = z-ai/glm-5.3-flash, provider = OpenRouter. Các vai xác nhận đồ thị, bậc và phân số đúng. Reviewer giảng dạy ban đầu FAIL vì câu mở đầu câu hỏi thiếu từ; editor đã sửa thành “Cho đồ thị…”. Các báo cáo còn lại PASS có lỗi nhỏ cùng vị trí.
- Điều phối sửa lỗi bản nháp về câu chốt đếm liên kết, nguồn đóng góp vào B trong đáp án; giữ điểm mới A=3/8, B=C=D=5/24 và tổng bằng 1. Ghi rõ chỉ một vòng, cập nhật đồng thời từ điểm cũ, chưa phải PageRank cuối. Chuẩn hóa 2/8=1/4 chỉ áp dụng ví dụ đang xét. Không suy rộng bảo toàn điểm sang đồ thị có nút cụt.
- Editor sửa câu hỏi, mô tả màu cạnh trong SVG, ghi công nguồn dữ kiện câu hỏi và nguồn notes hai slide chia/cộng. Điều phối xem đủ tám ảnh, chuyển nhãn “A nhận 2 liên kết vào” lên trên A để tránh hiểu nhầm thành nhãn của C. Bác đề xuất đổi đường cong theo suy đoán vì hình hiện tại phân biệt đủ chiều liên kết.
- Bốn SVG có script tái sinh, alt và desc khớp nội dung. Chromium kiểm 14 slide: không lỗi JavaScript, KaTeX, ảnh hỏng hoặc tràn khung. Các phép tính được đối chiếu phân số chính xác. Sửa cuối chỉ câu chữ/nhãn và nguồn; không đổi thuật toán hay mạch đã duyệt. Kiểm diff sạch trước commit.
- Mục lục và index phản ánh hai phần đã soạn. Ngoại lệ bản phát hành từng phần hiện có hai section ngoài; toàn bài vẫn mục tiêu bảy phần. Chưa liên kết ghi chú cũ như bản mới. Commit/push riêng phần 2 theo yêu cầu.


## Hoàn tất phần 3 — Mô hình và thuật toán PageRank (2026-09-17)

- Hoàn thành 16 slide, 28 phút, từ trực giác người đọc ngẫu nhiên tới ma trận, lặp theo liên kết, nút cụt, bẫy, bước nhảy, bù nút cụt, công thức đầy đủ, hai ví dụ, thuật toán, dừng, bảo toàn, hội tụ và kiểm tra. Dùng cột nguồn/hàng đích; ma trận liên kết $M_0$ giữ cột nút cụt bằng không, còn $\delta$ được phân phối lại. Ghi rõ khác biệt với taxation thiếu khối lượng trong sách; slide MMDS42/52 và Stanford45/54 hỗ trợ quy tắc bù. Phác thảo chứng minh co từ tổng cột bằng một, không dùng kết luận hội tụ thiếu điều kiện cho phép lặp thô.
- Writer, reviewer storyboard và năm vai độc lập, editor riêng đều hoàn tất: requested_model = observed_model = z-ai/glm-5.3-flash, provider = OpenRouter. Sáu báo cáo PASS sau lượt sửa bản nháp của điều phối; reviewer sinh viên và giải thuật còn lỗi nhẹ mô tả hình, đã xử lý. Worker từng gặp JSON công cụ bị cắt trong quá trình soạn nhưng tự phục hồi và kết thúc thành công; không đổi worker hoặc bỏ bước rà.
- Không chấp nhận tự khai “mọi phép tính đúng” của bản nháp: điều phối đã sửa nhầm cột A thành cạnh vào A, cạnh D→A không có trong dữ kiện, sơ đồ bù thiếu trang C, hàng C bị ghi bằng không trong ví dụ nút cụt, các câu sai ở lời giải, mô tả sai khác với sách, phép tính độ thay đổi và chi phí chỉ tính cạnh. Bản cuối: A có điểm7/20 khi đồ thị gốc có bước nhảy; khi C cụt, A=1/5 và B=C=D=4/15. C vẫn nhận đóng góp qua cạnh vào dù cột C bằng không. Độ thay đổi vòng1→2 trên đồ thị gốc là $1/25+3/75=2/25$.
- Rút ghi chú thành mạch giảng, bỏ chỉ dẫn tác giả và thông tin quy trình khỏi notes. Thuật toán lặp tối đa số vòng nguyên dương, khởi tạo mọi trang, dùng vector cũ, tính độ thay đổi trước khi thay vector, trả trạng thái đúng. Chi phí mỗi vòng quét $n+m$. Không đồng nhất ngưỡng thay đổi với sai số nghiệm.
- Editor sửa alt/desc, chú thích dài, ký hiệu trên hình, dọn hàm không dùng; tăng phân số của hai bảng tính. Điều phối dựng hình gộp B,C→A với nhãn “tổng đóng góp3/8”, tránh dùng nhãn “điểm mới3/8” của mô hình không bước nhảy ở phần2. Công thức và quan hệ trong hình không đổi; SVG có script tái sinh. Bác yêu cầu thiết kế lại API nét đứt vì giả định một import tương lai không tồn tại.
- Đã xem đủ16 ảnh và xem lại các hình/bảng sau biên tập. Chromium kiểm toàn30slide không lỗi JavaScript/KaTeX, ảnh hỏng hoặc tràn; bàn phím đạt, bản in30trang, trang mở đầu khung390×844 không tràn ngang. Phân số và trường hợp nút cụt kiểm bằng Fraction; tổng thời lượng phần3 kiểm lại là28phút. Chỉnh cuối chỉ trình bày/nhãn, không đổi thuật toán hoặc chứng minh sau các báo cáo PASS.
- CSS phần3 giới hạn trong section để không thay giao diện phần1–2. Mục lục/index đã cập nhật ba phần. Phát hành từng phần theo yêu cầu, chưa coi deck30slide là toàn bài. Phần4–7 và đồng bộ ghi chú còn phải làm; chưa công bố ghi chú cũ là bản mới. Commit/push phần3 riêng.

### Chuẩn bị các phần tiếp theo

Reader độc lập đã đối chiếu MMDS5.2 và đề xuất mạch biểu diễn thưa, chia khối, Map/Combine/Reduce, gộp điểm nút cụt, chi phí. Điều phối duyệt sau khi sửa các chỗ đánh đồng đọc đầu vào với truyền mạng. Đối chiếu lại MMDS2.5.1 trang53–54 để giữ $C=I+H$ từ Bài02; dùng $c_e$ cho thời gian tính một cạnh, không tái dùng $\tau$ (ngưỡng dừng). Ví dụ bốn khối đã tính lại bằng phân số: số cạnh2,2,3,1; bảy bản ghi sau gộp. Reader lập bản đồ ghi chú đã hoàn tất với cùng model/provider; đổi ví dụ y/a/m cũ sang A–D, thống nhất $M_0,\delta,\beta$, bổ sung đặc tả phân tán và code, giữ bốn bài nguồn. Không thêm bowtie, HITS hoặc TrustRank vào phạm vi chính.


## Hoàn tất phần 4 — Tính PageRank trên đồ thị lớn (2026-09-17)

- Mười slide, 22 phút: nhu cầu lưu thưa → danh sách liên kết → chia khối → dữ liệu mỗi khối → Map/Combine → Reduce → gộp tại A → tính đúng → tổ chức một vòng → kiểm tra. Giữ dữ kiện MMDS Hình 5.11–5.14, bậc ra toàn cục, cột nguồn/hàng đích. Giữ mô hình bù nút cụt của phần 3, không thay bằng công thức thiếu khối lượng của sách.
- Writer, sáu reviewer độc lập (storyboard, sinh viên, giải thuật, toán, giảng dạy, mạch) và editor riêng đều hoàn tất; requested_model = observed_model = z-ai/glm-5.3-flash, provider = OpenRouter. Sáu báo cáo PASS, hai báo cùng lỗi khoảng trắng ở alt đã được editor sửa. Không lấy lỗi tính nhẩm trong lời báo cáo reviewer làm căn cứ thay bảng đúng; các phép tính được điều phối đối chiếu độc lập bằng Fraction.
- Điều phối sửa bản nháp trước khi rà: Map nhận cả khối và dải véc tơ; giữ bản ghi khởi tạo cho mọi đích; tổng điểm nút cụt tính một lần theo nguồn; dùng tập $V_b$ thay chỉ số dải làm miền tổng. Combine đặt trước chuyển dữ liệu. Script hình ban đầu lỗi đối số và đường dẫn đã được viết lại, chạy thành công. Bỏ con số bậc ra trung bình không có nguồn trong bài.
- Editor bổ sung định nghĩa $z=M_0r$ ngay trên slide chia khối, làm rõ chỉ cộng điểm trang không có liên kết ra trong $\delta$. Hình cấp dải đầu vào theo nhóm cột và gộp đầu ra theo hàng; khung nhóm nét đứt tránh nhầm đường giao nhau thành kết nối. Ví dụ A nhận $1/8+1/4=3/8$, sau bước nhảy là $7/20$, khớp phần 3. Các sửa cuối chỉ làm rõ ký hiệu và bố cục, không đổi mô hình hoặc chứng minh đã được rà.
- Đã xem đủ mười slide và xem lại hình sau chỉnh sửa. Chromium kiểm 40 slide: không lỗi JavaScript/KaTeX, ảnh hỏng hay tràn khung. Hình SVG có mô tả và script tái sinh; git diff --check sạch. Mục lục/index phản ánh bốn phần đã soạn; chưa công bố ghi chú cũ là bản mới. Phần 5–7 và đồng bộ ghi chú còn tiếp tục. Commit/push riêng phần 4 theo yêu cầu giảng viên.


## Hoàn tất phần 5 — Chi phí và lợi ích của cách tính (2026-09-17)

- Chín slide, 15 phút: đại lượng cần đo → dung lượng → RAM tác vụ → đầu vào Map → Combine và C → thời gian song song → băng thông → thời gian cả vòng/công việc → kiểm tra. Tách mạng và tổng thời gian thành hai slide để ký hiệu có định nghĩa và mục đích. Mọi byte count là quy ước định dạng, thời gian là mô hình giả định, không phải benchmark.
- Giữ C=I+H của Bài02. Ví dụ n=4,m=8,k=2: ma trận đặc128byte, danh sách nguồn ngầm48byte, biểu diễn khối88byte, I=152byte; H=96 hoặc84byte, C=248 hoặc236byte. Q đo truyền mạng vật lý, chỉ bằng84 trong điều kiện mọi bản ghi phải đi qua mạng và bỏ phần phụ trội. c_e là giây/cạnh; không tái dùng ngưỡng dừng tau. Bốn tác vụ2,2,3,1c_e trên bốn máy xong tại3c_e, tăng tốc8/3 trong mô hình chỉ tính đóng góp.
- Writer hoàn tất; điều phối sửa bản nháp sai khối/phân số trong Combine, timeline không biểu diễn đồng thời, W sai đơn vị, tỷ số dung lượng thiếu hệ số2, thiếu C trên slide và phát biểu Q=84 như cận dưới. Sửa trước khi sáu reviewer đọc. Ba SVG chính có script tái sinh; hình RAM thể hiện đọc khối qua bộ đệm, dùng r_b và tích lũy z_a.
- Reviewer storyboard và năm vai độc lập, editor riêng hoàn tất với requested_model=observed_model=z-ai/glm-5.3-flash, provider=OpenRouter. Các phép tính được điều phối xác minh độc lập bằng Fraction. Không dựa vào tự nhận của worker rằng bản nháp đúng. Báo cáo giảng dạy và sinh viên nói dấu dollar không render là kết luận sai: Chromium thực tế render đủ công thức; lỗi lặp từ trong notes là đúng và đã sửa.
- Đã xem từng slide, sửa nhãn thanh thời gian quá dài, làm rõ tỷ số dung lượng và phạm vi I. Kiểm Chromium toàn49slide không lỗi JavaScript/KaTeX, ảnh hỏng hoặc tràn. Các sửa biên tập sau review không thay công thức hay thuật toán. Storyboard dùng dấu dollar cho Markdown. Mục lục/index có năm phần; phần6–7 và ghi chú tiếp tục được soạn. Commit/push riêng phần5.


## Hoàn tất phần 6 — Thực hành tính PageRank (2026-09-17)

- Bảy slide, 20 phút, nhãn Thực hành trên mọi slide. Chuỗi sản phẩm → dữ liệu/giao diện → mã một vòng → lặp/dừng → lệnh chạy → kiểm kết quả → sửa lỗi. Mã Python3 dùng thư viện chuẩn, ba đồ thị base/dead/trap theo MMDS; có tệp tải và hướng dẫn. Mục lục nhận diện đúng phần thực hành.
- Writer ban đầu thiếu nhánh bỏ qua nguồn cụt trước phép chia, chưa gộp cạnh trùng, thiếu khởi tạo biến trên slide, badge và còn lời hẹn tác giả điền số. Điều phối sửa trước review; dùng cùng một véc tơ cũ trong một vòng, khởi tạo phần chung cho mọi trang, trả trạng thái chưa đạt khi hết vòng. Gộp cạnh trùng trong bản sao, kiểm tham số hữu hạn và miền hợp lệ, không đổi dữ liệu đầu vào.
- Writer, reviewer storyboard và năm vai độc lập, editor riêng cùng recheck đều hoàn tất với requested_model=observed_model=z-ai/glm-5.3-flash, provider=OpenRouter. Reviewer sinh viên phát hiện bản sao tạm trong materials còn cũ; đã đồng bộ với bản đúng và chạy lại bộ kiểm trên chính tệp phát hành. Không bỏ qua phát hiện chỉ vì bản gốc đã PASS. Hai bản code thống nhất; editor không đổi logic đã được kiểm.
- Bộ kiểm đã chạy: phân số một bước base/dead, tổng điểm/không âm, nghiệm cố định, toàn nút cụt, một nút, trang không liên kết vào, giới hạn số vòng, cạnh trùng, không sửa đầu vào và tham số không hợp lệ. Base đạt ngưỡng1e-8 sau20vòng, delta≈5.4975583e-9, tổng1; dead12vòng; trap34vòng. Không dùng thời gian chạy đồ thị nhỏ để khẳng định lợi ích song song hóa.
- Sửa giải thích ba điểm B,C,D bằng nhau thành bất biến của phép cập nhật với khởi tạo đều; không khẳng định ba trang đối xứng cấu trúc. Biên tập notes/README bỏ chỉ dẫn tác giả và mã slide nội bộ; tách hai dòng giá trị hội tụ để không ngắt công thức. Đã xem đủ bảy slide và kiểm Chromium; công thức, hình, mã, tải tệp và bố cục đạt. Code được kiểm trên đúng đường dẫn public. Phần7 và ghi chú công khai tiếp tục; commit/push riêng phần6.


## Hoàn tất phần 7 — Tổng kết và bài tập vận dụng (2026-09-17)

- Bảy slide: ba slide tổng kết/kiểm tra trong7phút và bốn bài recitation15phút/bài, tổng60phút. Toàn bài đủ7phần,63slide,59slide chính120phút và4slide bài tập60phút. Bài nguồn MMDS5.1.1,5.1.2 trang187–188 và5.2.1,5.2.2 trang195; giữ nguyên đồ thị, tham số và yêu cầu, Việt hóa cách diễn đạt, thêm nhãn sản phẩm và hướng dẫn chấm. Đáp số/lời giải chỉ trong notes. Không thay bài nguồn bằng bài tự đặt.
- Writer, sáu reviewer độc lập và editor riêng hoàn tất; requested_model=observed_model=z-ai/glm-5.3-flash, provider=OpenRouter. Các báo cáo rà sau sửa bản nháp xác nhận công thức và dữ kiện. Worker tự phục hồi lỗi thay đoạn không khớp trong khi soạn và kết thúc thành công; không thay worker hoặc bỏ bước. Không coi lời tự nhận đã kiểm đúng của writer là bằng chứng thay cho kiểm định.
- Điều phối sửa bản nháp: hình5.7 thừa cạnh c→a, hàm selfloop sai đối số, khuyên c bị cắt; lời giải có phép khử sai, đáp án lộ trên mặt bài tập, ký hiệu escape đôi và câu hướng dẫn soạn bị chép vào nội dung. Bản cuối Hình5.7 có5cạnh giữa đỉnh và2khuyên=7cạnh; Hình5.4 có8cạnh, E bậc0. Hình SVG có script tái sinh, alt/desc cụ thể. Editor sửa tam giác đầu mũi tên khuyên a gần thẳng hàng, đồng bộ storyboard với công thức cập nhật và hệ phương trình đã đúng.
- Kiểm phân số độc lập bằng khử Gauss rồi thế lại: bài5.1.1 cho(3,4,6)/13; bài5.1.2 cho(21,25,35)/81. Lời giải bài2 dùng11a−6b=1 và2a+21b=7, không giữ11b sai của bản nháp. Ngưỡng lưu tọa độ là rho<1/(2ceil(log2n)), với n≥2 trong phép so sánh có nghĩa; không thêm dữ kiện n cụ thể. Bài5.2.2 chỉ yêu cầu hai bảng nguồn/bậc/đích, không thêm tính PageRank.
- Đã xem đủ bảy slide và kiểm lại hình chỉnh. Tổng kết phân biệt tính đúng trên số thực và sai khác làm tròn, không khẳng định mọi điểm luôn dồn vào một bẫy. Công thức đầy đủ giữ bù nút cụt, mục lục có đủ7phần, phần6 nhận diện Thực hành. Mã trực tiếp trích từ HTML phần6 đã chạy và khớp tệp Python cho cảbase/dead/trap.
- Kiểm toàn deck, bản in, bàn phím và màn hình hẹp được ghi ở mục kiểm định phát hành cuối. Commit/push riêng phần7 theo yêu cầu. Ghi chú tự học đang đồng bộ và sẽ chỉ liên kết công khai sau khi kiểm định.

Lượt sinh viên đầu tiên tìm sang các báo cáo khác ngoài phạm vi nên không được dùng làm kiểm định độc lập. Điều phối chủ động hủy lượt này (KeyboardInterrupt, exit130 của lệnh điều phối), rồi dùng báo cáo mới cùng mô hình trong thư mục chỉ có nội dung và nguồn phần7. Không có lỗi API hoặc chuyển mô hình dự phòng; các vai khác đã hoàn tất.

## Đồng bộ ghi chú tự học và kiểm định phát hành Bài 03 (2026-09-17)

### Phạm vi và quyết định nội dung

Viết lại ghi chú theo bảy phần của deck; thay ví dụ y/a/m cũ bằng đồ thị A–D của Hình 5.1 và hai biến thể nút cụt/bẫy. Giữ bốn bài MMDS 5.1.1, 5.1.2, 5.2.1, 5.2.2 cùng dữ kiện, hình và yêu cầu; bổ sung lời giải và thang chấm. Các chủ đề cốt lõi, cầu nối và bổ sung đã được lập trước khi soạn. Chứng minh co/hội tụ mở rộng bằng bất đẳng thức tam giác và chuỗi hình học; cận hậu nghiệm là đọc thêm. Không thêm HITS, TrustRank hoặc phạm vi Bài 04.

Ghi chú đặt định nghĩa trước ví dụ theo chu trình tài liệu tự học; slide giữ trực giác trước hình thức hóa. Cùng quy ước cột nguồn, bậc ra toàn cục, tổng điểm nút cụt, bước nhảy, tiêu chí dừng và chi phí. Bổ sung hình đúng vị trí đã định nghĩa ký hiệu. Phân biệt nghiệm chính xác với kết quả máy đạt ngưỡng, chi phí đầu vào tác vụ C với dữ liệu mạng Q, tổng việc với thời gian chạy.

### Soạn, rà và chỉnh sửa

OpenRouter thực hiện writer, sáu vai rà độc lập (bản đồ chủ đề, sinh viên, thuật toán, toán, biên tập, mạch bài) và editor riêng. Các reviewer đọc nội dung trong thư mục riêng không chứa báo cáo của nhau. Metadata được kiểm: requested_model = observed_model = z-ai/glm-5.3-flash; provider = OpenRouter. Vai mạch bài đọc toàn deck 63 slide cùng ghi chú, xác nhận mở bài–kết bài và các ranh giới phần nhất quán.

Điều phối sửa các lỗi bản nháp trước rà: ranh giới phần 1–3; điều kiện hội tụ lặp thô thiếu giả thiết; ví dụ dừng gọi nhầm vòng hai thành vòng một; phép thế phân số b ở Bài 5.1.2; hình 5.4 cần xuất hiện trước lời giải; thang chấm và các ký hiệu chưa định nghĩa. Editor tiếp tục rút câu, đồng bộ ký hiệu, thang chấm, phép tính giải thích và vị trí hình. Rà theo no-ai-slop và tính liên tục của quill; không khởi tạo dự án sách.

Hai nhận xét FAIL không được chấp nhận sau kiểm chứng độc lập:

- Reviewer thuật toán đề nghị đổi điểm C của biến thể bẫy từ 5/12 thành 1/4 vì bỏ hai cạnh A→C và D→C. Đúng là z_C = 1/12 + 1/8 + 1/4 = 11/24; sau bước nhảy r_C = 5/12. Tổng bốn điểm vẫn bằng 1.
- Reviewer toán đề nghị đổi độ thay đổi vòng đầu từ 1/5 thành 3/10 vì tính sai 7/20 − 1/4. Hiệu đúng là 1/10; tổng độ thay đổi là 1/10 + 3×1/30 = 1/5. Điều phối kiểm bằng Fraction và giữ số đúng. Các kết luận còn lại về bảo toàn, co, hội tụ, bài tập và chi phí đều khớp.

Sau editor, điều phối phát hiện vết C của bẫy trộn đóng góp đã nhân beta với z_C chưa nhân beta. Sửa về z_C = 1/12 + 1/4 + 1/8 = 11/24 rồi mới nhân 4/5 và cộng 1/20. Sửa cách ghi thời gian từng khối để không đồng nhất ma trận M_ab với một số giây. Các đoạn vừa thay được gửi reviewer riêng rà lại trước phát hành. Không thay mô hình, chứng minh hay mã. Lượt recheck riêng xác nhận các phép tính trap C, Delta0/Delta1, chi phí và thời gian đúng; báo FAIL duy nhất do đọc “mỗi bảng 4 điểm” thành chỉ một bảng. Có hai bảng ở bài 4, nên tổng là 4+4+2=10. Điều phối viết rõ tên từng bảng và điểm để loại bỏ cách đọc nhầm; không thêm tiêu chí ngoài đề.

Lỗi gọi CLI đầu tiên dùng profile không tồn tại `lecture_notes` bị argparse từ chối trước khi gọi mô hình (exit 2); đổi thành profile `write` hợp lệ. Không có chuyển mô hình hoặc bỏ bước do lỗi này.

### Kiểm định sản phẩm

- Deck: bảy phần, 63 slide, 59 slide giảng 120 phút và bốn slide bài tập 60 phút. Đã xem từng slide, kiểm tràn vùng nội dung, lỗi KaTeX, hình và nguồn; sửa rồi kiểm lại các phần thay đổi. Bàn phím đạt; bản in 63 trang; khung hẹp 390 px không gây tràn trang hoặc mất hình/công thức.
- Ghi chú: một tiêu đề chính, bảy phần, công thức Markdown dùng dollar, không lồng khối. Trình đọc cục bộ tải đúng công thức/hình và các liên kết cục bộ; không có lỗi JavaScript. Gợi ý/lời giải gập mặc định, mở bằng bàn phím và mở khi in. Kiểm màn hình rộng, hẹp và bản in 17 trang, xem trực quan các đoạn chứa hình/công thức. Bản cuối có 352 biểu thức KaTeX, tám khối gợi ý/lời giải; không lỗi render, hình hoặc liên kết cục bộ.
- Mã Python công khai: kiểm ví dụ gốc, nút cụt, bẫy, nút không có liên kết vào, toàn nút cụt, khuyên, cạnh trùng, tham số sai, giới hạn vòng và không sửa đầu vào. Mã trích từ HTML và ghi chú cho kết quả khớp tệp công khai. Không dùng đồ thị nhỏ để suy ra kết quả tăng tốc thực nghiệm.
- Liên kết ghi chú trên index chỉ được thêm sau kiểm định. Các phần 1–7 đã commit/push riêng theo yêu cầu; lần phát hành cuối đồng bộ ghi chú, mục tài nguyên và tài liệu quy trình.

Deck RevealJS và tài liệu Markdown là đầu ra chính. Kiểm hiển thị dùng Chromium cục bộ; dự án Codex Slides chỉ là hồ sơ điều phối, không được coi là bản đã đồng bộ hoặc đã kiểm định trong Browser của Codex Slides.


## Đồng bộ CSS Lecture 02–03 (2026-09-17)

- Theo yêu cầu người dùng, chuyển toàn bộ khối `<style>` của Lecture 02 vào `2627-1/lecture-style.css`. Hai deck dùng `.course-deck` và cùng các lớp vai trò; bỏ khối `<style>` riêng của Lecture 03, bỏ ghi đè cỡ chữ nội dòng và thống nhất tiêu đề, mục lục, nội dung, bảng, mã, công thức, chú thích, nguồn và badge.
- Giữ phần nền CSS cũ; thành phần mới có phạm vi `.reveal.course-deck`, bố cục PageRank có phạm vi `.reveal.lecture-pagerank`. Các deck chưa nhận lớp mới không chịu tác động. Lecture 02 là chuẩn đối chiếu: đo tất cả h1/h2/h3/p/li/pre/table cho thấy cỡ chữ, dòng, độ đậm, lề và màu không đổi.
- Hai trang đầu cùng thang chữ: tiêu đề bài 75,6px; tên môn 35,7px; học kỳ 29,4px; tiêu đề mục lục 67,2px; dòng mục lục 42px. Cỡ chữ nội dung dùng lớp theo loại slide, không đặt lại riêng theo phần của Lecture 03.
- Parser xác nhận nội dung, notes, mã, SVG, ID và thứ tự của cả hai deck không đổi. Trang tiêu đề Lecture 03 chỉ đổi thẻ tên môn sang đoạn văn, ngắt dòng tiêu đề và thay dấu phân cách đơn vị bằng xuống dòng. Không đổi mục tiêu, thời lượng hoặc ghi chú tự học.
- OpenRouter chỉ nhận Lecture 03 theo phạm vi được cho phép: reader kiểm kê/kế hoạch, writer tách component CSS, sáu reviewer độc lập và editor tổng hợp đều hoàn tất; requested_model = observed_model = z-ai/glm-5.3-flash, provider = OpenRouter. Tác tử không được dùng để xác nhận hiển thị thay cho Chromium. Yêu cầu gửi kèm Lecture 02 bị tự động từ chối; sau đó chỉ so sánh và di chuyển style Lecture 02 cục bộ, không gửi nó hoặc CSS của nó sang OpenRouter.
- Kiểm hiển thị: 81 slide Lecture 02 và 63 slide Lecture 03 không tràn khung, không lỗi KaTeX, không thiếu hình/JavaScript. Xem trực quan trang tiêu đề, mục lục, mở phần và nội dung tiêu biểu; đối chiếu cỡ chữ thực. Bàn phím đạt; bản in 81/63 trang; khung hẹp 390px không tràn trang. Script kiểm cũ chứa ID cố định lec03 được sửa riêng để kiểm Lecture 02, không phải lỗi deck.
- AGENTS.md bổ sung nguyên tắc CSS chung là nguồn duy nhất cho các thành phần lặp lại, scope cho bố cục riêng và kiểm hồi quy cả hai deck khi sửa CSS chung.


## Điều chỉnh cách viết và minh họa (2026-09-17)

### Phạm vi và bằng chứng

Đối chiếu cục bộ hai deck sau khi đã dùng CSS chung cho thấy khác biệt chủ yếu ở quan hệ giữa dữ liệu, phép tính và kết quả. Quyết định theo từng cụm được ghi trong `visual-revision.md` và bảng bổ sung của storyboard. Thay cách thể hiện 21 slide; bổ sung định nghĩa C ở s05-05 sau rà soát, tổng cộng 22 slide có diff. Giữ bảy phần, 63 slide, ID, thứ tự, notes, mã Python, đề bài và thời lượng.

Ba SVG mới: ánh xạ cạnh vào cột A, hai phân phối qua phép cập nhật F, và dữ liệu cục bộ/qua mạng. Script `render_visual_revision.py` tái sinh đúng byte các hình. Các biểu diễn còn lại dùng HTML/KaTeX: thanh tổng điểm, ba nguồn cộng, ma trận thực chia khối, bảng vết Map/Combine, bảng byte theo tác vụ, timeline và trạng thái cạnh mã. CSS mới chỉ có phạm vi `.reveal.lecture-pagerank`, không thêm ghi đè cỡ chữ.

### Điều phối và lỗi công cụ

- Hai reader lập kế hoạch/kiểm kê, writer đặc tả nhóm mô hình và writer biên tập nhóm tính toán đã hoàn tất; requested_model = observed_model = `z-ai/glm-5.3-flash`, provider = `OpenRouter`. Điều phối viên dựng HTML/SVG, đối chiếu các quan hệ và loại đề xuất sai hoặc làm tăng tải.
- Lượt writer ban đầu dừng với `model exceeded the tool-call limit (30)`. Lượt tiếp tục lặp đọc cùng một SVG nên điều phối viên chủ động dừng. Không áp dụng bản HTML/SVG chưa đạt trong thư mục tạm; chia đầu ra thành đặc tả nội dung ngắn và giữ nguyên mô hình OpenRouter.
- Lượt soạn nhóm tính toán gặp `RuntimeError: OpenRouter request exceeded 480s wall timeout`. Tạm dừng phần phụ thuộc, tiếp tục kiểm định cục bộ; lượt thử lại cùng mô hình đã hoàn tất. Không chuyển ngầm sang tác tử khác.
- Lecture 02 chỉ được đọc và đối chiếu cục bộ. Phạm vi gửi OpenRouter chỉ gồm Lecture 03; không gửi CSS chứa nguồn Lecture 02, bản phân tích có nội dung Lecture 02, hoặc tệp bí mật.

### Quyết định từ các báo cáo đã nhận

- Rà toán nhóm mô hình: không thấy lỗi trong slide. Báo cáo viết nhầm nguồn góp vào A là D ở một phép kiểm, trong khi đồ thị và slide ghi B,C. Bác chỗ nhầm trong báo cáo; giữ đúng cạnh B→A và C→A.
- Rà giảng dạy: bổ sung định nghĩa dung lượng các khối $S_{\mathrm{blocks}}$ và tổng đầu vào Map+Reduce $C=I+H$ ngay trên mặt slide. Không thêm một lớp thông tin hoặc thu nhỏ chữ; sửa phần diễn đạt sẵn có.
- Rà giải thuật: báo cáo tự rút cáo buộc sai phương trình bài tập 2 sau khi nhận ra cạnh a→c. Giữ lời giải theo đồ thị nguồn. Bác đề nghị đổi 20 vòng thành 19: $\Delta_{19}$ so sánh $r^{20}$ và $r^{19}$, nên đã thực hiện 20 lần cập nhật. Chạy mã công khai xác nhận `iterations=20`, `delta=5.4975582974847725e-09`, `rank_sum=1.0`.

### Kiểm định cục bộ đã chạy

- Phân số độc lập: $r^1=(7/20,13/60,13/60,13/60)$; $r^2=(31/100,23/100,23/100,23/100)$; $\Delta_0=1/5$, $\Delta_1=2/25$.
- Đếm từ danh sách cạnh: M11/M12/M21/M22 lần lượt 24/24/28/12 byte; tổng khối 88, bốn lượt đọc dải 16 byte cho 64; I=152.
- Parser xác nhận 63 ID và thứ tự, notes và tất cả khối mã không đổi. Ba SVG không có nhãn vượt viewBox hoặc chồng nhau; tái sinh được.
- Chromium: toàn bộ 63 slide Lecture 03 và 81 slide Lecture 02 không tràn khung, không lỗi KaTeX, ảnh hoặc JavaScript. Sửa một caption chi phí sát chân trang rồi kiểm lại. Sau bổ sung định nghĩa ký hiệu, chín slide phần chi phí đều đạt.
- Bàn phím đạt; bản in 63 trang; màn hình hẹp 390px không tràn trang và không thiếu ảnh/công thức.
- Ghi chú công khai dùng cùng dữ kiện, công thức và giả thiết; không bị tác động vì notes/mã không đổi, hình cũ mà ghi chú tham chiếu vẫn giữ nguyên. Không cần phát hành lại ghi chú cho thay đổi bố cục.

Trạng thái sau biên tập: đã đủ báo cáo, xử lý các nhận xét và kiểm bản hiển thị cuối; đủ điều kiện commit/push. Không coi kiểm hiển thị là bằng chứng thay thế việc rà nội dung. Giới hạn Codex Slides như đã ghi: kiểm bản RevealJS phát hành bằng Chromium cục bộ, không tuyên bố đồng bộ bản Browser của dịch vụ.


### Hoàn tất các lượt rà và biên tập

| Vai trò | Phạm vi thực sự đọc | Kết quả và quyết định |
|---|---|---|
| Storyboard | 22 slide thay đổi có notes, bản đồ 63 slide, dữ kiện kiểm chứng | Đạt mạch dữ liệu → thao tác → kết quả; không phát hiện lỗi kiến thức. |
| Góc nhìn sinh viên | Toàn bộ HTML 63 slide, phạm vi thay đổi và ba SVG mới | Hình nối đúng đối tượng, vết chạy và byte khớp. Bác nhận xét cho rằng Delta0/Delta1 không nhất quán; chấp nhận làm rõ nhãn delta đo Δ cạnh mã. |
| Giải thuật và dữ liệu | Toàn bộ HTML và phạm vi thay đổi | Khối, bậc toàn cục, Combine, seed, delta và chi phí đúng. Bác nhầm chỉ số vòng và cáo buộc bài tập đã được chính reviewer rút lại. |
| Toán học | 22 slide thay đổi có notes, bản đồ toàn bài, dữ kiện; trước đó có lượt riêng 10 slide mô hình + SVG | Đạt phân số, bảo toàn tổng, giả thiết hội tụ, phân hoạch khối, công thức byte và quy ước chỉ số Delta. |
| Giảng dạy | Toàn bộ HTML và phạm vi thay đổi | Hai thiếu sót nhỏ về tên gọi Sblocks/C đã bổ sung; không lỗi chặn hoặc nghiêm trọng. |
| Liên tục, nguồn, mạch viết | 22 slide thay đổi có notes, bản đồ toàn bài và dữ kiện | Đạt quan hệ ví dụ–hình thức–tác vụ–chi phí–mã; giữ nguồn và ký hiệu. |
| Editor riêng | Hai slide cần chốt diễn đạt cùng quyết định hợp nhất sáu báo cáo | Nhãn `delta đo Δ` ở s06-04; thêm mỗi dải đọc k lần ở s05-04. Không đổi công thức, mã, notes hoặc thang chữ. |

Tất cả các lượt thành công trong bảng có requested_model = observed_model = `z-ai/glm-5.3-flash`, provider = `OpenRouter`. Ba lượt rà đầu về storyboard/toán/liên tục gặp timeout 480 giây; đã thử lại cùng mô hình bằng hồ sơ chỉ chứa phần thay đổi kèm bản đồ toàn bài và hoàn tất. Không thay kết luận bằng trạng thái tiến trình hoặc lời tự nhận của tác tử.

Điều phối viên kiểm lại các nhận xét trước khi áp dụng. Báo cáo sinh viên viết phép trừ A thiếu dấu trị tuyệt đối trong lời kiểm, nhưng bảng trên slide dùng đúng trị tuyệt đối; không sửa số trong slide theo câu đó. Báo cáo liên tục có một chỗ gom r1 thô và r1 có bước nhảy khi liệt kê ID; HTML vẫn phân biệt rõ s03-03 thô với s03-09 có bước nhảy. Phép tính phân số độc lập là căn cứ chấp nhận dữ kiện.

Editor trả chuỗi JSON escape thừa; điều phối viên chuẩn hóa dấu ngoặc/KaTeX khi áp dụng và dùng ký tự Δ trong heading thay công thức KaTeX. Đây là sửa định dạng, không thay ý toán học. Tự rà theo no-ai-slop: cắt lời dẫn lặp, gắn câu chốt với dữ kiện; theo Quill: giữ đối tượng A–D và ký hiệu qua các phần, không tạo dự án sách.


Kiểm cuối sau hai chỉnh sửa của editor: toàn bộ 63 slide không tràn khung, không lỗi KaTeX, hình hoặc JavaScript; xem trực tiếp lại hai slide sửa cuối. Bản in vẫn 63 trang, bàn phím và khung hẹp đạt. Đối chiếu mã/notes vẫn nguyên vẹn. CSS không đổi sau lượt hồi quy 81 slide Lecture 02. Đã kiểm trường runtime của 11 đầu ra thành công (hai reader, hai writer, sáu reviewer và editor), không dựa vào lời tự khai trong báo cáo. Không còn việc nội dung hoặc kiểm định cần xử lý trong phạm vi yêu cầu.

## Bổ sung trang tiêu đề mạch 2026-10-14

Căn cứ: `AGENTS.md` mục "Trang tiêu đề mạch" và hai gạch đầu dòng về mạch mở đầu, mạch kết luận trong "Mẫu RevealJS bắt buộc"; yêu cầu người dùng 2026-10-14 bổ sung trang tiêu đề mạch cho các bài đã phát hành theo từng đợt có nhật ký. Đợt 1 gồm Bài 01–05; một tác tử soạn duy nhất ghi tệp (Claude Opus 5.5; loại tác tử và effort do điều phối ghi theo lệnh gọi Agent); không commit.

Trang thêm (6), mỗi trang là `<section>` trong đầu tiên của section ngoài, `class="strand-title"`, `id="mach-N"`:

| N | Mã | Tên mạch | Dòng dẫn |
|---:|---|---|---|
| 2 | lec03-s02-00 | Bài toán xếp hạng trang web | Muốn xếp hạng trang theo liên kết, phải đặc tả đầu vào, đầu ra và thử quy tắc chia điểm trên bốn trang. |
| 3 | lec03-s03-00 | Mô hình và thuật toán PageRank | Muốn lặp phép chia điểm trên đồ thị bất kỳ, phải xử lý nút cụt, bẫy liên kết và nêu điều kiện dừng. |
| 4 | lec03-s04-00 | Tính PageRank trên đồ thị lớn | Muốn tính một vòng khi đồ thị không vừa bộ nhớ, phải lưu thưa và chia ma trận, véc tơ thành khối. |
| 5 | lec03-s05-00 | Chi phí và lợi ích của cách tính | Muốn biết cách chia khối tiết kiệm được gì, phải đo dung lượng, bộ nhớ một tác vụ, tổng việc và thời gian. |
| 6 | lec03-s06-00 | Thực hành tính PageRank | Muốn kiểm công thức cập nhật bằng số, phải viết chương trình Python và đối chiếu với kết quả tính tay. |
| 7 | lec03-s07-00 | Tổng kết và bài tập vận dụng | Muốn vận dụng PageRank, phải nắm chuỗi từ chia điểm tới công thức đầy đủ và chọn được biểu diễn đồ thị. |

Dòng dẫn 21–23 âm tiết; từ khóa 4–5 cụm, không có ký hiệu công thức; ghi chú diễn giả 80–88 âm tiết, công thức trong notes viết bằng `\(...\)` như phần còn lại của bài. Số trang 63 → 69.

Trang đổi: sáu trang mở phần `lec03-s0N-01` có `<h1>N · tên phần</h1>` kèm hình, thẻ, bảng; giữ trang nhưng đổi tiêu đề theo nội dung của chính trang để không trùng tên mạch: s02-01 "Điểm và thứ tự cho mỗi trang", s03-01 "Chia điểm và bước đi ngẫu nhiên", s04-01 "Ma trận đặc và danh sách liên kết", s05-01 "Bốn đại lượng chi phí", s06-01 "Sản phẩm và môi trường thực hành", s07-01 "Chuỗi kết quả và giới hạn của PageRank". Giữ thẻ `h1`, nội dung, notes và thứ tự. `aria-label` của section 2 viết thường "xếp hạng" cho khớp tên mạch.

Trang Nội dung: lec03-s01-02 đã có; `ul` đổi thành `ol` 1–7, tên trùng từng chữ với tên mạch, mạch 1 giữ "Giới thiệu bài học"; "Xếp hạng" ở mục 2 viết thường. Mặt trang khoảng 43 âm tiết; notes hiện có giữ nguyên vì đã nêu quan hệ giữa các phần.

Cố ý chưa làm (việc của đợt sau): mạch mở đầu đầy đủ (Tiên quyết và quy ước, Vấn đề trung tâm, câu luận đề trên trang bìa); chuẩn mật độ mặt trang; mạch kết luận theo khuôn mới (bảng tổng kết ba cột, trả lời vấn đề trung tâm, câu hỏi tự kiểm tra, nguồn và tài liệu đọc) và tách bài tập recitation thành section ngoài riêng. Không sửa CSS, SVG, ghi chú bài giảng, index. Các notes cũ còn dùng "ta", "phần ba/phần năm" là văn phong có từ trước, ngoài phạm vi.

Kiểm tra: section mở/đóng 76/76; 69 `data-slide-id` và 76 `id` duy nhất. Chromium Playwright trên máy chủ cục bộ cổng 8771: ở 1600×900, `#/2` … `#/7` mở đúng trang tiêu đề mạch 2–7; khối tiêu đề nằm trong khung (đáy lớn nhất 775 px trên 900 px), không cuộn ngang; 0 lỗi console, 0 `.katex-error`, không yêu cầu mạng ngoài; trang Nội dung đọc ra đúng bảy tên mạch; ba trang mở phần đổi tiêu đề (s02-01, s03-01, s07-01) không tràn khung. Ở 390×844, RevealJS chuyển sang chế độ cuộn và bỏ qua hash khi nạp; các trang được chụp sau khi cuộn tới phần tử, không tràn ngang. Đã tự xem ảnh. `git diff --check` sạch.

### Sửa sau rà lại đợt 1

Sau rà lại độc lập, sửa notes của lec03-s03-00 (mức nhẹ): "thêm bước nhảy với hệ số \(\beta\)" thành "thêm bước nhảy với xác suất \(1-\beta\)", vì trên lec03-s03-06 \(\beta\) là xác suất đi theo liên kết và \(1-\beta\) là xác suất nhảy. Dòng dẫn mạch 2 còn cụm "đầu vào, đầu ra" ở dạng văn xuôi, không phải nhãn; giữ nguyên trong đợt này. `git diff --check` sạch.

### Sửa sau rà lại đợt 2 (2026-10-14)

Theo báo cáo rà lại đợt 2 (không có phát hiện chặn bàn giao, nghiêm trọng hoặc trung bình), viết lại 5 ghi chú diễn giả của trang tiêu đề mạch: bỏ các câu lấy tài liệu hoặc trang làm chủ ngữ ("Phần này …", "Trang đầu …", "trang tiếp …", "Phần cuối …", "ở phần sau") theo `AGENTS.md` "Tiêu chuẩn trang chiếu và ghi chú diễn giả"; chủ ngữ mới là đối tượng, thuật toán hoặc kết quả; giữ ba ý kế thừa, nhiệm vụ, kết quả giao và độ dài 40–100 âm tiết (no-ai-slop, chế độ Edit). Dòng từ khóa: khoảng trắng trong mỗi cụm và trước dấu "·" đổi thành khoảng trắng không ngắt (`&nbsp;`), nên dấu "·" không đứng đầu dòng và không cụm nào bị tách ở 1600×900; không sửa CSS. Kiểm lại: section mở/đóng cân bằng; `#/2` … `#/N` mở đúng trang tiêu đề mạch ở 1600×900; 0 lỗi console, 0 `.katex-error`; `git diff --check` sạch.

## Sửa toàn diện theo chuẩn 2026-10-14

Căn cứ: `AGENTS.md` ("Mẫu RevealJS bắt buộc", "Trang tiêu đề mạch", "Phân loại phần lớn", "Văn phong và mật độ mặt trang chiếu", "Tiêu chuẩn trang chiếu và ghi chú diễn giả"), `slide_authoring_standard.md`, deck mẫu Bài 06; kế hoạch sửa `plan-lec03.md`; quyết định của điều phối viên (mục "Bài 03" và "Chung cho mọi bài").

**Phân công.** Điều phối viên: phiên Claude Code, Opus 5.5, effort `high`. Tác tử lập kế hoạch: chỉ đọc, `subagent_type: "fork"` (kế thừa Opus 5.5, effort `high`). Tác tử soạn: `subagent_type: "fork"` (kế thừa Opus 5.5, effort `high`), tác tử ghi duy nhất; bằng chứng là lời gọi Agent của điều phối viên. Không commit. Phạm vi ghi: deck 03 và ba tệp planning; không sửa CSS, SVG, index, ghi chú bài giảng, deck khác.

**Quyết định của điều phối viên đã áp dụng.**

1. Phương án A: gộp mạch 1 cũ với mạch 2 cũ; tách tổng kết (mạch 6, section `pagerank-summary`) và bài tập (mạch 7, section `summary-exercises`); giữ 7 mạch; không sửa CSS. `id` trang tiêu đề mạch đổi theo số mới (`mach-2` … `mach-7`); đã kiểm `index.html` (dòng 114, 116 chỉ liên kết tệp, không có `#/h/v`), `materials/lec-03/lecture-note.md` và các deck khác: không có liên kết sâu vào deck 03.
2. Quy ước đếm: trang có bảng dữ liệu tối đa 8 dòng kể cả hàng bảng; khối thẻ HTML chỉ chứa công thức hoặc nhãn ngắn tính như một hình (s03-08, s03-15, s05-01, s05-08; ghi trong storyboard).
3. Luận đề: "Mỗi vòng PageRank là một phép nhân ma trận thưa với véc tơ; bước nhảy và bù nút cụt bảo đảm phép lặp hội tụ." (25 token).
4. s03-11 thêm dòng "Trường hợp biên: mọi trang là nút cụt (kể cả $n=1$) cho $r^1=u$ ngay vòng đầu." Suy luận: $\delta=1$ nên phần chung $(1-\beta+\beta\cdot1)/n=1/n$, không có cạnh nên $r^1=u=r^0$ và $\Delta=0$. Chờ tác tử rà toán kiểm.
5. s03-14: hai dòng "Chứng minh." trên mặt trang ($F(x)=\beta Sx+(1-\beta)u$; phần nhảy triệt tiêu, cột của $S$ có tổng 1 nên co theo hệ số $\beta$); chứng minh đầy đủ ở ghi chú (194 âm tiết, ≤ 250).
6. s05-04 đổi sang khuôn `Bước | Số lần | Chi phí mỗi lần | Đóng góp`: 7 × 8 = 56; 8 × 4 = 32; $k^2=4$ × 16 = 64; tổng 152; $S_{\text{blocks}}=56+32=88$. Bảng theo tác vụ cũ (24, 24, 28, 12; dải 16 byte) chuyển vào ghi chú làm phép kiểm.
7. "véc tơ" thống nhất trong bài (11 chỗ "vector" đổi); "MapReduce" theo `sources/source.md`; Bài 02 viết "Map-Reduce", không sửa Bài 02 trong đợt này.
8. `h1` → `h2` ở s03-01, s04-01, s05-01, s06-01, s07-01 (s02-01 bị bỏ); `role="img"` thêm cho `cost-memory.svg`, `cost-combine.svg`, `cost-timeline.svg`; bỏ hai `style` nội dòng ở s02-03, s02-04 (lớp `.main-figure` có sẵn đặt 320 px; đã xem ảnh, bảng cạnh hình không tràn).
9. Năm Stanford CS246: 2026 (tệp `stanford-cs246/09-pagerank.pdf`, Leskovec và Kanatsoulis, PDF tạo tháng 2/2026).
10. Rà rút gọn ba vai: chờ điều phối viên giao.

Chung: "Đáp án" → "Lời giải" (5 chỗ); bỏ "ta", "Ta sẽ", "Hãy", "phần N" (đổi thành "mạch N" theo số mới hoặc gọi tên kết quả); trang bài tập giữ dòng "Nguồn:" lớp `ex-note`; thuật ngữ nút cụt (dead end), bẫy liên kết (spider trap), bước nhảy ngẫu nhiên (teleport), bộ nhớ chính (RAM) giải nghĩa ở lần đầu trên mặt trang; mọi trang nội dung có đoạn "Nguồn:" trong ghi chú (trừ Nội dung, trang nguồn và đề recitation có dòng nguồn trên mặt trang).

**Thay đổi cấu trúc.** 69 → 72 trang (67 giảng + 5 bài tập); bảy mạch 14/17/12/10/8/6/5; 120 + 60 phút (26,5/28/22,5/15/20/8 + 60). Thêm s01-07, s04-11 (tách từ s04-03), s07-08, s07-09, s07-T; bỏ s02-00, s02-01; đổi vai trò s01-06, s07-02, s07-01, s07-03. Bảng từng trang (quyết định, âm tiết trước → sau, dòng, phút, lý do) ở `storyboard.md`, mục cùng tên.

**Con số mới.** Không có số liệu mới về đồ thị; mọi số trên trang mới lấy từ deck hoặc ghi chú đã kiểm. Phép tính mới đưa lên mặt trang: $\beta\delta/n=(4/5)(1/4)/4=1/20$ (s03-07); trường hợp biên $r^1=u$ (s03-11); $56+32=88$, $4\cdot16=64$ (s05-04); tổng kiểm $9/28+3\cdot19/84=27/84+57/84=1$ và $(4/5)(19/168+19/84)+1/20=9/28$ (ghi chú s07-01); $10^9&lt;2^{31}$ cho mã 4 byte.

**Mật độ trước → sau** (`python3 -I scratchpad/p03/dens03.py 2627-1/lecture-03-pagerank-mo-hinh-va-tinh-toan.html`; trang nội dung, không tính trang tiêu đề mạch).

| Chỉ số | Trước (69 trang) | Sau (72 trang) |
|---|---:|---:|
| Trung vị âm tiết | 46 | 43 |
| Số trang > 40 | 41 | 40 |
| Số trang > 60 | 16 | 4 (đều trần 80: s01-03 71, s07-02 71, s07-08 71, s07-01 80) |
| Số trang > 80 | 2 | 0 |
| Trang trần 60 vượt 60 | 10 | 0 |
| Dòng > 20 âm tiết (trừ dòng dẫn tiêu đề mạch và luận đề) | 11 | 0 |
| Ghi chú diễn giả > 150 âm tiết | 13 | 7 (s03-14 194 và s04-08 191 là chứng minh; s07-03 179 là lời giải; s06-04 165, s06-05 163, s06-07 161, s06-06 158) |

**Tự kiểm no-ai-slop (Edit, đối chiếu `eval.md`).** Văn bản mới: luận đề (của điều phối viên), s01-07, s01-03, s01-02, s01-06, s02-02, s04-11, s07-02, s07-08, s07-01, s07-03, s07-09, s07-T, các dòng nhãn và ghi chú diễn giả viết lại. Đạt: không lời nói mô phỏng ("ta", "Ta sẽ", "Hãy"), không câu chỉ đường ("Phần sau: …", "Tổng kết phần: …"), không câu hỏi tu từ, không khẩu hiệu (câu "Biểu diễn thưa giảm lưu trữ, …" ở s05-09 bỏ), không gạch ngang dài; định nghĩa viết bằng "là"/"gọi là". Liên tục và thuật ngữ kiểm bằng rà tay và tìm kiếm chuỗi ("vector", "phần N", "Đáp án", `\text{}` có chữ Việt); chưa chạy kỹ năng `quill` trong lượt soạn này.

**Kiểm kỹ thuật.** `git diff --check` sạch cho deck và ba tệp planning. HTML cân bằng (`html.parser`: 0 thẻ chưa đóng, 0 thẻ đóng sai); 72 `data-slide-id` duy nhất; mọi `id` duy nhất; 0 `<style>`, 0 thuộc tính `style=`, 0 `fragment`, 0 lớp `.dense`; mọi `img` có `role="img"`; 0 chữ có dấu trong `\text{}`. Playwright Chromium, máy chủ cổng 8771, `wait_until="load"`, tắt chuyển cảnh, bộ lọc console bắt `error` và cảnh báo KaTeX:
- 1600×900: cả 72 trang qua `Reveal.getIndices` + `Reveal.slide(h, v, 99)`; 0 lỗi console, 0 cảnh báo KaTeX, 0 lỗi trang, 0 `.katex-error`, 0 yêu cầu mạng ngoài, không cuộn ngang, không phần tử vượt khung. Trang sát đáy nhất: s03-14 (839/864 px, chân trang 845).
- 390×844: 0 phần tử vượt mép phải, `scrollWidth` = `clientWidth` = 390, 0 lỗi, 0 `.katex-error`.
- Ảnh đã tự xem ở 1600×900: cả 72 trang (ghép 9 trang mỗi ảnh); đã sửa ba công thức bị ngắt dòng (s07-01, s07-02, s07-08) bằng nhóm KaTeX.

**Tác động tới ghi chú bài giảng `materials/lec-03/lecture-note.md`.** Không sửa. Ký hiệu, ví dụ, con số và kết luận không đổi. Điểm để đợt sửa ghi chú xử lý: (a) dòng trường hợp biên mọi trang là nút cụt (nếu tác tử rà toán duyệt); (b) bảng đầu vào các tác vụ theo khuôn mới (số giữ nguyên); (c) cấu trúc: ghi chú có bảy mục khớp bảy phần cũ, nay mục 1–2 ứng với mạch 1, mục 3–6 với mạch 2–5, mục 7 với mạch 7; (d) thuật ngữ "véc tơ" và "MapReduce".

| Mức độ | Trang chiếu | Vấn đề | Bằng chứng | Đề xuất sửa | Trạng thái |
|---|---|---|---|---|---|
| trung bình | s03-11 | Dòng "Trường hợp biên" là suy luận mới từ công thức | quyết định 4 | Tác tử rà toán kiểm $\delta=1\Rightarrow r^1=u$ | đã xác nhận (rà toán 2026-10-14: đúng, kể cả $n=1$) |
| nhẹ | toàn deck | Chữ $B$ có bốn nghĩa (trang B, khối $B_{ab}$, $B_{\text{task}}$, $B_{\text{buf}}$) | quill | Giữ (đổi là sửa nội dung toán và ghi chú); chỉ số phân biệt | đóng ở lượt sửa sau rà ba vai: bỏ $B_{ab}$, quy ước $B$ nêu ở s05-01 |
| nhẹ | s01-xx, s02-xx | Chân trang ẩn trên cả mạch 1 vì quy tắc CSS chung ẩn chân trang khi section đầu đang hiện | `lecture-style.css` dòng 78–79 | Ngoài phạm vi (CSS chung); mạch 1 nay dài 14 trang | mở |
| nhẹ | s03-11, s04-05, s04-06 | Phông đơn cách của giả mã đặt dấu thanh lệch trên Chromium Linux | ảnh 1600×900 | Kiểm phông ở đợt CSS chung | mở |
| nhẹ | Bài 02 ↔ Bài 03 | "Map-Reduce" (Bài 02) và "MapReduce" (Bài 03) | quyết định 7 | Thống nhất ở đợt thuật ngữ chung | đóng: deck Bài 02 nay viết "MapReduce" ở mọi chỗ (đợt sửa Bài 02, 2026-10-14); câu biên soạn về chính tả bỏ khỏi ghi chú s01-07 |
| nhẹ | 7 ghi chú | Ghi chú > 150 âm tiết | bảng mật độ | Rút ở lượt sửa sau rà nếu không mất giả thiết hay lời giải | mở |

## Lượt sửa sau rà ba vai (2026-10-14)

**Giao việc.** Điều phối viên giao tác tử soạn (loại `fork`, Claude Opus 5.5, effort `high`, theo lệnh gọi Agent của điều phối viên) sửa theo `fix-d03.md`, hợp nhất ba báo cáo rà chỉ đọc: rà toán (`review-d03-math.md`), kết nối và mạch viết (`review-d03-storyline.md`), sinh viên kèm mật độ (`review-d03-student.md`); ba tác tử rà là `fork` Opus 5.5 theo lệnh gọi của điều phối viên. Phạm vi ghi: deck 03 và ba tệp `planning/lec-03/`. Không commit. Skill `no-ai-slop` nạp ở chế độ Edit trước khi sửa chữ. Thay đổi được áp bằng một tệp đặc tả bổ sung trên bộ dựng deck (`scratchpad/w03/spec/s9fix.py`).

**Quyết định cho từng phát hiện.** Mã: T = rà toán, M = mạch viết, S = sinh viên.

| Mã | Mức độ | Trang chiếu | Phát hiện | Quyết định |
|---|---|---|---|---|
| M1, S1 | nghiêm trọng | s03-08, s03-03, s03-14, s03-11, s07-02 | $u$ và phương trình điểm bất động không có trên mặt trang | sửa: s03-08 "khởi tạo $r^0=u$, với $u_i=1/n$" và dòng "Dạng khác: $r^{t+1}=\beta M_0r^t+((1-\beta)+\beta\delta^t)u$"; s03-03 "phép lặp tìm $r^*=M_0r^*$"; s03-14 "hội tụ tới phân phối duy nhất $r^*=F(r^*)$", "$\bar M$ không âm"; ghi chú s03-08 bỏ câu định nghĩa $u$ đã lên mặt trang. Đây là giao diện ký hiệu với Bài 04 |
| M2 | trung bình | s03-14 | $S$ vừa là ma trận vừa là dung lượng | sửa: $S\to\bar M$ (khớp Bài 04). Mặt trang định nghĩa bằng lời "$M_0$ có cột nút cụt thay bằng $u$"; dạng $\bar M=M_0+uz^{\mathsf T}$ chỉ ở ghi chú, vì trên mặt trang $z$ đã là $z=M_0r$ của mạch 3 (lệch có chủ ý so với `fix-d03.md` mục 2) |
| M3, S8 | trung bình | s03-15 | trang Map/Reduce nằm cuối mạch mô hình, trùng s04-07 | sửa: chuyển sang mạch 3 sau s04-01 làm bước trực giác; câu kết thành "Một vòng là phép nhân ma trận–véc tơ của Bài 02: Map phát (đích, đóng góp), Reduce cộng theo đích"; ghi chú s04-07 nêu điểm mới (hai khối cùng phát khóa A). Phút mạch 2/3: 28 → 27, 22,5 → 23,5 |
| M4 | trung bình | s07-03 | câu tự kiểm tra trùng s03-16, s05-09 và có lời giải trên s07-01, s07-02 | sửa: bốn câu vận dụng mới (bỏ phần bù trên biến thể nút cụt C, đáp $4/5$; $\beta=1$ trên biến thể bẫy; tác vụ đọc $r$ đang đổi; xếp bốn tác vụ trên hai máy, đáp $4c_e$); lời giải trong ghi chú; ghi chú s07-02 bỏ các câu là lời giải của bốn câu này |
| M5 | trung bình | s07-09 | thiếu dòng nối Bài 04 | sửa: "Bài 04 giữ phép lặp, đổi nơi đến của bước nhảy theo chủ đề hoặc tập tin cậy." Giữ thuật ngữ "bước nhảy" của Bài 03 thay "bước dịch chuyển" trong `fix-d03.md`; ghi chú nêu Bài 04 gọi là bước dịch chuyển |
| M6, T1, T2, S4, M13 | trung bình | s01-06, s07-01 | đối ứng dòng, thiếu điều kiện, thiếu ≈, 7 dòng, Kết luận là câu phạm vi | sửa: năm mục s07-01 theo đúng năm dòng s01-06 (dòng 3 gộp $n=10^9$, liên kết ra $\approx4(10^9+m)$ so với $8\cdot10^{18}$, $k^2$ khối); "đồ thị bốn trang gốc" cho $9/28$, $19/84$; "chỉ pha Map, ví dụ bốn khối $2,2,3,1\,c_e$" cho $8/3$; Kết luận có điều kiện ($0<\beta<1$, $m\ll n^2$); câu phạm vi vào ghi chú; 6 dòng, 72 âm tiết |
| S2 | trung bình | s04-04 | thiếu bản ghi $M_{12}$, $M_{22}$ | sửa: dòng "$M_{12}$: (C, 1, [A]), (D, 2, [B]); $M_{22}$: (D, 2, [C])" theo định dạng bản ghi của trang; 8 dòng kể cả hàng bảng; câu kết rút để giữ trần 60 (56) |
| S3 | trung bình | s04-05, s04-11, s05-01 | trùng ký hiệu $B$, $r_b$/$r_i$, $z_a$/$z_A$ | sửa: bỏ $B_{ab}$ (khối viết $M_{ab}$, cả giả mã); dòng "Ký hiệu:" ở s04-11, trang đầu dùng dải; quy ước $B$ nghiêng (bộ nhớ), B đứng (trang) ở s05-01. Không đổi tên dải vì hình `cost-memory.svg` ghi $r_b$, $z_a$ (tệp SVG ngoài phạm vi) |
| T3 | nhẹ | s03-14 | thiếu "không âm" | sửa (cùng M1) |
| T4 | nhẹ | s07-02 | công thức chia khối thiếu số hạng | sửa: $\sum_b\sum_{j\in V_b,\,j\to i}r_j/d_j=\sum_{j\to i}r_j/d_j$ |
| T5 | nhẹ | s07-08 | cột chi phí trộn đại lượng; thiếu $B_{\text{buf}}$; ghi chú lệch s05-02 | sửa: hàng 1 "$O(n+m)$ mỗi vòng; bộ nhớ $16n$ byte"; hàng 2 "$16n/k+B_{\text{buf}}$ byte một tác vụ"; ghi chú theo đề xuất |
| T6 | nhẹ | s01-06 | "chuyển nhiều hơn", "một nghiệm" | sửa: "liên kết của nguồn ít đích mang nhiều điểm hơn", "nghiệm duy nhất"; dòng Nhu cầu và dòng 3 rút để giữ 60 |
| T7 | nhẹ | ghi chú s05-05 | lý do bỏ bản ghi $(i,0)$ mâu thuẫn s04-06 | sửa: "ví dụ không đếm $n$ bản ghi khởi tạo $(i,0)$, nếu đếm thì $H$ tăng thêm $4\cdot12=48$ byte ở cả hai phương án" |
| T8 | nhẹ | s01-02, s07-09 | tr.176 → tr.175 | sửa |
| T9 | nhẹ | ghi chú s04-04 | Hình 5.14 ở tr.194 | sửa: tr.192–194 |
| M7 | nhẹ | 12 ghi chú | gọi "mạch N"; "bốn mạch trước" | sửa: gọi bằng tên kết quả (bảng một vòng có bước nhảy, quy tắc cập nhật đầy đủ, thuật toán PageRank lặp, danh sách liên kết ra…); s07-00 "năm mạch trước" |
| M8 | nhẹ | s03-01 | "bước đi ngẫu nhiên" và "bước nhảy ngẫu nhiên" dễ lẫn | sửa: câu kết "Bước đi ngẫu nhiên (random walk): $r_i$ là xác suất…" |
| M9 | nhẹ | s01-03, s03-11 | $M_0$, $\tau$, $T_{\max}$ chưa gọi tên | sửa: "Lập ma trận liên kết"; "ngưỡng $\tau>0$, giới hạn vòng $T_{\max}$" |
| M10 | nhẹ | ghi chú s02-02 | thiếu câu vì sao xác định đầu ra trước | bác bỏ: ghi chú s02-02 đã nêu đầu ra không âm, tổng một để so sánh được; thêm câu sẽ lặp |
| M11 | nhẹ | s07-T, s07-00 | dòng dẫn tự quy chiếu; từ khóa "Câu trả lời" | sửa: dòng dẫn mạch 7 theo đề xuất (24 âm tiết); từ khóa "Một tỷ trang" |
| M12 | nhẹ | s02-03 ↔ s04-02 | tên cột khác nhau | sửa bằng ghi chú s04-02 (cột theo thứ tự trường bản ghi); giữ bảng s02-03 vì đọc trực tiếp từ hình |
| S5 | nhẹ | s01-06 | thuật ngữ dùng trước định nghĩa | giữ: khuôn trang Vấn đề trung tâm của deck mẫu 06; ghi chú nói các câu trả lời có điều kiện được xây ở các mạch sau |
| S6 | nhẹ | s03-01 | $d_j$ trước định nghĩa | sửa: "(bậc ra)" sau $d_j$ |
| S7 | nhẹ | s02-08 | câu 2 có đáp án trên s02-07 | sửa: $r^0=(1/2,1/6,1/6,1/6)$, D nhận $1/6+1/12=1/4$; cần tác tử rà toán xác nhận ở recheck |
| S9 | nhẹ | s03-11, s04-05, s04-06 | phông đơn cách lệch dấu tiếng Việt | mở: CSS chung (`lecture-style.css`, phông đơn cách), ngoài phạm vi; kiểm trên máy chiếu |
| S10 | nhẹ | s04-05 | "Map yield", "Combine yield" | sửa: "Map phát", "Combine phát" |
| S11 | nhẹ | s06-02 | $\tau$, $T_{\max}$ khác tên tham số | sửa: "$\tau$ (`tol`)", "$T_{\max}$ (`max_iter`)" |
| S12 | nhẹ | s01-05 | "EB" chưa giải nghĩa | sửa: "(1 EB là $10^{18}$ byte)" |
| S13 | nhẹ | s03-14 | sát đáy | giữ: không thêm dòng; đáy 839/864 px, trên chân trang 845 |
| S14 | nhẹ | bìa, trang tiêu đề mạch | mẩu một từ khi xuống dòng | giữ (vai sinh viên đánh giá chấp nhận được) |
| S15 | nhẹ | s03-01, s05-03, s05-06 | chú giải SVG nhỏ, chỉ số gõ thô | mở: tệp SVG ngoài phạm vi |
| S16 | nhẹ | s04-10 | câu 3 để ngỏ | sửa: "Nêu một cách phân bổ." |
| S17 | nhẹ | ghi chú s01-07 | câu biên soạn về "MapReduce" | sửa: bỏ khỏi ghi chú; ghi ở đây và ở dòng chính tả phía trên |
| S18 | nhẹ | ghi chú s06-05, s06-06 | lặp số trên mặt trang | mở: câu thay thế đề xuất ("$\Delta$ giảm khoảng hệ số $\beta$ mỗi vòng") không đúng với đồ thị này ($\Delta$ từ 0,2 xuống $5{,}5\cdot10^{-9}$ sau 20 vòng, tỉ số trung bình khoảng 0,4 < $\beta$); cần câu khác đã kiểm |
| S19 | nhẹ | storyboard | âm tiết, dòng lệch deck | sửa cho các trang đổi trong lượt này (bảng storyboard đánh dấu "lượt sửa"); trang không đổi giữ số của công cụ đếm `dens03.py`, khác quy ước đếm của vai sinh viên |

**Mật độ sau sửa** (`scratchpad/p03/dens03.py`, `w03/capcheck.py`): không trang trần 60 nào vượt 60 (s01-06, s07-03 bằng 60); trang trần 80 cao nhất s07-08 74, s07-01 72; không dòng nào vượt 20 âm tiết (dòng dẫn trang tiêu đề mạch tối đa 25). Ngoại lệ dòng giữ như storyboard; s03-08 thêm một dòng (khối thẻ tính như hình), s04-04 8 dòng kể cả hàng bảng.

**Kiểm tra.** `git diff --check` sạch (deck và ba tệp kế hoạch). Thẻ HTML cân bằng; 72 `data-slide-id` duy nhất; không `style`, `fragment`; 0 "Map-Reduce". Chromium Playwright, cổng 8771, 27 trang đổi (s01-02, s01-03, s01-05, s01-06, s02-08, s03-01, s03-03, s03-08, s03-11, s03-14, s03-15, s03-16, s04-01, s04-02, s04-04, s04-05, s04-10, s04-11, s05-01, s06-02, s07-00, s07-01, s07-02, s07-03, s07-08, s07-09, s07-T) và lượt toàn deck do công cụ kiểm: 1600×900 0 lỗi console, 0 cảnh báo KaTeX, 0 `.katex-error`, 0 yêu cầu mạng ngoài, không cuộn ngang, không phần tử vượt khung; đáy thấp nhất s03-14 839/864 px (chân trang 845). 390×844: 0 lỗi, không tràn phải. Đã tự xem ảnh 1600×900 của 18 trang đổi chính (hai ảnh ghép).

**Tác động.** Deck Bài 04 (ghi chú trang hội tụ, dòng "Bài 03 ký hiệu ma trận này là $S$") nay lệch vì Bài 03 dùng $\bar M$; cần sửa câu đó ở đợt Bài 04 (ngoài phạm vi). Ghi chú bài giảng `materials/lec-03/lecture-note.md` (mục chứng minh hội tụ dùng $S$) cần đổi sang $\bar M$ ở đợt sửa ghi chú; con số và kết luận không đổi. `index.html` không đổi.

**Recheck cần chạy** (CLAUDE.md, "Recheck"): rà toán trên s02-08 câu 2, s03-14, s07-01, s07-02, s07-03 (lời giải), s07-08, ghi chú s05-05; mạch viết trên s03-03…s03-16, ranh giới mạch 2/3 quanh s03-15, s04-01…s04-07, s07-00…s07-T.

### Đồng bộ ký hiệu $\bar M$ sau lượt sửa (2026-10-14)

Theo giao việc của điều phối viên (tác tử soạn, `fork`, Opus 5.5, effort `high`; không commit): ghi chú bài giảng `materials/lec-03/lecture-note.md`, đoạn **Hội tụ** của chứng minh hội tụ, đổi $S$ thành $\bar M$ ở ba chỗ (định nghĩa, $F(r)=\beta\bar Mr+(1-\beta)u$, bất đẳng thức $\|\bar Mv\|_1\le\|v\|_1$); nội dung, con số và kết luận không đổi; $S$ ở phần 5 của ghi chú vẫn là dung lượng. Ghi chú diễn giả trang hội tụ của deck 04 sửa câu "Bài 03 ký hiệu ma trận này là $S$" thành "Bài 03 cũng ký hiệu ma trận này là $\bar M$…" (ghi ở review-log Bài 04). Kiểm: `material-viewer.html?doc=materials/lec-03/lecture-note.md&deck=lecture-03-pagerank-mo-hinh-va-tinh-toan.html` trên cổng 8771, 1600×900 và 390×844: 352 khối KaTeX, 0 `.katex-error`, không tràn ngang; một thông báo console về chính sách bảo mật nội dung (CSP) do máy chủ phát triển chèn script tự nạp lại (không có trong `material-viewer.html`), không liên quan ghi chú. Đã tự xem ảnh đoạn Hội tụ. Mục tác động "ghi chú bài giảng dùng $S$" của lượt sửa sau rà ba vai: đóng.

### Sửa sau recheck (2026-10-14)

Theo `recheck-d03.md` (vai recheck toán và mạch viết, `fork` Opus 5.5; không phát hiện chặn bàn giao hay nghiêm trọng) và giao việc của điều phối viên; tác tử soạn `fork`, Opus 5.5, effort `high`; không commit.

| Mã | Mức độ | Trang chiếu | Quyết định |
|---|---|---|---|
| T1 | trung bình | s04-01 → s03-15 → s04-02 | sửa: s03-15 chuyển xuống sau s04-02 (trước s04-03); ghi chú mở bằng bản ghi $(B,2,[A,D])$ của danh sách liên kết ra và câu cuối dẫn vào chia khối; phút không đổi; storyboard đánh số lại, outline cập nhật thứ tự |
| N1 | nhẹ | s03-15 | sửa: thẻ Reduce ghi $1/8+1/4$ và $=3/8$, không dùng $z_A$; ghi chú gọi "tổng đóng góp về A" |
| N2 | nhẹ | s05-01 | sửa: bỏ quy ước nghiêng/đứng; dòng Ký hiệu viết "$B$ là bộ nhớ, khác trang B" |
| N3 | nhẹ | s03-08 | sửa: "với $u_i=1/n$" ở cuối dòng "Dạng khác" (lần dùng đầu); chú thích còn "khởi tạo $r^0=u$" |
| N4 | nhẹ | ghi chú s07-09 | sửa: bỏ câu biên soạn; còn "Bài 04 dùng lại ký hiệu PageRank của bài này và gọi bước nhảy là bước dịch chuyển." |
| N5 | nhẹ | s07-01 | sửa: "$k^2$ khối, cùng điểm cũ: như một máy" (75/80 âm tiết, 6 dòng) |
| — | nhẹ | s03-14, s05-01 (390×844) | giữ như recheck đề xuất (đáy sát chân trang; chế độ cuộn ở cỡ hẹp do CSS chung) |

Mật độ sau sửa (`p03/dens03.py`): s03-08 30, s03-15 47, s04-01 58, s04-02 43, s04-03 37, s05-01 53, s07-01 75, s07-09 54; không dòng nào vượt 20 âm tiết.

## Viết lại ghi chú và lập tệp bài tập theo chuẩn 2026-11 (đợt B3, 2026-11-11)

Căn cứ: `prompt_fix_lecture_notes.md` (đợt B3, hàng 03: viết lại toàn bộ; giữ dữ kiện, vết tính, mã, bốn lời giải; định lý hội tụ bốn phần có chứng minh chia bước; bỏ "Hướng dẫn chấm"); `AGENTS.md` §"Tiêu chuẩn giáo trình", §"Cấu trúc bắt buộc" 1–10; "The author's voice" của `../CLAUDE.md`. Điều phối viên: Claude Opus 5.5, effort high, không soạn hay rà. Nguồn: MMDS 3e Ch.5 §5.1–5.2 (`sources/textbooks/mmds-3e-ch05-link-analysis.pdf`, trang in = trang PDF + 174); trang chiếu MMDS ch05, CS246 09; `materials/lec-03/code/pagerank.py`.

### Tác tử (lấy từ lời gọi công cụ)

| Vai trò | Loại | Mô hình | Effort | Ghi |
|---|---|---|---|---|
| Lập kế hoạch chương | general-purpose | opus | high | không |
| Soạn, sau đó biên tập hai vòng (SendMessage) | general-purpose | opus | high | ghi chú, `exercises.md`, `img/lec-03/note-*.svg` và bộ sinh trong `tools/`, `outline.md`, `storyboard.md` |
| Rà vai sinh viên năm hai | general-purpose | opus | high | không |
| Rà chuyên gia miền | general-purpose | opus | high | không |
| Rà độ chính xác (ba lượt) | general-purpose | opus | high | không |
| Rà sư phạm, `no-ai-slop` Detect | general-purpose | opus | high | không |
| Rà mạch và liên kết (ba lượt) | general-purpose | opus | high | không |

### Quyết định của điều phối viên

- Tồn tại và duy nhất qua tính khả nghịch của $I-\beta\bar M$; hội tụ qua tính co hệ số $\beta$ (Bổ đề 03.14, Định lý 03.15, Hệ quả 03.16 cận $\beta\Delta/(1-\beta)$ trong mạch chính cho Bài 04).
- Phần Đọc thêm thu gọn: loại nút cụt đệ quy (§5.1.4) và Bài tập 03.5; không đưa cập nhật theo dải (§5.2.5).
- Ký hiệu: $K$ thay $T_{\max}$; $t_{\text{dừng}}$; ký hiệu Bài 02 khi cùng nghĩa; $\bar M=M_0+u\mathbf 1_{\mathcal D}^{\mathsf T}$; bảng đối chiếu deck ↔ ghi chú trong `outline.md`.
- Bài tập: `exercises.md` 03.7–03.12 = MMDS 5.2.2, 5.1.1, 5.1.2, 5.2.1 (recitation s07-07, s07-04, s07-05, s07-06; giữ bốn lời giải cũ), 5.1.3 (!), 5.1.7; ghi chú 03.1 (5.1.5), 03.3 (5.2.3), 03.4 (5.2.4, đề chỉ câu (a) của sách), 03.5 (5.1.6, đọc thêm). Bỏ 5.1.4 (!!). Không mục Thực hành trong `exercises.md` (bài tập chỉ từ giáo trình).
- Mục tiêu hội tụ/ngưỡng dừng và mục tiêu chạy `pagerank.py` không có bài sách: thêm Bài tập 03.2 (cuối §2.5, đồ thị $\mathrm A\rightleftarrows\mathrm B$, $\beta=4/5$) và 03.6 (cuối Mục 5, `step` và `--variant dead`) trong ghi chú, dựng trên dữ kiện của ghi chú (`AGENTS.md` mục 10).
- Bài tập 5.1.3: giải theo quy tắc bù của ghi chú; so với công thức không bù của MMDS trong lời giải (Mệnh đề 03.17), không trong đề.

### Phát hiện và quyết định

| mức độ | vị trí | vấn đề | quyết định |
|---|---|---|---|
| nghiêm trọng | Bài tập 03.4 (cũ 03.3) | $S_{\text{blocks}}-S_{\text{adj}}=4n-8=4R$ sai | chấp nhận: $=4R-4$; khối không lưu bậc 0 của trang $n$ |
| nghiêm trọng | bảng mục tiêu | mục tiêu hội tụ và mục tiêu chạy mã không có bài tập | chấp nhận: Bài tập 03.2, 03.6 trong ghi chú; đánh lại số bài tập theo thứ tự đọc |
| trung bình | Ví dụ 03.21, Tóm tắt, hình | $H$ bỏ cặp khởi tạo (96/84) | chấp nhận: $H=144/132$, $C=296/284$ |
| trung bình | Định nghĩa 03.25, Mệnh đề 03.28 | $Q$ hai nghĩa; $b_{\text{eff}}$ chưa thỏa điều kiện Mệnh đề 02.38 | chấp nhận |
| trung bình | Nhận xét 03.10 cũ | kết quả có chứng minh dựa vào định lý đứng sau | chấp nhận: Mệnh đề 03.17 sau Ví dụ 03.13 |
| trung bình | ký hiệu, thuật ngữ | $u,I,a,s,S,W,q$ nhiều nghĩa; "lặp thô/lặp lũy thừa"; "danh sách nguồn" | chấp nhận |
| trung bình | nguồn | "vote with their feet" gán sai; "phần lớn web" không có trong MMDS; câu (b) thêm vào 5.2.4 | chấp nhận |
| trung bình | mạch | câu nối Bài 02 sai; ranh giới mục lặp; Tóm tắt thiếu quy mô $10^9$; Ví dụ 03.6 mặc nhiên hội tụ | chấp nhận |
| trung bình | vai trò giả thiết, chi phí | thiếu "Bỏ …: …" có số; thiếu bảng chi phí 03.22, 03.31; Phạm vi Hệ quả đọc sai | chấp nhận |
| nhẹ | khoảng 70 mục | trích trang, phân số, câu chỉ đường, tên tiếng Anh, … | chấp nhận |
| — | rút gọn phân số Ví dụ 03.11 | bác bỏ: giữ mẫu số chung như MMDS Ví dụ 5.6 |
| — | bỏ "nơi Bài tập … đứng ngay sau các mục" ở `exercises.md` | bác bỏ: câu của mẫu |
| — | thêm dữ kiện bộ nhớ cho Tình huống 03.1 | bác bỏ: giữ $k$ ký hiệu, điều kiện chọn $k$ bằng công thức |

Đổi số hiệu so với bản nháp: Thuật toán 03.11→03.10, Mệnh đề 03.12→03.11, Nhận xét 03.13→03.12, Mệnh đề 03.14→03.13, Bổ đề 03.15→03.14, Định lý 03.16→03.15, Hệ quả 03.17→03.16, Nhận xét 03.10→Mệnh đề 03.17. Ghi chú cũ (đã công bố) không dùng số hiệu; ghi chú Bài 04 chưa dẫn số hiệu Bài 03 (sửa ở đợt B4).

Dữ kiện tự dựng (không ghi trong ghi chú): đồ thị hai trang $\mathrm A\rightleftarrows\mathrm B$ (phản ví dụ $\beta=1$, Bài tập 03.2); các phản ví dụ bốn trang (chia theo bậc vào; cập nhật không đồng bộ, tổng $9/8$ và $404/375$; bậc cục bộ, cột A tổng $4/3$, $z$ tổng $13/12$; $\delta$ đếm hai lần, tổng $6/5$; danh sách lặp $23/60$, $11/60$; $r$ âm; dải chồng nhau; $n=4$, $k=3$); trang E giả định; suy diễn $\Delta_t=\tfrac15(2/5)^t$; giả thiết cặp khởi tạo tạo ở máy Reduce ($Q=84$). Trang chiếu MMDS tr.53 ghi 40 GB khi chỉ đếm mã đích (ghi chú dùng $4{,}4\cdot10^{10}$ byte gồm cả bậc).

Sai khác với deck (không sửa deck trong đợt này): deck s07-04…07 dẫn "ghi chú mục 7, Bài 1–4" và "Hướng dẫn chấm"; deck s05-05 ghi $H$ 96/84, $C$ 248/236; ký hiệu $T_{\max}$, $L$, $p$, $B$, "véc tơ"; `desc` của `model-spider-trap.svg`, `visual-contraction.svg` không khớp hình. Hình `model-collect.svg` không còn trang nào dùng, xóa khỏi kho.

### Kết quả kiểm tra

- Độ dài: ghi chú 5 349 (bản cũ) → 23 846; `exercises.md` 2 241.
- Khối: bộ đếm chung 03.1–03.33; Ví dụ 03.1–03.24; Bài tập 03.1–03.12; Tình huống 03.1–03.2; mọi dẫn 03.k/02.k/01.k đúng khối.
- `pagerank.py`: base 20, dead 12, trap 34 vòng, khớp ghi chú.
- Grep mẫu cấm: 0 (trừ " — " ở tiêu đề theo mẫu); `git diff --check` sạch.
- Trình duyệt (`http.server`, Playwright Chromium): ghi chú và `exercises.md` ở 1600×900, 390×844: 0 lỗi console, 0 request hỏng, 0 `.katex-error`, trang không cuộn ngang, 0 công thức tràn ở 390 px; phần Đọc thêm thu gọn, mở khi in.


## Rà soát deck theo nguyên tắc deck mới và đối chiếu ghi chú bài giảng (2026-11-13)

**Bối cảnh.** Yêu cầu người dùng (2026-11-13): kiểm tra các deck 01–10 xem deck nào chưa tuân thủ các nguyên tắc của deck mới và chưa khớp với ghi chú bài giảng, ghi bảng phát hiện đầy đủ vào `review-log.md` của từng bài, thời điểm phát hiện là ngày 2026-11-13. Đợt này chỉ đọc: deck, ghi chú và `exercises.md` không đổi (HEAD `45ddcf9`; md5 deck `cbafcb6e`, ghi chú `0e292b8c`, `exercises.md` `8e423c45`, trùng nhau lúc bắt đầu và lúc kết thúc lượt rà).

**Căn cứ.** `AGENTS.md` dòng 1–190 và 381–650; `slide_authoring_standard.md`; `CLAUDE.md` của học phần ("Course-specific rules", "Writing", "Deck structure and content"); `../CLAUDE.md` ("Writing course content", "The author's voice", gồm các luật 2026-11-04 và 2026-11-09); quy ước tác giả 2026-10-28/29 (`planning/lec-08/review-log.md` mục "Trang bài toán đầu mạch", `planning/lec-08/danh-gia-giang-day.md` "Định hướng chung"); quy ước của deck làm lại từ ghi chú (Bài 09 ngày 2026-11-04, Bài 10 ngày 2026-11-08): deck là bản tóm lược của ghi chú, ký hiệu theo bảng ký hiệu của ghi chú, mục tiêu khớp ghi chú, trang bài toán có hình sau mỗi trang tiêu đề mạch, chứng minh tách trang, mỗi bài recitation có trang "Lời giải:", dẫn chiếu khối ghi chú và bài tập trỏ đúng khối hiện tại.

**Tác tử (theo lời gọi công cụ).** Vai trò: rà soát chỉ đọc (quy tắc deck mới và đối chiếu ghi chú), một tác tử riêng cho Bài 03; loại `general-purpose`, mô hình `opus` (Opus 5.5), effort `high`; `no-ai-slop` chế độ Detect. Không ghi tệp trong kho, không commit. Mười tác tử của mười bài chạy song song (đều chỉ đọc). Điều phối viên: phiên Opus 5.5.

**Quét cơ học của điều phối viên** (Playwright, 1600×900 và 390×844, máy chủ tĩnh cục bộ): 72 trang, 7 section ngoài; trang tiêu đề mạch `mach-2…7` mở đúng `#/2…7`; 0 lỗi console/trang, 0 request hỏng, 0 `.katex-error`, 0 `fragment`; mã nguồn không có `<style>`, `style=""`, `.dense`; dẫn chiếu `03.k` của deck so với khối hiện có của ghi chú và `exercises.md` (đều tồn tại; loại khối và nội dung do tác tử kiểm). Các cờ quét được tác tử kiểm lại; cờ giả ghi ở mục "Đã kiểm" bên dưới.

**Điều phối viên kiểm lại trên tệp gốc:** Mệnh đề 03.11 (note:621) và Hệ quả 03.16 (note:782) không có trên deck, không trang nào có $\beta^t$; ghi chú diễn giả còn câu "$\Delta_t$ nhỏ không cho biết trực tiếp sai số tới nghiệm", trái Hệ quả 03.16; dẫn chiếu "mục 7, Bài 1", "mục 7, Bài 2" còn trên deck. Đúng như báo cáo.

**Quyết định của điều phối viên:** **chấp nhận** báo cáo làm bảng phát hiện của bài. Mọi phát hiện ở trạng thái **mở**; deck chưa được sửa. Cột "phát hiện" ghi thời điểm phát hiện.

**Kết luận:** cần sửa. Deck soạn 2026-10-14, trước khi ghi chú được viết lại (2026-11-11). Ba lý do chính: deck thiếu các kết quả cốt lõi của Mục 2.4–2.5 trong ghi chú (tính đúng của thuật toán lặp, tốc độ hội tụ, cận sai số khi dừng); ký hiệu và số liệu lệch ghi chú ($T_{\max}$, $p$, $L$, $B$; $H$ 96/84 thay vì 144/132); và deck chưa theo các quy ước mới (không có trang "Lời giải:" cho bài tập recitation, mạch 3–5 thiếu trang bài toán có hình, dẫn chiếu "mục 7, Bài 1–4" không còn tồn tại). Toán và các số tính tay trên deck đều đúng.

**Số phát hiện:** chặn bàn giao 0 · nghiêm trọng 1 · trung bình 12 · nhẹ 14.

Quy ước dẫn: `html:` là dòng trong deck, `note:` là `lecture-note.md`, `ex:` là `exercises.md`, `storyboard:` / `review-log:` là các tệp trong `planning/lec-03/`.

| mức độ | trang chiếu | vấn đề | bằng chứng | đề xuất sửa | phát hiện |
|---|---|---|---|---|---|
| nghiêm trọng | lec03-s03-11, s03-12, s03-14, s07-02, s01-03 | Lệch ghi chú: thiếu nội dung cốt lõi của Mục 2.4–2.5. Không trang nào trình bày Mệnh đề 03.11 (tính đúng của Thuật toán 03.10, bất biến khởi tạo–duy trì–kết thúc), Định lý 03.15(b)(c) (nghiệm duy nhất là phân phối, tốc độ $\lVert r^t-r^*\rVert_1\le\beta^t\lVert r^0-r^*\rVert_1\le2\beta^t$), Hệ quả 03.16 (cận sai số $\beta\Delta_t/(1-\beta)$, chọn $\tau\le(1-\beta)\varepsilon/\beta$) hay Ví dụ 03.13. Đây là mục tiêu 3 của ghi chú. Quy tắc: cụm thuật toán phải có bước "tính đúng bằng bất biến". | note:13 "Chứng minh tổng điểm được bảo toàn và phép lặp hội tụ; dùng độ thay đổi $\Delta_t$ cùng cận sai số để chọn ngưỡng dừng"; note:621–651 (Mệnh đề 03.11 và chứng minh bất biến); note:729–741, 782–794, 811–845. Deck chỉ có hai câu né tránh: html:378 "mô hình đầy đủ cho phép chặn sai số bằng độ thay đổi, nhưng hai đại lượng không bằng nhau"; html:395 chỉ có (a). Hàng "Điều kiện dừng" ở html:867 không có cận. Quyết định cũ storyboard:732 "cận hậu nghiệm β/(1−β)Δ chỉ đọc thêm" trái với ghi chú mới, nơi Hệ quả 03.16 thuộc mạch chính (review-log:681), và storyboard:949 đã ánh xạ Hệ quả 03.16 và Ví dụ 03.13 vào s03-13, s03-14, s03-16 mà các trang này không có. | Thêm "Tính đúng: PageRank lặp" (bảng khởi tạo–duy trì–kết thúc theo note:637–650, kèm phản ví dụ cập nhật không đồng bộ $404/375$, note:655) sau s03-11. Tách s03-14 thành "Định lý (Định lý 03.15)" với (a)–(c) và "Chứng minh: hội tụ". Thêm trang "Cận sai số khi dừng (Hệ quả 03.16)": $\lVert r^{t+1}-r^*\rVert_1\le\frac{\beta}{1-\beta}\Delta_t$, với $\beta=4/5$ hệ số 4. Thêm "Ví dụ: sai số của $r^2$ trên bốn trang": $r^*=(9/28,19/84,19/84,19/84)$, sai số $4/175\le8/25$, 86 vòng cho $\varepsilon=10^{-8}$. Thêm hàng "Cận sai số" vào s07-02 và cập nhật mục tiêu 3. Sửa storyboard:732. | 2026-11-13 |
| trung bình | lec03-s01-03 | Lệch ghi chú: mục tiêu học tập. Deck có 5 mục tiêu, ghi chú có 6 (thêm 1 mục Đọc thêm). Deck không có "giải hệ $r=M_0r$ / hệ có bước nhảy" (mục tiêu 1–2 của ghi chú) và cả mục tiêu 3 (chứng minh bảo toàn, hội tụ, cận sai số). Mục tiêu 4 của ghi chú ghi thêm "đầu vào Reduce có và không có Combine". | note:11–16; html:41–45 ("Đặc tả Map, Combine, Reduce theo khối; lập luận kết quả bằng phép tính một máy"). | Dùng đúng sáu mục tiêu note:11–16, bỏ mục Đọc thêm. Mỗi mục tiêu cần một trang phục vụ: mục 1–2 dùng s07-04/05, mục 3 dùng các trang thêm ở dòng trên. | 2026-11-13 |
| trung bình | lec03-s03-11, s03-12, s06-02, s07-02, s07-08 ($T_{\max}$); s05-01, s05-06 ($p$, $B$); s05-08 ($L$); s03-14 ghi chú ($z$); toàn deck ("véc tơ", $r_A$) | Lệch ghi chú: ký hiệu và thuật ngữ. $T_{\max}$ thay cho $K$; $p$ thay cho $P$; $L$ thay cho $t_{\text{dừng}}$; $B$ là bộ nhớ một tác vụ thay cho $B_{\text{task}}$ (ghi chú dành $B$ cho băng thông của Bài 02); $z_j$ chỉ báo nút cụt trùng chữ với $z=M_0r$, ghi chú dùng $\mathbf 1_{\mathcal D}$; "véc tơ" (44 lần) thay cho "véc-tơ"; tên trang in nghiêng $r_A$ thay cho chữ đứng $r_{\mathrm A}$; "dải tích lũy" thay cho "dải tổng"; "Thành phần chung"/"Chung" thay cho "phần chung". Thuật ngữ: "người đọc", "Bước đi ngẫu nhiên (random walk)" thay cho "người lướt ngẫu nhiên (random surfer)"; "taxation" để nguyên tiếng Anh thay cho "đánh thuế (taxation)"; "Bước nhảy ngẫu nhiên (teleport)" thay cho "bước nhảy (còn gọi là dịch chuyển, teleport)". | note:49 ($K$, $t_{\text{dừng}}$), 57 ($P$), 55, 79 ($B$ không dùng riêng), 44 ($\mathbf 1_{\mathcal D}$), 67 (chữ đứng), 985 (dải tổng), 448 (phần chung), 224, 421; html:351, 377, 766, 867, 877 ($T_{\max}$); html:597 "\(B\): bộ nhớ một tác vụ", 611 "\(p\) máy"; html:697 "\(L\) vòng"; html:400 "\(\bar M=M_0+uz^{\mathsf T}\) với \(z_j=1\)…"; html:214, 217, 290 ("Sách gọi phép biến đổi này là taxation"), 285; html:339, 341; html:631 "dải tích lũy". review-log:710 đã ghi các sai khác này nhưng chưa sửa deck. | Thay toàn deck: $T_{\max}\to K$, $p\to P$, $L\to t_{\text{dừng}}$, $B\to B_{\text{task}}$, $z\to\mathbf 1_{\mathcal D}$ trong ghi chú s03-14, "véc tơ" → "véc-tơ", $r_A\to r_{\mathrm A}$, "dải tích lũy" → "dải tổng", "Thành phần chung" → "Phần chung". Ở s03-01 viết "người lướt ngẫu nhiên (random surfer)". Ở s03-06 viết "Bước nhảy (còn gọi là dịch chuyển, teleport)", và trong ghi chú diễn giả viết "MMDS gọi cách sửa này là đánh thuế (taxation)". | 2026-11-13 |
| trung bình | lec03-s05-05, s07-08 (ghi chú), s05-09 | Lệch ghi chú: số liệu $H$, $C$. Ghi chú định nghĩa $H$ gồm cả $n$ cặp khởi tạo, nên $H$ là 144 → 132 byte, $C$ là 296 → 284 byte, Combine giảm $1/12$ của $H$. Deck lấy $H$ không có cặp khởi tạo: 96 → 84, 248 → 236, "giảm một phần tám". | note:56, 1174 "$H$ tính cả các cặp khởi tạo"; note:1312, 1337–1344; review-log:698 (đã chấp nhận sửa ở ghi chú). html:661–664, 667 "\(C=I+H\) giảm từ \(248\) xuống \(236\) byte", 668 "giảm một phần tám của \(H\)… ví dụ không đếm \(n\) bản ghi khởi tạo"; html:881 "Combine giảm \(H\) từ 96 xuống 84 byte". | Bảng s05-05 dùng ba cột như note:1337: "Cặp từ Map 8/7, cặp khởi tạo 4/4, $H$ 144/132". Caption: "$C=I+H$ giảm từ 296 xuống 284 byte (khoảng 4,1%)". Sửa ghi chú s05-05 ("giảm $12/144=1/12$ của $H$") và s07-08 ("144 xuống 132"). $Q=84$ ở s05-07 giữ nguyên, kèm giả thiết bốn cặp khởi tạo tạo tại máy Reduce (note:1342). | 2026-11-13 |
| trung bình | lec03-s07-04, s07-05, s07-06, s07-07 (ghi chú), s07-T | Lệch ghi chú: dẫn chiếu trỏ tới khối không còn tồn tại. "Lời giải đầy đủ ở ghi chú bài giảng, mục 7, Bài 1…4". Ghi chú mới không có mục 7; bốn bài này là Bài tập 03.8, 03.9, 03.10, 03.7 trong `exercises.md`. | html:944 "mục 7, Bài 1", 959 "mục 7, Bài 2", 972 "mục 7, Bài 3", 986 "mục 7, Bài 4"; html:929 "trong ghi chú bài giảng"; ex:3, 19, 58, 85, 108; storyboard:924, 965 (ánh xạ 03.8 ↔ s07-04, …). | Thay bằng "Lời giải: Bài tập 03.8 (tệp bài tập Bài 03)" cho s07-04; tương tự 03.9 cho s07-05, 03.10 cho s07-06, 03.7 cho s07-07. Sửa storyboard:924. | 2026-11-13 |
| trung bình | lec03-s07-04, s07-05, s07-06, s07-07 | Quy tắc: mỗi bài tập recitation phải có trang "Lời giải:" riêng, cùng tiêu đề (quy ước tác giả 2026-10-28/29; deck mẫu 09 và 10 mỗi deck có 7 trang "Lời giải:"). Deck 03 có 0 trang; lời giải chỉ nằm trong ghi chú diễn giả. | html:932–987 (bốn trang đề, không có trang kế tiếp); grep `Lời giải:</strong>`: deck 03 = 0, deck 09 = 7, deck 10 = 7. | Sau mỗi trang đề, thêm một trang cùng tiêu đề, mở bằng "**Lời giải:**", mỗi dòng một bước, kết bằng một kết luận ngắn. Ví dụ: s07-04 → "$b=4a/3$, $c=2a$; $a+b+c=1$ cho $a=3/13$, $b=4/13$, $c=6/13$". Lời giải lấy đúng ex:66–83, 93–106, 116–128, 34–54. Ghi chú diễn giả của trang lời giải giữ hướng dẫn chấm. | 2026-11-13 |
| trung bình | lec03-s04-01 (mạch 3), s05-01 (mạch 4), s06-01 (mạch 5) | Quy tắc: ngay sau trang tiêu đề mạch phải có trang bài toán có hình minh họa, nêu động lực bằng số liệu có nguồn trong ghi chú. s04-01 chỉ có chữ và thẻ, không có hình. s05-01 chỉ có biểu tượng đại lượng, không có bài toán và không có số. s06-01 không có hình. Lệch ghi chú: s04-01 bỏ các số mở Mục 3 ($m\approx10^{10}$, $4(n+m)=4{,}4\cdot10^{10}$ byte, hai véc-tơ $1{,}6\cdot10^{10}$ byte). s05-01 bỏ câu mở Mục 4 (một máy 8 đơn vị, bốn máy 3 đơn vị). | struct.txt: s04-01 `[-]`, s06-01 `[-]`; html:427–434, 587–613, 726–744; note:915–917, 1167. | s04-01: hình ma trận $10^9\times10^9$ với tỷ lệ ô khác 0 $10^{-8}$, cạnh hai cột byte "đặc $8\cdot10^{18}$ / liên kết ra $4{,}4\cdot10^{10}$", câu dẫn "Muốn …". s05-01: trang bài toán dùng `cost-timeline.svg` thu nhỏ (một máy 8 $c_e$, bốn máy 3 $c_e$), chuyển bốn thẻ đại lượng ra trang sau. s06-01: hình luồng `adj` → `pagerank.py` → JSON so với bảng tính tay. | 2026-11-13 |
| trung bình | lec03-s01-04…s03-10 (mạch 1–2), s06-05 | Lệch ghi chú: các ví dụ và nội dung của ghi chú không có trang phục vụ. Gồm: động cơ thư rác theo từ và trại thư rác (lý do loại cách đếm liên kết vào); Ví dụ 03.6 (lặp thô ba vòng, $r^*=(1/3,2/9,2/9,2/9)$); cấu trúc nơ thắt; bảng ba vòng của Ví dụ 03.7 (tổng $1,3/4,13/24,19/48$) và 03.8 (dãy tiến tới $(0,0,1,0)$); Ví dụ 03.11 (bẫy có bước nhảy, $95/148\approx0{,}64$); Mệnh đề 03.17; Ví dụ 03.24 (ba biến thể, 20/12/34 vòng). s03-05 và s03-06 nêu kết luận nhưng không có số. | note:89–91, 299–315, 348–359, 369–410, 521–542, 849–870, 1591–1602. html:273 "Trên ví dụ này, lặp thô dồn toàn bộ điểm về C."; html:289 "Bước nhảy cho người đọc cơ hội rời bẫy liên kết và tới bất kỳ trang nào."; html:815–818 (chỉ biến thể `base`). | s02-04: thêm một dòng "Nhu cầu:" về trại thư rác (note:91). s03-03: thêm $r^2,r^3$ và $r^*=(1/3,2/9,2/9,2/9)$. s03-04 và s03-05: dùng bảng ba vòng của Ví dụ 03.7 và 03.8. s03-06: thay caption bằng "Với $\beta=4/5$, C giữ $95/148\approx0{,}64$ tổng điểm; mọi trang có điểm dương (Ví dụ 03.11)". s06-05: dùng bảng ba biến thể của Ví dụ 03.24. | 2026-11-13 |
| trung bình | lec03-s07-01, s01-06 (ghi chú) | Lệch ghi chú: câu trả lời cho vấn đề trung tâm thiếu số liệu mà ghi chú đã có. Ghi chú diễn giả viết "chưa đặt giá trị \(m\) vì bài không có số cạnh của web", trong khi ghi chú dùng $m\approx10^{10}$ (MMDS §5.2.1), $S_{\text{adj}}=4{,}4\cdot10^{10}$ byte, và 86 vòng cho sai số $10^{-8}$ (Tình huống 03.1). | html:889 "liên kết ra \(\approx4(10^9+m)\) byte"; html:894 "chưa đặt giá trị \(m\) vì bài không có số cạnh của web"; note:915, 1659–1675, 1704. | Dòng 3 của s07-01: "$n=10^9$, $m\approx10^{10}$: liên kết ra $4{,}4\cdot10^{10}$ byte so với $8\cdot10^{18}$". Thêm vào dòng 2: "86 vòng bảo đảm sai số $10^{-8}$". Bỏ câu "chưa đặt giá trị $m$…". | 2026-11-13 |
| trung bình | lec03-s03-11, s04-05, s04-06, s07-08 | Quy tắc: cụm thuật toán phải có "câu chi phí rồi bảng đếm". Thuật toán PageRank lặp chỉ có một câu trong ghi chú diễn giả ("thời gian tỉ lệ \(n+m\)"), thiếu bảng `Bước \| Số lần \| Chi phí mỗi lần \| Đóng góp` và tổng $3n+m$ của ghi chú. Một vòng theo khối (Thuật toán 03.22) cũng thiếu bảng đếm sáu bước của ghi chú. | html:366; html:877 "\(O(n+m)\) mỗi vòng"; note:573–582 (bảng, "$3n+m$ thao tác, tức $\Theta(n+m)$"), 1049–1058. | Thêm trang "Chi phí: một vòng PageRank lặp" sau s03-12. Dòng "Mô hình:" ghi số lần thực hiện thân vòng lặp; bảng bốn bước theo note:575–580; tổng $3n+m=\Theta(n+m)$; bộ nhớ $16n$ byte. Ở s04-06 hoặc ở mạch 4, thêm bảng đếm của Thuật toán 03.22. | 2026-11-13 |
| trung bình | lec03-s03-14 | Quy tắc: không đặt định lý, chứng minh và hình trên cùng một trang; nội dung phải nằm trong khung. Trang gồm định lý, công thức hiển thị, hình, hai dòng chứng minh và câu kết. Chiều cao nội dung 703 px, bắt đầu ở y = 9, nên đáy ở 712 > đỉnh chân trang 704: câu "Do đó dãy lặp hội tụ…" đè lên chân trang và nút điều hướng ở 1600×900. | Đo trong trình duyệt: `offsetHeight=703`, `offsetTop=9`, chân trang `offsetTop=704`. Ảnh `SP/shots-03/lec03-s03-14-1600.png`. html:393–399. | Tách trang như dòng nghiêm trọng ở trên: trang định lý (phát biểu và hình) và trang "Chứng minh: hội tụ" (ba bước: phần nhảy triệt tiêu; Bổ đề 03.14 cho $\bar M$; $\beta<1$). | 2026-11-13 |
| trung bình | lec03-s03-13 | Quy tắc: tràn khung. Thanh `.mass-bar` rộng 1280 px nhưng bắt đầu ở x = 80 của khung, nên vượt mép phải 80 px; ô "Nhảy: 1/5" bị cắt viền phải ở 1600×900. Cờ quét `overflow_1600` (độ lệch ~19 000 px) do các path SVG của `\underbrace` KaTeX gây ra, đó là cờ giả. Lỗi tràn thật nằm ở thanh này. | Đo: `bar.offsetWidth=1280`, phần tử con cuối `offsetLeft=1023`, `offsetWidth=255`. Ảnh `SP/shots-03/lec03-s03-13-1600.png`. html:387. | Đặt độ rộng thanh theo vùng nội dung (`width:100%` của khối chứa có padding) trong `lecture-course.css`, phạm vi `.lecture-pagerank .complete-mass`, hoặc đặt thanh trong cùng khối với văn bản. Kiểm lại cả s03-04 (thanh nằm trong cột phải, không tràn). | 2026-11-13 |
| trung bình | lec03-s04-08, s05-07 | Quy tắc: giả thiết quyết định phải hiện trên mặt trang. Mệnh đề chia khối trên s04-08 chỉ nêu "cùng \(r\)" và "tập nguồn không chồng nhau". Thiếu "bậc ra toàn cục" và "mỗi trang có đúng một cặp khởi tạo", và cần "phân hoạch" thay cho "không chồng nhau". Ghi chú chỉ ra mỗi giả thiết này có phản ví dụ ($z$ tổng $13/12$; E vắng mặt). s05-07 không nêu điều kiện "mọi byte của $Q$ đi qua một đường nối dùng chung" của cận $Q/b_{\text{eff}}$; bỏ điều kiện này thì cận chỉ còn $42/b_{\text{eff}}$. | html:545, 547–551, 682, 684; note:1092–1098, 1121–1126, 1315, 1354. | s04-08: "**Giả thiết:** $V_1,\ldots,V_k$ là phân hoạch của $V$; bậc ra toàn cục; mọi tác vụ đọc cùng $r$; $\delta$ tính một lần; mỗi trang một cặp $(i,0)$" (Mệnh đề 03.23). s05-07: thêm vào dòng "Mô hình:" vế "mọi byte của $Q$ qua một đường nối dùng chung băng thông $b_{\text{eff}}$". | 2026-11-13 |
| nhẹ | lec03-s04-07 | Lệch ghi chú: ví dụ gộp hai khối. Ghi chú gộp tại B ($1/12$ từ $M_{11}$, $1/8$ từ $M_{12}$, có cặp khởi tạo, $13/60$). Deck gộp tại A, lặp lại đúng hai số $1/8+1/4$ của s03-15. | note:1079–1087; html:536–539, 459–461. | Đổi sang "Ví dụ: bốn trang web, gộp hai khối tại B" với $L_{\mathrm B}=[0,1/12,1/8]$, $z_{\mathrm B}=5/24$, $r^1_{\mathrm B}=13/60$. | 2026-11-13 |
| nhẹ | lec03-s01-05 (mặt trang và ghi chú), s01-06, s05-00, s05-01, s05-03, s05-06, s07-09 (ghi chú) | Quy tắc (văn phong tác giả): có câu nói về xuất xứ số liệu ("giả định", "không phải số đo"). Lệch ghi chú: nguồn của $n=10^9$ là trang chiếu MMDS tr.48, deck ghi CS246 tr.51. | html:82 "Giả định \(n=10^9\) trang"; html:91 "quy mô giả định theo Stanford CS246… nơi mỗi ô dùng 4 byte; bài dùng 8 byte mỗi ô"; html:67 "là giả định của trang chiếu Stanford CS246, không phải số đo"; html:584, 612 "là mô hình suy từ cấu trúc thuật toán, không phải số đo…"; html:639 "công thức là mô hình giả định"; html:677 "\(c_e\) là tham số giả định"; html:916 "chỉ dùng để đối chiếu; mọi hình được vẽ lại"; note:93. | s01-05: "Đồ thị có $n=10^9$ trang; mỗi ô 8 byte." Xóa các câu xuất xứ (ghi vào `review-log.md`). Dòng nguồn ghi "trang chiếu MMDS Chương 5, tr.48". | 2026-11-13 |
| nhẹ | lec03-s01-04, s02-04, s02-07, s03-03, s03-06, s03-12, s03-13, s03-14, s05-05, s05-07, s07-00, s07-04 (ghi chú) | Quy tắc (no-ai-slop Detect; không rào đón về vị thế đoạn văn; giải thích đi thẳng vào ý): có câu nói đoạn văn "chưa phải…", liệt kê điều phủ định, đánh dấu phạm vi. | html:147 "Đây chưa phải kết quả PageRank."; 179 "Kết quả một vòng chưa phải điểm PageRank cuối"; 244 "Chưa suy ra được phép lặp này luôn có giới hạn trên mọi đồ thị"; 290 "xác suất nhảy không đồng nghĩa với xác suất chắc chắn rời một nhóm trang; điều nó bảo đảm là…"; 378 "\(\Delta_t\) không phải sai số so với nghiệm…"; 389 "Bảo toàn tổng không tự nó chứng minh hội tụ"; 400 "không dùng kết luận hội tụ thiếu điều kiện cho ma trận liên kết thô"; 668 "không phải một phần tám thời gian chạy"; 687 "không phải cận dưới cho mọi cách phân bố"; 858 "Không có khái niệm mới."; 75 "Hình chỉ mô tả các vai trò, không mô phỏng toàn bộ một máy tìm kiếm hiện nay"; 944 "Không suy rộng kết luận hội tụ…". | Nói thẳng nội dung dương. Ví dụ: html:378 → "Sai số không quá $\beta\Delta_t/(1-\beta)$, với $\beta=4/5$ là $4\Delta_t$ (Hệ quả 03.16)". html:290 → "Với xác suất $1-\beta$ người lướt chọn đều một trong $n$ trang, nên mọi trang có xác suất tới ít nhất $(1-\beta)/n$". Xóa html:147, 858, 75, 944. | 2026-11-13 |
| nhẹ | lec03-s01-07, s02-07, s03-01, s03-03, s03-13, s04-01, s06-02, s06-05 (ghi chú); s06-06 (mặt trang); s07-T | Quy tắc: không chỉ đường hay dẫn tới mục khác, trừ khi người đọc phải mở chỗ đó để lấy số. | html:35 "ở đầu mạch mô hình"; 179 "được định nghĩa ở mạch tiếp theo"; 218 "được hoàn thiện trước khi phát biểu thuật toán"; 244 "hai biến thể tiếp theo cho thấy…"; 389 "cần lập luận co ở trang kế tiếp"; 433 "Chi phí chi tiết được đếm ở mạch chi phí."; 767 "Kiểm tra đầy đủ nằm trong tệp mã."; 819 "xem practice-README.md"; 832 "kiểm trong practice-README.md"; 929 "Lời giải và hướng dẫn chấm nằm trong…". | Xóa các câu này. Ở s06-06, thay câu caption bằng nội dung của note:1621: "toàn nút cụt: $\delta=1$, mỗi vòng trả lại $u$; khuyên `"A": ["A"]` có $d_{\mathrm A}=1$". | 2026-11-13 |
| nhẹ | lec03-s04-02, s04-07, s06-03, s07-06 (ghi chú) | Quy tắc: không có lời chú của người soạn trong ghi chú diễn giả. | html:452 "Cột của bảng được xếp theo thứ tự trường… khác thứ tự của bảng bậc ra trước đó nhưng cùng dữ liệu"; 540 "Đây là đồ thị gốc, không dùng con số một phần năm của biến thể nút cụt."; 786 "Mã trên trang chiếu trùng khớp mã trong tệp chạy được."; 972 "Ký hiệu \(m\) và \(\rho\) chỉ giúp đặc tả; đề giữ nguyên." | Xóa; nếu cần, chuyển vào `storyboard.md`. | 2026-11-13 |
| nhẹ | lec03-s05-04, s06-05, s06-04 (ghi chú) | Quy tắc (cắt từ làm mềm không có nội dung định lượng): có từ làm mềm và lời đệm trong khi ghi chú đã có số cụ thể. | html:651 "dữ liệu khối thường nằm cục bộ"; 819 "Sai khác làm tròn rất nhỏ có thể xuất hiện giữa môi trường chạy"; 806 "để người dùng biết tình trạng"; note:1612 (A in ra $0{,}32142857064$, lệch $9/28$ khoảng $8\cdot10^{-10}$). | html:819 → "Giá trị in ra của A lệch $9/28$ khoảng $8\cdot10^{-10}$; sai số thật $(2/5)^{20}/7\approx1{,}6\cdot10^{-9}$". html:651 → "$Q$ chỉ đếm phần đi qua mạng; $Q\le H$". | 2026-11-13 |
| nhẹ | lec03-s01-04, s01-06, s07-01 (ghi chú) | Quy tắc: có nhận xét bên lề lặp lại ba lần mà không được dùng tiếp. | html:75, 67 "PageRank chỉ là một tín hiệu xếp hạng; mức phù hợp với truy vấn được đánh giá riêng.", 894 "PageRank đo cấu trúc liên kết, không đo mức phù hợp truy vấn". | Giữ một lần ở s01-04, xóa ở s01-06 và s07-01. | 2026-11-13 |
| nhẹ | lec03-s07-03, s02-08, s03-16, s04-10, s05-09, s02-04, s03-13, s04-06 | Quy tắc: nhãn và tiền tố. (a) Trang "Câu hỏi tự kiểm tra" phải mở bằng "Câu hỏi: trả lời và nêu kết quả đã dùng.". (b) Dòng "Câu hỏi:" không mang thông tin (no-ai-slop: câu dẫn rỗng). (c) "Nhu cầu:" dùng cho một thao tác thử, không phải một nhu cầu. (d) Tiền tố "Tính đúng:" dành cho thuật toán, nhưng s03-13 phát biểu mệnh đề về $F$. (e) Trang thuật toán Reduce thiếu dòng "Đầu ra:". | html:899 "Câu hỏi: vận dụng."; 184 "trên đồ thị bốn trang vừa xét."; 405 "trên mô hình vừa xây dựng."; 565 "vận dụng cách chia khối."; 704 "dùng các công thức chi phí."; 131 "Nhu cầu: thử quy tắc đơn giản nhất là đếm liên kết vào."; 382; 525 (không có Đầu ra). | (a) html:899 → "Câu hỏi: trả lời và nêu kết quả đã dùng." (b) Gộp yêu cầu vào dòng nhãn, ví dụ "Câu hỏi: trên đồ thị A–D, trả lời ba câu sau." (c) "Nhu cầu: một quy tắc chấm điểm từ liên kết; quy tắc đơn giản nhất là đếm liên kết vào." (d) Tiêu đề "Bảo toàn tổng điểm"; thêm "(Mệnh đề 03.13)" sau phát biểu. (e) "**Đầu ra:** cặp $(i,F(r)_i)$ cho mỗi trang $i$". | 2026-11-13 |
| nhẹ | lec03-s02-06, s02-07, s03-09, s03-10, s03-15, s04-02, s04-07, s04-11 | Quy tắc: trang "Ví dụ: …" phải có dòng "Tính …" sau dữ kiện. | html:161–164, 169–170, 323–324, 337–339, 456–457, 437–451, 536–537, 481–485: không có dòng "Tính". s01-05 (html:83) có dòng này. | Thêm một dòng sau dữ kiện, ví dụ s03-09 "Tính $r^1$ với $\beta=4/5$."; s04-11 "Xác định dải điểm cấp cho từng khối." | 2026-11-13 |
| nhẹ | lec03-s04-07 (173), s05-05 (160), s06-02 (157), s06-04 (165), s06-05 (167), s06-06 (160), s07-01 (157), s05-04 (151) | Quy tắc: ghi chú diễn giả dài quá 150 âm tiết trên trang không phải chứng minh hay lời giải. | `scan/03/density.json` (`notes`). | Cắt các câu đã nêu ở các dòng trên (xuất xứ, chỉ đường, lời chú của người soạn); khi cắt, tất cả trang này về dưới 150 âm tiết. | 2026-11-13 |
| nhẹ | lec03-s02-04, s03-01, s03-04, s03-07 (hình); s03-05, s03-14 (mô tả SVG) | Quy tắc: nhãn SVG phải ≥ 18 px ở khung 1280×720. Bốn hình có cỡ chữ nhỏ nhất 24 trên `viewBox` rộng 800, hiển thị rộng 597 px, nên chỉ đạt 17,9 px. `desc` của hai SVG không khớp hình hoặc chứa từ của người soạn. | Đo: `graph-inlinks.svg`, `model-one-round.svg`, `model-dead-end.svg`, `model-dead-redistribute.svg` cho 17,9 px. `img/lec-03/model-spider-trap.svg` desc có "nhãn C tới C đặt trên vòng lặp" nhưng hình không có nhãn đó; `visual-contraction.svg` desc có "Công thức trên slide…". review-log:710. | Nâng `font-size` nhỏ nhất lên 25 trong bộ sinh (`tools/courses/ds-foundation-algorithms/2627-1/img/lec-03/`) rồi sinh lại hình. Sửa hai `desc` cho đúng nội dung hình. | 2026-11-13 |
| nhẹ | lec03-s01-07 | Quy tắc: mọi kết quả của bài trước phải được nhắc lại trước lần dùng đầu. s05-06 dùng thời gian pha $=\max_\nu t_\nu$ và mức tăng tốc $T_1/T_P$ (Định nghĩa 02.30, 02.39); s05-07 dùng cận truyền $Q/B$ (Mệnh đề 02.38). Trang tiên quyết không nhắc lại các kết quả này. | html:30–32; note:28–29. | Thêm vào s01-07: "**Nhắc lại:** thời gian một pha là $\max_\nu t_\nu$; mức tăng tốc $T_1/T_P$; chuyển $Q$ byte qua đường băng thông $B$ cần ít nhất $Q/B$ giây (Bài 02)." | 2026-11-13 |
| nhẹ | lec03-s07-04…s07-07, s07-06, s01-03 (ghi chú) | Lệch ghi chú: thứ tự và chi tiết bài tập recitation. `exercises.md` xếp 03.7 (5.2.2) ở mức nhận biết, trước 03.8–03.10; deck đặt bài này cuối. Đề 03.10 có điều kiện "$n\ge2$", mặt đề s07-06 không có. Ghi chú diễn giả s01-03 gán 5.2.2 cho mục tiêu 1, `exercises.md` gán cho mục tiêu 4 (Mục 3). | ex:7–15, 19, 109; html:964–970, 47. | Đặt s07-07 lên đầu mạch 7. Thêm "$n\ge2$" vào câu hỏi s07-06. Sửa ánh xạ mục tiêu trong ghi chú s01-03 theo bảng ex:7–15. | 2026-11-13 |
| nhẹ | lec03-s03-11, s05-02, s05-03, s07-08 | Lệch ghi chú: đặc tả và công thức. Đầu ra của thuật toán thiếu $t_{\text{dừng}}$ và $\Delta$. Ghi chú viết $S_{\text{adj}}=4(n+m)$ và $B_{\text{task}}=16n/k+B_{\text{buf}}$ là đẳng thức, deck viết "≈". Ghi chú dùng $\Theta(n+m)$, deck dùng $O(n+m)$. | html:352 "véc tơ điểm xấp xỉ và trạng thái"; 621, 634, 879, 877; note:558, 1190–1192, 1253, 582. | html:352 → "**Đầu ra:** $r$, số vòng $t_{\text{dừng}}$, độ thay đổi cuối $\Delta$, trạng thái đạt/chưa đạt ngưỡng". Dùng "=" ở hai công thức byte. Dùng "$3n+m=\Theta(n+m)$". | 2026-11-13 |

### Đã kiểm, không lỗi / bác bỏ cờ quét

- md5 của ba tệp ở đầu và cuối lượt rà trùng nhau (`cbafcb6e`, `0e292b8c`, `8e423c45`). Không sửa tệp nào trong kho.
- Cấu trúc: 7 section ngoài. Các trang tiêu đề mạch `mach-2…7` mở đúng `#/2…7`; số và tên khớp trang "Nội dung" (html:52). Dòng dẫn dài 22–25 âm tiết, mở bằng "Muốn …, phải …"; dòng từ khóa ≤ 5 cụm; ghi chú diễn giả 70–94 âm tiết. Tên mạch khác tiêu đề trang nội dung đầu tiên. Mạch mở đầu đúng thứ tự: bìa có câu luận đề (html:21) → Tiên quyết và quy ước ("Nhắc lại:", "Ký hiệu:", "Quy ước:") → Mục tiêu → Nội dung (đánh số, có "Đọc trước:") → Vấn đề trung tâm (một câu trả lời có điều kiện cho mỗi mạch). Mạch kết luận đủ hai bảng (s07-02, s07-08), trang trả lời vấn đề trung tâm, trang câu hỏi tự kiểm tra có lời giải, trang nguồn có ghi công `http://www.mmds.org`, liên kết viewer và dòng nối sang Bài 04 (html:914). Mỗi mạch nội dung có một trang "Câu hỏi:" và lời giải trong ghi chú diễn giả (s02-08, s03-16, s04-10, s05-09, s06-07).
- Mạch ↔ mục của ghi chú: mạch 1 ↔ §1, mạch 2 ↔ §2, mạch 3 ↔ §3, mạch 4 ↔ §4, mạch 5 ↔ §5. Phần "Đọc thêm: Loại nút cụt đệ quy" không có trang, đúng quy định.
- Đã tính lại mọi số trên deck: s02-07 ($3/8$, $5/24$, tổng 1); s02-08 câu 2 ($1/6+1/12=1/4$); s03-04 ($M_0r^0=(3/24,5/24,5/24,5/24)$, tổng $3/4$); s03-07 ($\beta\delta/n=1/20$); s03-09 ($7/20$, $13/60$); s03-10 (phần chung $1/10$; $1/5$, $4/15$); s03-12 ($r^2=(31/100,23/100,\ldots)$, $\Delta_1=1/25+3/75=2/25$); s03-13 ($3/5$, $1/5$, $1/5$); s03-16 (cột D $(0,1/2,1/2,0)$); s04-03 ($M_0$); s04-04 (7 bản ghi, phân bố 2, 2, 2, 1); s04-05 ($(C,1/12)$, $(D,5/24)$); s04-07 ($r^1_A=7/20$); s05-02 (128, 48 byte); s05-03 (32 byte); s05-04 ($56+32+64=152$; theo tác vụ 24/24/28/12); s05-05 (96/84, 248/236: số học đúng, chỉ lệch định nghĩa $H$); s05-06 ($8/3$; hai máy $4c_e$); s06-04 ($\Delta_0=0{,}2$); s07-01 (điểm cố định $(4/5)(19/168+19/84)+1/20=9/28$); s07-03 (câu 1: $4/5$; câu 4: $4c_e=\max(4,3)c_e$).
- Bài tập recitation khớp `exercises.md`. Đề lấy từ sách và ghi số bài (5.1.1, 5.1.2, 5.2.1, 5.2.2); lời giải trong ghi chú diễn giả trùng ex:66–83 ($3/13,4/13,6/13$), ex:93–106 ($7/27,25/81,35/81$), ex:116–128 ($\rho<1/(2\lceil\log_2n\rceil)$), ex:34–54 (hai bảng liên kết ra); có hướng dẫn chấm.
- Mã trên s06-02…s06-04 trùng `materials/lec-03/code/pagerank.py` (hàm `step`, vòng lặp). Đã chạy `pagerank.py --variant base --beta 0.8 --tol 1e-8 --max-iter 100`: 20 vòng, $\Delta=5{,}4976\cdot10^{-9}$, A $0{,}3214285706$, B–D $0{,}2261904765$, khớp s06-05.
- Mật độ: `over60` có s01-03 (73), s07-02 (71), s07-08 (74), s07-01 (75). Cả bốn là trang mục tiêu hoặc tổng kết có trần 80, đúng storyboard:902; không trang trần 60 nào vượt 60. Không trang nào có quá 3 công thức hiển thị; không có `fragment`, `.dense`, `style=""`, "chúng ta", "ta thấy", "rõ ràng". `style_blocks=1` là cờ giả (thẻ do runtime chèn). Nhãn in đậm trên mặt trang đều thuộc danh sách cho phép (các thẻ `strong` bọc $T_\delta$, … ở s05-08 là tên pha, không phải nhãn).
- Cờ quét `overflow_1600` của lec03-s03-13 (độ lệch ~19 000 px, đáy âm) là cờ giả: phần tử bị gắn cờ là các path SVG của `\underbrace` KaTeX. Trang này vẫn có tràn thật do `.mass-bar` (xem bảng). Đã đo chiều cao không co giãn của cả 72 trang: chỉ s03-14 chạm chân trang (703 px từ y = 9).
- refcheck: deck không dẫn số khối nào của ghi chú (0 đúng, 0 sai). Đây là điều được phép; các dẫn chiếu "mục 7, Bài k" sai đã ghi ở bảng.
- Ảnh chụp (1600×900, 390×844, đã tắt hiệu ứng chuyển trang) nằm trong `SP/shots-03/`: s01-06, s03-08, s03-13, s03-14, s04-04, s04-05, s05-05, s07-01, s07-07, s07-08.

### Quyết định của người dùng (2026-11-13)

- Quyết định của người dùng (2026-11-13): thống nhất thuật ngữ "véc-tơ" cho deck và ghi chú (tên tiếng Anh "vector" chỉ trong ngoặc ở lần dùng đầu). Deck 03 còn "véc tơ" (44 chỗ): đổi thành "véc-tơ".

## Sửa deck theo bảng phát hiện 2026-11-13

**Bối cảnh.** Yêu cầu người dùng (2026-11-13): sửa deck 01–10 theo nguyên tắc deck mới và bảng phát hiện của từng bài, nội dung thống nhất theo ghi chú bài giảng. Căn cứ: bảng phát hiện ở mục trên (27 dòng), quyết định người dùng 2026-11-13 ("véc-tơ"), quyết định G1–G18 và D03 của điều phối viên. Không sửa `materials/`, CSS, deck khác; không commit.

**Tác tử.** Tác tử sửa deck (writer) cho Bài 03, `no-ai-slop` chế độ Edit; loại, mô hình và effort do điều phối viên ghi từ lời gọi công cụ. Bản sao trước khi sửa: `SP/fix/lec-03/backup/`.

**Kết quả.** Deck 72 → 82 trang: 73 trang giảng (120 phút), 9 trang bài tập (60 phút). Thêm s03-17, s03-18, s03-19, s03-20, s03-21, s03-22, s04-12, s07-10, s07-11, s07-12, s07-13; gộp s02-06 vào s02-05; tách s03-14 (định lý) và s03-20 (chứng minh). Chi tiết trang, âm tiết trước/sau và thời lượng ở `storyboard.md`, mục cùng tên.

**Xuất xứ số liệu (ghi một lần, không đưa lên mặt trang).** Quy mô $n=10^9$ trang lấy từ trang chiếu MMDS Chương 5, tr.48; khoảng 10 liên kết ra mỗi trang từ MMDS §5.2.1, tr.190. Mô hình 8 byte mỗi điểm hay ô ma trận, 4 byte mỗi mã trang hay bậc ra, 12 byte mỗi cặp trung gian là mô hình byte của ghi chú (Định nghĩa 03.25). Thời gian $c_e$ mỗi cạnh là tham số mô hình của ghi chú, không có giá trị số. Các phản ví dụ ($404/375$, $13/12$, $6/5$, $97/300$, $18/37$) và Ví dụ 03.13 do ghi chú dựng trên đồ thị MMDS Hình 5.1, 5.3, 5.6.

| phát hiện | xử lý | trang | ghi chú |
|---|---|---|---|
| nghiêm trọng: thiếu Mục 2.4–2.5 (Mệnh đề 03.11, Định lý 03.15(b)(c), Hệ quả 03.16, Ví dụ 03.13) | đã sửa | s03-18, s03-14, s03-20, s03-21, s03-22, s07-02, s01-03, s03-12 | thêm Tính đúng (bảng khởi tạo–duy trì–kết thúc, phản ví dụ $404/375$ trong ghi chú diễn giả), định lý (a)–(c), chứng minh bốn bước, cận $\beta\Delta_t/(1-\beta)$ với $\tau=\varepsilon/4$, ví dụ $4/175\le8/25$ và 86 vòng; hàng "Dừng và cận sai số" ở s07-02; bỏ câu "$\Delta_t$ nhỏ không cho biết trực tiếp sai số"; quyết định cũ storyboard:732 được ghi là đã thay |
| trung bình: mục tiêu học tập lệch ghi chú | đã sửa | s01-03 | sáu mục tiêu theo note:11–16, bỏ mục đọc thêm; 80 âm tiết (đếm tay 11 + 17 + 14 + 15 + 17 + 6); mỗi mục tiêu có trang phục vụ (storyboard, "Mục tiêu → trang phục vụ") |
| trung bình: ký hiệu và thuật ngữ ($T_{\max}$, $p$, $L$, $B$, $z$, "véc tơ", $r_A$, "dải tích lũy", "Thành phần chung", "người đọc", "taxation", "Bước nhảy ngẫu nhiên (teleport)") | đã sửa | toàn deck; s03-01, s03-06, s03-10, s03-11, s05-01, s05-08, s03-20 (ghi chú), s04-11, `cost-memory.svg` | $K$, $P$, $t_{\text{dừng}}$, $B_{\text{task}}$, $\mathbf 1_{\mathcal D}$; "véc-tơ" (0 chỗ "véc tơ"); tên trang trong KaTeX viết `\mathrm`; "dải tổng" cả trong nhãn SVG; "phần chung"; "người lướt ngẫu nhiên (random surfer)"; "Bước nhảy (còn gọi là dịch chuyển, teleport)"; "đánh thuế (taxation)" trong ghi chú diễn giả s03-06 |
| trung bình: $H$ 96/84, $C$ 248/236 thay vì 144/132, 296/284 | đã sửa | s05-05, s07-08 | bảng ba cột theo note:1337 (cặp từ Map, cặp khởi tạo, $H$); caption $C$ 296 → 284 byte, khoảng 4,1%; ghi chú $12/144=1/12$; $Q=84$ ở s05-07 kèm giả thiết cặp khởi tạo tạo tại máy Reduce |
| trung bình: dẫn chiếu "mục 7, Bài 1…4" | đã sửa | s07-04, s07-05, s07-06, s07-07, s07-T | ghi chú diễn giả dẫn Bài tập 03.8, 03.9, 03.10, 03.7; câu "Lời giải và hướng dẫn chấm nằm trong…" của s07-T bỏ |
| trung bình: không có trang "Lời giải:" | đã sửa | s07-10, s07-11, s07-12, s07-13 | mỗi đề có trang kế tiếp cùng tiêu đề, mở bằng "**Lời giải:**", khớp ex:34–54, 66–83, 93–106, 116–128; hướng dẫn chấm ở trang đề, lỗi thường gặp ở trang lời giải |
| trung bình: mạch 3–5 thiếu trang bài toán có hình | đã sửa | s04-01, s05-01, s06-01 | s04-01 "Một tỷ trang trên một máy" với `large-problem.svg` ($10^{-8}$ ô khác 0; $8\cdot10^{18}$, $4{,}4\cdot10^{10}$, $1{,}6\cdot10^{10}$ byte); s05-01 dùng `cost-timeline.svg` (8 và 3 đơn vị) và dòng Ký hiệu thay bốn thẻ biểu tượng, không thêm trang; s06-01 với `practice-flow.svg`. Mạch 6 không có hình đầu mạch (trang mở là bảng kết quả, như T02 của Bài 09) |
| trung bình: ví dụ và nội dung của ghi chú không có trang (thư rác, Ví dụ 03.6, nơ thắt, 03.7, 03.8, 03.11, Mệnh đề 03.17, Ví dụ 03.24) | đã sửa | s01-04, s02-04, s03-03, s03-17, s03-04, s03-05, s03-06, s03-13, s06-05 | thư rác theo từ ở s01-04, trại thư rác ở Nhu cầu s02-04; bảng ba vòng và $r^*=(1/3,2/9,2/9,2/9)$; trang nơ thắt mới; bảng ba vòng của Ví dụ 03.7 và 03.8; caption $95/148\approx0{,}64$; Mệnh đề 03.17 trong ghi chú diễn giả s03-13, s03-20 và cột "Nghiệm chính xác" của s06-05; bảng ba biến thể 20/12/34 vòng |
| trung bình: câu trả lời vấn đề trung tâm thiếu số | đã sửa | s07-01, s01-06 | dòng 2 thêm 86 vòng cho $10^{-8}$; dòng 3 $m\approx10^{10}$, $4{,}4\cdot10^{10}$ byte; bỏ "chưa đặt giá trị $m$"; ghi chú theo Tình huống 03.1 |
| trung bình: thiếu câu chi phí và bảng đếm | đã sửa | s03-19, s04-12, s07-08 | bảng bốn bước, $3n+m=\Theta(n+m)$, $16n$ byte; bảng sáu bước của Thuật toán 03.22 trên trang mới sau tính đúng (s04-06 không đủ chỗ) |
| trung bình: s03-14 dồn định lý, chứng minh, hình; chạm chân trang | đã sửa | s03-14, s03-20 | tách hai trang; ảnh 1600×900 của cả hai nằm trong khung |
| trung bình: `.mass-bar` tràn ở s03-13 | đã sửa | s03-13 | đặt thanh trong `.grid2` cạnh dòng dữ kiện, nhãn "(1) 3/5", "(2) 1/5", "(3) 1/5" (D03, không sửa CSS); ảnh 1600×900 xác nhận thanh nằm trong khung; cờ `overflow_1600` còn lại là cờ giả của `\underbrace` |
| trung bình: thiếu giả thiết quyết định (s04-08, s05-07) | đã sửa | s04-08, s05-07 | s04-08 dòng Giả thiết: dải phân hoạch, bậc toàn cục, cùng $r$, $\delta$ một lần, mỗi trang một cặp $(i,0)$; bốn phản ví dụ trong ghi chú diễn giả; s05-07 dòng Mô hình nêu đường nối dùng chung, ghi chú nêu cận $42/b_{\text{eff}}$ khi bỏ |
| nhẹ: ví dụ gộp khối tại A thay vì B | đã sửa | s04-07 | Ví dụ 03.18: $L_{\mathrm B}=[0,1/12,1/8]$, $z_{\mathrm B}=5/24$, $r^1_{\mathrm B}=13/60$; hình mới `rlarge-merge-b.svg`; `rlarge-merge-a.svg` không còn dùng |
| nhẹ: câu xuất xứ số liệu; nguồn $n=10^9$ | đã sửa | s01-05, s01-06, s05-00, s05-01, s05-03, s05-06, s07-09 | "Giả định" → "Đồ thị có"; bỏ "không phải số đo", "mô hình giả định", "tham số giả định", "chỉ dùng để đối chiếu"; nguồn trang chiếu MMDS tr.48; xuất xứ ghi ở đoạn trên |
| nhẹ: câu rào đón, liệt kê phủ định | đã sửa | s02-04, s02-07, s03-03, s03-06, s03-12, s03-13, s03-14, s05-05, s05-07, s07-00, s07-04, s01-04 | bỏ html:147, 179, 244, 389, 400, 668, 687, 858, 75, 944; html:290 thay bằng câu dương "mọi trang có xác suất tới ít nhất $(1-\beta)/n$"; html:378 thay bằng cận của Hệ quả 03.16 ở s03-21 |
| nhẹ: câu chỉ đường | đã sửa | s01-07, s02-07, s03-01, s03-03, s03-13, s04-01, s06-02, s06-05, s06-06, s07-T | bỏ các câu; caption s06-06 thay bằng trường hợp biên của note:1621 |
| nhẹ: lời chú của người soạn | đã sửa | s04-02, s04-07, s06-03, s07-06 | bỏ cả bốn câu |
| nhẹ: từ làm mềm | đã sửa | s05-04, s06-05, s06-04 | "$Q$ chỉ đếm phần đi qua mạng; $Q\le H$" (s05-04 ghi chú bỏ câu); s06-05 nêu độ lệch $8\cdot10^{-10}$ và sai số thật $1{,}6\cdot10^{-9}$; bỏ "để người dùng biết tình trạng" |
| nhẹ: nhận xét bên lề lặp ba lần | đã sửa | s01-04, s01-06, s07-01 | giữ ở s01-04, bỏ ở hai trang còn lại |
| nhẹ: nhãn và tiền tố (a)–(e) | đã sửa | s07-03, s02-08, s03-16, s04-10, s05-09, s02-04, s03-13, s04-06 | (a) "Câu hỏi: trả lời và nêu kết quả đã dùng."; (b) dòng "Câu hỏi:" mang dữ kiện đồ thị; (c) Nhu cầu nêu trại thư rác; (d) tiêu đề "Bảo toàn tổng điểm" + "(Mệnh đề 03.13)"; (e) "Đầu ra: cặp $(i,F(r)_i)$" |
| nhẹ: trang "Ví dụ" thiếu dòng "Tính" | đã sửa | s02-05, s02-07, s03-09, s03-10, s03-15, s04-02, s04-07, s04-11 | s02-06 gộp vào s02-05; s04-02 "Lập bản ghi…; dựng lại cột A", s04-11 "Xác định dải điểm…" |
| nhẹ: ghi chú diễn giả quá 150 âm tiết | đã sửa | s04-07, s05-05, s06-02, s06-04, s06-05, s06-06, s07-01, s05-04 | sau sửa các trang này 82–136 token; trang dài nhất ngoài chứng minh: s04-08 (165, ghi chú chứng minh và bốn phản ví dụ), s03-20 (168, chứng minh) |
| nhẹ: nhãn SVG dưới 18 px; `desc` sai | đã sửa | s02-04, s03-01, s03-04, s03-07, s01-05, s05-01, s05-06, s03-05, s03-14 | cỡ nhỏ nhất 24 → 25 trong `render_problem.py`, `render_model.py`; `cost-timeline.svg` lên 29–30, `intro-scale.svg` lên 23 (hai hình này cũng dưới 18 px khi đo lại); sửa `desc` của `model-spider-trap.svg`, `visual-contraction.svg`; đo trên mọi trang: 18,2–29,4 px |
| nhẹ: s01-07 thiếu kết quả Bài 02 về thời gian và truyền | đã sửa | s01-07 | dòng "Nhắc lại: $C=I+H$; thời gian pha $\max_\nu t_\nu$; mức tăng tốc $T_1/T_P$; chuyển $Q$ byte cần ít nhất $Q/b_{\text{eff}}$ giây"; mô hình byte chuyển sang mạch 4 để giữ trần 60 |
| nhẹ: thứ tự recitation, "$n\ge2$", ánh xạ mục tiêu | đã sửa | s07-07, s07-06, s01-03 | 03.7 lên đầu mạch 7; đề s07-06 thêm $n\ge2$; ghi chú s01-03 theo bảng ex:7–15 |
| nhẹ: đặc tả và công thức ("Đầu ra", "≈", $O$) | đã sửa | s03-11, s05-02, s05-03, s07-08 | Đầu ra có $t_{\text{dừng}}$, $\Delta$; "=" ở $S_{\text{adj}}$, $B_{\text{task}}$, $4(n+m)$; $3n+m=\Theta(n+m)$ |

**Kiểm G17 (tác tử tự chạy).** `check_deck.py` (máy chủ 8796, 1600×900 và 390×844): 82 trang, 7 section ngoài, 0 lỗi console/trang, 0 request hỏng, 0 `.katex-error`, 0 trùng mã, mọi trang có ghi chú diễn giả, không trang nào quá 3 công thức hiển thị, không cuộn ngang ở 390, `hash_strand` đúng `mach-2…7` ở `#/2…7`, `style_blocks=1` (thẻ runtime), 0 `fragment`; `over60` chỉ gồm các trang trần 80 (s01-03 80, s04-12 78, s07-08 72, s07-01 71, s07-02 65); `overflow_1600` chỉ còn s03-13 với độ lệch 19 033 px (cờ giả `\underbrace`, ảnh chụp xác nhận). `refcheck.py 03`: 118 dẫn chiếu đúng, 0 sai; mỗi mặt trang có tối đa một số hiệu khối. `git diff --check` trên deck, `img/lec-03/`, `planning/lec-03/`: sạch. Ảnh chụp các trang mới và trang sửa nhiều: `SP/fix/lec-03/shots2…4/`.

### Lượt sửa sau kiểm lại (2026-11-13)

Căn cứ: danh sách 17 mục đã duyệt của điều phối viên sau hai lượt kiểm lại (`SP/fix/lec-03/merge-03.md`: 4 trung bình, 13 nhẹ), gồm quyết định thêm trang mở mạch 6 có hình. Cùng tác tử sửa, cùng phạm vi ghi (G18). Deck 82 → 83 trang.

| mục | xử lý | trang |
|---|---|---|
| 1 [TB] thứ tự chứng minh hội tụ; Bước 1 | đã sửa: Bước 3 chỉ cho $\lVert r^t-r^*\rVert_1\le\beta^t\lVert r^0-r^*\rVert_1$; cuối Bước 4: "$r^*$ là phân phối, $\lVert r^0-r^*\rVert_1\le2$, cho (b), (c)"; Bước 1 "ma trận không âm có tổng mỗi cột $\le1$ thì không làm tăng $\lVert\cdot\rVert_1$"; ghi chú diễn giả đổi theo | s03-20 |
| 2 [TB] số $404/375$ sai chỗ | đã sửa: lỗi `r[i] += …` trộn điểm cũ với điểm mới, trái với cập nhật đồng bộ (Mệnh đề 03.11), theo note:1623 | s06-07 (ghi chú) |
| 3 [nhẹ] sai khác cho phép | đã sửa: "cách nghiệm không quá $4\tau$ (Hệ quả 03.16)" | s06-01 (ghi chú) |
| 4 [nhẹ] giả thiết của Hệ quả 03.16 | đã sửa: "Giả thiết như định lý hội tụ" (viết bằng lời vì mặt trang đã có "(Hệ quả 03.16)", tối đa một số hiệu mỗi trang); Ý nghĩa "khi trả trạng thái đạt ngưỡng"; ghi chú "trên số học chính xác" và ba giả thiết | s03-21 |
| 5 [nhẹ] hàng "Dừng và cận sai số" | đã sửa: thêm $0<\beta<1$, cập nhật đồng bộ | s07-02 |
| 6 [nhẹ] điều kiện của $9/28$ | đã sửa: "bốn trang, $\beta=4/5$: $r^*_{\mathrm A}=9/28$" | s07-01 |
| 7 [nhẹ] dòng Ký hiệu | đã sửa: "$S_{\cdot}$ dung lượng", "$I$ đầu vào Map, $H$ đầu vào Reduce, $Q$ byte qua mạng" | s05-01 |
| 8 [nhẹ] $r^0=u$, $t_{\text{dừng}}\le K$, phản ví dụ | đã sửa: thêm $r^0=u$ và $t_{\text{dừng}}\le K$ vào Mệnh đề; phản ví dụ $404/375$ giữ trong ghi chú diễn giả vì thêm dòng sẽ vượt trần 60 (51 → khoảng 65) | s03-18 |
| 9 [TB] trang mở mạch 6 có hình | đã sửa: trang mới `lec03-s07-14` "Xếp hạng một tỷ trang" với `summary-question.svg` (mới), dòng Nhắc lại và dòng "Câu hỏi:", không lời giải; bù 1 phút bằng s07-01 và s07-03 (mỗi trang −0,5); storyboard bỏ lý do "như T02 của Bài 09" | s07-14 |
| 10 [TB] s05-01 dùng chung hình và lộ đáp số | đã sửa: hình dữ kiện mới `four-blocks-data.svg` (bốn khối, cạnh của từng khối, 2, 2, 3, 1 cạnh); caption chỉ nêu dữ kiện; $3c_e$ giữ ở s05-06 | s05-01 |
| 11 [nhẹ] dòng "Tính" | đã sửa: thêm "số vòng để cận (c) đạt $10^{-8}$" | s03-22 |
| 12 [nhẹ] đường băng thông | đã sửa: "chuyển $Q$ byte qua đường băng thông $b_{\text{eff}}$" (60 âm tiết, bằng trần) | s01-07 |
| 13 [nhẹ] mục tiêu 5; "Mục 1" | đã sửa: "đầu vào Reduce có và không có Combine"; bù ở mục tiêu 1 ($\sum_ir_i=1$ bằng công thức) và bỏ "tác vụ"; đếm tay 9 + 17 + 14 + 15 + 19 + 6 = 80; ghi chú "Mục tiêu 1…6" | s01-03 |
| 14 [nhẹ] câu nối sang chia khối | đã sửa: caption "Reduce cho $r^1_{\mathrm A}=7/20$; chia dải dọc thì $z$ dài bằng $r$, gần mỗi số hạng phải đọc ghi đĩa" | s03-15 |
| 15 [nhẹ] câu về tên của Bài 04 | đã sửa: bỏ | s03-06 (ghi chú) |
| 16 [nhẹ] kiểu "X, không phải Y" | đã sửa: s04-09 "$k^2$ tác vụ khối chạy trên số máy tùy chọn; với $k=2$, bốn tác vụ chạy được trên hai máy"; s05-03 bỏ vế phủ định; `alt` của s03-14 viết dương | s04-09, s05-03, s03-14 |
| 17 [nhẹ] dòng dẫn mạch 7; câu thay thế trong storyboard | đã sửa: "Muốn kiểm mô hình điểm và cách lưu đồ thị, phải lập bảng liên kết ra, hệ cân bằng, so hai cách lưu." (23 âm tiết); storyboard ghi mục 2026-11-13 thay mọi mục trang trước đó | s07-T; `storyboard.md` |

**Kiểm G17 sau lượt sửa.** `check_deck.py 8796`: 83 trang, 7 section, 0 lỗi console/trang, 0 request hỏng, 0 `.katex-error`, 0 trùng mã, 0 thiếu ghi chú, `hscroll_390` false, `hash_strand` đúng `mach-2…7`; `over60` chỉ trang trần 80 (s01-03 80, s04-12 78, s07-08 72, s07-01 72, s07-02 69); `overflow_1600` chỉ cờ giả s03-13. `refcheck.py 03`: 121 đúng, 0 sai; tối đa một số hiệu khối mỗi mặt trang. Nhãn SVG mới: `four-blocks-data.svg` 20,1 px, `summary-question.svg` 22,7 px. `git diff --check` trên deck, `img/lec-03/`, `planning/lec-03/`: sạch.

### Kiểm lại và duyệt của điều phối viên (2026-11-13)

**Tác tử (theo lời gọi công cụ).** Sửa deck: `general-purpose`, `opus` (Opus 5.5), effort `high`, `no-ai-slop` chế độ Edit; lượt sửa sau kiểm lại do cùng tác tử (tiếp tục bằng `SendMessage`). Kiểm lại vai A (độ chính xác và khớp ghi chú) và vai B (mạch, cấu trúc, văn phong, `no-ai-slop` Detect): mỗi vai một tác tử `general-purpose`, `opus` (Opus 5.5), effort `high`, chỉ đọc.

| vai | kết luận | phát hiện (chặn/nghiêm trọng/trung bình/nhẹ) | quyết định |
|---|---|---|---|
| A | cần sửa | 0/0/2/6 | chấp nhận; thứ tự chứng minh s03-20 (cận 2 cần $r^*$ là phân phối, note:260–271) và con số $404/375$ gán sai ở s06-07 (note:655, 1623). Tám mục vào `merge-03.md` |
| B | cần sửa | 0/0/2/8 | chấp nhận; mạch 6 thêm trang mở có hình (như Bài 08–10), s05-01 không dùng chung hình và không lộ đáp số của s05-06. Chín mục vào `merge-03.md` |

Lượt sửa sau kiểm lại: 17/17 mục làm; s03-21 ghi giả thiết bằng lời (một số hiệu khối mỗi trang); phản ví dụ $404/375$ ở s03-18 giữ trong ghi chú diễn giả vì trần 60 — chấp nhận. Trang mới s07-14 "Xếp hạng một tỷ trang" (hình `summary-question.svg`), hình dữ kiện mới `four-blocks-data.svg` cho s05-01. Nhịp mạch 2 khoảng 1,77 phút/trang (bốn trang chứng minh mới) — chấp nhận. `rlarge-merge-a.svg` không còn trang nào dùng: xóa trong commit này. Đề nghị sửa ghi chú để lại cho người dùng: note:1291 (alt "dải tích lũy" → "dải tổng"), note:1542 ("không quá ngưỡng" → "không quá $4\tau$").

Kiểm của điều phối viên sau lượt sửa: `check_deck.py` (Playwright, 1600×900 và 390×844) 83 trang, ID không trùng, 0 lỗi console/trang, 0 request hỏng hoặc ra ngoài, 0 `.katex-error`, không cuộn ngang ở 390 px, `#/2…7` mở đúng `mach-2…7`; cờ `overflow_1600` ở s03-13 là path SVG của `\underbrace` (điều phối viên xem ảnh: thanh khối lượng nằm trong khung); năm trang trên 60 âm tiết đều thuộc loại trần 80 (s01-03 80, s04-12 78, s07-02 69, s07-08 72, s07-01 72). `refcheck.py`: 121 dẫn chiếu, 0 sai. `git diff --check` sạch. Điều phối viên tự xem ảnh s03-13, s07-14 (1600×900).

Quyết định: **chấp nhận**; mọi phát hiện của bảng 2026-11-13 đã đóng.

## Sửa ghi chú theo đề nghị của đợt sửa deck (2026-11-13)

| mục | thay đổi | vị trí |
|---|---|---|
| Alt hình cost-memory | "dải tích lũy z_a" → "dải tổng z_a", khớp bảng ký hiệu, Định nghĩa 03.21 và nhãn "Dải tổng z_a" trên hình; không còn "dải tích lũy" trong ghi chú | `materials/lec-03/lecture-note.md` dòng 1291 |
| Mở đầu Mục 5 | "sai khác không quá ngưỡng đã chọn" → "Theo Hệ quả 03.16 với $\beta=4/5$, khi chương trình đạt ngưỡng $\tau$, véc-tơ trả về cách nghiệm $r^*$ không quá $4\tau$."; khớp hệ số $\beta/(1-\beta)=4$ sau Hệ quả 03.16 và ghi chú diễn giả của deck | `materials/lec-03/lecture-note.md` dòng 1542 |
| Mở đầu Mục 5, sửa theo duyệt của điều phối viên | Câu ở dòng trên khẳng định kết quả dấu phẩy động trùng nghiệm tính tay và bỏ điều kiện số học chính xác của Hệ quả 03.16. Sửa thành "… phải cho lại các con số đó trong một dung sai. Theo Hệ quả 03.16 với $\beta=4/5$, trên số học chính xác, khi thuật toán dừng vì đạt ngưỡng $\tau$, véc-tơ trả về cách $r^*$ không quá $4\tau$. Phép làm tròn còn có thể làm kết quả khác ở các chữ số cuối."; khớp dòng 1133 ("có thể khác ở các chữ số cuối", "Phép so sánh dùng dung sai") và Nhận xét 03.18 ("trên số học chính xác") | `materials/lec-03/lecture-note.md` dòng 1542 |

Người dùng duyệt các đề nghị sửa ghi chú ngày 2026-11-13.

### Kiểm lại và duyệt của điều phối viên (2026-11-13)

| vai trò | loại tác tử | mô hình | effort | kết quả |
|---|---|---|---|---|
| sửa ghi chú | general-purpose | opus (Opus 5.5) | high | chấp nhận |
| kiểm lại độ chính xác, mạch, no-ai-slop Detect (chỉ đọc) | general-purpose | opus (Opus 5.5) | high | đạt, một mục trung bình ở note:1542 |

Điều phối viên đối chiếu từng thay đổi với tệp nguồn (nhãn SVG, bảng ký hiệu, số bài recitation trong deck). Kiểm lại yêu cầu sửa note:1542 (dấu phẩy động, Hệ quả 03.16 chỉ đúng trên số học chính xác); tác tử sửa đã sửa, điều phối viên chấp nhận. Kiểm trình xem ở 1600×900 và 390×844: không lỗi console, không yêu cầu hỏng, 0 `.katex-error`, ảnh tải đủ; `git diff --check` sạch. Chấp nhận.
