# Nhật ký rà soát Bài 12

## Trạng thái bản nháp

- HTML: `2627-1/lecture-12-mo-hinh-io-va-sap-xep-ngoai-bo-nho.html`.
- Giữ 53 trang theo đúng thứ tự nguồn đã biên tập: 46 trang giảng và 7 trang recitation.
- Bảy `<section>` ngoài gồm mở bài, mô hình I/O, thuật toán trộn ngoài, đầu ra và chi phí, chọn thay thế, kết luận, recitation.
- Phần giảng giữ 120 phút; recitation giữ 60 phút. Thời lượng chỉ nằm trong storyboard, không nằm trong ghi chú diễn giả.
- `2627-1/index.html` đã có đúng một thẻ Bài 12 và liên kết đúng tới HTML. Không sửa tệp chỉ mục.
- Bản nháp đã qua kiểm định storyboard, năm báo cáo độc lập và một lượt chỉnh sửa hợp nhất. Chưa chạy QA trực quan cuối.

## Báo cáo lập kế hoạch

Kế hoạch được chấp nhận theo hướng sửa cục bộ, giữ 53 trang và thứ tự hiện tại. Rủi ro chính là tám wrapper ngoài, thời lượng trong notes, dẫn nguồn bài tập thiếu số trang PDF, lịch ba khung của bài 15.1 dễ bị hiểu thành quy tắc tổng quát, công thức đệm dài thiếu miền và nhận định $2H$ dễ bị gán giả thiết quá mức cho nguồn Wisconsin.

## Báo cáo phân tích nguồn và quyết định

| Mức độ | Trang chiếu | Vấn đề | Bằng chứng | Quyết định bản nháp |
|---|---|---|---|---|
| chặn bàn giao | Toàn bài | Có tám wrapper ngoài | `Q00–Q02` và `S12–S17` là hai wrapper liên tiếp nhưng cùng một tuyến điều kiện đầu ra → công thức chi phí | Gộp hai wrapper, không đổi thứ tự hoặc số trang; còn bảy mạch ngoài. |
| nghiêm trọng | 53 notes | Notes chứa thời lượng | Mỗi notes có một mốc phút hoặc tổng thời lượng | Xóa toàn bộ thời lượng khỏi notes; giữ bảng 120+60 trong storyboard. |
| nghiêm trọng | I03 | Dẫn Chương 13 trang 19 không hỗ trợ đóng gói bản ghi | Trang 19 nói về khối/đệm; bản ghi cố định và không vượt biên khối nằm ở trang 2–3 | Đổi nguồn I03 sang Chương 13, trang chiếu 2–3. |
| nghiêm trọng | X05, X06 | Dẫn bài tập/lời giải thiếu hoặc sai trang PDF | Bài 15.9 ở đề PDF 2/tr. 48, lời giải PDF 5/tr. 115; bài 13.5 ở đề PDF 2/tr. 42, lời giải PDF 5/tr. 95 | Sửa HTML, outline và storyboard theo bốn mốc này. |
| nghiêm trọng | X03 | Lịch luân phiên ba khung có thể bị hiểu là mô tả nguyên văn hoặc $k=B$ tổng quát | Nguồn chỉ cho dữ kiện một tuple/khối và kết quả trộn ba dãy | Ghi rõ lịch triển khai được suy ra từ dữ kiện một tuple/khối; không khái quát thành $k=B$. |
| nghiêm trọng | S16 | Hai công thức fan-in thiếu miền và lẫn nguồn với suy ra | Bài 15.9 chỉ nêu đánh đổi định tính | Thêm $b_b\in\mathbb{Z},b_b\ge1$, điều kiện $k\ge2$; ghi rõ công thức được suy ra từ phân bổ khung. |
| nghiêm trọng | R08 | Gán mô hình xác suất chi tiết cho Wisconsin | Wisconsin chỉ nêu độ dài trung bình khoảng hai lần bộ nhớ | Chỉ quy nhận định trung bình cho nguồn; deck giới hạn sử dụng khi thứ tự đến giống ngẫu nhiên và luồng đủ dài, không coi là bảo đảm. |
| trung bình | R05 | Kết quả ba dãy không có nguồn | Vết kết hợp dữ liệu bài 15.1 với cơ chế Wisconsin | Ghi cả nguồn dữ liệu, nguồn cơ chế và trạng thái chạy lại. |

