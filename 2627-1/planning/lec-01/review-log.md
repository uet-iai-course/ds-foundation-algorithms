# Nhật ký rà soát Bài 1

## Vòng rà 2026-08-30

Kế hoạch: hợp nhất các sửa đã duyệt vào HTML, SVG bản đồ, outline, storyboard và nhật ký này; giữ 7 section ngoài và tổng thời lượng 120+60.

Phân tích nguồn: đọc `AGENTS.md`, bản đồ nguồn, bản HTML và planning cùng bản trích xuất MMDS, Stanford, BHK; các sửa lấy từ quyết định của điều phối viên, không thêm số liệu, nguồn hay ví dụ mới.

Kiểm định storyboard: đếm lại 41 trang, 7 section ngoài, tổng thời lượng phần giảng 120 phút và phần bài tập 60 phút; các mạch A–D giữ chức năng, kết nối vào/ra và đóng góp mục tiêu; bản đồ chu trình rút gọn cho B–E đã ghi bước gộp, bước không áp dụng và lý do.

Năm vai độc lập (mỗi vai một lượt rà riêng):

| mức độ | trang | vấn đề | bằng chứng | quyết định |
|---|---|---|---|---|
| nghiêm trọng | toàn bộ aside | Thời lượng lặp giữa HTML và storyboard | Cụm “Thời lượng dự kiến: … phút.” xuất hiện ở mọi ghi chú | Xóa khỏi mọi aside; chỉ giữ trong storyboard/outline |
| trung bình | A06 | pre quá nhỏ | font-size .66em | Nâng lên .75em |
| trung bình | A07 | Chưa nêu rõ điều kiện dừng | Ghi chú nói “dừng sau n bước” nhưng mặt trang không nêu | Thêm “mỗi bước xử lý một bản ghi” vào bước kết thúc |
| trung bình | B06 | Ký hiệu e, w chưa định nghĩa | Công thức điểm(e) dùng e, w ngay trên mặt trang | Định nghĩa e là thư, w là từ trên mặt trang |
| trung bình | B07 | Câu hỏi lặp câu B04 | Câu hỏi bảng tổng đã có ở B04 | Đổi sang phân loại “phân phối ước lượng từ mẫu”; notes đáp mô hình thống kê |
| trung bình | C05 | Câu hỏi lặp câu A08 | Câu hỏi trường hợp thất bại đã có ở A08 | Đổi sang phép đánh đổi khi O(h) không vừa bộ nhớ; notes nêu đổi đặc tả, tóm tắt xấp xỉ hoặc thu hẹp truy vấn, phải nêu rõ |
| trung bình | D01 | Giả thiết độc lập chưa hiện trên mặt trang | Chỉ có trong notes D02 | Viết rõ mỗi người mỗi ngày xác suất q=0,01, độc lập giữa người/ngày |
| trung bình | D03 | Tiêu đề gán sai thuật ngữ | “Nguyên lý Bonferroni đếm biến cố trùng kỳ vọng” | Đổi thành “Đếm biến cố trùng bằng kỳ vọng”; notes phân định MMDS gọi đây là Bonferroni phi hình thức, công thức dùng tính tuyến tính của kỳ vọng, không dùng union bound |
| nhẹ | D04 | Tiêu đề dài, chữ số bằng chữ | “Kỳ vọng có khoảng hai trăm năm mươi nghìn…” | Đổi thành “Kỳ vọng khoảng 250.000 biến cố trùng” |
| trung bình | D05 | Ba thẻ hé chiều tác động | Thẻ cũ ghi sẵn “số cặp ngày gần gấp bốn” | Ba thẻ chỉ nêu dữ kiện; câu hỏi yêu cầu xác định số phép thử và xác suất thay đổi thế nào |
| trung bình | E02 | Độ dày 1/d chỉ có trong notes | Câu hỏi O(1/d) xuất hiện trước khi nêu dữ kiện | Giới thiệu trên mặt trang trước câu hỏi rằng vành ngoài dày cỡ 1/d lần bán kính |
| trung bình | E03 | Từ “mạch” không phù hợp cho bản đồ học phần | Tiêu đề, alt, SVG title/desc/footer dùng “mạch” | Đổi thành “Bản đồ 15 bài theo năm nhóm”; Bài 1 là nền chung; giữ nguyên nội dung năm nhóm và quan hệ |
| trung bình | E04 | Notes chưa thu hồi mở đầu rõ | Ghi chú chỉ liệt kê bốn câu kiểm tra | Notes thu hồi: kho nhật ký không vừa bộ nhớ dẫn tới đặc tả, chi phí, bảo đảm; nhiều phép thử và số chiều buộc nêu mô hình/giả thiết; đây là kết luận phần giảng |
| trung bình | R01 | Gộp sai hai thay đổi độc lập và hé sản phẩm | “nên có 200.000 khách sạn”; sản phẩm “ba công thức và ba giá trị” | Tách thành hai thay đổi độc lập (người, khách sạn); sản phẩm chỉ ba công thức; tham chiếu dữ kiện tới trang D01 thay vì chỉ Mục 1.2.3 |
| nghiêm trọng | R05 | Đáp số và kết luận hiện trên mặt trang | Fragment chứa công thức và kết luận trong khi hoạt động 15 phút | Chuyển toàn bộ công thức, đáp số 1,898·10^-4, C(1000,10), cận xác suất, rubric và hai giới hạn vào notes; mặt trang chỉ giữ yêu cầu và sản phẩm; thêm câu kết nối thu hồi khung Bài 1; không đổi dữ kiện 10^8 |

