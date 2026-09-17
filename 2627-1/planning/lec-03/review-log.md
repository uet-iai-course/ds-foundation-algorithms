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