## Kiểm định storyboard

| mức độ | trang chiếu | vấn đề | bằng chứng | đề xuất sửa |
|---|---|---|---|---|
| trung bình | T01, X00–X03 | Quy ước số đường trộn chưa được bàn giao rõ từ kết luận sang bài 15.1. | T01 dùng $k=B-1$ theo một khung đầu ra; X03 theo lời giải nguồn lại trộn ba dãy bằng ba khung. | Giới hạn $k=B-1$ theo mô hình; gọi X03 là biến thể nguồn và đối chiếu hai lịch. Rà T00–T01, X00–X04. |
| trung bình | R00–R02 | Cầu nối định lượng từ khung sang heap đổi đơn vị mà chưa giải thích. | R00 dùng $B$ khối; R01–R02 chuyển sang $H$ bản ghi. | Nêu $H$ là số bản ghi vừa vùng heap; chỉ trong vết một bản ghi/khối mới có $H=B=3$. Rà S17–R03. |

Quyết định: áp dụng cả hai. Không đổi thứ tự trang; thêm điều kiện mô hình tại T01/X03 và cầu nối đơn vị tại R00–R01.

## Báo cáo độc lập 1 — Góc nhìn sinh viên

| mức độ | trang chiếu | vấn đề | bằng chứng | đề xuất sửa |
|---|---|---|---|---|
| trung bình | S06–S08 | Ví dụ dừng ở lần chọn `emu`, chưa cho thấy refill/flush trước bất biến và giả mã. | Người học phải tự suy ra cách khung đầu vào cạn và khung đầu ra đầy được xử lý. | Thêm một vết chọn–refill–flush tại S06. |
| trung bình | S16, S17, X05 | Hai công thức $b_b$ chưa có phép thế định lượng. | S16 chỉ đưa công thức; S17 quay về trường hợp $b_b=1$; X05 chỉ hỏi định tính. | Thêm một phép thế ngắn tại S16 hoặc đổi bài kiểm tra. |
| trung bình | X03 | Ngoại lệ ba khung nằm trong chữ nhỏ, chưa có bảng trạng thái. | Mặt slide chưa buộc người học nêu giả thiết một tuple/khối hoặc đối chiếu S08. | Làm nổi biến thể và cho hai–ba bước trạng thái. |
| trung bình | I05–I08 | `Bẩn` và `nạn nhân` chưa được định nghĩa trên mặt slide. | I08 dùng `A bẩn`; I05 chỉ giải thích trong notes. | Định nghĩa khối bẩn và giải thích khung nạn nhân trước vết. |
| nhẹ | P01, R01, R06 | Tiên quyết hàng đợi ưu tiên và logarit chưa được báo. | R06 dùng heap và $O(\log H)$ ngay. | Thêm nhắc tiên quyết ngắn ở P01/notes. |
| nhẹ | X01, X03, X04 | Dữ liệu hoặc đáp án dài ở cỡ chữ nhỏ. | X01 có 12 tuple trên một dòng; X04 có 12 khóa trên một dòng. | Chia dữ liệu và đáp án thành nhiều dòng. |

Quyết định: áp dụng toàn bộ. S16 dùng phép thế $B=11,b_b=2$ thay vì đổi S17; I05 định nghĩa khối bẩn trên mặt slide và giải thích nạn nhân trong notes; X01/X04 được chia dòng.

## Báo cáo độc lập 2 — Chuyên gia giải thuật và khoa học dữ liệu