Hai phát hiện bị bác:

- (a) “A00–A08 cộng sai thời lượng” — bác. A00–A08 cộng đúng 32 phút (2+5+4+2+4+4+4+4+3).
- (b) “R05 đáp số sai bậc 10” — bác. R05 đúng 1,898·10^-4 vì C(10^8,2)≈5·10^15, không phải 5·10^17.

Quyết định khác: không đổi tên học phần “của” trong tiêu đề vì đây là quy ước toàn bộ kho theo AGENTS, không sửa cục bộ một deck.

Runtime: reader, reviewer và writer đều có requested_model=observed_model=z-ai/glm-5.3-flash, provider=OpenRouter.

### Tái kiểm sau chỉnh sửa

- Vai độ chính xác rà lại A07, B06–B07, C05, D01–D05, E02–E04 và R01–R05: mọi giả thiết, ký hiệu, ba biến thể, kết quả số và cận xác suất đều đúng; đáp án chỉ còn trong ghi chú. Không còn lỗi `chặn bàn giao` hoặc `nghiêm trọng`.
- Vai kết nối và mạch viết rà lại toàn bài rồi rà hẹp D04–E04 và R05 sau lần sửa cuối: D05→E00, E02→E03, E04→R00 và kết luận R05 đều có câu nối; E04 thu hồi bốn mục tiêu P01; đủ 7 section ngoài. Không còn lỗi bắt buộc.
- Tự kiểm `no-ai-slop/eval.md`: giữ nguyên mệnh đề và số liệu nguồn; không có từ cấm, lời dẫn rỗng, câu hỏi tu từ trong tiêu đề, kết luận lặp hoặc nhịp câu quảng bá. Câu chữ hiển thị và ghi chú dùng động từ trực tiếp, thuật ngữ nhất quán.
- Rà mạch theo Quill Outline Workflow mà không tạo `quill.json`: tuyến kho nhật ký → thuật toán → tầng lời giải → chi phí → tín hiệu giả → kết luận → bài tập tiến triển liên tục; bảng ký hiệu và thuật ngữ nội bộ được đồng bộ.

### Kiểm định kỹ thuật và giới hạn công cụ

- Bộ phân tích HTML xác nhận 7 section ngoài, 41 `data-slide-id` duy nhất, 41 ghi chú, không thiếu đường dẫn cục bộ; cả 5 SVG phân tích XML thành công; `git diff --check` đạt.
- `python3 -m reloadserver 8765` không chạy vì môi trường không có mô-đun `reloadserver`. Cổng 8765 đang do một tiến trình cũ phục vụ `/tmp/lec03-webroot.wGW4jP` chiếm; không dừng tiến trình ngoài phạm vi.
- Máy chủ thay thế chỉ gắn `127.0.0.1`, chỉ phục vụ `2627-1/` tại cổng 8766. HTML, RevealJS, Notes, Highlight, Math, ba tài nguyên KaTeX và SVG E03 đều trả HTTP 200; máy chủ được dừng sau kiểm tra.
- Codex Slides đọc lại thành công dự án `20260827112432-b-i-1-b-i-to-n-d-li-u-l-n-v-m-h-nh-thu-t-8tlj`: nguồn và yêu cầu vẫn còn, nhưng dự án ở checkpoint `clarify` và có 0 trang. Phiên này không có Codex in-editor Browser hay trình duyệt Chromium/Firefox để rà canvas. Không tải bản HTML mới tới Codex Slides vì quyền gửi tệp đã cấp cho OpenRouter, không bao gồm đích Codex Slides. Vì vậy không tuyên bố đã rà trực quan bản sửa mới bằng Codex Slides; kiểm định hiển thị trước vòng này vẫn là mốc tham khảo, còn vòng mới dựa trên cấu trúc, HTTP và rà bố cục từ DOM/CSS.

## Trạng thái sau chỉnh sửa

- Tệp trang chiếu: `2627-1/lecture-01-bai-toan-du-lieu-lon-va-mo-hinh-thuat-toan.html`.
- Phần giảng: 120 phút. Phần bài tập: 60 phút.
- Bài tập lấy trực tiếp MMDS Bài 1.2.1 và 1.2.2, trang 8; đáp án chỉ ở ghi chú diễn giả.
- Tài sản trực quan: 5 SVG; không dùng ảnh raster.
- `2627-1/index.html` đã có thẻ Bài 1 và liên kết đúng tới tệp HTML; vòng này không cần sửa chỉ mục.

## Báo cáo kiểm định storyboard

