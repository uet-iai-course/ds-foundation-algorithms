# Nhật ký rà soát Bài 2

## Phạm vi bản nháp

- Tệp đích: `2627-1/lecture-02-mapreduce-va-ngan-xep-xu-ly-du-lieu-lon.html`.
- Nguồn chính: MMDS 3e Chương 2 và `sources/reference-slides/mmds/ch02-mapreduce.pdf`, trang chiếu 2–40 theo ánh xạ chọn lọc. Ghi công bộ trang chiếu: http://www.mmds.org.
- Phần giảng: 120 phút.
- Phần bài tập: 60 phút, chỉ dùng MMDS Bài 2.2.1(a–c) và 2.3.1(a–d).
- Ngoài phạm vi: PageRank, phép nối, nhân ma trận–vector và Bài 2.5.1.

## Quyết định biên tập ban đầu

| Quyết định | Lý do | Trang bị ảnh hưởng |
|---|---|---|
| Tách nền tảng MapReduce khỏi PageRank | Tuân theo thứ tự đề xuất trong `sources/source.md`; PageRank thuộc Bài 3 | Toàn bộ |
| Mở bằng kho tài liệu phân tán | Dùng lại trực tiếp trong Word Count, chi phí và lệch tải | A00–D04 |
| Giữ ba vai trò map, nhóm khóa, reduce | Ngăn người học nhầm nhóm khóa là mã do người dùng viết | B00–B04 |
| Thêm đặc tả và chứng minh Word Count | Nguồn cho thuật toán và cơ chế; chuẩn học phần yêu cầu điều kiện và lập luận đúng | B05–B06 |
| Phân biệt reducer với Reduce task | Cần để giải đúng Bài 2.2.1 | C03–C05, R01–R04 |
| Đặt hai quy ước chi phí cạnh nhau | Giáo trình MMDS và bộ trang chiếu chính thức MMDS đếm khác nhau; không được trộn | D03–D04 |
| Chỉ định vị Spark | Giữ đúng phạm vi “ngăn xếp” mà không lấn sang API hoặc thuật toán ngoài mục tiêu | E00–E01 |
| Dịch sát bài tập và giữ nguyên yêu cầu toán học | Tuân yêu cầu bài tập lấy trực tiếp từ giáo trình | R01–R08 |

## Sai khác so với nguồn

- B01 dùng cụm từ tiếng Việt ngắn để chạy tay thay cho từ tiếng Anh trong Ví dụ 2.1–2.2. Quan hệ toán học và luồng cặp khóa–giá trị không đổi.
- C01 dùng số lần xuất hiện minh họa để cho thấy bộ kết hợp giảm số cặp. Đây không phải dữ liệu đo; ghi rõ trong notes.
- B05–B06 viết rõ điều kiện trước, điều kiện sau, trường hợp biên và bất biến từ thuật toán nguồn. Không thêm bảo đảm vượt quá mô hình nguồn.
- R06 gộp cách trình bày ý (a) và (b), không gộp yêu cầu hoặc lời giải.
- R01–R08 không thêm nhãn sản phẩm hoặc yêu cầu phụ ngoài giáo trình.

## Tài sản trực quan

| Tệp | Loại | Tình trạng |
|---|---|---|
| `img/lec-02/he-tep-phan-tan.svg` | Sơ đồ hệ tệp | Vẽ lại, có `role`, `title`, `desc` |
| `img/lec-02/luong-mapreduce.svg` | Luồng Word Count | Vẽ lại, có `role`, `title`, `desc` |
| `img/lec-02/phan-vung-va-bo-ket-hop.svg` | Luồng bộ kết hợp | Vẽ lại, có `role`, `title`, `desc` |
| `img/lec-02/khoi-phuc-tac-vu.svg` | Sơ đồ lỗi tác vụ | Vẽ lại, có `role`, `title`, `desc` |
| `img/lec-02/ngan-xep-du-lieu.svg` | Sơ đồ tầng phần mềm | Vẽ lại, có `role`, `title`, `desc` |

Không có ảnh raster và không có ngoại lệ tài sản.

## Tự kiểm biên tập `no-ai-slop`

- Giữ thuật ngữ nhất quán: map, reduce, Map task, Reduce task, bộ kết hợp, nhóm theo khóa, lệch tải.
- Cắt lời dẫn, nhận định quảng bá, câu hỏi tu từ và kết luận lặp.
- Mỗi trang có một luận điểm; các câu dài được chuyển sang notes.
- Không dùng số liệu, trích dẫn hoặc ví dụ thực nghiệm không có nguồn.
- Tiêu đề thuần Việt; chỉ giữ MapReduce, Word Count, Hadoop, HDFS và Spark là tên riêng hoặc tên thuật toán cần thiết.
- Không dùng nhịp đối lập giả, câu kết khẩu hiệu, emoji, dấu gạch ngang dài hoặc từ cường điệu.