| mức độ | trang chiếu | vấn đề | bằng chứng | đề xuất sửa |
|---|---|---|---|---|
| trung bình | S15, T00–T01 | Chi phí CPU chưa chốt cho toàn bộ các lượt trộn. | Mặt S15 chỉ nêu $O(n\log k)$ mỗi lượt; kết luận chưa thu hồi chi phí. | Hiển thị $O(np\log k)$ cho phần trộn và tách chi phí sắp mẻ đầu trong notes. |
| trung bình | I06–I07, S16, X05 | Quan hệ truyền khối–seek mới dừng ở định tính. | Hai lịch có thể có cùng số truyền nhưng khác số đoạn tuần tự. | Giữ mô hình $n_Tt_T+n_St_S$ trong lời giảng và nối S15–S16–X05. |
| trung bình | X03 | Sản phẩm chưa buộc nêu giả thiết một tuple/khối và đối chiếu mô hình chung. | Đáp án nguồn trộn ba dãy trong khi phần giảng dùng $k=B-1$. | Thêm giả thiết, trạng thái khung và câu không khái quát thành $k=B$. |
| nhẹ | I00, Q00–Q02, T00 | Kết luận chưa thu hồi tình huống `ORDER BY` và lựa chọn đầu ra. | T00 chỉ liệt kê đại lượng, không trở lại toán tử nhận. | Thu hồi `ORDER BY`, vật chất hóa và truyền dòng tại T00–T01. |

Quyết định: áp dụng các sửa hiển thị và câu nối. Không thêm công thức thời gian mới lên mặt slide vì nguồn chỉ hỗ trợ đánh đổi định tính; giữ diễn giải số truyền và số seek tách biệt trong notes và bài X05.

## Báo cáo độc lập 3 — Độ chính xác toán học và thuật toán

Không phát hiện lỗi `nghiêm trọng` hoặc `chặn bàn giao`.

| mức độ | trang chiếu | vấn đề | bằng chứng | đề xuất sửa |
|---|---|---|---|---|
| trung bình | S01, S03, S05, S09–S11 | Đặc tả chưa đặt điều kiện trước về $B$. | Tạo dãy cần $B\ge1$; nếu $N>B$, $B=2$ cho $k=1$ nên số dãy không giảm, còn $B=1$ cho $k=0$. | Nêu $B\ge1$ và nếu $N>B$ thì mô hình cần $B\ge3$. |
| trung bình | Q02, S13 | Chi phí truyền dòng bỏ trống trường hợp $p=0$. | Với $N=0$, chi phí bằng 0; với $0<N\le B$, đọc $N$ khối, sắp trong bộ nhớ rồi truyền trực tiếp. | Viết công thức từng trường hợp trước công thức $N(2p+1)$ cho $p\ge1$. |
| nhẹ | R08 | Giả thiết xác suất cho nhận định $2H$ chưa đủ hình thức. | Wisconsin chỉ nêu độ dài trung bình khoảng $2H$; nguồn không đặc tả không gian xác suất hay độc lập. | Tách mệnh đề của Wisconsin khỏi giới hạn sử dụng của bài giảng; không quy điều kiện “luồng đủ dài có thứ tự đến giống ngẫu nhiên” cho nguồn. |

Quyết định: áp dụng toàn bộ. Chạy lại xác nhận $r_0=4,k=2,p=2$, $C_{\mathrm{mat}}=72$, $C_{\mathrm{pipe}}=60$; S17 cho $4,16,2,480$; hai công thức fan-in S16 đúng; vết chọn thay thế cho ba dãy dài $7,3,2$ đúng đa tập.

## Báo cáo độc lập 4 — Phản biện học thuật và giảng dạy