| mức độ | trang chiếu | vấn đề | bằng chứng | đề xuất sửa |
|---|---|---|---|---|
| chặn bàn giao | A04, A05, B00–B07, C00–C03 | Ví dụ chạy tay đứng sau đặc tả, giả mã và một phần khảo sát | Khoảng 39 phút sau thuật toán mới quay lại vết chạy | Chuyển vết chạy lên trước đặc tả và hoàn tất chu trình trước phần B |
| nghiêm trọng | D01–D04 | Công thức Bonferroni xuất hiện trước tình huống | D01 nêu nguyên lý, D02 mới nêu hồ sơ lưu trú | Đặt tình huống trước, rồi giả thiết, đếm phép thử và kỳ vọng |
| nghiêm trọng | R04–R05 | Đáp án hiện trước khi hoạt động kết thúc | R05 hiện công thức dù được tính 15 phút | Giữ câu hỏi trước; chỉ hiện lời giải khi chữa |
| nghiêm trọng | P01 | Mục tiêu hiển thị không khớp outline | Bốn mục tiêu trên slide, sáu mục tiêu trong outline | Đồng bộ phạm vi; cao chiều chỉ định tuyến |
| trung bình | B02–B06 | Nhiều ví dụ rời làm đứt tình huống xuyên suốt | Giao thoa, học máy, PageRank và lọc thư nối tiếp | Dùng lại kho nhật ký; thu gọn khảo sát |
| trung bình | E01–E02 | Thiếu cầu nối và nhập hai hiện tượng | Công thức khoảng cách dẫn thẳng sang hình thể tích | Phân biệt rõ hai hiện tượng và thêm câu kiểm tra |
| trung bình | D05, R01–R03 | Phần giảng tiết lộ bài tập | Ghi chú D05 cho đáp số phần c | Bỏ đáp số khỏi phần giảng |
| nhẹ | A05, B01 | Tiêu đề chưa nêu luận điểm | “Điểm nghẽn nằm ở đâu”; phủ định “không được nhập” | Dùng tiêu đề khẳng định trực tiếp |

## Báo cáo góc nhìn sinh viên

| mức độ | trang chiếu | vấn đề | bằng chứng | đề xuất sửa |
|---|---|---|---|---|
| chặn bàn giao | A04, A05, B00–B07, C00–C03 | Ví dụ chạy tay xuất hiện sau hình thức hóa, giả mã và chứng minh | Khoảng cách khoảng 39 phút | Đưa vết chạy trước đặc tả và hoàn tất chu trình trước B |
| nghiêm trọng | E03 | Bản đồ 15 bài có chữ quá nhỏ | SVG 1200×640 dùng chữ 17 px, khi co chỉ còn khoảng 11–12 px | Tách hai trang hoặc gộp thành năm mạch chữ lớn |
| nghiêm trọng | R04–R05 | Trang chữa lộ công thức và đáp số | R05 hiện toàn bộ đáp án nhưng vẫn tính 15 phút | Dùng ghi chú hoặc fragment và thêm sản phẩm R04 |
| trung bình | A05 | Một trang gánh giả mã, bất biến, dừng, biên và chi phí | Thời lượng bốn phút | Tách thuật toán, chứng minh và chi phí |
| trung bình | P01, E00–E02 | Mục tiêu không báo trước chứng minh hoặc phần cao chiều | Mặt slide có bốn mục tiêu, outline có sáu | Đồng bộ; lược cao chiều khỏi đánh giá nếu chỉ định tuyến |
| trung bình | B02–B06 | Tải chuyển ngữ cảnh cao | Nhiều lĩnh vực và ví dụ mới trong vài phút | Gộp nội dung và dùng lại kho nhật ký |
| trung bình | E01–E02 | Thiếu ví dụ hoặc câu kiểm tra | Hai trang chỉ trình bày công thức và hình | Thêm phép tính hoặc câu kiểm tra có căn cứ từ BHK |
| nhẹ | B07 | Câu hỏi quá rộng cho hai phút | Yêu cầu xét mỗi sản phẩm và dữ liệu phải giữ | Chọn một sản phẩm, có đáp án mẫu trong ghi chú |

## Báo cáo chuyên gia giải thuật và khoa học dữ liệu

| mức độ | trang chiếu | vấn đề | bằng chứng | đề xuất sửa |
|---|---|---|---|---|
| nghiêm trọng | A04, A05, C03 | Chu trình thuật toán sai thứ tự | Vết chạy sau đặc tả và thuật toán | Chuyển vết chạy trước đặc tả |
| nghiêm trọng | D02–D04, R01–R03 | “Cùng khách sạn” mơ hồ | Nguồn cho phép khách sạn khác giữa các ngày | Ghi rõ cùng một khách sạn trong từng ngày, có thể khác qua ngày |
| nghiêm trọng | R04–R05 | Thiếu giả thiết và câu hỏi gốc của Bài 1.2.2 | Không có giả thuyết cặp thật chắc chắn mua cùng tập 10 món | Khôi phục bằng ngôn ngữ trung tính và hỏi so trùng thật với trùng ngẫu nhiên |
| nghiêm trọng | E01–E02 | Nhập khoảng cách với thể tích gần biên | Hình thể tích mang tiêu đề khoảng cách | Đổi tiêu đề và thêm cầu nối |
| trung bình | B04–B07 | “Mô hình tính toán” dễ nhầm computational model | Thuật ngữ có nghĩa khác trong lý thuyết tính toán | Dùng “mô hình dữ liệu theo truy vấn” |
| trung bình | C02, C05, E04 | Sai số bị gọi là nguồn chi phí | C02 liệt kê bốn nguồn chi phí | Dùng “Ba chi phí và một bảo đảm” |
| trung bình | D03–D05, R01–R03 | Phần giảng lặp và tiết lộ bài tập | D05 cho biết biến thể giảm dưới 1 | Bỏ đáp số và điều chỉnh hoạt động |
| trung bình | R05 | Biểu thức đếm cặp lượt mua, không chính xác cặp người | Một cặp người có thể trùng nhiều lần | Định nghĩa $X$ là số cặp lượt hoặc dùng xác suất đúng/xấp xỉ |
| trung bình | C00, C02 | Nguồn Stanford 67–70 mâu thuẫn quyết định phạm vi | Ghi chú vẫn dẫn các trang này | Bỏ mọi dẫn nguồn này |
| nhẹ | A05 | Tiêu đề sai trọng tâm | “Điểm nghẽn nằm ở đâu” trên trang giả mã | Đổi tiêu đề theo luận điểm |
| nhẹ | E03 | Dùng “moment” trong hình | Chưa thuần Việt | Dùng “mômen” |