Kết quả tự kiểm theo `no-ai-slop/eval.md`: đạt ở bản nháp; cần bốn tác tử rà soát độc lập xác nhận tiếp.

## Kiểm tra kỹ thuật bản nháp

- [x] Đối chiếu số `data-slide-id` với storyboard sau rà soát.
- [x] Kiểm tra mọi trang có ghi chú diễn giả.
- [x] Kiểm tra cấu trúc section ngang/dọc.
- [x] Kiểm tra KaTeX, đường dẫn SVG và tài nguyên cục bộ.
- [ ] Kiểm tra hiển thị 1280 × 720 và màn hình hẹp.
- [x] Chạy bốn rà soát độc lập và xử lý lỗi nghiêm trọng.
- [ ] Rà trực quan bằng Codex Slides hoặc ghi giới hạn công cụ.

## Báo cáo rà soát độc lập

### A. Kiểm định storyboard

| mức độ | trang chiếu | vấn đề | bằng chứng | đề xuất sửa | quyết định |
|---|---|---|---|---|---|
| chặn bàn giao | R01, R06 | Mặt trang thêm yêu cầu không có trong giáo trình | R01 buộc phân biệt thuật ngữ; R06 buộc dùng bộ kết hợp và “trạng thái đủ” | Chỉ giữ nguyên yêu cầu MMDS | Đã bỏ các yêu cầu thêm; hướng dẫn tổ chức và chấm chỉ còn trong ghi chú |
| nghiêm trọng | B03, C02, C03, D04 | Công thức không nằm trong dấu phân cách KaTeX | Chuỗi LaTeX xuất hiện trực tiếp trong thẻ `p` | Bọc bằng `$...$` | Đã sửa cả bốn trang |
| nghiêm trọng | R07, R08 | Đặt số nguyên vào sai trường của cặp đầu ra | R07 nói reducer “phát x”; R08 không giữ rõ $x$ ở trường giá trị của lượt 1 | Ghi rõ $(\text{khóa không dùng},x)$ | Đã sửa ghi chú R07; R08 đọc $x$ từ trường giá trị ở lượt 2 |
| trung bình | C06 | Câu hỏi và đáp án cùng xuất hiện | Hai thẻ dưới câu hỏi nêu thẳng cặp tổng–số lượng | Chuyển đáp án sang ghi chú hoặc mảnh hiện dần | Đã chuyển toàn bộ đáp án sang ghi chú; không dùng mảnh hiện dần để tránh lộ khi in |
| nhẹ | R01–R08 | Không dành thời gian giao việc | R01 ghi 0 phút | Phân bổ lại đủ 60 phút | Đã dùng nhịp $4+8+11+9+14+6+8=60$ phút |

### B. Góc nhìn sinh viên

| mức độ | trang chiếu | vấn đề | bằng chứng | đề xuất sửa | quyết định |
|---|---|---|---|---|---|
| nghiêm trọng | C02, C06, R06 | Phần giảng làm trước gần trọn bài trung bình và R06 mở rộng đề | C02 nêu trực tiếp trạng thái; C06 hiển thị lời giải; R06 yêu cầu bộ kết hợp | Giữ nguyên lý tổng quát ở C02, ẩn đáp án C06, trả R06 về đề gốc | Đã sửa; C02 nói tính đóng và ngữ nghĩa mà không dùng ví dụ trung bình |
| nghiêm trọng | A01, B01, C01, D02, E01 | Chữ trong năm SVG nhỏ khi chiếu | Nhãn 19–22 px và nhiều câu dài, đặc biệt C01, D02 | Tăng chữ và rút nhãn | Đã tăng nhãn chính lên khoảng 24–29 px, rút câu, ghi rõ “Reduce task” |
| nghiêm trọng | D03, D04 | $I,M,O$ chưa tự đủ; nghĩa của $M$ thay đổi | Ký hiệu chỉ có trong ghi chú; D04 gọi $M$ là số cặp | Định nghĩa trên mặt trang và dùng một nghĩa | Đã định nghĩa $I,M,O$ ở D03; $M$ luôn là kích thước dữ liệu trung gian |
| trung bình | C03–C05, R03 | Dễ lẫn reducer, Reduce task và máy | Ba cấp thực thi được nói chủ yếu trong ghi chú | Đặt phân biệt lên mặt trang | Đã sửa C04; C05 tách gộp tải trong task với lập lịch task lên máy |
| trung bình | C03, D03 | Ký hiệu $h,r,p(k),I,M,O$ xuất hiện trước định nghĩa | Công thức đứng riêng | Thêm chú giải ngay trên trang | Đã thêm ở C03 và D03 |
| trung bình | R01–R08 | Nhịp 60 phút không dành thời gian giao việc | Các trang dẫn ghi 0 phút | Dành 4 phút giao việc | Đã phân bổ lại đủ 60 phút |
| nhẹ | C06 | Lời giải xuất hiện ngay sau câu hỏi | Người học không có thời gian tự xây dựng trạng thái | Chỉ giữ câu hỏi | Đã thực hiện |