| mức độ | trang chiếu | vấn đề | bằng chứng | đề xuất sửa |
|---|---|---|---|---|
| nghiêm trọng | S05, S08–S10, X03 | Bài tập dùng lịch ba dãy không theo thuật toán vừa hình thức hóa. | S08 dành một khung đầu ra nên $k=B-1$; lời giải 15.1 trộn ba dãy với ba khung. | Gọi X03 là biến thể nguồn, đối chiếu S08 và chứng minh bằng trạng thái khung. |
| trung bình | I04, S00, S04–S05, S11 | Công thức $k,r_0,p$ xuất hiện sớm so với ví dụ. | $k$ được giới thiệu ở I04 trước đặc tả và ví dụ trộn. | Cân nhắc hoãn $k$ hoặc bỏ công thức khỏi sơ đồ mở pha. |
| trung bình | S06–S08 | Chứng minh đứng trước thao tác refill/flush tổng quát. | S06 mới chỉ chọn đầu nhỏ nhất; S07 nêu bất biến rồi S08 mới cho refill/flush. | Thêm vết refill/flush tại S06 hoặc đổi thứ tự. |
| trung bình | S01–S04 | Đặc tả đứng trước ví dụ chạy tay. | Chu trình ưu tiên ví dụ trước hình thức hóa. | Cân nhắc đưa S02 trước S01. |
| trung bình | S16–S17, X05 | Công thức đệm dài chưa nối sang quyết định tham số. | Không có phép thế để thấy fan-in đổi thế nào. | Thêm so sánh số ngắn và nối sang X05. |
| nhẹ | I05–I09 | Bộ quản lý đệm có nguy cơ thành nhánh phụ. | Cụm trúng/trượt chưa nối rõ với lần ghi bẩn ở I08. | Nối I05 với vết I08 và bài X06. |
| nhẹ | T00–T01 | Kết luận chưa thu hồi chuỗi phụ thuộc và $H$. | Các đại lượng xuất hiện như danh sách, không thành quan hệ. | Thu hồi $B\to(r_0,k)\to p\to C$ và vai trò $H$. |

Quyết định: xử lý lỗi nghiêm trọng và mọi cầu nối. Không đổi thứ tự S01/S02 hoặc S07/S08: S01 xác lập sản phẩm để kiểm ở S02; vết mới tại S06 đủ nối thao tác sang bất biến rồi giả mã. Không hoãn $k$ khỏi I04 vì đó là hệ quả trực tiếp của phân bổ khung và được kiểm ngay ở I09; S01 nay đặt đầy đủ điều kiện trước.

## Báo cáo độc lập 5 — Kết nối và mạch viết

| mức độ | trang chiếu | vấn đề | bằng chứng | đề xuất sửa |
|---|---|---|---|---|
| trung bình | P02 | Bản đồ đặt chọn thay thế trước đầu ra/chi phí, khác thứ tự deck. | Vai trò trong mạch là báo lộ trình; kết nối ra hiện dẫn sai sang R trước Q/S. | Đổi vị trí hai thẻ để khớp thứ tự thật. |
| trung bình | S11→Q00 | Thiếu câu nối từ số lượt sang điều kiện đầu ra. | Vai trò S11 là cho $p$; Q00 cần biết lần ghi cuối nhưng kết nối vào chưa nêu. | Thêm câu “biết $p$ chưa đủ; còn phải chốt lần ghi cuối”. |
| trung bình | S15→S16 | Thiếu tín hiệu từ ba loại chi phí sang đánh đổi seek–fan-in. | Vai trò S15 là tách chi phí; S16 đổi đệm nhưng chưa nhận đầu vào “cùng transfers, khác seeks”. | Thêm câu nối về số lần định vị. |
| trung bình | T00–T01 | Kết luận chưa thu hồi `ORDER BY`, toán tử nhận và lựa chọn đầu ra. | Vai trò kết luận là đóng tình huống I00; kết nối ra X00 mới chỉ là quy trình công thức. | Thu hồi use case và quyết định vật chất hóa/truyền dòng. |
| nhẹ | S16→S17→R00 | Ký hiệu $b_b$ đứng riêng trước khi chuyển sang chọn thay thế. | Kết nối ra chưa nói đổi $k$ và giảm $r_0$ đều tác động lên $p$. | Thêm câu chuyển chung theo mục tiêu giảm $p$ và nhắc X05 luyện đánh đổi. |

Quyết định: áp dụng toàn bộ bằng sửa P02, câu nối trên mặt slide hoặc notes và kết luận mới. Giữ bảy section; mạch Q00–S14 không lặp chức năng. Do thay câu chuyển tại bốn ranh giới và sửa luận điểm kết luận, yêu cầu vai kết nối rà lại toàn deck theo AGENTS.md.

## Lượt chỉnh sửa hợp nhất sau rà soát

