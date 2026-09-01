# Nhật ký rà soát Bài 2

## Phạm vi bản nháp

- Tệp đích: `2627-1/lecture-02-mapreduce-va-ngan-xep-xu-ly-du-lieu-lon.html`.
- Nguồn chính: MMDS 3e Chương 2 và `sources/reference-slides/mmds/ch02-mapreduce.pdf`, trang chiếu 2–40 theo ánh xạ chọn lọc. Ghi công bộ trang chiếu: http://www.mmds.org.
- Phần giảng: 120 phút.
- Phần bài tập: 60 phút, chỉ dùng MMDS Bài 2.2.1(a–c) và 2.3.1(a–d).
- Ngoài phạm vi: PageRank, phép nối, nhân ma trận–vector và Bài tập 2.5.1.

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
- Hai ý 2.3.1(a) và 2.3.1(b) được tách thành hai trang dọc; dữ kiện, yêu cầu và lời giải của nguồn không đổi.
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

Kết quả tự kiểm theo `no-ai-slop/eval.md`: đạt ở bản nháp; các lượt rà soát độc lập được ghi theo từng chu kỳ bên dưới.

## Kiểm tra kỹ thuật bản nháp

- [x] Đối chiếu số `data-slide-id` với storyboard sau rà soát.
- [x] Kiểm tra mọi trang có ghi chú diễn giả.
- [x] Kiểm tra cấu trúc section ngang/dọc.
- [x] Kiểm tra KaTeX, đường dẫn SVG và tài nguyên cục bộ.
- [ ] Kiểm tra hiển thị 1280 × 720 và màn hình hẹp.
- [x] Chạy đủ năm vai rà soát độc lập trong chu kỳ 2026-08-30 và xử lý lỗi nghiêm trọng.
- [ ] Rà trực quan bằng Codex Slides hoặc ghi giới hạn công cụ.

## Báo cáo rà soát độc lập

### A. Kiểm định storyboard

| mức độ | trang chiếu | vấn đề | bằng chứng | đề xuất sửa | quyết định |
|---|---|---|---|---|---|
| chặn bàn giao | R01, R06 | Mặt trang thêm yêu cầu không có trong giáo trình | R01 buộc phân biệt thuật ngữ; R06 buộc dùng bộ kết hợp và “trạng thái đủ” | Chỉ giữ nguyên yêu cầu MMDS | Đã bỏ các yêu cầu thêm; hướng dẫn tổ chức và chấm chỉ còn trong ghi chú |
| nghiêm trọng | B03, C02, C03, D04 | Công thức không nằm trong dấu phân cách KaTeX | Chuỗi LaTeX xuất hiện trực tiếp trong thẻ `p` | Bọc bằng `$...$` | Đã sửa cả bốn trang |
| nghiêm trọng | R07, R08 | Đặt số nguyên vào sai trường của cặp đầu ra | R07 nói reducer “phát x”; R08 không giữ rõ $x$ ở trường giá trị của lượt 1 | Ghi rõ $(\text{khóa không dùng},x)$ | Đã sửa ghi chú R07; R08 đọc $x$ từ trường giá trị ở lượt 2 |
| trung bình | C06 | Câu hỏi và đáp án cùng xuất hiện | Hai thẻ dưới câu hỏi nêu thẳng cặp tổng–số lượng | Chuyển đáp án sang ghi chú hoặc mảnh hiện dần | Đã chuyển toàn bộ đáp án sang ghi chú; không dùng mảnh hiện dần để tránh lộ khi in |
| nhẹ | R01–R08 | Không dành thời gian giao việc | R01 ghi 0 phút | Phân bổ lại đủ 60 phút | Đã dùng nhịp $4+8+11+9+6+8+6+8=60$ phút |

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
| nhẹ | toàn bộ | Cần xác nhận cấu trúc section | RevealJS yêu cầu phần ngoài và trang trong | Kiểm tra lại cây section | Bản hiện hành có bảy phần ngang; mỗi trang là section dọc |

## Chỉnh sửa sau các rà soát trước

