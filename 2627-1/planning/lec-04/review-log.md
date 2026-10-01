# Nhật ký dựng lại dàn bài Bài 04

## Phạm vi và căn cứ ngày 27/09/2026

Yêu cầu: xoá toàn bộ dàn bài cũ và lập lại từ đầu bằng `build-slide-deck-outline`; chỉ dùng GPT-6-Astra `xhigh`; tiêu đề và nội dung trang chiếu trang trọng, học thuật, không văn nói hoặc chỉ dẫn người soạn. Chỉ dẫn bổ sung: **dùng sách làm nền để tạo mạch slide deck**.

Thay thế ba tệp kế hoạch tại `planning/lec-04/`; không nhập lại nội dung hay báo cáo đạt của bản trước. Không sửa HTML, hình, ghi chú bài giảng, mã thực hành hoặc trang chỉ mục trong yêu cầu lập dàn bài này. Không kế thừa tuyên bố render/kiểm định của sản phẩm cũ.

Kỹ năng đã đọc: `.agents/skills/build-slide-deck-outline/SKILL.md` cùng `references/course-context.md`, `references/output-template.md`; `/home/tqlong/.codex/skills/no-ai-slop/SKILL.md`, `eval.md`; `/home/tqlong/.codex/skills/quill/SKILL.md` và mục Outline Workflow. Quy định năm2 của kho thay mặc định năm3 của skill. Không tạo `quill.json`.

## Điều phối và bằng chứng tác tử

| Tác tử | Vai trò và thứ tự giao việc | Mô hình và mức suy luận được chỉ định | Đầu ra/quyết định |
|---|---|---|---|
| /root | Điều phối; soạn outline và nhật ký bản đầu | Phiên điều phối hiện tại | Hợp nhất nguồn và kế hoạch; chấp nhận 13 sửa cục bộ trước khi giao editor |
| /root/lec04_plan_fresh | Lập kế hoạch độc lập, sau đó được giao viết storyboard | gpt-6-astra, xhigh | Đề xuất 7 phần; viết đủ 51 phiếu theo outline mới; ngừng sửa trước vòng phản biện |
| /root/lec04_source_fresh | Phân tích nguồn; sau đó rà độc lập toán học và thuật toán | gpt-6-astra, xhigh | Kiểm kê 192 trang slide nguồn; đối chiếu MMDS §5.3–5.5; kiểm công thức, giả mã, bảng số, lời giải |
| /root/lec04_external_compare | Đối chiếu Cambridge và bố cục; rà độc lập học thuật/giảng dạy; sau khi đủ năm báo cáo mới được giao editor | gpt-6-astra, xhigh | Báo cáo AR01–AR07 được chốt trước khi chuyển vai; chỉ sửa ba tệp kế hoạch theo phiếu điều phối |
| /root/lec04_student_review | Rà độc lập từ góc nhìn sinh viên năm 2, chỉ đọc | gpt-6-astra, xhigh | Rà tải nhận thức, tiên quyết, đường giải tay và thời lượng |
| /root/lec04_flow_review | Rà độc lập kết nối và mạch viết, chỉ đọc | gpt-6-astra, xhigh | Rà đủ 51 kết nối vào–ra; đề xuất F1/F2 |
| /root/lec04_expert_review | Rà độc lập chuyên ngành giải thuật và khoa học dữ liệu, chỉ đọc | gpt-6-astra, xhigh | Báo cáo CG-01/CG-02 về phạm vi chi phí và đồng bộ mô hình |

Các tác tử con được tạo với model gpt-6-astra, reasoning_effort xhigh và fork_turns none; các vai tiếp theo được giao bằng lời gọi follow-up. Bằng chứng chỉ định nằm trong lời gọi `collaboration.spawn_agent` của phiên này. Không có bằng chứng độc lập về tuyến xác thực hoặc mô hình thực chạy ngoài thông tin công cụ; không coi lời tự khai là chứng cứ. Không gọi OpenRouter, script mô hình, API mô hình hoặc nạp tệp khóa.

## Tiếp nhận nguồn và trạng thái truy cập