- Không thêm, bỏ hoặc đổi thứ tự trang; vẫn có 53 trang và bảy section ngoài.
- Thay đổi luận điểm/câu chuyển tại P02, S11→Q00, S15→S16, S16→S17→R00 và T00–T01.
- Bổ sung đặc tả ở S01; trường hợp biên truyền dòng ở Q02/S13; vết refill/flush ở S06; phép thế ở S16; cầu nối $B/H$ ở R00–R01; tại R08 tách nhận định $2H$ của Wisconsin khỏi giới hạn sử dụng do bài giảng đặt ra.
- X03 nay là “biến thể ba khung của nguồn”, có ba bước trạng thái và sản phẩm chứng minh; ghi rõ không phải `mergeGroup` S08. X01 và X04 chia dữ liệu/đáp án thành nhiều dòng.
- Cần rà lại độ chính xác S01, Q02–S14, S16, R00–R08, T00–T01, X01–X04; rà mạch toàn deck vì kết luận và nhiều ranh giới đã đổi.

## Bảy mạch và quyết định không gộp trang

Wrapper `Q00–Q02` được nối trực tiếp với `S12–S17`, tạo mạch “đầu ra và chi phí”. Câu nối là: điều kiện sau quyết định lần ghi cuối, rồi mới dẫn xuất $C_{\mathrm{mat}}$ và $C_{\mathrm{pipe}}$.

Bốn cặp được cân nhắc nhưng không gộp:

- `I01/I02`: hệ phân cấp truyền dữ liệu khác với phân biệt bản ghi–khối;
- `I06/I07`: lần truyền khối khác lần định vị;
- `Q01/Q02`: thời điểm có thể phát dòng khác điều kiện sau của thuật toán;
- `R06/R07`: giả mã khác mệnh đề và chứng minh tính đúng.

Gộp các cặp này sẽ đặt hai luận điểm trung tâm hoặc giả mã với chứng minh trên cùng trang. Bản nháp giữ riêng để tránh tăng tải nhận thức.

## Sai khác có chủ ý so với nguồn

- Chuẩn hóa $B$ thành tổng số khung; trộn tổng quát dành một khung đầu ra nên $k=B-1$.
- Dùng $H$ cho sức chứa heap theo bản ghi để không đổi đơn vị của $B$.
- Dùng chuỗi 12 bản ghi của bài 15.1 xuyên suốt phần giảng; không đổi dữ kiện hoặc thứ tự đầu vào.
- Lịch ba khung ở recitation là diễn giải suy ra từ một tuple/khối và kết quả lời giải; phần giảng vẫn dùng quy ước tổng quát $k=B-1$.
- Hai công thức tại S16 là suy ra từ cách phân bổ khung. Nguồn bài 15.9 chỉ hỗ trợ đánh đổi giữa seek và số dãy trộn đồng thời.
- Đưa vật chất hóa/truyền dòng trước công thức chi phí và ví dụ trước giả mã để giữ chu trình học tập.

## Ảnh hưởng của kỹ năng biên tập

- `no-ai-slop`: giữ câu ngắn, trực tiếp; cắt nhãn quy trình và thời lượng khỏi notes; không thêm số liệu hoặc kết luận ngoài nguồn. Bản cuối của lượt soạn được đối chiếu `eval.md`.
- Quill: rà mạch $N,B,k,r_0,p$; giữ $H$ riêng cho chọn thay thế và $b_b$ riêng cho biến thể đệm dài; kiểm tra câu nối giữa điều kiện đầu ra và chi phí. Không tạo `quill.json`.

## Kiểm tra tĩnh của bản nháp

- HTML có 53 mã trang duy nhất, 53 ghi chú diễn giả và đúng bảy `<section>` ngoài.
- Ghi chú không còn thời lượng hoặc mã trang nội bộ; storyboard phủ đủ 53 mã trang.
- Tám SVG đều phân tích được bằng bộ phân tích XML, có `role="img"` và mô tả tiếp cận.
- HTML không tham chiếu ảnh raster, tài nguyên mạng hoặc đường dẫn ảnh thiếu.
- `git diff --check` đạt; không tạo `quill.json`.

## Rà lại sau chỉnh sửa