- Xử lý toàn bộ lỗi `chặn bàn giao` và `nghiêm trọng`.
- Giữ nguyên đề MMDS trên mặt R01–R08; bỏ toàn bộ nhãn sản phẩm và yêu cầu phụ. Việc dịch và tách hai ý R06 không đổi dữ kiện hay yêu cầu toán học.
- Không dùng đề xuất hiển thị đáp án C06 bằng mảnh hiện dần; chuyển hẳn vào ghi chú để bản in cũng không lộ lời giải.
- Không chọn thiết kế một lượt ở R08 làm đáp án chuẩn. Chỉ chấp nhận như phương án khác nếu người học chứng minh được tổng toàn cục.
- Chu kỳ trước đã rà các trang ảnh hưởng và hai trang lân cận. Chu kỳ 2026-08-30 đổi thứ tự phần B và thêm hai mã `lec02-r06a`, `lec02-r06b`; phạm vi này được rà lại riêng bên dưới.
- Theo yêu cầu bổ sung của người dùng, đã so sánh slide chính thức MMDS với Stanford CS246 theo từng cụm. MMDS được chọn cho động cơ, hệ tệp, Word Count, thực thi, lỗi, bộ kết hợp, phân vùng và $I+2M+O$; Stanford 49–60, 62 và 66–69 được chọn cho DAG, Spark, metadata Web, chi phí và giới hạn theo lô vì trực quan và hiện thời hơn slide MMDS v2.1. MMDS 3e kiểm chứng phần bổ sung. Không sao chép CSS, tài sản nhị phân hay hình nguồn; nội dung được Việt hóa và hình được vẽ lại.

## Tự kiểm sau chỉnh sửa

- [x] Công thức tại B03, C02, C03, D03 và D04 dùng đúng dấu phân cách KaTeX; ký hiệu không chứa chữ Việt có dấu trong chế độ toán.
- [x] R01–R08 chỉ hiển thị đề MMDS đã dịch; lời giải và chấm nằm trong ghi chú.
- [x] Tổng phần giảng giữ 120 phút; phần bài tập dùng đúng 60 phút.
- [x] R07 phát $(\text{khóa không dùng},x)$; R08 giữ $x$ ở trường giá trị của lượt 1.
- [x] Năm SVG là tài sản cục bộ, có `role`, `title`, `desc`; nhãn đã tăng và rút gọn.
- [x] Không có PageRank, phép nối, nhân ma trận, ảnh raster hoặc phụ thuộc mạng mới.
- [x] Rà theo `no-ai-slop/eval.md`: không thêm mệnh đề ngoài nguồn; không còn lời dẫn rỗng, câu hỏi tu từ, nhịp đối lập giả, kết luận lặp hoặc từ cường điệu.
- [x] Rà mạch theo Quill Outline Workflow mà không tạo `quill.json`: động cơ → hệ tệp → khóa–giá trị → tính đúng → bộ kết hợp → thực thi → chi phí → phạm vi → bài tập; thuật ngữ và ký hiệu truyền liên tục.
- [x] Chu kỳ trước đã kiểm tra bằng Chromium headless ở 1280 × 720 và 800 × 600 với bản 41 trang. Kết quả này không thay thế kiểm tra hiển thị cho bản hiện hành 42 trang.
- [x] Dự án Codex Slides bền vững `20260827135942-b-i-2-mapreduce-v-ng-n-x-p-x-l-d-li-u-l--4cwy` vẫn truy cập được và giữ đúng yêu cầu, năm học, nguồn tải lên cùng cấu hình 30 trang. Dự án đang ở bước làm rõ, có 0 trang và không có lượt chạy; phiên này không có Codex in-editor Browser để mở liên kết bàn giao, nên không tuyên bố đã rà trực quan bằng Codex Slides. Bản RevealJS cục bộ là bản đã được kiểm định hiển thị.

## Kiểm định cuối