- Đọc `sources/source.md`: Bài04 theo thứ tự đề xuất, buổi gốc5, CLO2; tiên quyết Bài03.
- Dòng4 `sources/reference-slides/README.md`: MMDS linkanalysis1/2 và Stanford10-spam đều hiện diện. Sách `sources/textbooks/mmds-3e-ch05-link-analysis.pdf` có38 trang; phần§5.3–5.5 là PDF21–34, số in195–208.
- Tác tử nguồn đọc trọn60+60+72 trang nguồn, xem contact sheet, kiểm riêng hình dùng ở độ phân giải cao. Điều phối viên đối chiếu trực tiếp Hình5.15,5.16,5.9 và các trang minh họa MMDS2 10,33,57; kiểm các phép tính từ văn bản sách.
- [Trang Stanford](https://web.stanford.edu/class/cs246/) và [PDF Stanford](https://web.stanford.edu/class/cs246/slides/10-spam.pdf) mở được. Trang `http://www.mmds.org`, HTTPS và bản không `www` bị hết thời gian chờ qua công cụ web; đã đọc được PDF chính thức cục bộ cùng trang ghi công. Đây là giới hạn truy cập trang chủ, không phải thiếu nguồn nội dung.
- [Cambridge](https://www.cl.cam.ac.uk/teaching/1112/InfoRtrv/lecture_slides2.pdf), Simone Teufel, Lent2012: đọc65–85 và xem79–85. So sánh cách dẫn nhập, vết số, công thức, giả mã và mật độ; không dùng làm nguồn trục.
- Đã đọc [SLIDE_STYLE_GUIDE.md](https://github.com/uet-iai-course/machine-learning/blob/main/SLIDE_STYLE_GUIDE.md). Không kế thừa khuyến nghị văn nói, không sao giao diện hoặc tài sản.
- Cornell CS431/2006 và CS5220/2024 đã được thử nhưng không chọn: tài liệu thứ nhất chỉ phù hợp PageRank cơ sở; tài liệu thứ hai chủ yếu thuật toán đồ thị tổng quát, không có cụm HITS đủ chi tiết. Không tính hai nguồn này là đối chiếu HITS.

## Hợp nhất đề xuất trước bước soạn

Điều phối viên chấp nhận mạch sách §5.3 → §5.4 → §5.5. Tách các bước của sách thành7 phần: bài toán, PageRank theo chủ đề, cơ chế liên kết rác, TrustRank/Spam Mass, HITS, so sánh, bài tập. Không dùng mục lục của slide Stanford hoặc dàn bài cũ làm khuôn.

| Nội dung | Quyết định | Bằng chứng và lý do |
|---|---|---|
| Truy vấn đa nghĩa và giới hạn vector từng người | Giữ | Sách§5.3.1 tr.195–196; tạo nhu cầu và được thu hồi trong phân tích lưu trữ/so sánh |
| VD5.10/Hình5.15 | Giữ | Đồ thị nối với Bài03, dùng lại được cho TrustRank và Bài5.3.1 |
| Đổi bước nhảy và giữ bù nút cụt | Thêm cầu nối | Bài03 bù đều; phải tách khỏi phân phối chủ đề mới để không mất tổng1 hoặc đổi mô hình ngầm |
| Bảo toàn, tính co, cận dừng | Bổ sung | Phương trình nguồn cần lập luận đúng và tiêu chí dừng; suy ra từ tổng cột1, ghi là diễn giải toán học của dàn bài |
| Cụm thao túng | Tách | Kiến trúc, điểm hỗ trợ, dòng quay lại, phương trình và hệ số có các sản phẩm suy luận khác nhau |
| Spam Mass | Sửa bảng số | Hình5.17 dùng PageRank không dịch chuyển với TrustRank beta0.8; tính lại cả hai cùng beta0.8 |
| HITS | Giữ sách, sửa phát biểu quá mạnh ở slide tham khảo | Chuẩn max và hai lượt VD5.15; không trộn chuẩnL2/tổng1; không khẳng định giới hạn duy nhất vô điều kiện |
| Jaccard§5.3.4 | Chuyển chi tiết sang Bài05 | Chưa học Jaccard; Bài04 chỉ nhận chủ đề và tỷ lệ quan tâm làm đầu vào |
| SimRank/Pixie/Twitter | Bỏ khỏi tuyến chính | Ngoài phạm vi sách§5.3–5.5 và không phục vụ mục tiêu bắt buộc |
| Bài5.4.1 | Giữ(a,c), lược(b) | Bảo toàn dữ kiện hai ý; tránh mở thêm mô hình bù nút cụt trong bài phân tích20 phút |
| Bài5.5.2 | Giữ nguyên hình và yêu cầu | Lời giải theo n vừa20 phút; Hình5.9 có khuyên ở đỉnh1, không được thay bằng chuỗi thuần |
| Bài5.5.1 | Bỏ khỏi recitation | Nghiệm G4 cần lặp số hoặc đa thức bậc ba; không được chỉ làm hai vòng rồi coi hoàn tất |

## Sai khác nguồn đã xử lý

1. Sách tr.203/Hình5.17: bảng Spam Mass mới giữ đồ thị và tập tin cậy nhưng đổi PageRank đều về beta4/5, công khai là phép tính lại. Không gán số mới cho bảng nguyên nguồn.
2. Sách tr.201: giữ phương trình đầy đủ có bước nhảy trực tiếp vào đích trước khi ghi mô hình xấp xỉ; hệ số khoảng3.6 lần không diễn đạt thành tăng360%.
3. MMDS2 tr.45/Stanford65: thay kết luận nhị phân về spam bằng chỉ báo cần rà soát; giá trị âm hợp lệ, chỉ số không phải xác suất.
4. MMDS2 tr.55,58–59 dùng nhiều chuẩn HITS; thống nhất chuẩn max sách tr.205–207, uy tín trước rồi trung tâm dùng uy tín mới. Công thức chỉ số trong slide tham khảo được kiểm lại bằng L và chuyển vị.
5. MMDS2 tr.56 nói điểm ổn định duy nhất: chỉ giữ phát biểu có điều kiện phổ. Sách tr.208 gọi nghiệm dương, trong khi cả hai nghiệm của đa thức đều dương: nếu trình bày nghiệm, dùng “trị riêng lớn nhất”.
6. Bài5.5.2: đề nhắc chuỗi nhưng hình có khuyên. Đã bác đáp án sơ bộ cho chuỗi không khuyên, truy hình5.9 rồi tính lại theo đúng cạnh. Trường hợp n=1 vẫn có cạnh tự khép.
7. DMOZ, tên miền và nhận định công cụ tìm kiếm trong nguồn thuộc bối cảnh lịch sử; không chuyển thành sự thật hiện hành. Không dùng số liệu quảng bá Pinterest trong bài.

## Phạm vi ảnh hưởng tới sản phẩm hiện có

Dàn bài mới không xác nhận nội dung HTML, ghi chú, bài thực hành và SVG cũ đã khớp. Khi được giao triển khai, phải đối chiếu lại toàn bộ cấu trúc và mã slide, bảng Spam Mass, quy ước ma trận/chuẩn hóa, bài tập và hình chuỗi; không kế thừa báo cáo đạt trước đây. Không đổi nguồn, đề cương, CSS hoặc trang chỉ mục ở bước này.

## Năm báo cáo độc lập trên bản storyboard mới

Bản đầu được rà có 51 phiếu, 51 khối nội dung hiển thị và 51 khối ghi chú học thuật. SHA-256 của storyboard trước chỉnh cuối: a9d50154bad90c560ec53fcc59eaad41f1c4b86fc67b0dbca7d6464fd648bd87. Bản sao cả ba tệp trước sửa được lưu tại /tmp/lec04-reset/before-final-edit/. Năm báo cáo được hoàn tất trước khi điều phối viên giao editor; đây là kết quả trên bản trước chỉnh, không phải xác nhận độc lập cho bản sau sửa.

| Vai rà | Phạm vi và bằng chứng chính | Kết quả trên bản trước chỉnh |
|---|---|---|
| Toán học và thuật toán | Đọc đủ 51 phiếu/102 khối; đối chiếu HT1–HT6, MMDS và lập luận co ở Bài 03. Dùng phân số chính xác để kiểm nghiệm PageRank, các hiệu Spam Mass, vết HITS, mô hình hỗ trợ và chuỗi có khuyên. | Không phát hiện lỗi chặn bàn giao hoặc nghiêm trọng về công thức, giả mã hay số liệu. Phát hiện điều kiện cạnh vào ở S07-02, câu metadata về cận dừng S02-08 và HT4 chưa đồng bộ. |
| Góc nhìn sinh viên năm 2 | Đọc đủ 51 phiếu, các vết chạy, gợi ý, tiêu chí và thời lượng; xác nhận chuẩn 1/tính co đã có ở Bài 03. | Không phát hiện lỗi chặn hoặc nghiêm trọng trong phạm vi sư phạm. Hai vấn đề trung bình: tải S02-08 và điều kiện S07-02. Các bước giải tay của ba bài tập đã có; thời lượng chỉ là ước lượng kế hoạch. |
| Học thuật và giảng dạy | Đọc đủ tiêu đề và 102 khối công khai; dùng no-ai-slop Detect/eval và quill; đối chiếu sách, G4/G5 và ba bài tập. | Mạch và vết số cơ bản đúng; chưa đạt biên tập công khai. AR01–AR07 chỉ ra giả thiết mâu thuẫn, ký hiệu thô, phép chia mơ hồ, nhãn đỉnh lẫn điểm, chỉ dẫn biên soạn/thuật ngữ/khoảng trắng và nhận định quá mạnh. |
| Kết nối và mạch viết | Đọc đủ 51 phiếu và kết nối vào–ra; xác nhận 7 phần, 48+3 phiếu, 120+60 phút và thứ tự sách. | Không phát hiện lỗi chặn hoặc nghiêm trọng về mạch. F1 nhẹ: báo rõ trở về dịch chuyển đều; F2 trung bình: đưa giới hạn tính toán vào mở HITS và thu hồi ở chi phí. |
| Chuyên ngành | Đối chiếu đặc tả, điều kiện áp dụng, chi phí, dữ liệu thưa, phạm vi sách và tiên quyết hội tụ Bài 03. | Không phát hiện lỗi chặn hoặc nghiêm trọng. CG-01 trung bình: phân biệt thời gian một vector với tiền tính nhiều chủ đề; CG-02 trung bình: đồng bộ HT4. Không yêu cầu đổi cấu trúc hoặc ví dụ. |

### Phát hiện, bằng chứng và quyết định hợp nhất

Các mã AR, F và CG giữ theo báo cáo tương ứng. Hai báo cáo toán học và sinh viên không đặt mã cho từng phát hiện; bảng dưới ghi tên vai để bảo toàn nguồn nhận xét. Những phát hiện trùng nhau được hợp nhất thành một sửa, không đếm thành lỗi độc lập mới.

| Mức độ; báo cáo | Vị trí | Bằng chứng trong bản được rà và tác động | Quyết định và sửa đã thực hiện |
|---|---|---|---|
| Trung bình; toán học, sinh viên, AR01 | S07-02, nội dung hiển thị | Câu “hỗ trợ chỉ nhận cạnh từ đích” được gọi là giả thiết giữ nguyên, trong khi cả hai ý (a), (c) thêm khuyên. Khuyên tạo cạnh vào từ chính hỗ trợ; lời giải đã tính đúng phần tự đóng góp. | Giữ bài 5.4.1(a,c) và toàn bộ đáp án. Đổi thành không có cạnh từ ngoài cụm vào hỗ trợ; đích vẫn chỉ trỏ tới các hỗ trợ. Đồng bộ BT2, phân biệt mô hình gốc với hai biến thể. |
| Trung bình; toán học và CG-02; đã được báo ở lượt outline | HT4, VD2, đối chiếu S03-02–05 | HT4 chưa nói toàn đồ thị không nút cụt, đích chỉ có các cạnh tới hỗ trợ, hỗ trợ chỉ nhận từ đích. Thiếu một trong các giả thiết này làm xuất hiện mẫu chia hoặc đóng góp khác. Storyboard đã có đủ, nên không quy thành lỗi mới của S03. | Ghi đủ các giả thiết trong HT4/VD2, dịch chuyển đều và nghĩa của $x$ đã nhân $\beta$, chia bậc ra. Không đổi công thức chính xác/xấp xỉ; BT2 dẫn đúng phạm vi sau khi đổi cạnh. |
| Trung bình; sinh viên; lưu ý tải trong AR | S02-08, 3 phút | Mặt slide đưa đồng thời $z$, $\bar M$, $F$, chứng minh co, duy nhất, cận dừng và ví dụ. Phần mới cần học là quan hệ giữa thay đổi hai vòng và sai số; tính co đã có ở Bài 03. | Giữ số phút; đưa $z$ và chứng minh đầy đủ vào ghi chú. Mặt slide mô tả ma trận đã bù, nhắc co trong một dòng, đặt tổng đuôi $\beta\Delta+\beta^2\Delta+\cdots$ làm trung tâm và giữ ví dụ $4\Delta$. Cập nhật bố cục, trọng tâm và HT2. |
| Nhẹ; toán học và AR07 | Luận điểm trung tâm S02-08 | “Cận sai số lớn hơn chênh lệch hai vòng” sai khi $0<\beta<1/2$; công thức cận bên dưới vốn đúng. | Đổi thành cận theo chênh lệch hai vòng với hệ số xác định; giữ miền $0<\beta<1$, cận cho vector mới và quy tắc chọn ngưỡng. Không thêm điều kiện giả để cứu câu metadata. |
| Trung bình; AR02 | Toàn bộ 102 khối công khai, nổi bật S02-07–09, S03-04/08, S04-07, S05-06/09/10, S06-01/04, S07-03 | Các dạng r^(j), beta r_j/d_j, rho_B, LL chuyển vị, h0/a1 nằm ngoài công thức; có vector bị chia giữa văn bản và các mảnh toán. Ký hiệu không thống nhất với outline và có thể hiện nguyên cú pháp thô. | Chuẩn hóa biểu thức trong prose bằng $...$ hoặc $$...$$ và LaTeX; giữ cùng chỉ số, hướng ma trận, biến và số. Rà cả mặt slide lẫn ghi chú. Bảo toàn nguyên hai khối giả mã text; tên biến chương trình vẫn được phép dùng mã nội dòng. |
| Trung bình; AR03 | Ghi chú S05-04, S05-05, S05-11 | “Chia max 3 cho h1”, “chia 29/10 cho h2” có thể bị đọc đảo phép chia. | Nêu rõ chia từng thành phần của vector thô cho giá trị lớn nhất và ghi vector/điểm kết quả. Giữ các giá trị $3$, $29/10$ và $h_B^1=1/2$. |
| Trung bình; AR04 | Ghi chú S07-01 | Dùng B=D, B=C để nói bằng điểm; ở (b) nói A “nhận thêm” sau khi (a) đã có phần dịch chuyển $1/5$. | Dùng $r_B=r_D$, $r_B=r_C$ và biến chung $q$. Nêu A đổi từ $1/5$ thành $1/10$, C đổi từ $0$ thành $1/10$; giữ hai nghiệm và phép kiểm. |
| Thấp nhưng cần sửa trước công bố; AR05 | S02-11, S02-08, S04-06 và các khối công khai | Notes S02-11 có “Bài này giữ…” về quyết định lược; S04-06 đổi “hạt giống” sang seed; S02-08 lặp việc dịch chuyển triệt tiêu; nhiều chỗ thiếu khoảng trắng như “có1/5”, “và0”, “khoảng3,6”. | Chuyển quyết định lược sang metadata; công khai giả thiết chủ đề do người dùng cung cấp. Thống nhất “hạt giống”, bỏ câu lặp và sửa khoảng trắng toàn phạm vi public. Giữ câu hỏi đánh giá, các phân biệt toán học và chỉ dẫn bố cục nội bộ đúng chức năng. |
| Thấp; AR06 | S03-01 | Câu “rà thủ công toàn bộ liên kết cần được thay” mạnh hơn căn cứ nguồn và làm mờ vai trò đánh giá hạt giống. | Đổi thành phân tích cấu trúc/chỉ số hỗ trợ xác định trang cần rà soát; không gán bảo đảm phân loại hoặc đề xuất quy trình mới. |
| Trung bình; CG-01 | HT3, S02-10 | Tiêu đề nói các vector chủ đề nhưng công thức thời gian chỉ tính một vector; $k$ mới xuất hiện ở bộ nhớ. Dễ suy tăng số chủ đề không tăng thời gian tiền tính. | Ghi phạm vi một vector trên mặt slide. Notes/HT3 dùng số vòng thực $K_j$: $\Theta((\sum_jK_j)(n+\ell))$. Giới hạn tối đa $K$ cho cận $O(kK(n+\ell))$. Khi mọi vector chạy đủ $K$ vòng, chi phí là $\Theta(kK(n+\ell))$. Tách lưu $kn$ số, ghép $c$ ứng viên và chi phí hệ tìm kiếm. |
| Nhẹ; F1 | Ranh giới S02→S03, S03-01 | S02 kết thúc với $S=\{B,D\}$; tín hiệu đổi về dịch chuyển đều trước phân tích cụm chỉ rõ ở ghi chú và phép tính sau. | Công khai ngay khi mở S03: xét PageRank toàn cục với dịch chuyển đều, thay đổi các cạnh trong cụm. Cập nhật câu nối và ánh xạ mạch; giữ một luận điểm và không thêm mô hình. |
| Trung bình; F2 | S05-01 nối S05-10 | Mở HITS có đầu ra hai vai trò nhưng chưa có giới hạn tính toán; chi phí thưa ở cuối chưa thu hồi giới hạn đã đặt. MMDS tr.204, 206, 208 có căn cứ về đồ thị đầu vào và phép lặp thưa. | Nêu đồ thị trang/liên kết đã chọn, nhu cầu tính hai vector trên đồ thị lớn bằng lặp theo cạnh. S05-10 thu hồi bằng hai lượt cạnh và tránh tích có thể đặc hơn. Không thêm quy mô giả định, tập gốc/tập cơ sở hoặc triển khai hệ tìm kiếm. |

### Các điểm được kiểm và giữ nguyên

- Toán học: giữ $M_0$ cột nguồn, bù nút cụt bằng $u$ độc lập với $v$, cập nhật đồng thời và trạng thái đạt ngưỡng/hết vòng. Giữ cận sai số của vector mới, điều kiện ghép cùng ma trận và $\beta$. Không dùng bảo toàn tổng thay cho hội tụ.
- Số liệu: giữ đồ thị G4 tám cạnh, vết PageRank và nghiệm cố định; bảng PageRank/TrustRank dùng cùng $\beta=4/5$, Spam Mass âm hợp lệ. Giữ mô hình hỗ trợ chính xác trước xấp xỉ và cách diễn giải hệ số nhân.
- HITS: giữ G5 đã khai báo khác G4, $L$ hàng nguồn, uy tín mới dùng để tính trung tâm, chuẩn theo giá trị lớn nhất, hai lượt cạnh và ca đồ thị không cạnh. Mặt S05-09 chỉ giữ quan hệ tỷ lệ; ghi chú giải nghĩa điều kiện phổ ở mức phác thảo, không thành đầu ra đánh giá mới.
- Bài tập: giữ MMDS 5.3.1(a,b), 5.4.1(a,c), 5.5.2; nguồn, dữ kiện, sản phẩm, thang chấm và 20 phút mỗi bài. Bài chuỗi giữ khuyên $1\to1$, quy nạp cho cả hai vector và biên $n=1,2$.
- Mạch: §5.3 → §5.4 → §5.5; G4 được dùng lại trong TrustRank/Spam Mass, G5 xuất hiện trước phép tính HITS. S02-11 giữ đủ bốn bước §5.3.3; chủ đề do người dùng cung cấp, không thêm Jaccard hoặc tiên quyết ngược sang Bài 05.
- Nguồn: NG4 ghi đủ Jure Leskovec và Charilaos Kanatsoulis, ngày 05/02/2026 theo trang đầu slide Stanford. Không đổi vai trò sách làm trục nội dung.

## Biên tập cuối và tự kiểm văn phong

Điều phối viên chấp nhận 13 mục sửa cục bộ trong phiếu giao editor, bao gồm các phát hiện hợp nhất ở trên, đồng bộ HT3/HT4/HT6 và hai cầu nối F1/F2. Editor chỉ ghi outline.md, storyboard.md, review-log.md; không dựng HTML/SVG, không sửa ghi chú công khai hoặc tài sản của bài cũ. Giữ 7 phần, 51 phiếu, 48 phiếu giảng/120 phút và 3 phiếu bài tập/60 phút.

Phạm vi no-ai-slop Edit: 51 tiêu đề và 102 khối công khai dự kiến; các trường bố cục, giới hạn và điều phối bên ngoài public được giữ là metadata. Đã đối chiếu trực tiếp eval.md ở mức tự kiểm của editor:

| Nhóm tự kiểm | Kết quả tự kiểm và bằng chứng |
|---|---|
| Bảo toàn nội dung và giọng học thuật | Giữ giả thiết, ký hiệu, phân biệt thuật toán, ví dụ và đáp án; chỉ sửa các điểm đã duyệt. Quy định học thuật của học phần được ưu tiên hơn gợi ý giữ văn nói của skill. |
| Từ ngữ và mẫu diễn đạt | Đã xử lý metacommentary ở S02-11, thuật ngữ seed/hạt giống, câu lặp ở S02-08 và khẳng định quá mạnh ở S03-01. Không thêm lời ca tụng, tu từ hoặc câu chỉ dẫn tác giả vào public. |
| Tính trực tiếp và chức năng học tập | Đã làm rõ đối tượng phép chia HITS, đại lượng điểm trong bài tập và phạm vi chi phí. Giữ các đối chiếu cũ/mới, tin cậy/uy tín, xác suất/điểm vì chúng ngăn lỗi học thuật. |
| Hình thức và lần đọc cuối | Công thức trong prose được chuẩn hóa; hai khối giả mã giữ tên biến. Không dùng điểm phát hiện AI hoặc suy đoán tác giả. Đây là tự kiểm bản biên tập, chưa thay báo cáo độc lập sau sửa. |

Quill được dùng để rà liên tục giữa các phần: bước nhảy chủ đề → dịch chuyển đều và đổi cạnh → tập tin cậy → chênh lệch tương đối; HITS chuyển sang hai vector với tổng điểm không chia bậc ra. Giữ nhất quán $M_0$ cột nguồn, $L$ hàng nguồn, $\beta$ theo cạnh, $\rho$ cho TrustRank, $h/a$ chuẩn max và $x$ đã gồm hệ số theo cạnh. Không khởi tạo quill.json.

## Ma trận sáu nhóm tiêu chuẩn ở mức dàn bài

| Nhóm tiêu chuẩn | Bằng chứng và quyết định sau biên tập | Giới hạn hoặc việc rà tiếp |
|---|---|---|
| Đối tượng | Năm 2; tiên quyết Bài 03 cho chuẩn 1/tính co; S02-08 giảm tải mặt slide, S05-09 không đặt nhiệm vụ phổ mới; bài chuỗi có bước quy nạp và hai biên. | Mạch và trọng tâm S02-08 đã được rà lại sau sửa; thời lượng chưa được giảng thử và mật độ cần kiểm trên bản render. |
| Mục đích và mạch | 51 phiếu có luận điểm, đầu vào/sản phẩm và kết nối; bám sách §5.3–5.5. F1 làm rõ đổi mô hình, F2 nối nhu cầu đồ thị lớn với chi phí HITS; bảy phần có kiểm tra riêng. | Hai ranh giới đã được tác tử mạch rà độc lập sau sửa; F1/F2 đã đóng. |
| Thuật toán | HT1/HT6 và S02-05–08, S05-06–10 có miền, quy ước ma trận, thứ tự cập nhật, chuẩn hóa, điều kiện dừng/trạng thái, lập luận và biên. Mô hình hỗ trợ là phân tích đại số, không ép thêm giả mã. | Tác tử toán đã đối chiếu phần thay đổi trong 102 khối công khai sau sửa; kiểm cú pháp được dùng bổ trợ cho kiểm toán học. |
| Ví dụ | G4 truyền nguyên trạng qua các phần; G5 được khai báo trước khi tính; HT4/VD2/BT2 đã thống nhất giả thiết. Các bài nguồn giữ số, đồ thị, sản phẩm và lời giải. | Không coi vài vòng HITS là chứng minh hội tụ tổng quát; hình mới chưa được dựng. |
| Chi phí | S02-10 phân biệt một vector, tổng số vòng chủ đề, lưu và ghép; S04-06 tách chi phí hai phép lặp và đánh giá hạt giống; S05-10 đếm hai lượt cạnh và bộ nhớ. | Chỉ là mô hình phép toán đơn vị/danh sách cạnh; không có số đo thời gian, I/O, băng thông hoặc chi phí toàn hệ tìm kiếm. |
| Trực quan hóa | Mỗi phiếu có bố cục, trọng tâm, giới hạn và lý do năm 2; giữ vị trí đỉnh, nhãn trạng thái, ba nguồn điểm và hai chiều đóng góp. Công thức/bảng/giả mã dự kiến là nội dung văn bản; sơ đồ dự kiến vẽ lại SVG. | Chỉ rà đặc tả. Chưa có render mới; chưa xác nhận cỡ chữ, mật độ, tràn khung, tương phản, KaTeX thực tế, SVG, bàn phím hoặc bản in. |

## Trạng thái bàn giao sau biên tập

Ba tệp kế hoạch đã được chỉnh theo các quyết định trên và đã qua hai lượt rà độc lập sau sửa: toán học/thuật toán và kết nối/mạch viết. Các phát hiện trước chỉnh đã có quyết định; không còn vấn đề toán học hoặc mạch đang mở trong phạm vi được rà. Bằng chứng kết thúc được ghi ở mục cuối tài liệu.

Chưa có bản render hoặc phát hành công khai mới. Không suy trạng thái hoàn tất HTML, SVG, ghi chú, trang chỉ mục hay sản phẩm cũ từ độ đầy đủ của dàn bài.

## Kết quả kiểm tự động ngày 28/09/2026

| Kiểm | Kết quả và phạm vi |
|---|---|
| audit_plan.py | PASS: 51 mã duy nhất/liên tiếp; 7 phần; 48 phiếu giảng/120 phút và 3 phiếu bài tập/60 phút. Các phần lần lượt có 6, 12, 8, 7, 11, 4, 3 phiếu. Chỉ kiểm cấu trúc. |
| check_math_markup.cjs, KaTeX cục bộ | PASS về cú pháp: 305 biểu thức trong outline, 689 trong storyboard, 47 trong review-log tại lần kiểm. Không có lỗi phân tích. Có cảnh báo thiếu thông số phông cho ba ký tự tiếng Việt trong lệnh text; cần kiểm khi render, không phải lý do bỏ dấu. |
| check_public.py | PASS: đủ 51 khối hiển thị và 51 khối ghi chú; không phát hiện metadata lẫn vào public, mẫu ký hiệu thô được dò, ký tự điều khiển hoặc lỗi cặp dấu toán. Đây là phép dò theo mẫu, không thay biên tập hoặc phản biện. |
| Bảo toàn giả mã | Hai khối giả mã text giống nguyên bản trước chỉnh cuối. |
| git diff --check -- 2627-1/planning/lec-04 | Mã thoát 0, không có lỗi khoảng trắng được Git báo. |

Lượt chỉnh và kiểm cuối diễn ra ngày 28/09/2026; ngày lập hồ sơ ban đầu vẫn là 27/09/2026. Các kiểm tự động được đối chiếu với hai báo cáo độc lập sau sửa và kiểm tra của điều phối viên ở mục dưới. Chúng không chứng nhận chất lượng render.


## Rà sau sửa và chốt dàn bài ngày 28/09/2026

| Người rà | Phạm vi | Kết quả và bằng chứng |
|---|---|---|
| /root/lec04_source_fresh | Diff của outline/storyboard so với bản trước chỉnh cuối; 51 mặt slide và 51 ghi chú; HT4/VD2/BT2, cận dừng, chi phí, hai bài tập và phép chuẩn hóa | Đã đóng các phát hiện về giả thiết, khuyên, cận dừng và ký hiệu. Các bảng số, hướng ma trận, chuẩn HITS, hai khối giả mã và lời giải chuỗi được bảo toàn. Không phát hiện lỗi mới còn mở. |
| /root/lec04_flow_review | 23 phiếu: S02-06–12, S03-01–05, S04-05–07, S05-01–04, S05-08–11; hai ranh giới S02→S03 và S04→S05 | F1/F2 đã đóng: giả thiết dịch chuyển đều xuất hiện trước phân tích cụm; giới hạn tính toán mở HITS được thu hồi bằng hai lượt cạnh. S02-08 nối được thay đổi hai vòng với sai số và vẫn cung cấp tính duy nhất cho S02-09. Không phát hiện lỗi mạch hoặc văn phong công khai mới trong phạm vi hậu kiểm. |
| /root | Đối chiếu diff, nội dung công khai đã đổi, nhật ký và các kiểm tự động | Chấp nhận hai báo cáo; xác nhận cả ba tệp kế hoạch đã thay nội dung cũ và hai khối giả mã giống bản trước chỉnh cuối. Giữ nguyên số phiếu, bảy phần và thời lượng. |

Lượt rà toán sau sửa phát hiện thêm một lỗi diễn đạt ở HT3 và ghi chú S02-10: câu “chỉ khi mọi vector đều chạy đủ K vòng…” biến một điều kiện đủ thành điều kiện cần. Điều phối viên đã đổi thành “Nếu mọi vector đều chạy đủ K vòng thì…”, đồng bộ nhật ký; tác tử toán kiểm lại đúng bản đã sửa trước khi chốt báo cáo. Công thức theo tổng số vòng thực chạy và cận trên theo số vòng tối đa không thay đổi.

Bằng chứng tính số của bản dựng lại: bốn nghiệm PageRank được thế lại bằng phân số chính xác và có tổng bằng 1; hai vòng HITS khớp cả hai vector; chuỗi có khuyên được kiểm với n từ 1 đến 8 và t từ 1 đến 5; phương trình cụm hỗ trợ và biến thể (c) được kiểm ở ba giá trị beta. Các số thử mô hình chỉ dùng kiểm nội bộ, không được đưa thành dữ kiện học liệu.

Kết quả cuối: hoàn tất yêu cầu dựng lại dàn bài Bài 04 với sách MMDS §5.3 → §5.4 → §5.5 làm nền. Đầu ra gồm outline, storyboard và nhật ký mới, 48 phiếu giảng/120 phút cùng ba bài nguồn/60 phút. Tiêu đề, nội dung dự kiến và ghi chú dùng văn phong học thuật; quyết định biên soạn được giữ trong metadata. Chưa triển khai hoặc phát hành lại HTML, SVG, ghi chú bài giảng và trang chỉ mục; các kiểm hiển thị sẽ được thực hiện ở bước triển khai được giao sau này.

## Triển khai bản nháp học liệu ngày 28/09/2026

Vai trò writer duy nhất trong giai đoạn này; điều phối viên đã chấp nhận kế hoạch triển khai và hồ sơ nguồn trước khi giao viết. Chỉ sửa các đường dẫn Bài 04 được giao, thẻ Bài 4 của index và một quy tắc CSS bố cục được giới hạn theo lớp gốc. Không sửa hoặc xóa thực hành/mã cũ, không đọc tệp môi trường, không tạo tác tử, không commit/push. Ba tệp kế hoạch giữ nguyên toàn bộ tiền tố của baseline đã duyệt; các mục triển khai được nối thêm.

### Bằng chứng sản phẩm và quyết định đồng bộ

| Vị trí | Vấn đề hoặc yêu cầu | Bằng chứng và xử lý |
|---|---|---|
| HTML Bài 04 | Deck cũ có cùng tổng 51 nhưng khác cấu trúc | Viết lại cây section theo đúng 6/12/8/7/11/4/3; đủ 51 mã đúng thứ tự và 51 notes. Giữ tiêu đề phiếu, câu hỏi, lời giải, nguồn cụ thể và ba bài nguồn |
| S02; ghi chú §1–2 | Ký hiệu cũ không còn khớp plan | Dùng $M_0$ cột nguồn, bù đều $u$ độc lập $v$, $r^0=v$, độ thay đổi chuẩn 1 và cận cho vector mới. Chi phí nhiều chủ đề theo tổng $K_j$ trong notes/ghi chú |
| S03; ghi chú §3 | Mô hình cụm cần giả thiết và ký hiệu nhất quán | Đổi generator và văn bản cùng sang $m,n,p,x,y,b$; $x$ đã gồm hệ số theo cạnh. Giữ riêng ba nguồn $x$, $\beta mp$, $b$; dẫn xuất chính xác và xấp xỉ có dấu quan hệ phù hợp |
| S04; ghi chú §4 | Bảng cũ ghép hai tham số beta | Tính lại PageRank nền và TrustRank cùng $4/5$; giữ $-23/95$, giải thích dấu và không gán nhãn chắc chắn |
| S05; ghi chú §5 | Chuẩn/khởi tạo HITS và thuật ngữ | Dùng điểm uy tín, $h^0=a^0=\mathbf1$, uy tín trước rồi trung tâm bằng uy tín mới; chuẩn max và trạng thái không xác định khi không có cạnh. Phát biểu giới hạn duy nhất có điều kiện |
| S07; ghi chú §7 | Bài cũ không trùng bộ nguồn đã duyệt | Dùng 5.3.1(a,b), 5.4.1(a,c), 5.5.2; chuỗi giữ khuyên tại 1 và xử lý $n=1,2$. Ba notes ghi 20 phút; không hiển thị thời gian trên mặt slide |
| Tài sản SVG | Hình cũ thiếu các biến thể và dùng ký hiệu cũ | 20 SVG được sinh từ cùng generator, có role/title/desc; G4/G5 giữ tập cạnh; thêm tập T, sơ đồ luồng, hai cấu trúc hỗ trợ và chuỗi có khuyên. Bảng/công thức/giả mã vẫn là HTML/KaTeX/text |
| Ghi chú và index | Tài liệu công khai đã dùng mô hình cũ | Soạn lại tài liệu tự học 586 dòng theo thứ tự định nghĩa–ví dụ–lập luận, 26 khối chức năng không lồng. Bỏ link thực hành cũ ở note và thẻ Bài 4, giữ nguyên tệp thực hành/mã |

### Sửa theo kiểm render/gate sơ bộ của điều phối viên

Đây là kiểm bản nháp trước năm lượt rà độc lập, không thay các lượt đó.

| Vị trí → vấn đề | Bằng chứng sơ bộ | Sửa trong bản nháp |
|---|---|---|
| S03-07 → hình một hỗ trợ thiếu cạnh quay về cho phép đếm $2m$ | Gate chỉ ra hình cũ chỉ có đích→hỗ trợ và dịch chuyển, trong khi văn bản đếm hai chiều | Tạo `hai-nhom-canh-noi-bo.svg` qua generator, thể hiện đúng $m$ cạnh mỗi chiều |
| S05-02 → thiếu nhãn G5 trước chỗ gọi lại | Danh sách cạnh đã chuyển vào hình nhưng tên G5 chưa công khai | Thêm nhãn “Đồ thị G5” dưới hình |
| S06-04 → nguồn chạm footer | Render đầu: ba khung câu hỏi có padding cộng dồn | Dùng một khung và danh sách số 3–5, giữ nguyên nhiệm vụ |
| S07-03 → sản phẩm/nguồn chạm hoặc vượt khung | Render đầu ghi nhận phần dưới quá dài | Giữ nguồn đầy đủ ở đầu trang và notes, bỏ nguồn lặp ở đáy; hình chuỗi dùng chiều cao 160px |
| S07-02 → chữ SVG nhỏ sau co | Root đo chữ nhỏ nhất khoảng 13.09px ở bản đầu | Tăng chữ SVG qua generator lên tối thiểu 30px, không giảm chữ HTML |
| S02-12, S03-08, S04-07, S05-11 → các ý nhiệm vụ chạy nối | Gate phát hiện Markdown thiếu dòng trắng trước danh sách | Dựng bằng `ol/li` trong khung câu hỏi, bảo toàn số thứ tự và dữ kiện |

CSS chỉ thêm `.reveal.lecture-pagerank-advanced .l04-chain-diagram { height:160px; }`; không đổi vai trò chữ, font, màu hoặc khoảng cách của lớp dùng chung. Điều phối viên đã có baseline render Lecture 02/03; việc kiểm lại sau thay CSS thuộc bước kiểm định do điều phối viên thực hiện.

### Tự kiểm writer và giới hạn

- Bộ kiểm cấu trúc riêng bằng trình phân tích HTML và XML: PASS, 51 mã đúng thứ tự, 51 notes, bảy phần đúng phân bố, 20 SVG có role/title/desc, 21 nơi nhúng ảnh có alt và đường dẫn tồn tại, không style nội dòng/block, không fragment, không ký tự điều khiển. Ghi chú có heading cấp một, cặp khối cân bằng, đường ảnh hợp lệ và chỉ dấu toán dollar. Bằng chứng: `/tmp/lec04-implementation/writer-static.json`.
- Đọc và chạy `/tmp/lec04-reset/verify_math.py`: PASS bốn nghiệm PageRank/tổng1, hai vòng HITS chuẩn max, chuỗi có khuyên với $n=1$ đến $8$ và năm vòng, các phương trình cụm và biến thể(c) ở ba beta. Các số thử chỉ phục vụ kiểm nội bộ.
- KaTeX cục bộ: PASS 518 biểu thức ghi chú; không lỗi phân tích. Có cảnh báo thông số phông cho một số ký tự tiếng Việt trong `text`; điều phối viên cần xem hình hiển thị thực. Bằng chứng: `/tmp/lec04-implementation/writer-note-math.json`.
- Kiểm KaTeX ba tệp planning sau ánh xạ: PASS 308/691/47 biểu thức tại thời điểm trước mục nhật ký này. Đây là kiểm cú pháp, không chứng minh nội dung hoặc bố cục.
- `git diff --check` trên whitelist: mã thoát 0 tại tự kiểm. Đối chiếu baseline xác nhận tiền tố outline/storyboard/review-log được bảo toàn.
- Kiểm `audit_static.py` của root không chạy được bằng Python hệ thống vì thiếu `bs4`; writer dùng bộ kiểm chuẩn thư viện riêng ở trên. Root có thể chạy công cụ gốc trong môi trường đã chuẩn bị.

### No-ai-slop Edit và quill continuity

Đã đọc `no-ai-slop/SKILL.md`, tự kiểm trực tiếp `eval.md`, áp dụng Edit cho 51 mặt slide/notes, văn bản SVG, ghi chú tự học và thẻ index. Mục tiêu là văn phong học thuật của học phần; không thêm giọng kể, khẩu hiệu hoặc suy đoán tác giả. Các nhóm bảo toàn ý/ngữ điệu, từ và mẫu diễn đạt, hình thức và lần đọc cuối đều đạt ở mức tự kiểm: giữ giả thiết/thuật ngữ/công thức/nguồn; bỏ chỉ dẫn giảng viên cũ; các đối chiếu có chức năng như bù–dịch chuyển, trung tâm–uy tín và chính xác–xấp xỉ được giữ. Không dùng điểm phát hiện AI. Bản đầy đủ được lưu trong các tệp sản phẩm; bảng trên ghi những thay đổi chính.

Áp dụng quill theo phạm vi continuity đã yêu cầu, không tạo `quill.json`: đồ thị tiên quyết theo outline; G4 và beta truyền từ chủ đề sang TrustRank/Spam Mass; S03 nêu trở lại dịch chuyển đều; G5 được phân biệt với G4; ký hiệu ma trận đổi có giải thích; khuyên và biên được giữ tới lời giải chuỗi. Ghi chú dùng thứ tự định nghĩa trước ví dụ, khác chu trình slide theo đúng quy định loại tài liệu. Không đưa nội dung đọc thêm ngoài bản đồ đã duyệt vào tuyến chính.

Tại thời điểm writer bàn giao, bản nháp HTML/SVG/ghi chú/index đã đầy đủ. Điều phối viên đang kiểm bản render sau sửa, viewer rộng/hẹp/bàn phím/in, Codex Slides và năm lượt rà độc lập. Writer không xác nhận các bước chưa hoàn thành, không tuyên bố phát hành và không commit/push.

## Năm lượt rà độc lập bản triển khai và biên tập sau phản biện, 28/09/2026

Điều phối viên đã đọc đủ năm báo cáo về sản phẩm triển khai và hợp nhất quyết định trước khi giao `/root/lec04_final_editor` làm editor riêng, duy nhất có quyền ghi trong lượt này. Tất cả tác tử trong bảng và editor được chỉ định native GPT-6-Astra, mức suy luận `xhigh`. Các báo cáo này rà HTML, SVG, notes và ghi chú tự học mới, không thay thế bằng kết quả của giai đoạn dàn bài. Báo cáo tạm được tóm tắt dưới đây vì không nằm trong Git.

### Phạm vi và kết luận của từng vai

| Tác tử; báo cáo | Phạm vi đã thực hiện theo báo cáo | Phát hiện và quyết định |
|---|---|---|
| `/root/lec04_impl_student`; `review-student.md` | Đọc 51 mặt slide/51 notes và toàn bộ ghi chú; xem 51 ảnh wide, 12 ảnh narrow đúng mã; kiểm viewer 1440×900/390×844, một khối gập bằng Enter, 10 hình và mẫu PDF trang 4/16/27; tự tính G4/HITS và các nhiệm vụ. | Không có lỗi nội dung chặn bàn giao/nghiêm trọng. SV-01 trung bình: bản in cắt hình do min-width 900px còn hiệu lực với Bài 04. Chấp nhận sửa selector in cho mọi bài. Khả năng đọc deck điện thoại vẫn cần phóng to; không đổi kiến trúc deck. |
| `/root/lec04_expert_impl_review`; `review-expert.md` | Đọc 51 slide/notes, toàn bộ ghi chú, sách §5.3–5.5 và đề bài; tính độc lập các nghiệm, vết lặp, chuỗi và mô hình cụm; xem mẫu ảnh. | E1 nhẹ: định vị tiểu mục TrustRank/HITS; E2 nhẹ: bỏ quy mô định lượng sẵn có trong mở bài. Chấp nhận sửa nguồn và khôi phục quy mô minh họa của MMDS. Không thêm phần, thuật toán hoặc bài tập. |
| `/root/lec04_source_fresh`; `review-math.md` | Lượt rà mới trên HTML triển khai: đọc đủ 51 slide/notes, toàn bộ ghi chú, SVG và nguồn; tính độc lập bằng phân số từ tập cạnh. Kiểm cận vector mới, bù đều, cụm và biến thể, chuẩn hóa HITS, biên chuỗi. | Không có lỗi toán/thuật toán chặn, nghiêm trọng hoặc trung bình. M01 nhẹ: dẫn mục nguồn; M02 nhẹ: `desc` nhầm điều kiện cạnh ra của đích. Chấp nhận sửa câu nguồn/desc; giữ toàn bộ mô hình, thuật toán và kết quả số. |
| `/root/lec04_academic_review`; `review-academic.md` | Đọc đủ 51 slide/notes, toàn bộ ghi chú, chữ/nhãn của 20 SVG và các nguồn; xem sáu ảnh wide, ba narrow; tự kiểm số hữu tỷ. Dùng no-ai-slop Detect/eval và quill. | A1 trùng M02; A2 nhẹ: “max” trong văn xuôi/trạng thái trả về; A3 trùng M01. Chấp nhận sửa cục bộ, giữ toán tử và các phân biệt toán học cần thiết. Không có căn cứ đảo mạch sách. |
| `/root/lec04_flow_review`; `review-flow.md` | Đọc đủ 51 slide/notes, toàn bộ ghi chú, nhãn hình, 13 chủ đề và các mốc sách; xem mẫu S03-02/S05-01/S06-02; kiểm các ranh giới phần và cầu nối F1/F2. | FL-01 nhẹ: nhãn $x$ xuất hiện sớm trên hình kiến trúc; FL-02 trùng lỗi nguồn. Chấp nhận nhãn “Đóng góp từ ngoài”, giữ định nghĩa $x$ tại S03-04. Không có lỗi mạch chặn, nghiêm trọng hoặc trung bình. |

Cả năm vai không đề xuất đổi 51 trang, bảy phần 6/12/8/7/11/4/3 hoặc thời lượng 120 + 60 phút. Các vai chỉ xem mẫu render không tự chứng nhận toàn bộ giao diện; không có giảng thử hay phép đo máy chiếu thực tế. Những phủ định có chức năng như điểm HITS không là xác suất, không chia bậc ra, trạng thái hết vòng và giả thiết của xấp xỉ được giữ qua biên tập.

### Vị trí, bằng chứng và cách sửa được duyệt

| Mã; vị trí | Bằng chứng lỗi cụ thể | Sửa và phạm vi |
|---|---|---|
| M01/A3/E1/FL-02; S04-02/03 | Nhãn §5.4.3 dẫn vào phần chống liên kết rác; định nghĩa TrustRank nằm ở §5.4.4, tr.202–203. | Sửa nguồn mặt slide/notes; S04-03 vẫn dẫn Ví dụ 5.10, tr.196–197 cho G4. Đồng bộ phiếu nguồn và §4.1 ghi chú. Các dẫn §5.4.3 dùng cho chống liên kết rác vẫn được giữ. |
| M01/E1/FL-02; S05-02/06 | Hình 5.18, Hình 5.19 và định nghĩa $L$ thuộc §5.5.2; HTML đã dẫn §5.5.1. | S05-02 dùng §5.5.2, Ví dụ 5.14, Hình 5.18, tr.205–206; S05-06 dùng §5.5.2, Hình 5.19, tr.206. Giữ §5.5.1 ở trực giác S05-01; đồng bộ storyboard. |
| M02/A1; S02-01 | `desc` viết “đi tới trang có cạnh ra”, vô tình đặt điều kiện cho đích. | Viết “đi tới đích của một cạnh ra từ trang hiện tại”; sửa generator rồi tái sinh SVG. Không đổi nhãn hiển thị, quan hệ hoặc công thức. |
| A2; S05-05/07/08 và §5.4 ghi chú | “đây là max của trung tâm thô”, “không thể chia max”, “theo chuẩn max” rút gọn không phù hợp văn phong học thuật. | Dùng “giá trị lớn nhất” và “chuẩn hóa bằng giá trị lớn nhất”; nêu rõ trường hợp vector thô bằng 0. Giữ `max` và $\max$ trong các phép toán; bước trả trạng thái chỉ đổi câu chữ. Đồng bộ vùng công khai của storyboard. |
| FL-01; S03-02 và §3.1 ghi chú | Hình kiến trúc ghi “x đã gộp hệ số β”, trong khi S03-04 mới định nghĩa $x$. | Nhãn hình dùng “Đóng góp từ ngoài”; mô tả thay thế cũng bỏ $x$ theo xác nhận bổ sung của điều phối viên. Giữ toàn bộ cạnh, nhãn khác và định nghĩa ở S03-04. |
| E2; S01-04 và §1 ghi chú | Sách tr.195–196 minh họa vector nhiều tỷ thành phần cho khoảng một tỷ người dùng; bản triển khai chỉ nói chiều dài bằng số trang. | Thay một câu trong takeaway bằng quy mô minh họa MMDS; ghi cùng căn cứ ở notes/ghi chú. Giữ câu về số ít vector chủ đề và các trọng số; không thêm số byte, số máy hay số đo hiện hành. SVG lưu trữ giữ nguyên. |
| Kỹ thuật viewer; bảng ở viewport 390×844 | Điều phối viên đo document.scrollWidth 396px, innerWidth 390px, body 375px. Thử CSS tạm thêm position:relative làm documentWidth về 375px. | Thêm `position: relative` vào `.markdown-body table`; giữ các thuộc tính và cỡ chữ hiện có. Không đổi nội dung để né vấn đề vùng cuộn. |
| SV-01; bản in ghi chú | Reviewer sinh viên thấy PDF trang 4 cắt cung D→B, trang 16 cắt hộp trang học phần; selector in chỉ áp dụng `img/lec-01/`, trong khi màn hình dùng mọi `img/lec-`. | Mở rộng đúng hai selector trong `@media print` thành `img/lec-`; giữ min-width:0, max-width:100%, height:auto và overflow:visible. Chú thích CSS chuyển thành quy tắc chung. Không đổi width/min-width màn hình 900px. |

Hai sửa CSS chung được điều phối viên mở whitelist cụ thể. Không sửa `lecture-style.css`, index, bài khác, thực hành/mã cũ, AGENTS, tiêu chuẩn hoặc cấu hình. Các bước triển khai trước đó đã sửa những tệp khác được ghi trong mục lịch sử; editor không nhận chúng là thay đổi của lượt này.

### Bằng chứng kiểm định của điều phối viên trước sửa

Theo `review-technical.md` và thông báo bổ sung của điều phối viên: 51 slide có 51 notes, bảy phần đúng phân bố; ảnh wide đã được kiểm cấu trúc/KaTeX/tài sản. Ảnh narrow cũ có thời điểm chụp sai bề mặt do chế độ cuộn của Reveal nên bị loại khỏi bằng chứng. Lượt chụp lại đợi đúng mã và cuộn đúng slide tạo đủ 51 ảnh riêng; Lecture 02/03 cũng được kiểm 81/63 ảnh narrow. Hồi quy wide 02/03 ghi nhận font, hình chữ nhật bố cục và ảnh bằng nhau; PNG có sai khác do controls/progress nên không được gọi là toàn bộ ảnh giống byte.

Hồi quy viewer trước sửa đã đo đủ 14 ghi chú công khai trong index. Chỉ Bài 01 co hình đúng khi in; các bài còn lại giữ min-width 900px. Bài 04 có 10 hình, 518 biểu thức KaTeX không lỗi và 12 khối gập; cả 33 vùng cuộn đã được điều phối viên thử Tab/ArrowRight. Ở màn hình hẹp, Bài 04 có documentWidth 396px trước sửa; Bài 09 đã có cuộn ngang 489px trước sửa. Nếu Bài 09 còn hiện tượng ấy sau sửa, đó là vấn đề tồn tại trước, không thuộc whitelist lượt này. Những kết quả trước sửa không chứng nhận bản cuối; điều phối viên sẽ đo lại 14 ghi chú, bàn phím và PDF Bài 04.

### No-ai-slop Edit/eval và quill sau chỉnh cục bộ

Editor đã đọc `no-ai-slop/SKILL.md` và tự đối chiếu `eval.md` sau chỉnh: bảo toàn nội dung/giọng học thuật, chỉnh tối thiểu, không thêm nhận định hoặc số liệu ngoài nguồn được duyệt; giữ câu mạnh đã rõ, các phân biệt toán học và cấu trúc. Các câu mới gọi đúng nguồn, đối tượng và phép chuẩn hóa; không dùng mở đầu rỗng, khẩu hiệu, câu hỏi tu từ hoặc chỉ dẫn người soạn. Các mục về từ rỗng, nhịp lặp, gán thẩm quyền mơ hồ, hình thức trang trí và lần đọc cuối không phát hiện lỗi mới trong vùng sửa. Những yêu cầu riêng cho Detect không áp dụng cho editor. Toàn văn chỉnh được lưu trong các tệp sản phẩm; bảng quyết định phía trên ghi nội dung thay đổi. Không dùng điểm phát hiện AI hoặc suy đoán tác giả.

Quill được áp dụng cho dàn ý, ký hiệu và kết nối cục bộ, không tạo `quill.json`: quy mô minh họa nối tới lưu vector chủ đề và chi phí S02-10; mô tả hai nhánh không loại nút cụt ở đích; hình kiến trúc không dùng $x$ trước S03-04; nguồn TrustRank/G5/$L$ trỏ đúng bước định nghĩa; giá trị lớn nhất dùng thống nhất trong vết chạy, chuẩn hóa và trạng thái thuật toán. Giữ G4, G5, tham số, thứ tự cập nhật, giả thiết và các kết luận toán học. Rà độc lập mạch/toán sau sửa và kiểm render cuối vẫn do điều phối viên thực hiện.

### Tự kiểm editor và mốc bàn giao

| Kiểm đã chạy | Kết quả và giới hạn |
|---|---|
| `editor-audit-static.py` | PASS: 51 mã đúng thứ tự, 51 notes, bảy phần 6/12/8/7/11/4/3; 20 SVG có XML/role/title/desc hợp lệ, tập cạnh G4/G5 đúng; ảnh và tài sản cục bộ tồn tại; không style nội dòng/block hoặc fragment. Đây là kiểm cấu trúc. |
| `editor-audit-plan.py` | PASS: 48 trang giảng/120 phút, ba bài nguồn/60 phút; mã và thời lượng không đổi. |
| KaTeX cục bộ trên các Markdown bị sửa | PASS cú pháp: ghi chú 518 biểu thức; outline 309, storyboard 694, review-log 73 tại lượt trước bảng tự kiểm này. Có cảnh báo thông số phông cho một số ký tự tiếng Việt trong lệnh text; không có lỗi phân tích. Kiểm này không thay xem công thức render. |
| `editor-preservation.py` | PASS so với snapshot ngay trước sửa: 664 biểu thức HTML và 518 biểu thức ghi chú giữ nguyên; các khối giả mã HTML giống byte. Giả mã ghi chú chỉ đổi câu trạng thái không cạnh; toán tử và bước tính giữ nguyên. |
| Sinh lại SVG | PASS tính lặp lại: chạy generator lần nữa giữ nguyên hash của cả 20 SVG. So với snapshot, chỉ hai SVG đã duyệt đổi chữ; mọi thuộc tính hình học, nút XML và cạnh giữ nguyên. |
| Diff CSS so với snapshot | PASS: đúng một thuộc tính position, hai selector in và chú thích đã duyệt; không đổi thang chữ hoặc quy tắc màn hình của ảnh. |
| `git diff --check` trên whitelist | Mã thoát 0, không có lỗi khoảng trắng. |

Bằng chứng tự kiểm nằm trong `/tmp/lec04-implementation/editor-{static,plan,note-math,planning-math,preservation}.json`; snapshot riêng ở `editor-baseline/` dùng để phân biệt lượt editor với các thay đổi triển khai đã có. Chín tệp thay đổi trong lượt editor thuộc whitelist: HTML, ghi chú, CSS viewer, generator, hai SVG và ba tệp planning. Câu biên S05-07 đã được chốt rõ đối tượng: “Với đồ thị không cạnh, vector thô bằng 0 nên phép chuẩn hóa không xác định.”

Editor đã bàn giao bản nội dung công khai đóng băng cho điều phối viên; không commit/push. Trạng thái này chỉ xác nhận các sửa được duyệt và tự kiểm nêu trên. Render cuối, 14 ghi chú viewer trước/sau, bàn phím, PDF, rà độc lập toán/mạch sau sửa, kiểm trạng thái Codex Slides và công bố chưa được editor chứng nhận; điều phối viên ghi kết quả tiếp theo vào nhật ký.

## Kiểm định cuối của điều phối viên, 28/09/2026

Bản HTML chốt có SHA-256 `9b0070e616f10406a7e7bea78764b9c0f10988ddb4563648bb3ba9d54e2974c4`. Điều phối viên đã đối chiếu diff sau editor; chỉ các câu chữ, nguồn, mô tả hình và hai sửa CSS được duyệt thay đổi. Không có sửa ngoài phạm vi, không thay công thức, dữ kiện, cạnh, thuật toán hoặc thời lượng.

### Rà lại độc lập sau editor

- `/root/lec04_source_fresh` đã đối chiếu toàn bộ diff công khai, nguồn sách và câu cuối S05-07: M01/M02 đóng; quy mô minh họa đúng MMDS; 664 biểu thức HTML, 518 biểu thức ghi chú và bốn khối giả mã HTML giữ nguyên. Không phát hiện lỗi toán học hoặc nguồn mới. Báo cáo `recheck-math.md`.
- `/root/lec04_flow_review` đọc lại nội dung cả 51 slide, các notes/cụm ghi chú chịu ảnh hưởng, mở bài và kết luận: FL-01/FL-02/E2 đóng. Quy mô lưu trữ nối tới chi phí số vector chủ đề; hình kiến trúc không dùng ký hiệu sớm; kết luận thu hồi đủ ba yêu cầu. Báo cáo `recheck-flow.md`. Không có lỗi mạch còn phải sửa.

### Kết quả kỹ thuật và hiển thị

| Hạng mục | Bằng chứng và kết quả cuối |
|---|---|
| Cấu trúc và nguồn | Trình phân tích HTML/XML độc lập bằng thư viện chuẩn xác nhận 51 mã duy nhất đúng thứ tự storyboard, 51 notes, bảy phần 6/12/8/7/11/4/3, 20 SVG hợp lệ, tài sản và liên kết tồn tại; không ảnh raster, style riêng hoặc fragment. Các dẫn nguồn được sửa đồng bộ với sách. |
| RevealJS | Chụp đủ 51 slide ở 1280×720 và 51 slide ở 390×844; mỗi ảnh đợi đúng `data-slide-id`. Không phát hiện tràn biên, cuộn ngang nội dung, chạm chân trang, công thức lỗi, ảnh hỏng, lỗi JavaScript hoặc HTTP. Chặn mạng ngoài trong lúc kiểm; không có yêu cầu mạng ngoài cho tài sản cốt lõi. |
| Xem trực quan | Reviewer sinh viên đã xem đủ 51 ảnh rộng; điều phối viên xem toàn bộ bản đầu qua bảng ảnh và xem riêng các trang mật độ cao. Sau editor đã xem lại các vùng đổi chữ/hình, gồm S01-04, S03-02, S05-05/07/08. S07-02 có nhãn SVG tối thiểu tương đương 16,36px; nguồn ngắn tương đương 17,28px được reviewer xác nhận đọc được ở khung rộng. |
| Bàn phím deck | Khung rộng: ArrowDown chuyển sang trang dọc thứ hai, ArrowRight chuyển sang phần kế. Chế độ cuộn ở màn hình hẹp: PageDown chuyển từ S01-01 sang S01-02. Chiều rộng tài liệu bằng viewport ở cả hai chế độ. |
| SVG và số học | Cả 20 SVG đã render, có role/title/desc và không có chữ vượt viewBox. Các biến thể G4/G5 có đúng tập cạnh. Các kiểm phân số độc lập của reviewer khớp các vết lặp, nghiệm, hệ cụm thao túng và biên chuỗi. Generator tái tạo đúng 20 hình, không cần mạng. |
| Viewer Bài 04 | Ở 1440×900 và 390×844: 518 công thức không lỗi, 10 hình tải đúng/có alt, 30 đích mục lục hợp lệ, 12 khối gập đóng mặc định và mở/đóng được bằng Enter. Cả 33 vùng cuộn được tiếp cận bằng Tab và cuộn bằng ArrowRight. Không còn cuộn ngang toàn trang. Đường dẫn vượt thư mục và cặp doc/deck khác số bài bị từ chối. |
| Bản in | Mở đủ 12 khối gợi ý/lời giải khi in và phục hồi trạng thái gập sau in. PDF kiểm thử cuối dùng đúng media print, gồm 28 trang A4. Đã xem các trang 4, 9, 15, 24, 25, 27: G4, cụm thao túng, vai trò học phần, hai biến thể hỗ trợ và chuỗi giữ đầy đủ cạnh, khuyên và nhãn. PDF/PNG là bằng chứng tạm, không đưa vào Git. |
| Hồi quy CSS deck | Bài 02 và 03 được kiểm đủ 81/63 slide ở rộng và hẹp. Cỡ chữ, khung nội dung và ảnh không đổi sau selector riêng của Bài 04. Những PNG khác byte chỉ khác tại nút điều hướng và thanh tiến độ do hiệu ứng; không có sai khác ngoài các vùng đó. Không tuyên bố mọi PNG giống byte. |
| Hồi quy CSS viewer | Kiểm trước/sau đủ 14 ghi chú công khai trong index: không phát sinh lỗi công thức hoặc ảnh; tất cả hình co vừa vùng in. Chiều rộng mobile của Bài 04 giảm 396→375px; Bài 09 cũng giảm 489→375px sau cùng sửa bảng, không cần sửa nội dung Bài 09. Các ghi chú còn lại không tăng chiều rộng. |
| Index và phạm vi | Thẻ Bài 4 dẫn đúng deck và viewer; bỏ liên kết thực hành cũ khỏi thẻ và ghi chú. Tệp bài tập/mã thực hành cũ không thuộc lượt kiểm định này và không bị sửa. Không công bố liên kết planning. |

Bộ ảnh narrow đầu tiên bị loại vì RevealJS tự chuyển sang chế độ cuộn, làm ảnh đứng tên trang đích nhưng hiển thị trang trước. Bộ kiểm cuối dùng `scrollIntoView` và đợi đúng mã trước khi chụp. Kiểm PDF ban đầu còn giữ media screen từ lượt đo trước; đã sửa bộ kiểm để xuất đúng media print và xem PDF thật. Lần thử phục hồi khối gập cũng đã loại tác động của việc phát `beforeprint` hai lần. Các lỗi bộ kiểm này không được dùng làm bằng chứng đạt.

Bằng chứng tạm: `/tmp/lec04-implementation/final-renders/report.json`, `final-static.json`, `svg/report.json`, `final-materials/report.json`, `viewer-before/viewer-regression.json`, `viewer-after/viewer-regression.json`, `regression-pixel-analysis.json`. Các kết quả cần lưu lâu dài đã được mô tả trong bảng; các tệp tạm không thuộc sản phẩm Git.

### Đối chiếu tiêu chuẩn và giới hạn

Sáu nhóm tiêu chuẩn đã được đối chiếu với năm báo cáo và bản render: đối tượng năm 2/tiên quyết Bài 03; một luận điểm và kết nối học tập trên từng trang; đặc tả/giả mã/lập luận/biên; ví dụ có trạng thái trung gian; chi phí theo cùng mô hình; SVG mang đúng dữ liệu, chiều cạnh và nhãn. Phần giảng 120 phút và ba bài nguồn 60 phút giữ nguyên. Không còn lỗi chặn bàn giao, nghiêm trọng hoặc trung bình được phát hiện mà chưa xử lý.

Thời lượng là thiết kế, chưa có giảng thử hoặc đo máy chiếu trong lớp. Ở điện thoại, deck giữ nguyên khung nên cần phóng to để đọc bảng/mã; ghi chú web thích nghi theo chiều rộng và có vùng cuộn dùng được bằng bàn phím. Không khẳng định deck điện thoại đọc thuận tiện khi chưa phóng to.

### Codex Slides và tuyến công cụ

Giữ dự án `20260924100856-lecture-04-pagerank-theo-ch-li-n-k-t-r-c-3vgu`. Nhập thủ công 51 PNG render từ RevealJS và 51 notes trích từ HTML nguồn bằng công cụ deterministic. Đọc lại trạng thái dự án xác nhận đủ 51 trang có ảnh, tiêu đề và notes khớp; kiểm hash của 51 ảnh qua endpoint lưu trữ đều trùng PNG cuối. Chromium cục bộ mở canvas và bảng ghi chú, xác nhận nội dung hiển thị; không có lỗi JavaScript trong lượt đối chiếu.

Sau nhập, plugin vẫn giữ workflow outline nên giao diện không hiện ảnh dù 51 trang đã có trạng thái rendered. Đã đọc route PATCH và mã giao diện của plugin, chỉ cập nhật tiêu đề cùng workflow sang deck qua API cục bộ lưu metadata; không khởi chạy generate/render/chat hoặc lời gọi mô hình. Trường status cấp dự án vẫn là draft của luồng cũ; không gán nó thành kết quả một run sinh ảnh. Các nguồn HTML/Markdown và hồ sơ cuối được đưa vào Design Files để đối chiếu.

Phiên này không có công cụ Browser nhúng của Codex. Việc xác minh trực quan trong **in-editor Browser** còn chưa thực hiện; Chromium cục bộ và trạng thái/hash là bằng chứng thay thế, theo ngoại lệ công cụ của AGENTS. Liên kết đúng bề mặt ghi chú: `http://127.0.0.1:4311/project/20260924100856-lecture-04-pagerank-theo-ch-li-n-k-t-r-c-3vgu?slide=51&panel=speaker-notes`. Đã dùng hướng dẫn `codex-slides`, `codex-slides-verification` và `codex-slides-known-errors`; không tuyên bố đã kiểm bằng Browser nhúng.

Toàn bộ tác tử của lượt triển khai dùng cơ chế native với model được chỉ định GPT-6-Astra/xhigh; không gọi OpenRouter, script/API/CLI mô hình và không đọc `.env*`. Bằng chứng mô hình là tham số tạo tác tử; không suy đoán tuyến xác thực. Máy chủ cục bộ của kho chạy `python3 -m reloadserver 8765 --bind ::1`; cổng IPv4 hiện phục vụ kho khác nên được giữ nguyên. URL deck: `http://[::1]:8765/2627-1/lecture-04-pagerank-theo-chu-de-lien-ket-rac-va-hits.html`.

### Phạm vi công bố

Chỉ stage HTML Bài 04, ghi chú, SVG/generator, ba tệp planning, thẻ index và hai CSS đã kiểm. Các thay đổi sẵn có tại AGENTS, tiêu chuẩn, cấu hình và công cụ khác nằm ngoài commit này. Trước công bố đã fetch `origin/main`, xác nhận không lệch lịch sử; không dùng force hoặc viết lại lịch sử. Mã commit và xác nhận push được cung cấp trong bàn giao cuối sau khi Git xác nhận thành công.

## Lượt làm rõ nội dung ngày 29/09/2026 — bàn giao của tác tử soạn

Phạm vi được điều phối viên duyệt: sửa cục bộ cách giải thích trong deck và ba tệp quy trình; giữ dữ kiện, công thức, bảy phần và thời lượng 120 phút giảng + 60 phút bài tập. Đã đọc tiêu chuẩn biên soạn, bản đồ nguồn Bài 04, hồ sơ hiện có và các kỹ năng `no-ai-slop` (Edit và `eval.md`), `quill`, `build-slide-deck-outline`. Phân tích nguồn độc lập và kế hoạch tách trang đã được điều phối viên hợp nhất trước khi soạn. Không tạo dự án Quill.

| Vị trí | Vấn đề và bằng chứng | Quyết định đã thực hiện |
|---|---|---|
| S02-02 | Dòng $v=r^0$ ghép hai vai trò khác nhau | Tách phân phối đích của nhánh dịch chuyển và lựa chọn khởi tạo; nêu $v$ cố định, $r^t$ thay đổi |
| S02-09, S02-09a | Các vector mang chỉ số chủ đề chưa được giải nghĩa trước công thức tổng | Tách trang định nghĩa $j,v^{(j)},r^{(j)},w_j$ khỏi phép chứng minh; giữ cùng $\bar M,\beta$. Bổ sung nguồn MMDS §5.3.4, tr.199 |
| S02-10–11 | Chi phí ghép chưa gắn rõ với thao tác trên ứng viên | Định nghĩa $C,c$; tiền tính và lưu $r^{(j)}$, xác định trọng số tại truy vấn, ghép từng $r_i^*$ từ điểm đã lưu. Tách chi phí ghép khỏi tìm ứng viên, chọn trọng số và sắp xếp |
| S03-04–06 | Hệ số $\beta^2$ và hệ số khuếch đại cần truy nguyên theo luồng điểm | Diễn đạt $x$ đã gồm $\beta$; chỉ rõ hai bước đích → hỗ trợ → đích tạo $\beta^2y$. Phân biệt hệ số $400/111$ của riêng $x$, hạng $(17/37)(m/n)$ và hạng bỏ $1/[n(1+\beta)]$. Chuyển phần tăng 260,36% vào ghi chú |
| S04-01–03, S04-02a | Nguồn của $T$ và các ký hiệu trong phép lặp chưa đủ rõ trên mặt trang | Nêu đánh giá hạt giống ngoài phép lặp, giả định hướng liên kết và độ phủ. Tách bảng ký hiệu khỏi công thức có nhãn ba số hạng. B,D là giả thiết hạt giống đầu vào |
| S04-04–06 | Dấu hiệu và chỉ số tương đối có thể bị diễn giải thành nhãn rác | Thêm bảng dấu theo chiều PageRank → TrustRank; giải thích A,C cùng giảm 20% so với nền riêng. Nêu ưu tiên rà soát phụ thuộc $T$, không tự gán nhãn |
| S05-01–02 | Thuật ngữ hub/authority cần nối với ví dụ danh mục/nội dung | Mỗi trang có hai điểm; nêu vai trò trung tâm/uy tín và quan hệ hỗ trợ lẫn nhau. Phân biệt uy tín theo liên kết HITS với độ tin cậy TrustRank |

Bản HTML hiện có 53 trang, gồm 50 trang giảng và 3 trang bài tập; phân bố 6/13/8/8/11/4/3. Hai mã mới `lec04-s02-09a` và `lec04-s04-02a` giữ các mã trang cũ ổn định. Trong S02, bốn trang S02-03/04/07/08 giảm từ 3 xuống 2,5 phút, S02-09 còn 1 phút, trang mới 2 phút và S02-11 tăng lên 2 phút; tổng vẫn 30 phút. S04-02 còn 2 phút, trang mới 2 phút, S04-03 còn 1 phút; tổng vẫn 18 phút. Không lấy thời gian từ bài tập.

Đã cập nhật trực tiếp hai khối `public-slide` và `public-notes`, tiêu đề và metadata của các phiếu bị tác động; không chỉ thêm phần đính chính. Thuật ngữ và bảng tổng trong outline đã đồng bộ. Hai sơ đồ tổng vector và tiền tính/truy vấn không còn được dùng trên slide sau khi thay bằng bảng/thẻ có ký hiệu tường minh; giữ nguyên các SVG hiện có và mã tái tạo. Không thay CSS chung, index, mã thực hành hoặc tài sản dùng chung.

### Tự kiểm văn phong và mạch suy luận

- `no-ai-slop`, Edit: giữ thuật ngữ học thuật, giả thiết, ký hiệu và kết quả; sửa tối thiểu trong 17 trang. Câu “Không nhân thêm $\beta$ vào $x$” trên mặt S03-04 đã thành “Đóng góp $x$ đã bao gồm hệ số $\beta$”. Tự kiểm theo các nhóm nguyên tắc biên tập, từ rỗng, kiểu diễn đạt và đọc cuối trong `eval.md`: đạt trong phạm vi bản sửa. Không dùng điểm bộ phát hiện AI, suy đoán tác giả hoặc văn phong hội thoại.
- Quill: kiểm đầu vào trước ký hiệu, đầu ra trước chỗ tái sử dụng và các câu nối: $v\to r$; chủ đề riêng → tổng → truy vấn; $T\to\rho\to r-\rho\to s$; danh mục/nội dung → $h,a$ → phép cập nhật. Hai trang mới chỉ tách tải kiến thức, không mở rộng chủ đề.
- Đối chiếu ghi chú tự học §§1.1, 2.2, 2.5, 3.2–3.3, 4.1–4.3, 5.1: giữ cùng giả thiết, dữ kiện và công thức. Không có thay đổi học thuật cần sửa `lecture-note.md`; tệp này được giữ nguyên.

### Kiểm tra đã chạy và giới hạn bàn giao

Tác tử soạn đã chạy ba script do điều phối viên chuẩn bị trong `/tmp/lec04-clarify/`: `audit_plan.py`, `audit_static.py`, `check_math.py`. Kết quả: 53 mã duy nhất, 53 ghi chú diễn giả; thứ tự và tiêu đề khớp storyboard; 7 phần; tổng từng phần 12/30/20/18/30/10/60 phút. Các kiểm tra dữ liệu SVG, đường dẫn tài sản cục bộ và cấu trúc không báo lỗi. Kiểm tra toán xác nhận các vết G4, nghiệm PageRank/TrustRank, Spam Mass, hai vòng HITS, bài tập, công thức cụm thao túng, tính tuyến tính theo chủ đề và các hệ số khuếch đại.

Đây là bằng chứng kiểm tra tĩnh và phép tính. Tác tử soạn chưa xác nhận bản render, tràn khung, hình công thức hay khả năng đọc của lượt sửa này. Bản HTML đã bàn giao điều phối viên để kiểm trực quan và rà độc lập; các kết quả đó được ghi riêng sau khi thực hiện. Không commit hoặc push trong phần việc của tác tử soạn.

Trong quá trình đồng bộ, tác tử soạn đã mã hóa dấu nhỏ hơn thành `&lt;` ở các công thức HTML mới thuộc S04-02, S04-02a và S04-04, rồi tạo lại các khối Markdown tương ứng để giữ đủ điều kiện và dấu. Điều phối viên tiếp nhận các điểm cần rà tiếp: mật độ hai bảng S04-04; mức tường minh của từng phần tử $M_0$ trên mặt S04-02; cách gọi phần điểm nút cụt trước/sau nhân $\beta$ trong ghi chú; phân biệt rõ chi phí tiền tính với dung lượng lưu ở S02-10. Các điểm này chưa được tác tử soạn tự xác nhận qua render và được chuyển sang lượt rà độc lập, chỉnh sửa kế tiếp.

## Năm lượt rà độc lập và chỉnh sửa cuối ngày 29/09/2026

Điều phối viên chỉ định năm tác tử rà độc lập, mỗi tác tử dùng model `gpt-6-astra`. Bảng dưới ghi vai trò và báo cáo thực nhận; tên model là chỉ định của điều phối viên, không phải suy đoán tuyến thực thi. Editor riêng bắt đầu sau khi tác tử soạn và năm tác tử rà hoàn tất. Editor chỉ sửa HTML Bài 04 và ba tệp quy trình; không sửa CSS, SVG, ghi chú tự học, index hoặc mã thực hành.

| Tác tử theo vai trò được giao | Model được chỉ định | Báo cáo và phạm vi | Phát hiện và quyết định |
|---|---|---|---|
| Rà toán học và thuật toán | `gpt-6-astra` | `review-math.md`: nội dung, notes, nguồn và phép tính các cụm sửa cùng trang lân cận; không kiểm render | Giữ mã hóa dấu nhỏ hơn; đưa quy tắc phần tử M0 lên mặt S04-02; sửa lượng bù thành beta nhân tổng điểm nút cụt. Không đổi nghiệm hoặc giả thiết |
| Rà kết nối và mạch viết | `gpt-6-astra` | `review-flow.md`: toàn tuyến 53 trang, notes liên quan, metadata và tác động ghi chú tự học; không kiểm render | S02-10 gọi đúng dung lượng lưu k kết quả; S04-02 gọi tên ma trận liên kết. Giữ thứ tự và thời lượng; không sửa ghi chú tự học |
| Rà học thuật và giảng dạy | `gpt-6-astra` | `review-pedagogy.md`: toàn văn HTML/notes, nhãn SVG, ba ảnh wide S03-05/S04-02/S04-04 | Thêm giới hạn điểm/thứ hạng/nhãn rác; thay bảng dấu bằng đoạn để xử lý nguồn sát chân trang; thay “chứng nhận tin cậy” bằng “điểm tin cậy” trong notes S05-01 |
| Rà từ góc nhìn sinh viên năm 2 | `gpt-6-astra` | `review-student.md`: các cụm sửa và lân cận, mở/kết/bài tập, 16 ảnh wide và hai ảnh narrow | Chấp nhận cùng hai sửa S04-04 và định nghĩa M0. Giữ khung trình chiếu hiện có; khả năng đọc sau sửa cần điều phối viên kiểm lại |
| Rà chuyên gia giải thuật và khoa học dữ liệu | `gpt-6-astra` | `review-expert.md`: S01–S06, nguồn MMDS/Stanford liên quan, số học phân số và thời lượng; không kiểm render | Xử lý định nghĩa M0, giới hạn dấu hiệu và cụm “chứng nhận”. Không phát hiện sai số hoặc thiếu điều kiện làm sai kết quả trong phạm vi đã kiểm |

Các báo cáo đầy đủ được bàn giao trong `/tmp/lec04-clarify/`; bảng này lưu nội dung quyết định bền vững trong kho. Không dùng kết quả ngày 28/09 thay cho năm báo cáo hiện tại.

### Quyết định biên tập và đồng bộ

- S02-10: “Lưu k kết quả” chỉ dung lượng số cần lưu; chi phí tiền tính và mô hình phép toán giữ trong notes.
- S04-02: gọi tên ma trận liên kết theo cột nguồn, nêu giá trị phần tử theo cạnh khi bậc ra dương và bằng 0 trong các trường hợp khác, gồm cột nút cụt. Ghi chú phân biệt tổng điểm nút cụt với lượng điểm bù sau nhân beta. S04-02a ghi phân phối hạt giống bằng nghịch đảo kích thước tập trong T, bằng 0 ngoài T.
- S04-04: giữ nguyên bảng bốn trang và toàn bộ phân số. Thay bảng dấu bằng đoạn diễn giải ba trường hợp; bổ sung giới hạn về thay đổi thứ hạng và nhãn rác ở cả mặt trang và notes. Đây là sửa bố cục nhằm giải quyết phát hiện nguồn chạm chân trang; chưa khẳng định đã đạt qua ảnh sau sửa.
- S04-06: nêu rõ chỉ số lớn được dùng để ưu tiên rà soát, phụ thuộc T và không tự xác định nhãn rác; không thêm ngưỡng hoặc bộ phân loại.
- S05-01: thay hàm ý chứng nhận nội dung bằng điểm tin cậy, giữ phân biệt hai vai trò HITS.
- Mã hóa dấu nhỏ hơn của writer được giữ; Markdown dùng dấu toán thông thường. Các khối public-slide/public-notes của sáu phiếu bị sửa được sinh lại từ HTML; metadata bố cục/luận điểm/giới hạn và bảng thuật ngữ được cập nhật tại chỗ.

### Tự kiểm của editor

Áp dụng `no-ai-slop` ở chế độ Edit sau khi đọc SKILL.md và eval.md: sửa tối thiểu, giữ giả thiết, dữ kiện, ký hiệu và nguồn; loại cụm có hàm ý chứng nhận không phù hợp; dùng câu học thuật trực tiếp, không thêm chỉ dẫn giảng viên. Các nhóm nguyên tắc, từ rỗng, mẫu diễn đạt và đọc cuối của eval đạt trong phạm vi sửa. Bản chỉnh đầy đủ nằm trong HTML và storyboard; danh mục thay đổi nằm ngay trên. Không dùng điểm phát hiện AI hoặc suy đoán tác giả.

Áp dụng Quill để rà tính liên tục, không tạo quill.json: ký hiệu ma trận → ba hạng cập nhật → đối chiếu điểm → chuẩn hóa theo nền → ưu tiên rà soát; điểm tin cậy không trở thành chứng nhận khi chuyển sang HITS. Không đổi thứ tự khái niệm, nguồn, tổng thời lượng hoặc kết quả dùng chung với tài liệu tự học.

### Bằng chứng kiểm tra sau chỉnh của editor

Ba script `audit_static.py`, `audit_plan.py`, `check_math.py` đều PASS sau sửa: 53 mã/53 notes, bảy phần 6/13/8/8/11/4/3, thời lượng 12/30/20/18/30/10/60 phút; phép tính G4, Spam Mass, HITS, bài tập, cụm thao túng, bù nút cụt và ghép chủ đề giữ đúng. Trình phân tích raw HTML không nhận thẻ lạ; KaTeX cục bộ phân tích 819 biểu thức lấy từ văn bản HTML, gồm notes, không có lỗi cú pháp. KaTeX có cảnh báo thiếu thông số ký tự tiếng Việt trong nhãn văn bản; đây không phải bằng chứng về hình hiển thị, cần xem ảnh ở lượt render của điều phối viên.

Các ID thay đổi ở lượt editor: `lec04-s02-10`, `lec04-s04-02`, `lec04-s04-02a`, `lec04-s04-04`, `lec04-s04-06`, `lec04-s05-01`. Chưa chạy render sau sửa, chưa commit/push; bàn giao điều phối viên kiểm hình và rà lại toán/mạch trước công bố.

Rà lại mạch trong `recheck-flow.md` xác nhận nội dung và kết nối đạt; còn ba câu metadata S05-01 mô tả phiên trước. Editor đã đồng bộ Bố cục, Trọng tâm và Ví dụ theo HTML hiện hành: hai điểm được định nghĩa ngay tại S05-01, phân biệt uy tín HITS với độ tin cậy TrustRank; S05-02 diễn giải quan hệ cập nhật. Chỉ sửa metadata, không đổi HTML, thời lượng hoặc nội dung công khai.

## Kiểm định bản làm rõ trước công bố ngày 29/09/2026

### Tác tử và kết luận tái kiểm

Các tác tử được tạo bằng cơ chế gốc với model chỉ định `gpt-6-astra`: `/root/plan_lec04` lập kế hoạch rồi rà mạch; `/root/source_lec04` phân tích nguồn rồi rà toán; `/root/write_lec04` soạn; `/root/review_pedagogy` rà học thuật và giảng dạy; `/root/review_student` rà từ góc nhìn sinh viên; `/root/review_expert` rà chuyên gia; `/root/edit_lec04` chỉnh sửa riêng. Điều phối viên hợp nhất kế hoạch và phân tích trước khi giao soạn, chờ đủ năm báo cáo trước khi giao editor, rồi tự kiểm bản cuối. Không có hai tác tử ghi kho đồng thời; không dùng API/CLI mô hình hoặc đọc tệp môi trường chứa thông tin xác thực.

Tái kiểm toán trong `recheck-math.md` đạt: định nghĩa ma trận, hai phân phối, lượng bù, chi phí và diễn giải điểm đều nhất quán; không còn thẻ HTML lạ do dấu nhỏ hơn. Tái kiểm mạch trong `recheck-flow.md` đạt sau khi đồng bộ ba câu metadata S05-01. Không còn phát hiện cần sửa trong phạm vi hai lượt tái kiểm. Các kết luận này độc lập với kiểm hiển thị bên dưới.

### Kiểm cấu trúc, hiển thị và phạm vi

| Hạng mục | Bằng chứng bản cuối |
|---|---|
| Cấu trúc và thời lượng | 53 trang, 53 notes, bảy phần 6/13/8/8/11/4/3; 50 trang giảng trong 120 phút và ba bài nguồn trong 60 phút. Giữ 51 mã cũ; thêm S02-09a và S04-02a. Các phiếu và khối nội dung công khai khớp HTML. |
| Phép tính và công thức | Kiểm phân số độc lập giữ đúng G4, TrustRank, Spam Mass, HITS, bài tập, công thức khuếch đại và ghép chủ đề, gồm trường hợp có nút cụt. KaTeX phân tích 819 biểu thức gồm notes, không lỗi cú pháp; ảnh cuối xác nhận nhãn tiếng Việt trong công thức đọc được. |
| RevealJS | Chụp đủ 53 trang ở 1280 × 720 và 53 trang ở 390 × 844, đợi đúng mã trang. Không phát hiện tràn biên, cuộn ngang nội dung, chồng chân trang, lỗi KaTeX, ảnh hỏng, JavaScript, HTTP hoặc yêu cầu mạng ngoài cho tài sản cốt lõi. |
| Xem trực quan | Điều phối viên đã xem 16 trang rộng và hai trang hẹp của bản nháp; sau editor xem lại các trang có thay đổi hiển thị S02-10, S04-02/02a/04/06 và ảnh hẹp S04-04. Bảng ký hiệu, công thức ba thành phần và bảng so sánh đều rõ ở khung rộng; nguồn S04-04 đã tách khỏi chân trang. |
| Bàn phím | ArrowDown chuyển trang dọc, ArrowRight chuyển phần; PageDown ở chế độ cuộn chuyển đúng sang S01-02. Chiều rộng tài liệu bằng viewport ở cả hai kích thước. |
| Bảo toàn phạm vi | Ba trang recitation và cấu hình script giống từng byte với bản trước. CSS, SVG, index và lecture-note không đổi. Chỉ HTML Bài 04 và ba tệp planning thuộc lượt sửa. `git diff --check` đạt. |

Bằng chứng tạm của lượt này nằm trong `/tmp/lec04-clarify/`: `final-renders/report.json`, `preservation.json`, các báo cáo rà và phép kiểm tĩnh/toán. Bảng trên lưu kết quả cần thiết trong kho; ảnh và script kiểm thử không đưa vào Git. Giới hạn điện thoại giữ nguyên: deck co theo khung 16:9 nên cần phóng to để đọc bảng và công thức; không khẳng định khả năng đọc thuận tiện ở kích thước thu nhỏ.

Các sửa chỉ làm rõ tám nhóm yêu cầu đã ánh xạ trong bảng quyết định, dựa trên MMDS Chương 5 và nguồn slide đã kiểm. Hai trang bổ sung tách định nghĩa khỏi lập luận hoặc cập nhật, không mở rộng chủ đề. Không vẽ thêm hình và không thay dữ kiện. Đã đối chiếu ghi chú tự học; không có thay đổi giả thiết, ký hiệu chung hoặc kết quả cần sửa tệp đó.

### Đối chiếu Codex Slides và công bố

Dự án `20260924100856-lecture-04-pagerank-theo-ch-li-n-k-t-r-c-3vgu` đã nhận đủ 53 PNG của bản RevealJS cuối và 53 ghi chú. Đọc lại trạng thái xác nhận 53 trang rendered, 53 tiêu đề và ghi chú khớp nguồn. Chromium cục bộ mở từng trang, so hash ảnh tải từ canvas với PNG nguồn: 53/53 khớp; nội dung ghi chú: 53/53 khớp; không lỗi JavaScript. Điều phối viên xem ảnh giao diện của S04-02a, S04-04 và bảng ghi chú trang cuối. Trường trạng thái cấp dự án vẫn là draft của luồng cũ; lượt này chỉ cập nhật dữ liệu xác định, không chạy sinh nội dung hoặc ảnh bằng mô hình.

Phiên không có Browser nhúng của Codex; không tuyên bố đã kiểm trong in-editor Browser. Chromium cục bộ, trạng thái đọc lại và hash là bằng chứng thay thế. Các Design Files hiện hành là HTML cùng `uploaded/outline.md`, `uploaded/storyboard-2.md`, `uploaded/review-log.md`; bản storyboard cũ giữ vai trò lịch sử. Bằng chứng giao diện và đối chiếu nằm tại `/tmp/lec04-clarify/codex-final/report.json`. URL bản xem trước: `http://127.0.0.1:4311/project/20260924100856-lecture-04-pagerank-theo-ch-li-n-k-t-r-c-3vgu?slide=30`.

Phạm vi commit của lượt này chỉ gồm HTML Bài 04 và ba tệp planning. Đã fetch `origin/main` và xác nhận hai phía không có commit lệch trước công bố. Các thay đổi sẵn có của người dùng tại cấu hình, tiêu chuẩn và công cụ giữ ngoài commit. Điều phối viên cung cấp mã commit cùng xác nhận remote trong bàn giao sau khi Git hoàn tất; không dùng force hoặc viết lại lịch sử.

## Duyệt từng trang theo yêu cầu người dùng ngày 01/10/2026

Yêu cầu: duyệt lần lượt từng trang, xác định trang muốn nói gì, đề xuất rồi sửa để tiêu đề ngắn gọn và học thuật, mạch lập luận chặt, khái niệm không xuất hiện đột ngột; commit và push sau mỗi trang.

**Tác tử.** Điều phối viên là phiên Claude Code (Claude Opus 5.5, `claude-opus-5-5`). Hai tác tử chỉ đọc tạo bằng công cụ `Agent`, loại `fork` (kế thừa mô hình điều phối viên): (1) góc nhìn sinh viên năm 2 và phản biện học thuật, giảng dạy, no-ai-slop chế độ Detect; (2) kết nối, mạch viết và độ chính xác toán học. Một tác tử chỉnh sửa loại `fork` sửa tuần tự từng trang; không có hai tác tử ghi đồng thời. Báo cáo tạm nằm ngoài kho trong thư mục scratchpad của phiên.

**Kết quả chung của hai báo cáo.** Tính lại toàn bộ phân số: không có lỗi số học. Các vấn đề xuyên suốt được duyệt: (G1) Bài 03 gọi teleport là “bước nhảy ngẫu nhiên”, Bài 04 dùng “dịch chuyển” không có cầu nối; (G2) Bài 03 dùng $S$ cho ma trận đã bù nút cụt, Bài 04 dùng $\bar M$ và để $S$ cho tập chủ đề; (G3) “điểm cố định”, “tính co” chưa được nối với “phân phối không đổi” của Bài 03; (G4) tên G4 chỉ có trong văn bản thay thế; (G5) chuẩn hóa HITS dùng trước khi định nghĩa; (G6) tập ứng viên $C$ dùng trước khi định nghĩa; (G7) Spam Mass thiếu ý tưởng trước công thức; (G8) cầu nối S03→S04 lệch lập luận MMDS §5.4.3; (G9) liên kết rác và HITS thiếu động cơ ở S01, S05 thiếu câu vào; (G10) một số trang lặp nội dung đã học; (G11) dấu thập phân không thống nhất.

**Quyết định thuật ngữ.** Giữ “dịch chuyển” trong Bài 04 vì thuật ngữ này đã dùng trong ghi chú tự học và các trang sau; nêu cầu nối tại lần đầu: bước nhảy ngẫu nhiên của Bài 03, trong bài này gọi là dịch chuyển (teleport). Giữ $\bar M$ và nêu tương ứng với ma trận $S$ của Bài 03. Nối “điểm cố định” với “phân phối không đổi” của Bài 03 tại lần đầu dùng.

| Trang | Trang muốn nói | Quyết định | Thay đổi |
|---|---|---|---|
| lec04-s01-01 | Tên bài, học phần, học kỳ; ghi chú nêu ba yêu cầu và PageRank Bài 03 là đầu vào. | giữ | Không đổi; hai báo cáo không nêu vấn đề. |
| lec04-s01-02 | Bài gồm bảy phần; người học tính bốn loại điểm, giải thích cụm liên kết rác và chọn phương pháp. | sửa | Giữ tiêu đề và mục lục. Dòng mục tiêu nêu cụ thể đối tượng tính (PageRank theo chủ đề, TrustRank, Spam Mass, HITS), cơ chế cần giải thích và tiêu chí chọn. Ghi chú viết lại thành mạch bốn phương pháp, nối với bước nhảy ngẫu nhiên của Bài 03, không lặp mặt trang. |
| lec04-s01-03 | Cùng truy vấn “jaguar” cần thứ tự trang khác nhau theo chủ đề; PageRank toàn cục chỉ cho một thứ tự, nên cần điểm phụ thuộc chủ đề. | sửa | Tiêu đề “Truy vấn đa nghĩa và ngữ cảnh chủ đề” → “Truy vấn đa nghĩa”. Giữ hai thẻ Động vật/Ô tô; rút gọn dòng dữ liệu–đầu ra; câu giới hạn của PageRank toàn cục thành khối kết luận nêu nhu cầu. Ghi chú viết lại theo MMDS §5.3.1, coi chủ đề là đầu vào, nối sang phương án một vector cho mỗi người dùng. |
| lec04-s01-04 | Mỗi người dùng một vector PageRank toàn web không lưu được ở quy mô web; $k$ vector chủ đề và $k$ trọng số mỗi người dùng thay thế, đổi lại mất một phần độ chính xác. | sửa | Tiêu đề “Giới hạn lưu trữ của xếp hạng cá nhân” → “Chi phí lưu PageRank riêng”. Thêm dòng nêu phương án trực tiếp trước hình để khái niệm không xuất hiện đột ngột; khối kết luận nêu quy mô MMDS, phương án $k$ vector và cái giá về độ chính xác (MMDS §5.3.1). Ghi chú viết lại thành phép so sánh số vector dài, không lặp khối kết luận, nối sang ba nhu cầu. SVG `luu-vector-theo-chu-de.svg`: thêm nhãn chữ “Phương án trực tiếp” trên mũi tên hàng 1, “Phương án theo chủ đề” trên mũi tên hàng 2 và đường kẻ nét đứt ngăn hai phương án, để không dùng vị trí làm tín hiệu duy nhất; giữ nguyên hộp, nhãn và mũi tên cũ; cập nhật `<desc>` và văn bản thay thế trong HTML. |
| lec04-s01-05 | Bài xét ba yêu cầu; mỗi yêu cầu xuất phát từ một hạn chế của PageRank toàn cục và cho điểm một ý nghĩa khác. | sửa | Tiêu đề “Ba mục tiêu của xếp hạng liên kết” → “Ba yêu cầu xếp hạng liên kết”. Bảng đổi thành hai cột “Hạn chế của PageRank toàn cục” / “Yêu cầu đối với điểm”, thêm động cơ cho liên kết rác (MMDS §5.4.1) và hai vai trò (§5.5.1); bỏ cụm “tập trang tin cậy” chưa định nghĩa; thay câu kết tối nghĩa. Ghi chú ánh xạ ba hạn chế sang S02, S03–S04, S05, dùng thuật ngữ “cụm thao túng liên kết (spam farm)” như S03, và nêu HITS không dùng $M_0$. Nguồn ghi rõ §5.3.1, §5.4.1, §5.5.1. |
| lec04-s01-02 (bổ sung) | Như trên. | sửa | Thống nhất thuật ngữ “cụm thao túng liên kết” (như S03, S06 và ghi chú tự học) ở dòng mục tiêu và ghi chú; điều phối viên sửa sau phát hiện của editor tại s01-05. |
| lec04-s01-06 | Ôn tiên quyết Bài 03: phần điểm theo cạnh B→A bằng $\beta r_B/d_B=1/10$, bậc ra lấy tại nguồn, $(M_0)_{AB}=1/2$; đây là nhánh theo liên kết mà S02 giữ nguyên. | sửa | Tiêu đề “Kiểm tra chiều truyền điểm” → “Ôn tập phép truyền điểm” (trang kiểm tiên quyết, không kiểm đầu ra S01). Thêm nhãn “Đồ thị G4” dưới hình, lần đầu đặt tên đồ thị (G4). Ghi chú thêm cầu nối G1: hai nhánh của Bài 03, “bước nhảy ngẫu nhiên” được gọi là dịch chuyển (teleport) trong Bài 04. Từ trang này, tác tử chỉnh sửa bị người dùng dừng; điều phối viên tự sửa từng trang và giao tác tử chỉ đọc rà lại theo từng phần. |
| lec04-s02-01 | PageRank theo chủ đề chỉ đổi nơi đến của bước dịch chuyển: từ mọi trang sang tập chủ đề $S$; cạnh và nhánh theo liên kết giữ nguyên, nên trang ngoài $S$ vẫn có điểm. | sửa | Tiêu đề “Dịch chuyển ưu tiên theo chủ đề” → “Dịch chuyển vào tập chủ đề”. Dòng nhánh dịch chuyển thêm đối chiếu “Bài 03 chọn đều trong $n$ trang”; đổi bố cục 60/40 thành 55/45 để mỗi dòng không quá hai dòng (khắc phục G1: thay đổi so với kiến thức cũ chưa được nêu). Ghi chú đặt tên “tập dịch chuyển” trước khi s02-02 dùng; nêu giả định trực quan MMDS §5.3.2 (trang được trang chủ đề trỏ tới thường cùng chủ đề). |
| lec04-s02-02 | Với $S=\{B,D\}$, phân phối dịch chuyển $v=(0,1/2,0,1/2)^\mathsf T$; phép cập nhật trên G4 là $r^{t+1}=\beta M_0r^t+(1-\beta)v$, mỗi vòng B, D nhận thêm $1/10$. | sửa | Tiêu đề “Tập dịch chuyển trên đồ thị bốn trang” → “Phân phối dịch chuyển trên G4”. Thêm dòng quy tắc cập nhật (G4 không có nút cụt) vì s02-03 dùng hai số hạng $\beta(M_0r^0)_i$, $(1-\beta)v_i$ trước đó chưa được viết. Câu “$v$ cố định, $r^t$ thay đổi” chuyển vào ghi chú cùng đối chiếu với $(1-\beta)u$ của Bài 03. |
| lec04-s02-03 | Chạy tay vòng 1: mỗi trang nhận $1/5$ theo liên kết, chỉ B, D nhận thêm $1/10$; $r^1=(1/5,3/10,1/5,3/10)^\mathsf T$, tổng bằng 1. | sửa | Tiêu đề “Vòng lặp PageRank theo chủ đề thứ nhất” → “Vòng lặp thứ nhất trên G4” (bỏ trùng tên phần, tránh hiểu “chủ đề thứ nhất”). Thêm danh sách cạnh G4 trên dòng dữ kiện vì trang không có hình. Số liệu giữ nguyên. |
| lec04-s02-04 | Vòng 2 và điểm cố định cho thấy B, D được ưu tiên còn A, C ngoài $S$ vẫn có điểm dương; $r^*$ là phân phối không đổi qua phép cập nhật. | sửa | Tiêu đề “Vết lặp và điểm cố định theo chủ đề” → “Vòng thứ hai và điểm cố định”. Thêm dòng định nghĩa $r^*$ (nghiệm của $r=\beta M_0r+(1-\beta)v$, $\sum_ir_i=1$; phân phối không đổi của Bài 03) vì cột $r^*$ trước đó không nêu nguồn gốc (G3). Ghi chú nêu cách giải hệ và thế lại, nối với bài tập s07-01. Tính lại bằng phân số: $r^2$, $r^3$ và $r^*$ đúng. |
| lec04-s02-05 | Đặc tả tổng quát: ba thành phần theo liên kết, bù nút cụt, dịch chuyển theo $v$, cùng đầu vào, đầu ra và trạng thái dừng. | sửa | Tiêu đề “Đặc tả PageRank theo phân phối dịch chuyển” → “Đặc tả PageRank theo chủ đề”. Số hạng bù nút cụt trước đây xuất hiện không có lý do vì G4 không có nút cụt; thay dòng ký hiệu bằng câu “Khi có nút cụt, $\delta^t$ được bù đều theo $u$ như Bài 03; G4 có $\delta^t=0$”. Bỏ khỏi mặt trang câu quy ước cột $M_0$ (đã ôn ở s01-06, còn trong ghi chú). |
| lec04-s02-06 | Giả mã cài một vòng bằng danh sách cạnh: khởi tạo phần bù và dịch chuyển, cộng đóng góp theo từng cạnh từ vector cũ, dừng khi đạt ngưỡng hoặc hết $K$ vòng. | sửa | Tiêu đề “Thuật toán lặp PageRank theo chủ đề” → “Giả mã PageRank theo chủ đề”. Thêm dòng phân biệt `delta` ($\delta^t$, điểm ở nút cụt) với `Delta` ($\|r^{t+1}-r^t\|_1$, dùng để dừng); giữ hai tên vì chúng khớp ký hiệu ở s02-05 và s02-08. Giả mã không đổi. |
| lec04-s02-07 | Thay $u$ bằng $v$ vẫn giữ mỗi $r^t$ là phân phối xác suất, vì $v$ không âm và có tổng 1; bất biến chưa cho hội tụ. | sửa | Tiêu đề “Bảo toàn phân phối điểm” → “Bất biến tổng điểm”. Câu chốt nêu lập luận Bài 03 giữ nguyên và điều kiện mới duy nhất là $v\ge0$, $\sum_iv_i=1$ (G10: tránh trình bày lại kết quả Bài 03 như mệnh đề mới). Bảng và phương trình tổng giữ nguyên. |
| lec04-s02-08 | Phép cập nhật co theo hệ số $\beta$ nên có điểm cố định duy nhất; dừng khi $\Delta\le\tau$ cho cận sai số $\beta\Delta/(1-\beta)$. | sửa | Tiêu đề “Tính co và sai số dừng” → “Hội tụ và cận sai số khi dừng”. Nêu $\bar M$ là ma trận $S$ của Bài 03 và $S$ ở bài này là tập chủ đề (G2). Giải nghĩa “tính co” bằng lời, dẫn bất đẳng thức từ Bài 03 (G3). Thêm bước trung gian “các sai khác sau đó không quá $\beta\Delta,\beta^2\Delta,\ldots$” trước chuỗi. Công thức và số giữ nguyên. |
| lec04-s02-09 | Mỗi chủ đề $j$ có phân phối dịch chuyển $v^{(j)}$ và nghiệm $r^{(j)}$ trên cùng $\bar M$, $\beta$. | sửa | Tiêu đề “Các vector điểm theo chủ đề” → “Ký hiệu cho nhiều chủ đề”. Dòng đầu nêu từ đây $j$ chỉ chủ đề, $i$ chỉ trang (trước đó $j$ chỉ trang nguồn). Bỏ hàng $w_j$ khỏi bảng: trọng số được đưa vào ở trang xử lý truy vấn, nơi nhu cầu kết hợp xuất hiện (G6 và thứ tự cụm). Ghi chú nối với nhu cầu lưu $k$ vector thay vector riêng từng người dùng. Quyết định thứ tự cụm: s02-09 → s02-11 → s02-09a → s02-10. |
| lec04-s02-11 | Quy trình hai giai đoạn: trước truy vấn tính và lưu $k$ vector chủ đề; khi có truy vấn xác định $w_j$, $C$ và ghép điểm đã lưu, không lặp lại PageRank. | sửa, chuyển vị trí | Chuyển lên ngay sau s02-09, trước s02-09a (thứ tự bốn bước MMDS §5.3.3): nhu cầu kết hợp xuất hiện trước định lý kết hợp. Tiêu đề “Sử dụng điểm đã lưu khi có truy vấn” → “Tiền tính và xử lý truy vấn”. Định nghĩa $w_j\ge0$, $\sum_jw_j=1$ và $C$ tại đây (G6). Câu “jaguar” nêu cụ thể vai trò của trọng số. Ghi chú bỏ phép đếm $\Theta(kc)$ (chỉ còn ở s02-10), thêm ba cách xác định chủ đề theo MMDS và câu nối sang chứng minh phép ghép. |
| lec04-s02-09a | Nghiệm PageRank tuyến tính theo $v$: trộn các $v^{(j)}$ theo $w$ thì nghiệm là tổ hợp tương ứng của các $r^{(j)}$; vì vậy phép ghép ở trang trước đúng. | sửa | Tiêu đề “Kết hợp các vector chủ đề” → “Tính tuyến tính theo phân phối dịch chuyển” (gọi tên kết quả). Nay đứng sau s02-11 nên chứng minh trả lời nhu cầu đã nêu. Thêm khối kết luận thu hồi nhu cầu ở s01-04: phép ghép cho đúng PageRank với $v=\sum_jw_jv^{(j)}$, mỗi người dùng chỉ cần $k$ trọng số. Chứng minh giữ nguyên. |
| lec04-s02-10 | Tiền tính $k$ vector cần $O(kK(n+\ell))$ thời gian, $\Theta(kn)$ bộ nhớ lưu; khi có truy vấn, ghép điểm cho $c$ ứng viên cần $\Theta(kc)$. | sửa | Tiêu đề “Chi phí tính và lưu các vector chủ đề” → “Chi phí tiền tính và truy vấn”. Sau khi đổi thứ tự, $C$ và $w_j$ đã có trước trang này (G6). Đoạn văn chứa bốn số đo được thay bằng hai thẻ “Tiền tính” và “Khi có truy vấn” cùng bố cục với s02-11; bảng đếm mỗi vòng giữ nguyên. Ghi chú giữ phép đếm $\Theta((\sum_jK_j)(n+\ell))$ và các trường hợp. |
| lec04-s02-12 | Kiểm tra: tính $r_C^2=13/75$ từ đóng góp của A, D và bác mệnh đề “trang ngoài $S$ luôn có điểm 0”. | sửa | Tiêu đề “Kiểm tra phép cập nhật theo chủ đề” → “Kiểm tra PageRank theo chủ đề”. Câu hỏi giữ nguyên. Ghi chú thêm câu nối ranh giới S02→S03: điểm do cấu trúc liên kết quyết định nên người kiểm soát một phần đồ thị có thể thêm cạnh để làm tăng điểm. |
| lec04-s03-01 | PageRank cộng điểm theo liên kết vào nên người đặt được liên kết có thể làm tăng điểm một trang; S03 định lượng tác động của một cấu trúc đơn giản. | sửa | Tiêu đề “Liên kết rác và điểm xếp hạng” → “Liên kết rác”. Câu mở thêm cơ chế (PageRank cộng điểm theo liên kết vào). Thẻ “Quyền tác động” đổi thành “Thêm liên kết ở trang sở hữu hoặc được phép đăng” (không dùng “cụm” trước định nghĩa). Khối kết luận chung chung thay bằng vấn đề định lượng của phần. Đồng bộ khối công khai trong storyboard với bố cục ba thẻ. |
| lec04-s03-02 | Cụm thao túng đơn giản nhất (Hình 5.16): đích trỏ tới $m$ hỗ trợ, mỗi hỗ trợ chỉ trỏ lại đích, liên kết ngoài chỉ vào đích; đồ thị không có nút cụt. | sửa | Tiêu đề “Cấu trúc cụm thao túng liên kết” → “Cụm thao túng liên kết”. Bỏ cụm “nhóm sở hữu” chưa định nghĩa; ba vùng do hình thể hiện và ghi chú giải thích theo MMDS §5.4.1. Hai câu mô tả cạnh lặp ý được rút thành hai dòng ngắn. Sửa `hinh-5-16-cum-thao-tung.svg`: nhãn “Đóng góp từ ngoài” đè lên tiêu đề vùng giữa, chuyển xuống chân vùng thành “đóng góp từ ngoài vào đích” (SVG dùng chung với ghi chú tự học; chỉ đổi vị trí và chữ thường hóa nhãn). |
| lec04-s03-03 | Mỗi trang hỗ trợ có điểm cố định $p=\beta y/m+b$: phần $\beta y/m$ từ đích và phần dịch chuyển đều $b$. | sửa | Giữ tiêu đề “Điểm của một trang hỗ trợ”. Dòng ký hiệu nêu $y$, $p$ là điểm cố định, nối với khái niệm điểm cố định ở S02 và cho biết đây là phương trình cân bằng. Bỏ câu thừa “Mọi trang hỗ trợ có cùng phương trình trong mô hình này”. |
| lec04-s03-04 | Trang đích nhận ba nguồn: $x$ từ ngoài (đã gồm $\beta$), $\beta mp$ từ các hỗ trợ và $b$ từ dịch chuyển; $y=x+\beta mp+b$. | sửa nhẹ | Giữ tiêu đề “Ba nguồn điểm tại trang đích”, hình và bảng. Bỏ câu cuối “Đóng góp $x$ đã bao gồm hệ số $\beta$” vì lặp dòng định nghĩa $x$ ở đầu trang. |
| lec04-s03-05 | Phần điểm đi đích→hỗ trợ→đích quay về với hệ số $\beta^2$; thế $p$ vào phương trình của đích cho $y=(x+\beta mb+b)/(1-\beta^2)$. | sửa tiêu đề | “Vòng truyền điểm qua các trang hỗ trợ” → “Điểm cố định của trang đích” (cùng thuật ngữ “điểm cố định” với s03-03 và S02): trang có hai bước (trực giác $\beta^2$ rồi nghiệm $y$), tiêu đề gọi kết quả cuối. Đại số tính lại đúng; nội dung giữ nguyên. |
| lec04-s03-06 | Với $\beta=0{,}85$, cụm nhân đóng góp từ ngoài $x$ khoảng $3{,}6$ lần và nhận thêm khoảng $0{,}46\,m/n$ (MMDS Ví dụ 5.11). | sửa | Tiêu đề “Hệ số khuếch đại trong mô hình giản lược” → “Hệ số khuếch đại của cụm”. Dẫn nguồn “MMDS §5.4.2” thay cho “như phép phân tích của sách”. Dấu phẩy thập phân trên mặt trang (G11). Dòng cuối dồn hai ý được thay bằng khối kết luận diễn giải hai hệ số; hạng bị bỏ và cách MMDS gọi “360%” nằm trong ghi chú. $400/111$ và $17/37$ tính lại đúng. |

**Rà lại S01–S02 (tác tử chỉ đọc loại `general-purpose`, kế thừa mô hình điều phối viên).** Độ chính xác đạt: tính lại $r^1$, $r^2$, $r^3$, $r^*$, cận dừng, tính tuyến tính và các chi phí. Một phát hiện nghiêm trọng, một trung bình và các phát hiện nhẹ; xử lý như sau.

| Trang | Phát hiện rà lại | Quyết định | Thay đổi |
|---|---|---|---|
| lec04-s02-12 | (nghiêm trọng) Đáp án hai câu đã hiển thị ở s02-01, s02-04; không kiểm cận dừng hay phép ghép. | sửa | Câu 1 → tính $r_C^3=23/125$ từ $r^2$ (khớp MMDS tr.197); câu 2 → tính $\Delta=\|r^2-r^1\|_1=4/25$ và cận $16/25$. Ghi chú thêm sai số thật $8/175$ và sửa câu nối: điểm do cấu trúc liên kết và phân phối dịch chuyển quyết định. Thẻ storyboard đồng bộ. |
| lec04-s01-06 | (trung bình) Bảng phần ghi đây là trang kiểm tra riêng của S01, mâu thuẫn quyết định “ôn tiên quyết”. | sửa storyboard | Ghi ngoại lệ trong bảng phần: S01 là mở bài, trang này ôn tiên quyết, không có trang kiểm đầu ra riêng. |
| lec04-s02-11, lec04-s02-09a | (trung bình) $r_i^*$ được định nghĩa là tổng ghép trước khi chứng minh, trùng ký hiệu điểm cố định. | sửa | s02-11 dùng $q_i=\sum_jw_jr_i^{(j)}$ (khớp $q$ trong ghi chú s02-09a); s02-09a kết luận “Điểm cố định là duy nhất, nên tổng này bằng $r^*$” và khối kết luận nêu $q_i=r_i^*$. |
| lec04-s01-05 | (nhẹ) Ghi chú lặp câu tổng kết trên mặt trang; câu về HITS chưa phân biệt với PageRank. | sửa | Bỏ vế lặp trong ghi chú; câu HITS thêm “không chia theo bậc ra, rồi chuẩn hóa” (MMDS §5.5.2). |
| lec04-s01-06 | (nhẹ) Nét đứt mang hai nghĩa: tô sáng cạnh dữ liệu B→A ở trang này nhưng chỉ bước không phải cạnh dữ liệu ở s02-01. | sửa SVG | `hinh-5-1-kiem-tra.svg`: cạnh B→A đổi từ nét đứt sang nét đậm; văn bản thay thế cập nhật. Nét đứt từ đây chỉ dùng cho bước không phải cạnh dữ liệu. |
| lec04-s02-01 | (nhẹ) $S$ trên mặt trang chưa được gọi tên. | sửa | “dịch chuyển tới một trang trong $S$” → “dịch chuyển tới tập chủ đề $S$”. |
| lec04-s02-08 | (nhẹ) “thu hẹp khoảng cách ít nhất theo hệ số $\beta$” mơ hồ. | sửa | Đổi thành “Khoảng cách sau cập nhật không vượt $\beta$ lần khoảng cách trước (tính co)”. |
| lec04-s02-09 | (nhẹ) “Vector PageRank hội tụ” dễ đọc thành tính chất của dãy lặp. | sửa | Đổi thành “Điểm cố định PageRank của chủ đề $j$ trên $n$ trang”. |
| lec04-s02-10 | (nhẹ) Đầu cột không khớp ô; đoạn 3 ghi chú lặp mặt trang; nguồn chưa nói phép đếm do bài suy ra. | sửa | Đầu cột “Khối lượng mỗi vòng”; đoạn 3 ghi chú viết lại thành ý mới (bộ nhớ theo số chủ đề, không theo số người dùng; không dựng vector ghép trên $n$ trang); dòng nguồn trên trang và trong ghi chú thêm “phép đếm suy ra từ giả mã” (MMDS không phân tích chi phí này); storyboard đã ghi “Phép đếm từ HT1/HT3”. |
| lec04-s03-07 | Phát hiện cấu trúc cụm bị né bằng vô số biến thể; hướng bền hơn là đổi cách tính điểm dựa trên tập trang tin cậy, dẫn tới TrustRank và Spam Mass. | viết lại | Tiêu đề “Giới hạn của phân tích cấu trúc liên kết” → “Hai hướng chống liên kết rác”. Thân trang theo MMDS §5.4.3: hai thẻ “Phát hiện cấu trúc” (giới hạn: biến thể, nhóm liên kết dày hợp lệ) và “Đổi cách tính điểm” (tập trang đáng tin); khối kết luận nối sang S04 (G8). Bỏ hình $2m$ cạnh nội bộ và câu điều kiện áp dụng (đã có ở s03-03); `hai-nhom-canh-noi-bo.svg` không còn được deck hay ghi chú dùng, giữ tệp, không xóa. |
| lec04-s03-08 | Kiểm tra: sửa phương trình điểm đích thành $y=x+\beta mp+b$ và xác định hạng bị bỏ $1/[n(1+\beta)]$. | sửa | Tiêu đề “Kiểm tra nguồn điểm tại đích” → “Kiểm tra cụm thao túng liên kết”. Dòng dữ kiện lặp toàn bộ giả thiết được rút còn “Mô hình Hình 5.16, không có nút cụt” cùng các ký hiệu cần dùng. Câu hỏi giữ nguyên; đáp án câu 2 không còn hiển thị ở s03-06. |
| lec04-s04-01 | TrustRank là PageRank theo chủ đề với tập dịch chuyển $T$ gồm trang tin cậy, dựa trên giả định trang tin cậy hiếm khi trỏ tới trang rác; $T$ được chọn ngoài thuật toán. | sửa | Tiêu đề “Tập trang tin cậy và TrustRank” → “TrustRank”. Câu chính đặt đầu trang và đặt tên “tập hạt giống (seed set)”. Nêu đủ lý do hai chiều của giả định. Thêm hai cách chọn $T$ theo MMDS §5.4.4 (trang PageRank cao; miền .edu, .gov). Ghi chú thêm lý do của hai cách chọn và ví dụ trang báo có bình luận. |
| lec04-s04-02 → lec04-s04-02a | Phép lặp TrustRank là phép lặp PageRank theo chủ đề với $v=v_T$; không cần thuật toán mới. | gộp | s04-02 (bảng ký hiệu, bốn trong năm ký hiệu đã có ở S02, G10) bị bỏ; nội dung cần thiết gộp vào s04-02a với tiêu đề “Phép lặp TrustRank”. Luận điểm $r\mapsto\rho$, $v\mapsto v_T$ đặt đầu trang; bỏ bảng “nơi nhận điểm”. Ghi chú hợp nhất hai ghi chú cũ. Deck còn 52 trang; S04 còn 7 trang, giữ 18 phút (s04-02a nhận 4 phút). |
| lec04-s04-03 | Trên G4 với $T=\{B,D\}$, TrustRank trùng nghiệm ví dụ chủ đề vì cùng phân phối dịch chuyển; khác biệt nằm ở ý nghĩa của tập. | sửa | Tiêu đề “TrustRank trên đồ thị bốn trang” → “TrustRank trên G4”. Khối kết luận bỏ vế “B và D là hạt giống giả thiết” (lặp dòng dữ kiện), nêu rõ cùng phép tính, ý nghĩa tập đổi từ chủ đề sang độ tin cậy. |
| lec04-s04-03 (bổ sung) | Như trên. | sửa bố cục | Bản commit trước làm trang tràn khung (763/720 px); gộp $v_T$ vào dòng dữ kiện, bỏ vế “G4 giữ nguyên tám cạnh” (tên G4 đã có ở tiêu đề), rút khối kết luận còn một dòng. |
| lec04-s04-04 | So với PageRank nền cùng $\beta$, TrustRank làm A, C giảm điểm và B, D tăng điểm; hiệu $r_i-\rho_i$ ước lượng phần điểm không đến từ tập tin cậy. | sửa | Tiêu đề “So sánh PageRank và TrustRank” → “Hiệu giữa PageRank và TrustRank”. Dòng mở nêu ý tưởng MMDS §5.4.5 trước bảng (trước đó cột hiệu xuất hiện không có nhu cầu). Câu diễn giải dấu trừu tượng thay bằng kết quả cụ thể trên G4; câu về thứ hạng và nhãn rác đã có trong ghi chú. PageRank nền $(9/28,19/84,19/84,19/84)$ tính lại đúng. |
| lec04-s04-05 | Spam Mass $s_i=(r_i-\rho_i)/r_i$ là tỷ lệ của PageRank không được tập tin cậy giải thích; gần 1 gợi ý rác, âm hoặc nhỏ thì có lẽ không. | sửa | Tiêu đề “Định nghĩa và giá trị Spam Mass” → “Chỉ số Spam Mass”. Ý tưởng đứng trước công thức (G7). Câu chốt dùng cách đọc của MMDS §5.4.5 và đọc kết quả A, C. Ghi chú thêm “không phải xác suất” và đối chiếu với Ví dụ 5.12 (MMDS dùng PageRank không dịch chuyển, $s_A\approx0{,}229$). Bảng giữ nguyên, tính lại đúng. |
| lec04-s04-06 | Tính Spam Mass rẻ (hai phép lặp thưa và $\Theta(n)$ phép tính); chi phí chính và độ phủ nằm ở việc chọn tập tin cậy. | sửa | Tiêu đề “Độ phủ hạt giống và chi phí đánh giá” → “Chi phí và độ phủ tập tin cậy”. Dòng mở dùng ví dụ độ phủ của MMDS §5.4.4. Câu chốt nêu cách dùng chỉ số theo MMDS §5.4.5, nối với hướng “đổi cách tính điểm” ở s03-07; bỏ câu lặp s04-05. Ghi chú bỏ câu “Sau khi có $r$ và $\rho$, mỗi trang cần…” bị lặp. |
| lec04-s04-07 | Kiểm tra: tính Spam Mass từ dữ kiện sách và nhận ra chỉ số phụ thuộc cách tính PageRank nền; $s_A=1/5$ không đủ kết luận A là rác. | sửa | Tiêu đề “Kiểm tra cách diễn giải Spam Mass” → “Kiểm tra Spam Mass”. Câu 1 cũ có đáp án hiển thị ở s04-05; thay bằng tính $s_C=13/70$ từ dữ kiện MMDS Ví dụ 5.12 (khớp Hình 5.17) và giải thích chênh lệch với $1/5$. Câu 2 đổi sang dạng yêu cầu. Ghi chú cập nhật lời giải, giữ câu nối sang HITS. |
| lec04-s05-01 | Một mức quan trọng không phân biệt trang dẫn tới thông tin (trung tâm) với trang cung cấp thông tin (uy tín); HITS gán mỗi trang hai điểm $h_i$, $a_i$. | sửa | Tiêu đề “Hai vai trò trong mạng học phần” → “Trang trung tâm và trang uy tín”. Câu mở nối từ S04 và nêu giới hạn “một mức quan trọng” của PageRank, TrustRank (G9, MMDS §5.5.1). Định nghĩa hai vai trò bằng một câu; câu so sánh uy tín HITS với độ tin cậy TrustRank chuyển vào ghi chú. |
| lec04-s05-02 | Hai điểm định nghĩa lẫn nhau: $\tilde a_j=\sum_{i\to j}h_i$, $\tilde h_i=\sum_{i\to j}a_j$, chia cho thành phần lớn nhất sau mỗi bước; HITS không cần dịch chuyển dù G5 có nút cụt. | sửa | Tiêu đề “Điểm trung tâm và điểm uy tín” → “Định nghĩa tương hỗ của hai điểm”. Hai công thức cộng và quy tắc chuẩn hóa (cùng lý do “tăng không giới hạn” của MMDS §5.5.2) được đưa lên trước vết chạy (G5). Thêm ý E là nút cụt nhưng không cần dịch chuyển (MMDS Ví dụ 5.14); ghi chú thêm phương án chuẩn hóa tổng bằng 1 của sách. |
| lec04-s05-03 | Chạy tay bước uy tín đầu: B, C, D có uy tín thô lớn nhất bằng 2; chuẩn hóa cho $a^1=(1/2,1,1,1,1/2)^\mathsf T$. | sửa | Tiêu đề “Lượt cập nhật uy tín thứ nhất” → “Bước uy tín thứ nhất”. Câu cuối dẫn lại quy tắc cộng và chuẩn hóa vừa nêu ở s05-02 thay cho thao tác “chia toàn vector cho 2” chưa có lý do. Số liệu giữ nguyên. |
| lec04-s05-04 | Bước trung tâm dùng $a^1$ vừa tính: A cao nhất, E bằng 0; $h^1=(1,1/2,1/6,2/3,0)^\mathsf T$. | sửa | Tiêu đề “Lượt cập nhật trung tâm thứ nhất” → “Bước trung tâm thứ nhất”. Câu cuối nêu trước việc dùng $a^1$ rồi mới chuẩn hóa. Số liệu giữ nguyên. |
| lec04-s05-05 | Vòng 2: uy tín chuẩn hóa theo $5/3$, trung tâm theo $29/10$; trung tâm của C và uy tín của E giảm dần. | sửa | Tiêu đề “Vòng lặp HITS thứ hai” → “Vòng thứ hai trên G5”. Câu chốt “Hai vector thay đổi qua mỗi vòng” thay bằng điều quan sát được trên bảng; ghi chú giữ lưu ý đây là quan sát, không phải chứng minh. Số liệu tính lại đúng. |
| lec04-s05-06 | Viết HITS bằng ma trận: $\tilde a=L^\mathsf Th$, $\tilde h=La$; $L$ có hàng là nguồn và giá trị 1, khác $M_0$ chia theo bậc ra. | giữ | Tiêu đề và nội dung đạt; hai báo cáo không nêu vấn đề cần sửa. Đối chiếu $L$ với Hình 5.19: khớp. |
| lec04-s05-07 | Chuẩn hóa $N(q)=q/\max_iq_i$ giữ tỷ lệ và thứ hạng; điểm HITS không phải phân phối; đồ thị không cạnh làm chuẩn hóa không xác định. | sửa nhẹ | Giữ tiêu đề và vị trí (quy tắc đã nêu ở s05-02, G5). Câu mở nối với các phép chia đã dùng trong vết chạy. |
| lec04-s05-08 | Giả mã HITS: cập nhật uy tín rồi trung tâm, chuẩn hóa sau mỗi phép nhân, dừng theo thay đổi lớn nhất của hai vector. | sửa | Tiêu đề “Thuật toán HITS với cập nhật luân phiên” → “Thuật toán HITS”. Ghi chú thêm câu giải thích khởi tạo `a` toàn 1 chỉ phục vụ phép đo thay đổi ở vòng đầu. Giả mã giữ nguyên. |
| lec04-s05-09 | Ở điểm ổn định, $h$ là vector riêng của $LL^\mathsf T$ và $a$ là vector riêng của $L^\mathsf TL$; giới hạn duy nhất cần trị riêng lớn nhất có một hướng riêng. | viết lại | Tiêu đề “Điểm ổn định và giới hạn của HITS” → “Điểm ổn định của HITS”. Bỏ câu mở và hình đóng góp theo cạnh (thuộc cơ chế, đã có ở s05-02, s05-06); `dong-gop-hits.svg` không còn được dùng, giữ tệp. Định nghĩa ký hiệu $\propto$; khối kết luận gọi tên vector riêng và điều kiện giới hạn duy nhất. Ghi chú đổi số thập phân sang dấu phẩy. |

**Rà lại S03–S04 (tác tử chỉ đọc loại `general-purpose`, kế thừa mô hình điều phối viên).** Độ chính xác đạt: tính lại $p$, $y$, hạng bị bỏ, $400/111$, $17/37$, TrustRank, PageRank nền, hiệu, Spam Mass, $s_C=13/70$; gán nguồn MMDS §5.4.3–5.4.5 đúng. Hai phát hiện nghiêm trọng (đáp án đã hiển thị ở s03-08, s04-07) và các phát hiện trung bình, nhẹ; xử lý như sau.

| Trang | Phát hiện rà lại | Quyết định | Thay đổi |
|---|---|---|---|
| lec04-s03-07 | (trung bình) “nhóm liên kết dày cũng có thể hợp lệ” không có trong MMDS §5.4.3; phiếu storyboard còn trường của bản cũ; bảng ánh xạ SVG còn hình đã bỏ. | sửa | Thẻ “Phát hiện cấu trúc” chỉ giữ giới hạn theo nguồn (biến thể gần như không giới hạn); bỏ câu tương ứng trong ghi chú. Viết lại các trường phiếu theo hai hướng của §5.4.3; bảng ánh xạ SVG ghi `hai-nhom-canh-noi-bo.svg` và `dong-gop-hits.svg` không còn được tham chiếu. |
| lec04-s03-08 | (nghiêm trọng) Đáp án hai câu đã hiển thị ở s03-04, s03-05, s03-06; dẫn nhập gợi sẵn “$x$ đã gồm $\beta$”. | sửa | Câu 1: vận dụng công thức xấp xỉ với $\beta=0{,}9$ (hệ số $100/19$ và $9/19$) và so với $\beta=0{,}85$. Câu 2: xác định phương trình phải đổi khi hỗ trợ nhận cạnh từ ngoài cụm ($p=\beta y/m+x'+b$). Dẫn nhập chỉ còn tên mô hình. Ghi chú có lời giải và lỗi thường gặp. Phiếu storyboard đồng bộ. |
| lec04-s04-01 | (trung bình) Cầu nối S03→S04 bị trang kiểm tra s03-08 chen giữa; s04-01 mở thẳng bằng định nghĩa. Ý độ phủ nên nằm cùng cách chọn hạt giống. | sửa ghi chú | Câu đầu ghi chú nối TrustRank với hướng “đổi cách tính điểm” của s03-07. Ví dụ độ phủ .edu (MMDS §5.4.4) chuyển từ mặt s04-06 vào ghi chú trang này, cạnh hai cách chọn hạt giống. |
| lec04-s04-02a | (nhẹ) Dòng định nghĩa $\rho_i^t$, $\delta_\rho^t$ nằm sau phương trình; $u$ không được nhắc; ghi chú lặp câu mở và câu rào đón. | sửa | Đưa dòng ký hiệu lên trước phương trình, thêm “$u$ đều trên $n$ trang”. Ghi chú bỏ câu lặp mặt trang và câu rào đón “không chứng nhận độ tin cậy tuyệt đối” (giữ ý này một lần ở s04-05). |
| lec04-s04-03 | (trung bình) Câu rào đón lặp trong ghi chú S04. | sửa ghi chú | Bỏ câu “không xác nhận hoặc bác bỏ riêng lẻ tính tin cậy”. |
| lec04-s04-04 | (nhẹ) Ghi chú dùng “$\beta=0.8$” (dấu chấm), lặp diễn giải dấu đã có trên mặt trang và câu rào đón. | sửa ghi chú | Đổi thành $\beta=4/5$; bỏ các câu diễn giải dấu lặp và câu “không xác định thứ hạng hoặc nhãn rác”. |
| lec04-s04-05 | (nhẹ) Định nghĩa “tỷ lệ” chưa nói giá trị có thể âm; (liên quan nghiêm trọng ở s04-07) câu “A, C … gần 0 hơn 1” là đáp án câu hỏi kiểm tra. | sửa | Câu chốt nêu $s_i<0$ khi $\rho_i>r_i$ và cách đọc của MMDS §5.4.5; bỏ kết luận về A, C khỏi mặt trang (để câu hỏi ở s04-07 đòi vận dụng). |
| lec04-s04-06 | (trung bình) Ba luận điểm trên một trang; (nhẹ) ghi chú có mệnh đề suy luận ngoài MMDS và câu rào đón lặp. | sửa | Tiêu đề → “Chi phí tính Spam Mass”; dòng độ phủ .edu chuyển vào ghi chú s04-01; trang còn bảng chi phí và cách dùng $s_i$. Ghi chú bỏ câu “Điểm tin cậy thấp có thể phản ánh khoảng cách liên kết…” và câu “chỉ số không tự xác định nhãn rác”. |
| lec04-s04-07 | (nghiêm trọng) Câu 2 có đáp án trên mặt s04-05; (trung bình) dẫn nhập “PageRank không dịch chuyển” trả lời sẵn nửa sau câu 1 và “trang trước” chỉ sai trang. | sửa | Bỏ kết luận về A, C khỏi s04-05; dẫn nhập ghi nguồn số liệu (Ví dụ 5.2) thay cho tính chất của nó; câu 1 yêu cầu chỉ ra đại lượng làm $s_C$ khác $1/5$ và gọi đúng trang “Chỉ số Spam Mass”. Thẻ nhiệm vụ trong storyboard đồng bộ với câu hỏi mới. |
| storyboard | (nhẹ) Số đếm cũ: đầu tệp ghi 53 trang, mục S04 ghi 8 slide. | sửa | Cập nhật thành 52 trang (49 giảng, 3 bài tập) và 7 slide cho S04. Các mục lịch sử ngày 28–29/09 giữ nguyên số đếm của thời điểm đó. |
| lec04-s03-04 | (nhẹ) Ghi chú lặp số hạng $b$ đã có trên mặt trang. | sửa ghi chú | Bỏ câu “Phương trình đầy đủ còn có $b$ tại đích”; giữ ý ba số hạng thuộc cùng điểm cố định. Các câu lặp nhẹ còn lại trong ghi chú s04-05 (phép chia tại A) được giữ vì nêu bước tính chi tiết. |
| lec04-s05-10 | Mỗi vòng HITS duyệt cạnh hai lần: $\Theta(n+\ell)$ thời gian, $\Theta(n)$ bộ nhớ phụ; không dựng $LL^\mathsf T$. | sửa | Tiêu đề “Chi phí HITS trên đồ thị thưa” → “Chi phí HITS”. Bỏ vế “Hai lượt cạnh đáp ứng nhu cầu tính hai vector trên đồ thị lớn” (không mang thông tin). Bảng đếm giữ nguyên. |
| lec04-s05-11 | Kiểm tra: tính một bước uy tín mới, bác cách chia bậc ra, giải thích uy tín dương của nút cụt. | sửa | Tiêu đề “Kiểm tra một vòng HITS” → “Kiểm tra HITS”. Câu 1 và 3 cũ hỏi $h_B^1$, $h_E^1$ đã hiện ở s05-04; thay bằng tính $\tilde a_D=41/29$, $a_D^3=41/49$ và $a_E^3=1/49$ từ $h^2$ (tính lại bằng phân số). Câu 2 giữ ý không chia bậc ra. Hình đổi sang G5 không tô nét đứt; `hinh-5-18-kiem-tra.svg` không còn được tham chiếu. |
| lec04-s06-01 | Bốn phương pháp cho bốn loại đầu ra và cần các thông tin bổ sung khác nhau; uy tín HITS khác độ tin cậy TrustRank. | sửa nhẹ | Tiêu đề “Đối chiếu ý nghĩa các điểm xếp hạng” → “Ý nghĩa của các điểm xếp hạng”. Cột “Thông tin quyết định” → “Thông tin bổ sung cần có”. |
| lec04-s06-02 | Thu hồi ba tình huống mở bài và chọn phương pháp kèm điều kiện áp dụng; cùng bậc chi phí mỗi vòng không bảo đảm cùng thời gian. | sửa tiêu đề | “Lựa chọn phương pháp theo yêu cầu dữ liệu” → “Chọn phương pháp xếp hạng”. Nội dung giữ nguyên. |
| lec04-s06-03 | Kiểm tra: đổi tập dịch chuyển chỉ đổi $v$ (và khởi tạo theo $v$), giữ $M_0$, $\beta$; cùng bậc chi phí mỗi vòng không suy ra cùng thời gian chạy. | sửa | Tiêu đề “Tự kiểm về mô hình và chi phí” → “Câu hỏi về mô hình và chi phí”. Câu 1 đổi tập dịch chuyển từ {A} sang {C} để không trùng dữ kiện Bài tập 5.3.1(a); ghi chú đổi $v$ tương ứng thành $(0,0,1,0)^\mathsf T$. |
| lec04-s06-04 | Kiểm tra tổng hợp: kết hợp cụm thao túng với TrustRank, đánh giá cách xử lý Spam Mass âm, chọn HITS cho hai vai trò. | sửa | Tiêu đề “Kiểm tra tổng hợp các phương pháp” → “Câu hỏi so sánh các phương pháp”. Câu 3 cũ (lặp s03-08) thay bằng TrustRank của cụm không có trang trong $T$: $p=\beta y/m$, $y=x_\rho/(1-\beta^2)$, mất số hạng $m/n$ (suy ra từ phương trình S03 với $b=0$). Câu 4 bỏ số liệu lặp s04-05, giữ yêu cầu đánh giá việc cắt giá trị âm. Câu 5 bỏ cụm “mạng học phần”. Thẻ storyboard đồng bộ. |
| lec04-s07-01 | Bài tập 5.3.1(a, b): PageRank theo chủ đề trên G4 với tập {A} và {A, C}. | sửa nhẹ | Giữ tiêu đề, dữ kiện và lời giải ($r=(3/7,4/21,4/21,4/21)$; $(27/70,6/35,19/70,6/35)$, tính lại đúng). Dòng sản phẩm tách “tổng 1/điểm cố định” thành hai phép kiểm. |
| lec04-s07-02 | Bài tập 5.4.1(a, c): phân tích lại cụm khi hỗ trợ chỉ có khuyên, hoặc có khuyên và cạnh về đích. | sửa nhẹ | Tiêu đề “Bài tập cấu trúc liên kết hỗ trợ” → “Bài tập biến thể cụm thao túng”. Dòng giả thiết rút còn phần khác với Hình 5.16. Lời giải (a) $y\approx x$; (c) $y=[(2-\beta)(x+b)+\beta mb]/[(1-\beta)(2+\beta)]$ giữ nguyên. |
| lec04-s07-03 | Bài tập 5.5.2: điểm HITS giới hạn trên chuỗi có khuyên, với biên $n=1$, $n=2$. | giữ | Tiêu đề, dữ kiện và lời giải đạt; hai báo cáo không nêu vấn đề. Quy nạp $h^t$, $a^t$ và giới hạn $h^*=(1,0,\ldots,0)^\mathsf T$, $a^*=(1,1,0,\ldots,0)^\mathsf T$ kiểm lại đúng. |
| outline | Đồng bộ cấu trúc sau lượt duyệt. | sửa | Bảng phần ghi S04 có 7 trang; thêm mục “Duyệt từng trang ngày 01/10/2026” tóm tắt thứ tự mới ở S02, cầu nối S03→S04, gộp S04-02, thuật ngữ với Bài 03, các câu hỏi kiểm tra đã đổi và tác động tới ghi chú tự học. |

**Rà lại S05–S07 và toàn deck (tác tử chỉ đọc loại `general-purpose`, kế thừa mô hình điều phối viên).** Độ chính xác đạt (vết G5, $a^3$, phổ $LL^\mathsf T$, chi phí, ba bài tập). 52 tiêu đề đạt; mục lục khớp 7 phần; không còn mã trang nội bộ. Hai phát hiện nghiêm trọng (đáp án s06-03 câu 2 và s06-04 câu 5 hiển thị ở s06-02) và các phát hiện trung bình, nhẹ; xử lý như sau.

| Trang | Phát hiện rà lại | Quyết định | Thay đổi |
|---|---|---|---|
| lec04-s06-02 | (nghiêm trọng, liên quan s06-03) Câu “Cùng bậc chi phí mỗi vòng không bảo đảm cùng số vòng hoặc cùng thời gian thực” là đáp án câu 2 của s06-03. | sửa | Mặt trang chỉ giữ “mỗi vòng tuyến tính theo $n+\ell$”; ý về số vòng và thời gian thực nằm trong ghi chú. |
| lec04-s06-04 | (nghiêm trọng) Câu 5 có đáp án ở dòng 3 bảng s06-02; (trung bình) câu 3 thiếu giả thiết không có nút cụt (phần bù $\beta\delta_\rho u$ làm $p\ne\beta y/m$). | sửa | Câu 5 đổi thành tính $a^1$ trên G4 và so với PageRank nền (đáp án $a^1=(1,1,1,1)^\mathsf T$, giải thích vai trò của việc chia theo bậc ra). Câu 3 thêm “đồ thị không có nút cụt”. Ghi chú và thẻ storyboard đồng bộ. |
| lec04-s05-11 | (trung bình) Câu 2 có đáp án ở câu chốt s05-06 (“không chia bậc ra”); các trường phiếu storyboard mô tả bản cũ. | sửa | Câu 2 đổi thành tính lại $\tilde a_D$ khi chia theo bậc ra ($47/87$, khác $41/29$) và nêu định nghĩa bị thay. Cập nhật các trường đầu vào, bố cục, trọng tâm, lý do và đáp án trong phiếu. |
| lec04-s05-02 | (nhẹ) “tăng không giới hạn” mạnh hơn nguồn (MMDS: “typically grow beyond bounds”). | sửa | Đổi thành “thường tăng không giới hạn”. |
| lec04-s05-08 | (trung bình) Điều kiện trước “ít nhất một cạnh” mâu thuẫn với câu đầu ra nói đồ thị không cạnh trả trạng thái không xác định; giả mã không có nhánh đó. | sửa | Câu đầu ra: “Đồ thị không cạnh nằm ngoài điều kiện trước vì $N(0)$ không xác định.” Tên `tau` trong giả mã giữ như giả mã PageRank ở S02 (tên ASCII của $\tau$). |
| lec04-s05-07 | (nhẹ) Câu cuối ghi chú lặp trường hợp đồ thị không cạnh trên mặt trang. | sửa ghi chú | Bỏ câu lặp. |
| lec04-s05-01 | (nhẹ) Vế “ví dụ nhỏ cho phép kiểm từng phép cập nhật” mang tính siêu văn bản. | sửa ghi chú | Bỏ vế này. |
| lec04-s06-01 | (nhẹ) Ô “Thông tin bổ sung cần có” của HITS ghi cơ chế; câu cuối ghi chú lặp câu chốt. | sửa | Ô HITS → “Không cần; chỉ dùng cấu trúc liên kết”; bỏ câu lặp trong ghi chú. |
| lec04-s07-01 | (nhẹ) “$\beta=0.8$” dùng dấu chấm thập phân; khối công khai trong storyboard khác HTML. | sửa | Đổi thành $\beta=0{,}8$; đồng bộ khối công khai. |
| lec04-s07-03 | (nhẹ) Thiếu dòng nguồn trên mặt trang; thẻ storyboard ghi nhầm “Slide kiểm tra riêng của phần”. | sửa | Thêm dòng nguồn MMDS Bài 5.5.2 như s07-01, s07-02; sửa thẻ thành “Bài tập nguồn”. |
| lec04-s05-06 (storyboard) | (nhẹ) Khối công khai dùng `pmatrix` không nhãn, gộp công thức; khác HTML. | sửa storyboard | Chép lại khối công khai theo HTML (ma trận có nhãn A–E, hai công thức, bảng đối chiếu). |
| lec04-s07-01…03 (ghi chú) | Báo riêng: ghi chú ba trang bài tập có “Thời lượng dự kiến: 20 phút”; AGENTS.md vừa yêu cầu ghi thời lượng bài tập “trong storyboard và ghi chú” vừa cấm thời lượng trong ghi chú diễn giả. | giữ | Giữ theo quy định riêng cho phần bài tập (mục “Đối tượng và thời lượng”), là quy định cụ thể hơn; thời lượng không hiển thị trên mặt trang. Nêu điểm mâu thuẫn để người dùng quyết định nếu muốn bỏ. |

### Kiểm định cuối lượt duyệt từng trang, 01/10/2026

| Hạng mục | Kết quả |
|---|---|
| Cấu trúc | 52 trang (49 giảng, 3 bài tập), bảy phần 6/13/8/7/11/4/3; mục lục s01-02 khớp bảy phần; điều hướng phím mũi tên đúng. |
| Hiển thị | Playwright Chromium chụp đủ 52 trang ở 1600 × 900 và 390 × 844: không tràn khung, không cuộn ngang, không lỗi KaTeX, không lỗi console; cỡ chữ nhỏ nhất 18 px. Điều phối viên xem ảnh các trang đã sửa. Ảnh lưu ngoài kho. |
| Mã nội bộ | `s0x-yy` chỉ còn trong `id` và `data-slide-id`; không có trên mặt trang hay ghi chú. |
| Rà lại | Ba lượt rà chỉ đọc (S01–S02, S03–S04, S05–S07 và toàn deck); mọi phát hiện nghiêm trọng và trung bình đã xử lý, phát hiện nhẹ không áp dụng có lý do trong bảng trên. Phép tính được tính lại bằng phân số. |
| Phạm vi tệp | Chỉ HTML Bài 04, ba tệp planning, `luu-vector-theo-chu-de.svg`, `hinh-5-16-cum-thao-tung.svg`, `hinh-5-1-kiem-tra.svg`. CSS, index và `lecture-note.md` không đổi. `hai-nhom-canh-noi-bo.svg`, `dong-gop-hits.svg`, `hinh-5-18-kiem-tra.svg` không còn được deck tham chiếu, giữ trong kho. |
| Ghi chú tự học | Ký hiệu và thứ tự khái niệm tương thích; chưa có câu nối “bước nhảy ngẫu nhiên” của Bài 03 và các câu hỏi kiểm tra mới chỉ có trong deck. Cần một lượt sửa ghi chú riêng nếu muốn đồng bộ. |
| Giới hạn | Từ s01-06, các trang được điều phối viên sửa trực tiếp sau khi tác tử chỉnh sửa bị người dùng dừng; bù lại bằng ba lượt rà lại độc lập theo phần. Không chạy lại đủ năm vai rà độc lập cho toàn deck. |