- Độ chính xác toán học và thuật toán: đạt sau khi tách tại R08 nhận định trung bình khoảng $2H$ của Wisconsin khỏi giới hạn sử dụng do bài giảng đặt ra. Các điều kiện của $B$, trường hợp $p=0$, hai công thức fan-in, chi phí 72/60, vết chọn thay thế và lịch ba khung của bài 15.1 đều được chạy lại.
- Kết nối và mạch viết: đạt sau khi rà toàn bộ bảy mạch. Mở bài `ORDER BY` được thu hồi tại T00–T01; các ranh giới S11→Q00, S15→S16, S17→R00 và R09→T00 đều có đầu vào–đầu ra rõ.
- Rà cục bộ cuối R06–T00: đạt; bản vá R08 không tạo bước nhảy hoặc gán giả thiết xác suất cho nguồn.

## Kiểm định cuối

- Kiểm tra tĩnh: 53 trang, 53 mã duy nhất, 53 ghi chú, bảy `<section>` ngoài và 53 hàng storyboard khớp hoàn toàn. Không có mốc thời lượng hoặc mã nội bộ trong ghi chú.
- Tài nguyên: tám SVG đều là XML hợp lệ, có `role="img"` và `title` hoặc `desc`; không có ảnh raster, URL mạng cốt lõi, đường dẫn thiếu hoặc liên kết planning trên chỉ mục. `index.html` có đúng một liên kết tới Bài 12.
- Cấu hình RevealJS giữ `lang="vi"`, 1280×720, `controlsLayout: "edges"`, số trang, chỉ số băm một gốc, băm URL và các plugin cục bộ KaTeX, Notes, Highlight.
- Lệnh bắt buộc `python3 -m reloadserver 8765` không chạy vì môi trường thiếu mô-đun `reloadserver`. Kiểm định trình duyệt dùng máy chủ cục bộ tương đương tại cổng 8765.
- Chromium/Playwright duyệt đủ 53 trang tại 1280×720 và 800×600: không lỗi console, không lỗi KaTeX, không tràn hoặc chồng lấn theo kiểm tra hình học. Contact sheet và các trang thay đổi nhiều S13, S16, X01, X03, X04 đã được xem trực quan.
- Điều hướng bàn phím đạt: P00 `(0,0)` → phím phải I00 `(1,0)` → phím xuống I01 `(1,1)`.
- Dự án Codex Slides bền vững `20260828001844-b-i-12-m-h-nh-i-o-v-s-p-x-p-ngo-i-b-nh-9zjs` vẫn ở trạng thái bản nháp với 0 trang. HTML cuối đã tải lên thành tài liệu `20260830160804171-4q7e.html`. Công cụ trả liên kết bàn giao Browser, nhưng phiên này không có bề mặt Browser tích hợp để mở và xác minh canvas; vì vậy không tuyên bố đã rà trực quan bằng Codex Slides.
- `git diff --check` đạt; chưa tạo `quill.json`.

## Ghi chú tự học Bài 12

### Điều phối OpenRouter

- Ba reader dùng `z-ai/glm-5.3-flash`: lập kế hoạch phiên `27292`, ánh xạ nguồn phiên `53056`, bản đồ chủ đề phiên `87725`. Cảnh báo thiếu tệp do gốc tạm hẹp được đối chiếu lại trên kho thật trước khi bác bỏ.
- Writer dùng `deepseek/deepseek-v4-flash-0731`. Các phiên `44749`, `42398`, `30279`, `88884`, `35136` tạo các phần bản nháp; một số phiên chạm giới hạn gọi công cụ hoặc ghi dở. Codex chính chỉ hợp nhất phần có thể kiểm chứng và trực tiếp áp dụng các sửa đã được reviewer phê duyệt.
- Năm reviewer độc lập dùng `z-ai/glm-5.3-flash`: nguồn `64754`, toán–thuật toán `75649`, sư phạm `52013`, mạch viết `68655`, viewer `72287`. Cả năm kết luận đạt; reviewer viewer yêu cầu bằng chứng runtime vì gốc tạm không có tài sản, nên kết luận cuối dựa trên kiểm định Chromium ở kho thật.
- Hai lần chạy tái kiểm đầu tiên gặp lỗi truyền tải trước khi model trả lời. Sau khi chạy lại với kết nối được cấp phép, reviewer toán–thuật toán phiên `55540` và reviewer mạch phiên `61765` đều trả `PASS` trên đúng bản cuối và `goal.md`.
- Gốc tạm chỉ chứa các tệp cần cho từng vai; `.env`, bí mật và thông tin xác thực không được đưa vào phạm vi công cụ của worker.