### C. Chuyên gia giải thuật và khoa học dữ liệu

| mức độ | trang chiếu | vấn đề | bằng chứng | đề xuất sửa | quyết định |
|---|---|---|---|---|---|
| trung bình | D03, D04 | Gọi hai công thức là chi phí mạng gây hiểu sai | $I+M$ và $I+2M+O$ còn gồm đọc, ghi hoặc đầu vào tác vụ | Gọi đúng là mô hình I/O hoặc kích thước dữ liệu vào tác vụ | Đã đổi tiêu đề, mô tả và ghi chú; nói rõ không chỉ là byte mạng |
| trung bình | C05, R03 | Lệch giữa task khác khả năng bộ lập lịch cân việc giữa máy | Nhiều task có thể tăng linh hoạt lập lịch dù giảm trung bình hóa tải trong task | Tách hai cơ chế | Đã tách trên C05 và trong hướng dẫn chấm R03, không thêm yêu cầu mới vào đề |
| trung bình | R07 | Cặp đầu ra chưa đúng quy ước khóa bị bỏ | $x$ cần nằm ở trường giá trị | Phát $(\text{khóa không dùng},x)$ | Đã sửa |
| trung bình | E01 | Ngăn xếp quá trừu tượng | Không gắn tên hệ với tầng | Gắn HDFS, Hadoop MapReduce và Spark | Đã sửa SVG, văn bản thay thế và ghi chú |
| trung bình | E02 | Tiêu chí “đầu ra nhỏ hơn dữ liệu trung gian” không phải điều kiện phù hợp | MapReduce vẫn có thể phù hợp khi đầu ra không nhỏ | Thay bằng theo lô, quét tuần tự, phân hoạch hoặc tổng hợp theo khóa | Đã sửa |
| nhẹ | R08 | Thiết kế một lượt có thể gây tập trung tải | Ghi chú cho phép một lượt nhưng chưa nêu bảo đảm tổng toàn cục | Chỉ chấp nhận khi giải thích đúng | Đã giữ như phương án phụ trong ghi chú, không biến thành đáp án chuẩn |
| nhẹ | C02 | Thiếu tính đóng và ngữ nghĩa qua nhiều lần gộp | Chỉ có kết hợp và giao hoán | Bổ sung hai điều kiện | Đã bổ sung trên mặt trang và ghi chú |

### D. Độ chính xác toán học và phản biện giảng dạy

| mức độ | trang chiếu | vấn đề | bằng chứng | đề xuất sửa | quyết định |
|---|---|---|---|---|---|
| nghiêm trọng | R07, R08 | Vị trí khóa–giá trị làm sai luồng hai lượt | Lượt 2 cần nhận $x$ ở trường giá trị | Sửa cả hai lời giải | Đã sửa và kiểm tra sự truyền dữ kiện giữa hai lượt |
| trung bình | P01 | Mục tiêu trên trang không khớp outline | Thiếu chứng minh tính đúng và phân biệt hai quy ước chi phí | Đồng bộ mục tiêu | Đã thêm hai ý, giữ năm gạch ngắn |
| trung bình | C05, C06 | Phần kiểm tra làm recitation thành chép lại | C05 trùng Bài 2.2.1(b); C06 lộ đáp án 2.3.1(b) | Chỉ kiểm tra cơ chế, không trình bày lời giải hoàn chỉnh | C06 đã ẩn đáp án; C05 giữ câu hỏi cơ chế nhưng không giải trường hợp bộ kết hợp |
| trung bình | C03, D03–D04 | Ký hiệu chưa tự đủ | Người học phải dựa vào lời nói để hiểu miền ký hiệu | Định nghĩa trên mặt trang | Đã sửa |
| nhẹ | toàn bộ | Cần xác nhận cấu trúc section | RevealJS yêu cầu phần ngoài và trang trong | Kiểm tra lại cây section | Đã kiểm tra: sáu phần ngang, mỗi trang là section dọc; mã trang không đổi |