## Báo cáo độ chính xác toán học và thuật toán

| mức độ | trang chiếu | vấn đề | bằng chứng | đề xuất sửa |
|---|---|---|---|---|
| nghiêm trọng | E02 | Hình chỉ nói thể tích gần biên, không chứng minh khoảng cách tập trung | Hình BHK 2.2 là mặt cắt thể tích | Đổi tiêu đề và câu nối |
| trung bình | D04, R01–R03 | Tổ hợp đếm biến cố, không nhất thiết là số cặp người phân biệt | Một cặp người có thể góp nhiều cặp ngày | Gọi kỳ vọng số biến cố trùng; chỉ xấp xỉ cặp người khi biến cố hiếm |
| trung bình | R04–R05 | Công thức chính xác cho cặp lượt mua | Tử số là $\binom P2 100^2$ | Định nghĩa $X$ tương ứng; có thể dùng $\Pr(X\ge1)\le E[X]$ |
| trung bình | D02–D04, R01–R03 | Thiếu giả thiết độc lập và chọn đều | Công thức $(q^2/H)^k$ cần các giả thiết này | Ghi rõ độc lập giữa người/ngày và chọn đều có điều kiện |
| trung bình | A05 | Bất biến thiếu tập khóa | Chỉ phát biểu đúng giá trị cho khóa đã có | Thêm tập khóa đúng bằng máy chủ trong tiền tố |
| nhẹ | A04 | Miền $s_i$ và ràng buộc truy cập chưa chính xác | $s_i\ge0$; “đọc một lần” đặt trong điều kiện đầu vào | Dùng $s_i\in\mathbb{N}_0$; tách ràng buộc truy cập |
| nhẹ | C02 | $O(n)$ kỳ vọng thiếu giả thiết | Chi phí phụ thuộc bảng băm | Nêu mỗi cập nhật bảng băm kỳ vọng $O(1)$ |

Đối chiếu số học của phản biện: 249749,99975025; 999499,9990005; 249749,999875125; 0,0830834999; $\binom{1000}{10}=263409560461970212832400$; $1,8981846905\cdot10^{-4}$.

## Báo cáo phản biện học thuật và giảng dạy

| mức độ | trang chiếu | vấn đề | bằng chứng | đề xuất sửa |
|---|---|---|---|---|
| nghiêm trọng | A03–A05, B00–B07, C00–C03 | Phần khảo sát B chen giữa thuật toán và ví dụ/chi phí, phá mạch suy luận | Khoảng 39 phút mới quay lại vết chạy | Đưa ví dụ trước đặc tả, hoàn tất chu trình và chi phí trước phần khảo sát |
| nghiêm trọng | D00–D04 | Công thức Bonferroni xuất hiện trước tình huống | D01 trước D02 | Đặt hồ sơ lưu trú trước, rồi đếm phép thử, hình thức hóa và tính kỳ vọng |
| nghiêm trọng | R04–R05 | Đáp án hiện ngay khi hoạt động chưa kết thúc | R05 hiện công thức và số nhưng tính 15 phút | Giữ câu hỏi trước, chỉ tiết lộ khi chữa hoặc trong ghi chú |
| nghiêm trọng | P01 | Mục tiêu hiển thị không khớp outline | Bốn mục tiêu so với sáu | Đồng bộ hoặc thu gọn phạm vi |
| trung bình | B02–B06 | Nhiều ví dụ rời làm đứt tình huống xuyên suốt | Giao thoa, học máy, PageRank, lọc thư | Gộp và dùng lại kho nhật ký |
| trung bình | E01–E02 | Thiếu cầu nối và nhập hai hiện tượng | Công thức khoảng cách rồi hình thể tích | Phân biệt rõ và thêm câu kiểm tra |
| trung bình | D05, R01–R03 | Giảng tiết lộ bài tập | Ghi chú cho đáp số phần c | Bỏ đáp số khỏi phần giảng |
| nhẹ | A05, B01 | Tiêu đề không nêu luận điểm | “Điểm nghẽn…” và tiêu đề phủ định | Đổi tiêu đề trực tiếp |

## Quyết định chỉnh sửa

Tất cả đề xuất `chặn bàn giao` và `nghiêm trọng` đã áp dụng. Các đề xuất `trung bình` và `nhẹ` cũng đã áp dụng, với hai lựa chọn cụ thể:

- E03 dùng phương án gộp thành năm mạch thay vì tách hai trang; cách này giữ một luận điểm trung tâm và không tăng thời lượng.
- E01 dùng câu kiểm tra về kỳ vọng theo $d$ thay cho một ví dụ số dài; câu hỏi dựa trực tiếp vào công thức đang hiển thị và giữ cụm cao chiều ở mức định tuyến.