### Phát hiện và quyết định cho ghi chú

| Mức | Phát hiện | Quyết định |
|---|---|---|
| nghiêm trọng | Các phần writer để lại khối tùy biến, giả mã và công thức chưa liền mạch; có lúc tham chiếu hình không tồn tại | Khôi phục ba giả mã đầy đủ, dùng đúng tám SVG hiện có, chuẩn hóa 10 bộ `exercise`–`hint`–`solution` không lồng nhau |
| nghiêm trọng | Bản nháp có nguy cơ trộn biến thể ba khung của lời giải 15.1 với quy tắc chung $k=B-1$ | Tách riêng biến thể nguồn, giải thích giả thiết một bản ghi mỗi khối và không khái quát thành $k=B$ |
| nghiêm trọng | Vết chọn thay thế từng phân loại sai `hornbill` so với `hyena` | Chạy lại toàn bộ 12 tên; chốt ba dãy dài 7, 3 và 2 đúng thứ tự từ điển |
| trung bình | Thuật ngữ `heap`, `stream` chưa thuần Việt; “ổn định” chưa được định nghĩa | Dùng “đống (heap)” ở lần đầu rồi “đống”; đổi `stream` thành đầu vào; định nghĩa sắp ổn định là giữ thứ tự gốc giữa khóa trùng |
| trung bình | Storyboard hứa một vết trúng–trượt đệm nhưng ghi chú mới có định nghĩa | Thêm vết hai khung chứa `A` sạch, `B` bẩn và yêu cầu `A,C`, qua đó chỉ ra một lần trượt có thể gồm một ghi và một đọc |
| nhẹ | Bất biến trộn dùng cụm “đầu dãy giữ thứ tự” chưa chính xác về diễn đạt | Viết lại: dãy nguồn đã sắp nên đầu dãy là phần tử nhỏ nhất của phần chưa xuất |

Các nhận xét thiếu SVG, deck, thư viện cục bộ và CSS trong báo cáo viewer không phải lỗi của kho thật; reviewer chỉ thấy snapshot hẹp. Kiểm tra tệp và trình duyệt sau đó xác nhận toàn bộ tài sản tồn tại và tải thành công.

### Biên tập và tính liên tục

- `$no-ai-slop`: bỏ nhãn sản xuất, câu dẫn rỗng và nhịp liệt kê máy móc; giữ nguyên dữ kiện, công thức và mức độ chắc chắn của nguồn. Bản cuối được đối chiếu `eval.md`, không còn mã chủ đề, tên worker, prompt, goal, rubric hoặc thời lượng trong tài liệu công khai.
- `$quill`: rà tuyến `N01→N02→N03→N04→N05→N06→N07`, hai nhánh `N08` và `N09→N10`, rồi hội tụ `N11→N12`; thống nhất $n,b,N,B,k,r_0,p,H,b_b$ và các câu nối. Không tạo `quill.json`.

### Kiểm định viewer và index

- Chromium thật ở $1280\times720$ và $390\times844$: 33 heading khớp 33 liên kết mục lục, 201 biểu thức KaTeX, không lỗi KaTeX, tám ảnh không hỏng, ba khối mã có ngôn ngữ, 20 khối gập đóng mặc định, không tràn ngang, không lỗi console hoặc yêu cầu mạng.
- Bàn phím đạt cho liên kết bỏ qua nội dung và khối gập. Viewer từ chối đường dẫn vượt thư mục và từ chối ghép tài liệu với deck khác số bài.
- Bản in A4 gồm 18 trang; mọi `hint`/`solution` tự mở, mục lục và thanh thao tác bị ẩn, không có hình vượt khung.
- Sau khi viewer đạt, `index.html` mới được cập nhật. Liên kết Bài 12 xuất hiện đúng một lần, nhận focus bằng bàn phím và mở đúng ghi chú ở cả khung rộng và hẹp; tám ảnh cùng công thức tiếp tục tải không lỗi.
- Kiểm tra tĩnh: một H1; 10 `exercise`, 10 `hint`, 10 `solution` và 30 dấu đóng; ba khối mã `text`; tám SVG là XML hợp lệ; không có delimiter toán bị cấm; `git diff --check` đạt.