## Chỉnh sửa sau bốn rà soát

- Xử lý toàn bộ lỗi `chặn bàn giao` và `nghiêm trọng`.
- Giữ nguyên đề MMDS trên mặt R01–R08; bỏ toàn bộ nhãn sản phẩm và yêu cầu phụ. Việc dịch, gộp R06 và chia trang không đổi dữ kiện hay yêu cầu toán học.
- Không dùng đề xuất hiển thị đáp án C06 bằng mảnh hiện dần; chuyển hẳn vào ghi chú để bản in cũng không lộ lời giải.
- Không chọn thiết kế một lượt ở R08 làm đáp án chuẩn. Chỉ chấp nhận như phương án khác nếu người học chứng minh được tổng toàn cục.
- Rà lại các trang ảnh hưởng và hai trang lân cận: P00–A01; B01–B05; C00–D01; D01–E00; E00–E04; R00–R08. Không đổi thứ tự hoặc mã trang; các câu nối từ ví dụ đến đặc tả, chi phí và bài tập vẫn liên tục.
- Theo yêu cầu bổ sung của người dùng, đã so sánh slide chính thức MMDS với Stanford CS246 theo từng cụm. MMDS được chọn cho động cơ, hệ tệp, Word Count, thực thi, lỗi, bộ kết hợp, phân vùng và $I+2M+O$; Stanford 50–60 và 66 được chọn cho DAG, Spark và giới hạn theo lô vì trực quan và hiện thời hơn slide MMDS v2.1. MMDS 3e kiểm chứng phần bổ sung. Không sao chép CSS, tài sản nhị phân hay hình nguồn; nội dung được Việt hóa và hình được vẽ lại.

## Tự kiểm sau chỉnh sửa

- [x] Công thức tại B03, C02, C03, D03 và D04 dùng đúng dấu phân cách KaTeX; ký hiệu không chứa chữ Việt có dấu trong chế độ toán.
- [x] R01–R08 chỉ hiển thị đề MMDS đã dịch; lời giải và chấm nằm trong ghi chú.
- [x] Tổng phần giảng giữ 120 phút; phần bài tập dùng đúng 60 phút.
- [x] R07 phát $(\text{khóa không dùng},x)$; R08 giữ $x$ ở trường giá trị của lượt 1.
- [x] Năm SVG là tài sản cục bộ, có `role`, `title`, `desc`; nhãn đã tăng và rút gọn.
- [x] Không có PageRank, phép nối, nhân ma trận, ảnh raster hoặc phụ thuộc mạng mới.
- [x] Rà theo `no-ai-slop/eval.md`: không thêm mệnh đề ngoài nguồn; không còn lời dẫn rỗng, câu hỏi tu từ, nhịp đối lập giả, kết luận lặp hoặc từ cường điệu.
- [x] Rà mạch theo Quill Outline Workflow mà không tạo `quill.json`: động cơ → hệ tệp → khóa–giá trị → tính đúng → bộ kết hợp → thực thi → chi phí → phạm vi → bài tập; thuật ngữ và ký hiệu truyền liên tục.
- [x] Kiểm tra bằng Chromium headless ở 1280 × 720 và 800 × 600: 41 trang, 0 lỗi JavaScript hoặc tài nguyên, 0 trang tràn khung; đã duyệt bản ghép ảnh của toàn bộ 41 trang.
- [x] Dự án Codex Slides bền vững `20260827135942-b-i-2-mapreduce-v-ng-n-x-p-x-l-d-li-u-l--4cwy` vẫn truy cập được và giữ đúng yêu cầu, năm học, nguồn tải lên cùng cấu hình 30 trang. Dự án đang ở bước làm rõ, có 0 trang và không có lượt chạy; phiên này không có Codex in-editor Browser để mở liên kết bàn giao, nên không tuyên bố đã rà trực quan bằng Codex Slides. Bản RevealJS cục bộ là bản đã được kiểm định hiển thị.

## Kiểm định cuối

- HTML có 41 `data-slide-id` duy nhất và 41 khối ghi chú; cây có sáu phần ngang, các trang nội dung nằm ở cấp dọc.
- Năm SVG phân tích cú pháp XML thành công. Không có ảnh raster, tài nguyên cốt lõi từ xa hoặc liên kết tệp hỏng.
- Tổng thời lượng ghi chú là 120 phút giảng và 60 phút bài tập. Bài tập chỉ lấy từ MMDS 2.2.1(a–c) và 2.3.1(a–d).
- Kiểm tra Chromium cuối không còn cảnh báo KaTeX sau khi đổi hàm đếm từ có chữ Việt trong chế độ toán sang $f(w,d)$.