- HTML hiện có 42 `data-slide-id` duy nhất và 42 khối ghi chú; cây có bảy phần ngang, các trang nội dung nằm ở cấp dọc.
- Năm SVG phân tích cú pháp XML thành công. Không có ảnh raster, tài nguyên cốt lõi từ xa hoặc liên kết tệp hỏng.
- Thời lượng chỉ nằm trong outline và storyboard: 120 phút giảng, 60 phút bài tập. Bài tập chỉ lấy từ MMDS 2.2.1(a–c) và 2.3.1(a–d).
- Kiểm tra Chromium cuối không còn cảnh báo KaTeX sau khi đổi hàm đếm từ có chữ Việt trong chế độ toán sang $f(w,d)$.

## Chu kỳ rà soát 2026-08-30

### Runtime và phạm vi

- Một tác tử kiểm định storyboard và năm tác tử rà soát độc lập chạy qua OpenRouter. Mọi kết quả có `requested_model = z-ai/glm-5.3-flash`, `observed_model = z-ai/glm-5.3-flash`, `provider = OpenRouter`.
- Các tác tử chỉ đọc HTML, ba tệp quy trình và phần nguồn được giao. Tác tử sửa được giới hạn ở HTML cùng ba tệp quy trình của Bài 2.
- Hai báo cáo trong thư mục tạm cảnh báo thiếu SVG và tệp trích `.txt`. Điều phối viên bác cảnh báo này sau khi kiểm tra kho thật có đủ năm SVG và các PDF gốc; tệp `.txt` chỉ là bản trích tạm để giảm phạm vi đọc, không phải học liệu bắt buộc.

### Kiểm định storyboard

| mức độ | trang chiếu | vấn đề | bằng chứng | đề xuất sửa | quyết định |
|---|---|---|---|---|---|
| nghiêm trọng | P00–R08 | Ghi chú diễn giả chứa thời lượng | Mọi notes của bản cũ kết bằng số phút | Chỉ giữ thời lượng trong outline và storyboard | Đã xóa toàn bộ tham chiếu thời lượng khỏi notes |
| trung bình | B02–B05 | Giả mã xuất hiện trước đặc tả điều kiện trước và sau | Thứ tự cũ là B02, B03, B04, B05 | Đưa B05 lên trước B02 | Đã đổi thứ tự thành B01, B05, B02, B03, B04; giữ mã trang |
| trung bình | E04 | Trang cuối phần giảng không thu hồi tình huống A00 | E04 cũ chỉ hỏi chọn khóa | Chuyển E04 thành kết luận | Đã thu hồi kho 400 TB, tuyến chia khối–khóa–chịu lỗi–chi phí và nối sang recitation |
| trung bình | C05–C06 | Câu hỏi phần giảng làm sẵn hai ý recitation | C05 dùng đúng số 10/10.000; notes C06 nêu trọn trạng thái | Giữ cơ chế, hoãn lời giải cụ thể | C05 dùng tình huống trung tính; C06 chỉ giữ tiêu chí kiểm tra |

### Góc nhìn sinh viên

| mức độ | trang chiếu | vấn đề | bằng chứng | đề xuất sửa | quyết định |
|---|---|---|---|---|---|
| nghiêm trọng | B02, B04 | Giả mã dùng cỡ chữ 0,65 em | Quy tắc `pre` thấp hơn ngưỡng thân bài | Nâng lên ít nhất 0,75 em | Đã nâng lên 0,75 em |
| trung bình | R06 | Cực đại và trung bình tranh cùng một trang | Hai bài toán thiết kế độc lập gộp trong 14 phút | Tách thành hai trang dọc | Đã tách thành `lec02-r06a` và `lec02-r06b`, giữ tổng 14 phút |
| trung bình | E04 | Thiếu điểm chốt cho năm mục tiêu | Phần giảng kết bằng câu hỏi khóa | Thêm kết luận đối chiếu tuyến bài | Đã chuyển E04 thành kết luận |

### Chuyên gia giải thuật và khoa học dữ liệu