Không có đề xuất nào bị bác bỏ. Sau khi đổi thứ tự và số trang, đã rà lại toàn bộ cụm A, B, C, D, E và hai trang lân cận quanh mỗi điểm nối.

## Sai khác có chủ ý so với nguồn

| Mục | Quyết định | Lý do |
|---|---|---|
| Stanford trang chiếu 32–61 và 63–70 | Bỏ | Nội dung hệ phân tán thuộc Bài 2; trang 62 là ngoại lệ duy nhất để lấy lược đồ kho web |
| Ví dụ bốn bản ghi A04 | Tự dựng từ lược đồ nguồn | Cần vết chạy nhỏ; ghi rõ không phải dữ liệu thực nghiệm |
| MMDS Hình 1.1 về John Snow | Bỏ | Không cần cho mạch đặc tả, chi phí và nhiều phép thử |
| MMDS nguyên lý Bonferroni | Giữ ở mức phi hình thức | Nguồn không trình bày phép hiệu chỉnh thống kê đầy đủ tại đây |
| MMDS Bài 1.2.1 | Chia R01–R03 | Giữ nguyên dữ kiện và yêu cầu; thêm mốc hoạt động |
| MMDS Bài 1.2.2 | Chia R04–R05 | Giữ nguyên giả thuyết toán học; đáp án chỉ hiện khi chữa |
| Nhãn con người trong Bài 1.2.2 | Dùng “nhóm cần phát hiện” | Ngôn ngữ trung tính, không đổi cấu trúc toán học hoặc câu hỏi |
| BHK Chương 2 | Chỉ định tuyến | Định lý chi tiết vượt phạm vi Bài 1 |
| Bản đồ 15 bài | Gộp thành năm mạch | Chữ 17 px không đọc được khi chiếu; số bài được giữ theo mạch |

## Hình vẽ lại và tiếp cận

- `kho-nhat-ky-bo-nho.svg`: nhãn $D,M,b$, mũi tên và hoa văn bộ nhớ.
- `giao-thoa-khai-pha-du-lieu.svg`: ba hoa văn được dùng thật, cùng ba kiểu viền.
- `phep-thu-va-duong-tinh-gia.svg`: ba khối có nhãn và kiểu viền; đại lượng được gọi là biến cố trùng kỳ vọng.
- `the-tich-gan-bien.svg`: vành ngoài dùng hoa văn chấm; mô tả đúng hiện tượng thể tích.
- `ban-do-hoc-phan.svg`: năm mạch, chữ nhỏ nhất 22 px, biểu tượng và kiểu viền riêng.

Mỗi SVG có `role="img"`, `title`, `desc`; không dùng màu làm tín hiệu duy nhất.

## Tự kiểm biên tập

Đã dùng `no-ai-slop` và tự kiểm trực tiếp theo `no-ai-slop/eval.md`: giữ nguyên mệnh đề và số liệu nguồn; bỏ lời dẫn rỗng, câu hỏi tu từ, nhấn mạnh phô trương, nhịp câu máy móc và kết luận lặp. Tiêu đề dùng tiếng Việt, chỉ giữ tên riêng, tên thuật toán và ký hiệu chuẩn.

Đã dùng Quill ở mức Outline Workflow để rà mục tiêu, thứ tự khái niệm, thuật ngữ, ký hiệu và câu nối. Chuỗi $(u_i,s_i)$ đi liên tục từ vết chạy sang đặc tả, giả mã và bất biến; $P,T,H,q$ chỉ dùng trong cụm Bonferroni và bài tập. Không tạo `quill.json`.

## Kiểm tra tính đúng khi chỉnh sửa

- Bất biến gồm cả tập khóa và giá trị; chứng minh nêu mệnh đề, khởi tạo, duy trì, kết thúc và điều kiện dừng.
- Thời gian kỳ vọng $O(n)$ chỉ dưới giả thiết mỗi thao tác bảng băm kỳ vọng $O(1)$.
- Trong mô hình lưu trú, các quyết định độc lập giữa người/ngày; có điều kiện đã đi, khách sạn được chọn đều. Khách sạn có thể khác giữa các ngày.
- $X$ ở D03 là số biến cố trùng theo cặp người và cặp ngày. $X$ ở R05 là số cặp lượt mua trùng của hai người khác nhau.
- Công thức R05 cho kỳ vọng số cặp lượt mua; $\Pr(X\ge1)\le\mathbb{E}[X]$ theo bất đẳng thức Markov.

## Việc còn lại cho điều phối viên

- Không còn việc nội dung hoặc kỹ thuật phải xử lý trước bàn giao.
- Sau khi commit, điều phối viên đẩy lên `origin` và kiểm tra URL GitHub Pages.

## Kiểm tra tĩnh sau chỉnh sửa

- 41 `data-slide-id`, tất cả duy nhất; 41 trang đều có ghi chú.
- Storyboard có đúng 41 dòng ánh xạ; không thiếu hoặc thừa mã.
- Tổng thời lượng lấy từ ghi chú: phần giảng 120 phút, phần bài tập 60 phút.
- Số thẻ mở/đóng `<section>` là 48/48; số thẻ mở/đóng ghi chú là 41/41.
- Năm SVG đều phân tích XML thành công, có `role="img"`, `title` và `desc`.
- HTML không tham chiếu ảnh raster, URL ngoài hoặc tài nguyên cốt lõi trên mạng.
- Ba tệp Markdown chỉ dùng dấu đô la cho công thức nội dòng và công thức khối.
- `git diff --check` không báo lỗi khoảng trắng.