## Vòng đồng bộ deck với ghi chú — 2026-09-02

- Reader kế hoạch phiên `96490` và reader nguồn các phiên `45983`, `21434` đều dùng `z-ai/glm-5.3-flash` qua OpenRouter, kết luận `GO`. Kiểm trực tiếp PDF gốc bác false positive về lời giải 13.5: mốc đúng vẫn là PDF trang 5, trang in 95.
- Writer DeepSeek phiên `42641` chạy trên `/tmp/lec12-deck-writer`, sửa hai nhãn index trong bản sao rồi chờ API hơn bốn phút; phiên bị dừng minh bạch, không có metadata kết thúc và không chạm tệp sản phẩm trong workspace. Codex áp dụng trực tiếp đúng các delta reader phê duyệt.
- Index Bài 12 dùng nhãn `Bài giảng`, `Ghi chú bài giảng` và `aria-label="Tài nguyên Bài 12"`. Speaker notes P00, P01, P02, I06, I07, S06, S11, S15, S16, R00, T01 và X01 được viết trực tiếp hơn, giữ nguyên dữ kiện, công thức, thuật toán, nguồn và cấu trúc 53 trang.
- `$no-ai-slop/eval.md`: đạt ở phạm vi sửa. Quill: tuyến khối/khung→tạo dãy→trộn→chi phí→chọn thay thế và hệ ký hiệu $N,B,k,r_0,p,H,b_b$ giữ nguyên; không tạo `quill.json`.

### Năm cổng reviewer và tái kiểm

- Nguồn, phiên `4408`: **GO**. Đối chiếu lại các mốc nguồn, gồm Bài 13.5 ở PDF trang 5/trang in 95.
- Toán–thuật toán, phiên `89157`: **GO**. Không phát hiện thay đổi dữ kiện, công thức, điều kiện hoặc kết luận.
- Văn phong, phiên `18640`: **GO**. Các notes đã sửa đạt tiêu chí `$no-ai-slop` và vẫn giữ chỉ dẫn giảng cần thiết.
- Sư phạm, phiên thay thế `46598`: **GO**. Xác nhận bảy section ngoài, 53 ID/notes, 46+7 trang và 120+60 phút.
- Kỹ thuật, phiên thay thế `28972`: **GO**. Xác nhận cấu trúc lồng section, bảy mạch và inventory khớp.
- Hai báo cáo sư phạm/kỹ thuật ban đầu ở phiên `10656` và `39914` đếm nhầm sáu section ngoài nên đã được thay bằng hai lượt tái kiểm độc lập trên đúng bản cuối. Các phiên `9144`, `37105`, `13739`, `9870`, `51566` chạm giới hạn gọi công cụ; phiên `46291` đặt điều kiện nguồn sai. Tất cả đều bị loại khỏi bằng chứng nghiệm thu.

### Kiểm định runtime của vòng đồng bộ

- Chromium duyệt đủ 53 trang ở $1280\times720$, $800\times600$ và $720\times900$: không lỗi console/KaTeX, không tràn; điều hướng bàn phím đạt.
- Viewer có 33 heading, 23 liên kết mục lục, 201 biểu thức KaTeX, tám ảnh và 20 khối gập đóng mặc định. Khung rộng, hẹp, bàn phím, bản in, chặn path traversal và chặn ghép sai số bài đều đạt.
- Dự án Codex Slides `20260828001844-b-i-12-m-h-nh-i-o-v-s-p-x-p-ngo-i-b-nh-9zjs` truy cập được nhưng vẫn là draft với 0 slide; vì không có canvas để đối chiếu, kết luận hình ảnh dựa trên Chromium thật và không tuyên bố đã kiểm canvas Codex Slides.
- Index được kiểm sau viewer: liên kết Bài 12 xuất hiện đúng một lần, nhãn và URL doc/deck đúng.