| mức độ | trang chiếu | vấn đề | bằng chứng | đề xuất sửa | quyết định |
|---|---|---|---|---|---|
| trung bình | C03–C04 | `Reduce task` và `tác vụ reduce` dùng lẫn | Hai cách gọi cùng một đơn vị lập lịch | Chuẩn hóa thuật ngữ | Đã dùng nhất quán `Reduce task` |
| trung bình | E02 | Giới hạn vòng lặp thiếu giải thích chi phí | Chỉ liệt kê kém phù hợp | Nối với việc ghi và đọc trung gian | Đã bổ sung lập luận và nối với D03 |
| nhẹ | D03 | Hai công thức trông như hai đáp án cho cùng đại lượng | Hai thẻ đứng cạnh nhau | Nói rõ đo hai đại lượng khác nhau | Đã thêm kết luận trên mặt trang |

### Độ chính xác toán học và thuật toán

| mức độ | trang chiếu | vấn đề | bằng chứng | đề xuất sửa | quyết định |
|---|---|---|---|---|---|
| trung bình | E02 | Truy nguyên đặc tính hệ tệp sai trang | Notes cũ dẫn trang in 30–31 thay vì mục 2.1 | Dẫn trang in 21–24 | Đã sửa nguồn trong notes |
| nhẹ | A00 | Khoảng bốn tháng không bao phủ tốc độ 30 MB/giây | Phép tính cho khoảng 4,4–5,1 tháng | Ghi 4–5 tháng | Đã sửa mặt trang và notes |
| nhẹ | R06 | Biên tệp rỗng chưa nói rõ | Cực đại và trung bình không xác định | Ghi trong hướng dẫn chấm | Đã bổ sung ở hai trang tách |

### Phản biện học thuật và giảng dạy

| mức độ | trang chiếu | vấn đề | bằng chứng | đề xuất sửa | quyết định |
|---|---|---|---|---|---|
| trung bình | B06 | Mệnh đề và giả thiết chỉ nằm trong notes | Mặt trang cũ chỉ có bốn bước | Đưa mệnh đề và giả thiết lên mặt trang | Đã sửa B06 |
| trung bình | C02 | Điều kiện kết hợp, giao hoán thiếu cầu nối | Chưa nói thứ tự giá trị có thể thay đổi | Thêm lý do và phản ví dụ | Đã thêm lý do trên mặt trang, phản ví dụ trong notes |
| trung bình | D00 | Điều kiện chạy lại thiếu ví dụ đối lập | Chưa thấy hiệu ứng ngoài làm sai | Thêm ví dụ ghi trùng hoặc gửi lại | Đã thêm trong notes và ghi sai khác so với nguồn |

### Kết nối và mạch viết

| mức độ | trang chiếu | vấn đề | bằng chứng | đề xuất sửa | quyết định |
|---|---|---|---|---|---|
| nghiêm trọng | E04 | Vai trò kết luận chưa được thực hiện; kết nối vào từ E03 có nhưng không có kết nối ra thu hồi A00 | Trang cũ chỉ kiểm tra khóa, không nhắc kho 400 TB | Biến E04 thành kết luận; kết nối vào từ khuôn E03, kết nối ra sang R00 | Đã sửa và rà lại E02–R01 |
| trung bình | D05–E00 | Ranh giới từ chi phí job sang ngăn xếp đột ngột | Câu nối chỉ có trong storyboard | Thêm câu chuyển trong notes D05 | Đã sửa |
| nhẹ | B03–C03 | C03 lặp bảo đảm nhóm ở B03 | Chưa nói vai trò hình thức hóa | Gọi lại B03 trước công thức phân vùng | Đã sửa C03 |

### Quyết định sau hợp nhất

- Đã xử lý mọi phát hiện `chặn bàn giao` và `nghiêm trọng` hợp lệ. Cảnh báo thiếu tài sản do phạm vi thư mục tạm không được áp dụng.
- Không thêm trang kết luận mới; E04 được chuyển chức năng để giữ 7 mạch ngoài và tránh tăng nhịp phần giảng.
- Không đưa lời giải đầy đủ của câu hỏi trung bình vào notes C06; lời giải và hướng dẫn chấm vẫn nằm ở `lec02-r06b` theo đúng nguồn recitation.
- Không thêm caveat về cách Hadoop tùy chọn chạy combiner lên mặt trang vì bài dạy mô hình MMDS, không dạy API Hadoop. Nếu giảng viên cần nêu khác biệt cài đặt, dùng như lưu ý ngoài phạm vi.