## Kiểm định cuối của điều phối viên

- Chạy máy chủ tại thư mục gốc bằng `python3 -m reloadserver 8765`. Môi trường không cài mô-đun toàn cục nên dùng bản tạm trong `/tmp` qua `PYTHONPATH`; máy chủ phục vụ đúng ở cổng 8765.
- Tải thử HTML, RevealJS, CSS, plugin, ba tài nguyên KaTeX thực tế và năm SVG qua HTTP; tất cả trả mã 200.
- Dùng Chromium qua Playwright duyệt tuần tự đủ 41 trang ở khung 1280×720 và 800×600. Hai lượt kiểm thử đạt; không có lỗi JavaScript, yêu cầu mạng thất bại hoặc phần tử vượt khung trang đang trình chiếu.
- Chụp 41 ảnh ở khung 1280×720 và kiểm tra bản ghép toàn bộ. Các trang có giả mã, bảng vết chạy, công thức Bonferroni, năm mạch học phần và bài tập đều đọc được; fragment R05 ẩn đáp án trước bước chữa.

## Cập nhật mạch học tập

- **Mức độ:** nghiêm trọng. **Trang chiếu:** E03. **Vấn đề:** số bài trên bản đồ phản ánh các nhóm chủ đề nhưng không phản ánh thứ tự học liền mạch. **Bằng chứng:** hình cũ ghi `2, 7, 8`, `3, 4, 14`, `5, 6`, `9, 10`, `11–13, 15`; `sources/source.md` đã sắp lại năm mạch thành các khoảng liên tiếp. **Quyết định:** sửa SVG và trang E03 thành `2–4`, `5–7`, `8–9`, `10–11`, `12–15`; đổi tiêu đề từ “tuyến” sang “mạch”.
- E02 được sửa tham chiếu từ Bài 14 cũ sang Bài 7 mới. Đã rà lại E01–E04 theo quy tắc hai trang lân cận; không đổi thời lượng, công thức hoặc mạch lập luận của cụm số chiều lớn.
- Vòng rà lại E01–E04 đã mở rộng văn bản thay thế của E03 để nêu đủ tên năm mạch. Ghi chú E02 cũng được sửa: với vành dày $O(1/d)$, chỉ kết luận một tỷ lệ lớn thể tích nằm gần biên và tỷ lệ phụ thuộc hằng số ẩn; không còn tuyên bố giới hạn bằng 1.
- Kiểm tra lại bằng Chromium ở 1280 × 720 và 800 × 600: đủ 41 trang, không lỗi JavaScript hoặc tài nguyên, không tràn khung. E03 hiển thị đúng năm khoảng bài liên tiếp và đủ tên mạch.
- Kiểm tra bàn phím bằng API điều hướng RevealJS trong cùng chuỗi trang; cấu hình vẫn giữ `controlsLayout: "edges"`, `slideNumber`, `hashOneBasedIndex` và `hash`.
- `2627-1/index.html` đã có đúng một liên kết đến bài hoàn thành và không liên kết tới tệp quy trình.

### Giới hạn Codex Slides

Dự án bền vững có mã `20260827112432-b-i-1-b-i-to-n-d-li-u-l-n-v-m-h-nh-thu-t-8tlj`. Trạng thái chuẩn được đọc lại thành công, nhưng dự án vẫn ở bước làm rõ và có 0 trang nội bộ. Tải các tệp cuối vào Design Files trả lỗi HTTP 500; tải HTML làm material thành công nhưng lượt chat không gắn được material vào ngữ cảnh. Giao diện Browser trong trình soạn thảo không khả dụng ở phiên này. Vì vậy không tuyên bố đã rà trực quan bằng Codex Slides; kiểm định trực quan cuối dựa trên RevealJS cục bộ và Chromium.

## Vòng xây dựng ghi chú bài giảng 2026-09-01

### Phạm vi và quyết định chủ đề

- Chỉ xây dựng ghi chú bài giảng; không viết lại bộ trang chiếu. HTML chỉ được sửa hai điểm dùng chung: thống nhất thuật ngữ “quét–cộng dồn” và sửa nguồn BHK Hình 2.2 thành PDF trang 17.
- Bản đồ N01–N10 gồm bảy chủ đề `cốt lõi` và ba chủ đề `cầu nối` là N02, N09, N10. Không có chủ đề `bổ sung`. BHK PDF trang 18–21 giữ ở mức `đọc thêm`; bất đẳng thức Markov là cầu nối ngắn trong N08.
- Ghi chú dùng lại năm SVG đã có của Bài 01. Không tạo ảnh raster, không thêm dữ liệu, ví dụ thực nghiệm hoặc mệnh đề ngoài nguồn.
- Viewer kế thừa cục bộ cấu trúc phát hành an toàn từ kho `math-4-AI`, đổi toàn bộ nhận diện học phần và dùng Marked, DOMPurify, KaTeX cục bộ. Không gửi mã ngoài workspace đó tới OpenRouter.

### Worker OpenRouter và cổng duyệt

