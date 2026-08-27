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
- Chromium không giao diện duyệt đủ 38 trang ở khung $1280\times720$ và $800\times600$: không có lỗi bảng điều khiển, lỗi yêu cầu tài nguyên hoặc phần tử tràn khung. Ảnh liên hệ toàn bộ trang và các trang C07, E01–E05, R04 được kiểm tra trực quan.
- Kiểm tra tĩnh xác nhận 38 mã trang duy nhất, 38 ghi chú, 45 cặp thẻ `section`, mọi đường dẫn cục bộ tồn tại, năm SVG hợp lệ và không có tham chiếu ảnh raster.
- Dự án Codex Slides bền vững `20260827151722-b-i-3-pagerank-m-h-nh-v-t-nh-to-n-edg9` vẫn ở trạng thái nháp với 0 trang. Trình duyệt tích hợp không khả dụng trong phiên này; bốn lần tải tệp thiết kế cuối vào dự án đều trả HTTP 500. Vì vậy chưa thể tuyên bố bản RevealJS đã được rà trực quan trong Codex Slides. URL bàn giao của dự án: `http://127.0.0.1:4311/project/20260827151722-b-i-3-pagerank-m-h-nh-v-t-nh-to-n-edg9?mode=workspace&checkpoint=clarify`.