### Trạng thái sau sửa

- Bản hiện hành có 42 trang, 42 notes và 7 section ngoài. Năm SVG cục bộ vẫn được tham chiếu đúng; không có ảnh raster.
- `no-ai-slop`: đã cắt thời lượng, nhãn quy trình và lời dẫn rỗng khỏi notes; tiêu đề và câu nối giữ tiếng Việt ngắn, trực tiếp.
- Quill được dùng ở mức rà liên tục: đặc tả đi trước giả mã; thuật ngữ `Reduce task`, các ký hiệu $h,r,p(k),I,M,O$ và tuyến A00–E04 nhất quán; không tạo `quill.json`.
- Codex Slides Browser không khả dụng trong bề mặt làm việc hiện tại. Chưa tuyên bố rà trực quan bằng Codex Slides cho chu kỳ này. Kiểm định kỹ thuật và hiển thị của bản 42 trang phải được chạy sau bước sửa.

### Rà lại sau chỉnh sửa cấu trúc

| mức độ | trang chiếu | vấn đề | bằng chứng | đề xuất sửa | quyết định |
|---|---|---|---|---|---|
| trung bình | D05–E00 | Notes D05 chưa thực hiện câu nối đã ghi trong nhật ký | D05 chỉ chốt chi phí lỗi | Nối giới hạn chuỗi job sang ngăn xếp | Đã bổ sung trong notes D05 |
| trung bình | E02 | Truy nguyên hệ tệp còn dẫn trang in 30–31 | Hệ tệp thuộc MMDS mục 2.1 | Sửa thành trang in 21–24 | Đã sửa notes E02 |
| trung bình | C02 | Phản ví dụ nói sai rằng phép trừ có tính kết hợp | $(a-b)-c \ne a-(b-c)$ | Nêu phép trừ không kết hợp, không giao hoán | Đã sửa |
| trung bình | C05 | Câu hỏi cũ hàm ý tăng số Reduce task giảm tải của một khóa lớn | Một khóa vẫn về đúng một Reduce task | Tách rõ trung bình hóa trong task và linh hoạt lập lịch | Đã sửa mặt trang và giữ lời giải cơ chế trong notes |
| nhẹ | B05, C06 | Hai ranh giới B01–B05 và C06–D00 còn mờ | Notes chưa gọi lại vết chạy hoặc phần kế | Thêm câu nối | Đã bổ sung |
| nhẹ | B06 | Giả thiết dùng `reducer` thay cho đơn vị lập lịch `Reduce task` | B03 và C04 đã phân biệt hai khái niệm | Chuẩn hóa thuật ngữ | Đã sửa |

Rà lại mạch xác nhận đủ 7 section ngoài, 42 trang, mở đầu P, kết luận E04 và phần recitation R; không còn lỗi `chặn bàn giao` hoặc `nghiêm trọng`. Rà lại độ chính xác xác nhận A00, B05–B07, D03–D04, các biên ở hai trang R06 mới và luồng khóa–giá trị R07–R08 đúng sau các sửa trên.

### Kiểm định kỹ thuật cuối chu kỳ

- Lệnh `python3 -m reloadserver 8765` không khả dụng vì môi trường không cài mô-đun `reloadserver`; dùng cùng triển khai cục bộ `/tmp/reloadserver.py` với đối số vị trí `8765` từ thư mục gốc kho. URL kiểm tra: `http://localhost:8765/2627-1/lecture-02-mapreduce-va-ngan-xep-xu-ly-du-lieu-lon.html`.
- Chromium headless duyệt đủ 42 trang tại 1280 × 720 và 800 × 600: không tràn ngang hoặc dọc, không lỗi JavaScript, không lỗi trang và không yêu cầu tài nguyên thất bại. Ảnh kiểm B06 và E04 được xem trực tiếp ở cả hai kích thước.
- Kiểm tra tĩnh xác nhận 42 mã trang duy nhất, 42 khối notes, 7 section ngoài và 15 tham chiếu tệp cục bộ đều tồn tại. Năm SVG có `role="img"`, `title` và `desc`; không có ảnh raster.
- `2627-1/index.html` đã có liên kết duy nhất tới HTML Bài 2; không cần sửa danh mục trong chu kỳ này.
- Runtime Codex Slides cục bộ chỉ khởi động được ngoài sandbox do lỗi `listen EPERM` ở cổng 4311. Lệnh đọc dự án xác nhận dự án bền vững còn ở trạng thái `draft`, giai đoạn `clarify`, 0 trang và 0 outline; không có bản render để đối chiếu. Codex Slides Browser không khả dụng, vì vậy không tuyên bố rà trực quan bằng Codex Slides và không tải bản HTML hiện hành lên dịch vụ.
- Lượt rà lại cuối bằng OpenRouter xác nhận không còn lỗi trung bình hoặc nghiêm trọng ở B05–B06, C02, C05–D00 và D05–E02. Sau đó chỉ thay mã nội bộ trong lời nói bằng mô tả khái niệm; kiểm thử Chromium được chạy lại và vẫn đạt.