Các lượt được chấp nhận đều báo `requested_model=observed_model=z-ai/glm-5.3-flash` và `provider=OpenRouter` tại runtime.

| Giai đoạn | Vai | Kết quả dùng để triển khai |
|---|---|---|
| Lập kế hoạch | reader | Chốt goal, phạm vi, tiêu chí và rủi ro |
| Phân tích nguồn | reader | Kiểm kê MMDS, Stanford, BHK và ánh xạ nguồn |
| Bản đồ chủ đề | reviewer | Hợp nhất N01–N10; không đề xuất chủ đề bổ sung |
| Soạn và sửa | writer | Tạo bản nháp trong thư mục tạm, rồi sửa theo các báo cáo đã duyệt |
| Góc nhìn sinh viên | reviewer | Yêu cầu giải thích kỳ vọng biến cố, điều kiện $1/H$, ký hiệu và câu tự kiểm tra |
| Phản biện giảng dạy | reviewer | Yêu cầu chuyển hình ba miền, nối Markov vào bài tập và bổ sung kiểm tra |
| Chuyên gia giải thuật và khoa học dữ liệu | reviewer | Phát hiện nguồn BHK lệch, thuật ngữ chưa thống nhất và mục từ không dùng |
| Độ chính xác toán học và thuật toán | reviewer | Xác nhận số học; yêu cầu thống nhất nguồn BHK và bỏ dẫn Stanford lặp |
| Kết nối và mạch viết | reviewer | Yêu cầu cắt siêu bình luận, giải thích $249\,750$ so với $250\,000$ và chỉnh R01 |

Một số lượt reviewer ban đầu chạm giới hạn vòng công cụ và không được dùng làm báo cáo. Điều phối viên dừng phần phụ thuộc, thu hẹp phạm vi rồi chạy lại đúng vai; năm báo cáo trong bảng trên đều hoàn tất và độc lập.

### Sửa sau rà soát và tái kiểm

- Mọi lỗi `nghiêm trọng` đã sửa, đặc biệt là vị trí BHK Hình 2.2. Các điểm trung bình và nhẹ về kỳ vọng chính xác, xác suất có điều kiện, ký hiệu $y,z$, Markov, câu nối, câu tự kiểm tra và nguồn A03 cũng đã xử lý.
- Worker độ chính xác tái kiểm công thức tổ hợp, kỳ vọng, Markov, bất biến, chi phí và giả thiết độc lập: không còn lỗi chặn bàn giao hoặc nghiêm trọng. Xấp xỉ R03 được chuẩn hóa thành $0{,}083$ (xấp xỉ $1/12$).
- Worker mạch viết tái kiểm N01–N10. Sau khi thêm câu tự kiểm tra cho N03, N06, N07, N09 và đổi đầu ra N10 thành áp dụng khung trong các bài sau, lượt xác nhận cuối báo không còn lỗi chặn bàn giao, nghiêm trọng hoặc trung bình.

### Biên tập bản cuối

- Codex chính đọc toàn bộ `lecture-note.md`, dùng `$no-ai-slop` để bỏ lời dẫn rỗng, câu mô tả quy trình, nhịp câu máy móc và đoạn kết tóm tắt lặp. Không đổi mệnh đề, dữ kiện, giả thiết, ký hiệu, kết quả hoặc nguồn.
- Tự kiểm trực tiếp theo `no-ai-slop/eval.md`: đạt các tiêu chí về độ trung thành với nguồn, giọng tự nhiên, câu trực tiếp, không quảng bá, không siêu bình luận và không lặp kết luận.
- Rà mạch theo Quill Outline Workflow: N01–N10 nối liên tục; thuật ngữ, ký hiệu và sản phẩm học tập khớp outline và storyboard. Không tạo `quill.json`.

### Kiểm định viewer và index

- Kiểm tra tĩnh đạt: Markdown bắt đầu bằng H1; ba bảng có hàng tiêu đề; sáu khối directive cân bằng, không lồng; khối mã có ngôn ngữ; năm SVG tồn tại, có `role="img"`, `title`, `desc`; năm mã SRI khớp tệp cục bộ; JavaScript qua `node --check`; không có tài nguyên lõi từ mạng.
- Chromium/Playwright ở 1280×720 và 390×844: 23 mục lục, 178 công thức KaTeX, không lỗi công thức; năm SVG tải đủ; không tràn trang; không lỗi JavaScript, lỗi trang hoặc yêu cầu mạng; gợi ý và lời giải gập mặc định, mở được bằng bàn phím; liên kết bỏ qua điều hướng hoạt động.
- Viewer từ chối đường dẫn ngoài `materials/lec-NN/` và từ chối số bài của `doc`/`deck` không khớp. Bản in A4 gồm 15 trang, tự mở mọi khối gập và ẩn mục lục cùng thanh điều hướng.
- Sau khi viewer đạt, `index.html` mới được cập nhật. Kiểm tra index ở hai khung cho đủ 15 thẻ, đúng một liên kết ghi chú Bài 01, hai tài nguyên Bài giảng/Ghi chú, không tràn trang hoặc lỗi JavaScript.

## Vòng đồng bộ deck với ghi chú bài giảng 2026-09-02

### Điều phối và worker OpenRouter