## Chu kỳ xây dựng ghi chú bài giảng

### Quyết định phạm vi trước khi soạn

- Reader lập kế hoạch, reader nguồn và reviewer bản đồ chủ đề OpenRouter đều dùng `z-ai/glm-5.3-flash`; metadata quan sát khớp model yêu cầu và provider là OpenRouter.
- Giữ 11 chủ đề trong `.codex/goal_lecture_2.md`. Không đưa PageRank, phép nối, đại số quan hệ, nhân ma trận hoặc hướng dẫn API vào tuyến chính.
- Thêm có điều kiện chủ đề an toàn khi chạy lại. Gộp điều kiện đóng/cùng kiểu và bảo toàn ngữ nghĩa vào chủ đề bộ kết hợp. Cả hai là suy luận từ đặc tả, không gán nguyên văn cho MMDS.
- Đặt hai mô hình chi phí trong cùng một mục nhưng giữ phạm vi đo riêng: sách đếm tổng đầu vào task $I+M$; slide đếm tổng I/O tiến trình $I+2M+O$.
- Kiểm tra trực tiếp MMDS PDF trang 21 xác nhận Bài 2.3.1 xử lý tệp số nguyên lớn, không phải nhân ma trận. Giữ nguyên bốn yêu cầu và quy ước bỏ khóa đầu ra.
- Ghi chú dùng cùng ký hiệu, giả thiết, ví dụ Word Count và thứ tự khái niệm đã có trong deck. Chưa có thay đổi buộc sửa HTML; phải rà lại sau bản nháp.

### Sự cố worker trước bản nháp

- Lượt writer đầu đọc một gốc tạm quá rộng, chưa sửa tệp nào và dừng với lỗi nguyên văn `RuntimeError: OpenRouter request exceeded 300s wall timeout`.
- Không chấp nhận đầu ra dở dang. Lượt tiếp theo giữ nguyên model/provider, thu hẹp gốc ghi và chỉ giao soạn `lecture-note.md`; planning đã được Codex chính cập nhật trước theo goal duyệt.

### Năm lượt rà độc lập và sửa bản nháp