- Reader kế hoạch `45938` và reader nguồn `19318` dùng `z-ai/glm-5.3-flash` qua OpenRouter; cả hai kết luận không cần thêm, gộp, tách hoặc bỏ trang.
- Writer hợp lệ `15607` dùng `deepseek/deepseek-v4-flash-0731` qua OpenRouter trên bản sao tạm. Phiên `67191` bị dừng ngay vì dùng nhầm model; phiên DeepSeek `42928` hết thời gian trước khi ghi tệp nên không được tính.
- Năm báo cáo reviewer hợp lệ: nguồn–ghi chú `43467`, toán–giải thuật `83574`, sư phạm `26158`, no-ai + mạch Quill `64311`, kỹ thuật tĩnh `3556`. Tất cả reviewer hợp lệ báo `requested_model=observed_model=z-ai/glm-5.3-flash`, provider OpenRouter.
- Hai phiên kỹ thuật `74396` và `53521` chạm giới hạn lượt công cụ, không dùng làm báo cáo. Reviewer kỹ thuật được chạy lại với phạm vi hẹp và hoàn tất ở phiên `3556`.
- Không gửi `.env`, bí mật hoặc thông tin xác thực tới worker. Codex chính chỉ áp dụng các sửa nằm trong phạm vi đã duyệt.

### Quyết định sau năm báo cáo

- Chấp nhận sửa goal/prompt từ sáu thành bảy mạch; HTML và storyboard vốn đã có đúng bảy mạch, hợp chuẩn 5–7.
- Chấp nhận bỏ mã nội bộ `D01` khỏi R01, bỏ cụm “mốc hoạt động”, các nhãn câu nối và tên tệp nội bộ khỏi lời giảng.
- Chấp nhận thống nhất ký hiệu E01 với ghi chú, bổ sung giả thiết phương sai hữu hạn, làm rõ kết quả tổ hợp ở D03–D04/R02 và bán kính trong ở E02.
- Xác minh trực tiếp `mmds-3e-ch01-data-mining.pdf`, trang 7–8: ví dụ nằm ở Mục 1.2.3 và Bài 1.2.1 dùng dữ kiện của mục này.
- Bác đề xuất đổi cấu trúc index ngoài Bài 01 vì thuộc phạm vi đồng bộ toàn học phần, không phải lỗi của deck này. Giữ giả mã A06 không gắn lớp ngôn ngữ vì đây là giả mã, không có ngôn ngữ lập trình xác định. Giữ nhãn hiển thị “Bài 1” theo quy ước giao diện hiện có; `01` vẫn được dùng trong tên tệp và đường dẫn.

### Biên tập bản cuối

- Dùng `$no-ai-slop` trên toàn bộ nội dung hiển thị và ghi chú diễn giả. Kiểm tra theo `no-ai-slop/eval.md` không còn lời dẫn rỗng, nhãn quy trình, câu tổng kết lặp, quảng bá hoặc nhịp câu máy móc.
- Rà theo Quill Revise Workflow: chuỗi kho nhật ký → đặc tả → thuật toán → bất biến → chi phí và chuỗi mô hình ngẫu nhiên → kỳ vọng → bài tập giữ nguyên dữ kiện, ký hiệu và đầu ra. Không tạo `quill.json`.
- Ghi chú bài giảng chỉ đổi một công thức để thống nhất ký hiệu véc-tơ $\mathbf{y},\mathbf{z}$ và chỉ số $j$; đã rà lại E01 của deck và N09 của ghi chú.

### Kiểm định kỹ thuật và trực quan

- 41 `data-slide-id` duy nhất, 41 ghi chú diễn giả, 48 thẻ `<section>` mở/đóng cân bằng và bảy section ngoài.
- Năm SVG phân tích XML thành công, có `role="img"`, `title` và `desc`; không có ảnh raster hoặc tài nguyên lõi từ mạng.
- Chromium duyệt đủ 41 trang ở 1280×720, 800×600 và 720×900: không tràn khung, không lỗi JavaScript, KaTeX, trang hoặc yêu cầu tài nguyên.
- Điều hướng bàn phím đi đúng từ P00 xuống P01 và sang A00. Bản in A4 có 41 trang; 41 ghi chú tồn tại; không có phần tử `.katex-error`.
- Ảnh render D03, D04, E01, E02, E03, R01 và R02 được xem trực tiếp; công thức, nhãn SVG và phần bài tập đều đọc được.
- `index.html` đã có đúng liên kết Bài giảng và Ghi chú của Bài 01; không cần đổi URL hoặc tài nguyên.
- Dự án Codex Slides chuẩn `20260827112432-b-i-1-b-i-to-n-d-li-u-l-n-v-m-h-nh-thu-t-8tlj` đọc được nhưng vẫn ở bước làm rõ với 0 trang nội bộ. Browser Codex Slides không khả dụng trong phiên; vì vậy bằng chứng trực quan dùng RevealJS cục bộ và Chromium, không tuyên bố đã xem deck trong Codex Slides.

### Tái kiểm

- Toán–giải thuật: phiên `50263`, GLM/OpenRouter, PASS; tính lại D04, R02, R03, R05 và xác nhận bất biến, chi phí, giả thiết cùng hai SVG.
- Mạch/no-ai: phiên `29457`, GLM/OpenRouter, PASS; xác nhận E01, E03, R01, năm SVG, bảy mạch và việc dọn nhãn quy trình đều đạt.