- Bản nháp được writer `deepseek/deepseek-v4-flash-0731` tạo qua OpenRouter theo ngoại lệ model mà người dùng chỉ định. Phạm vi, nguồn và cổng kiểm định không đổi.
- Năm reviewer độc lập dùng `z-ai/glm-5.3-flash` qua OpenRouter ở các góc nhìn sinh viên, chuyên gia giải thuật, độ chính xác, sư phạm và mạch nguồn. Metadata quan sát khớp model yêu cầu và provider là OpenRouter.
- Lỗi nghiêm trọng ở lời giải Bài 2.2.1(c) đã sửa: với 100 Map task và combiner, mỗi khóa có nhiều nhất 100 tổng cục bộ, nên lệch độ dài danh sách giảm mạnh và không còn đáng kể như trường hợp không có combiner.
- Ví dụ $I=100,M=40,O=10$ đã sửa: chênh lệch giữa 190 và 140 là $M+O=50$, do phạm vi hạch toán khác nhau; không suy ra byte mạng từ hiệu này.
- Động lực metadata Web đã sửa để thừa nhận quét tuần tự dùng bộ nhớ nhỏ vẫn khả thi, nhưng bị giới hạn bởi băng thông và thời gian của một máy. Kết luận quay lại đúng phép Map $(host,kích\,thước)$, combiner/reduce cộng và vai trò của $M$.
- Đã thêm nền function/task, kết hợp–giao hoán, tổng trên phân hoạch; chứng minh ngắn cho combiner; ký hiệu $h$ và $p(k)=h(k)\bmod r$; ví dụ khóa nóng định lượng; các câu tự kiểm tra và nguồn Word Count/trang lệch tải.
- Bài 2.3.1 được giữ theo bản PDF trang 21 đã kiểm tra trực tiếp. Đầu ra ý (c) dùng $(\text{khóa không dùng},x)$; bỏ câu ngoài phạm vi về nhân ma trận.
- Liên kết deck đổi sang đường dẫn theo ngữ nghĩa viewer. Các đường dẫn SVG `img/lec-02/*.svg` được giữ nguyên: năm tệp tồn tại trong kho và viewer phân giải chúng từ thư mục `2627-1/`. Cảnh báo thiếu SVG trong gốc tạm và đề xuất đổi sang `../../img` bị bác.
- Writer sửa tự động thất bại nhiều lần do timeout, giới hạn tool call và lỗi giải mã JSON. Theo xác nhận của người dùng, Codex chính trực tiếp áp dụng các sửa đã được năm reviewer phê duyệt; không mở rộng nguồn hoặc phạm vi.

### Biên tập, tái kiểm và công bố ghi chú

- `$no-ai-slop` được áp dụng trực tiếp lên toàn bản ghi chú. Bản cuối giữ nguyên dữ kiện và mệnh đề, cắt câu mang tính quy trình, tránh nhịp đối lập giả và kết thúc bằng phép MapReduce cụ thể cho kho metadata Web. Tự kiểm theo `no-ai-slop/eval.md` đạt.
- `$quill` được dùng để rà thứ tự và tính liên tục, không tạo `quill.json`: nền function/task và tổng trên phân hoạch đi trước đặc tả; Word Count truyền dữ liệu sang combiner và phân vùng; chạy lại nối sang chi phí; DAG/Spark dẫn về kết luận và bài tập. Ký hiệu $h,r,p(k),I,M,O$ nhất quán.
- Hai reviewer `recheck` độc lập dùng `z-ai/glm-5.3-flash` qua OpenRouter xác nhận các sửa kỹ thuật và mạch viết đạt; cùng phát hiện một lỗi nhẹ `$oplus$`. Sau khi đổi thành `$\oplus$`, lượt GLM tái kiểm cuối xác nhận không còn lỗi trung bình hoặc nghiêm trọng và không còn nội dung quy trình trong ghi chú. Mọi lượt đều có `requested_model = observed_model = z-ai/glm-5.3-flash`, `provider = OpenRouter`.
- Kiểm định viewer bằng Chromium headless đạt ở 1280 × 720 và 390 × 844: 32 mục nội dung/mục lục, 101 công thức KaTeX không lỗi, năm SVG tải đủ, bốn khối `hint`/`solution` gập mặc định, liên kết bỏ qua và thao tác bàn phím hoạt động, không tràn, không lỗi JavaScript hoặc yêu cầu thất bại.
- Kiểm định bản in xác nhận mọi `details` mở, mục lục bên và thanh hành động ẩn. Viewer từ chối đường dẫn traversal và từ chối `doc`/`deck` lệch số bài.
- Sau khi viewer đạt, `2627-1/index.html` được cập nhật bằng đúng một liên kết Ghi chú cho Bài 2. Kiểm tra Chromium ở màn hình rộng và hẹp xác nhận đủ 15 thẻ bài, Bài 2 có đúng hai tài nguyên, không tràn và không lỗi tải.
- Ghi chú không làm thay đổi ký hiệu, giả thiết, ví dụ hoặc kết luận dùng chung theo cách buộc sửa deck. Năm SVG hiện có được tái sử dụng nguyên trạng.
