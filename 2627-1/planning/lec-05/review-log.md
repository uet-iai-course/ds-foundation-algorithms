# Nhật ký rà soát Bài 05 — bản viết mới

Ngày 28-09-2026. Nhật ký lưu các mốc lập kế hoạch, soạn, sửa và tái kiểm; kết luận hiện hành của điều phối viên nằm ở cuối tệp. Các phần ghi “giai đoạn planning” lưu bằng chứng tại thời điểm đó; trạng thái hiện hành và bàn giao nằm ở cuối nhật ký. Người dùng yêu cầu bỏ dàn bài cũ và viết lại toàn bộ slide cùng ghi chú theo MMDS 3e Chương 3, §§3.1–3.3, văn phong tiếng Việt học thuật và hệ ký hiệu thống nhất. Không kế thừa các tuyên bố hoàn tất hoặc kết quả kiểm thử trong nhật ký cũ.

## Điều phối và quyền ghi

| Tác tử | Vai trò và sản phẩm | Cấu hình được chỉ định trong lời gọi công cụ | Trạng thái |
|---|---|---|---|
| `/root` | Chấp nhận nguồn, kế hoạch, bản đồ chủ đề; tính lại số và chốt sai khác | Điều phối viên phiên gốc | Đã chấp nhận hồ sơ trước giai đoạn soạn |
| `/root/lec05_plan` | Lập kế hoạch độc lập; `/tmp/lec05-rebuild/planner.md` | `model: gpt-6-astra`, `reasoning_effort: xhigh`, `fork_turns: none` | Đã nộp; được điều phối viên chấp nhận |
| `/root/lec05_sources` | Phân tích nguồn, toán học, bản đồ chủ đề độc lập; `source-dossier.md` | Cùng cấu hình được chỉ định ở trên | Đã nộp; được điều phối viên chấp nhận |
| `/root/lec05_external` | Đối chiếu slide đại học; `external-dossier.md` | Cùng cấu hình được chỉ định ở trên | Đã nộp; được điều phối viên chấp nhận |
| `/root/lec05_storyboard_gate` | Chuẩn bị tiêu chí và kiểm định storyboard chỉ đọc | Cùng cấu hình được chỉ định ở trên | Đã có báo cáo sửa G01–G06 và `storyboard-plan-recheck.md`: PASS kế hoạch, được điều phối viên chấp nhận |
| `/root/lec05_writer` | Soạn ba tệp planning mới và triển khai bản nháp sau phê duyệt | Cùng cấu hình được chỉ định ở trên | Đã sửa G01–G06, nhận quyền giai đoạn 2 và bàn giao bản nháp để kiểm định độc lập |

Bảng ghi cấu hình được chỉ định do điều phối viên xác nhận từ lời gọi công cụ, không khẳng định mô hình thực thi phía sau nếu công cụ không cung cấp bằng chứng. Không dùng OpenRouter, `.env`, API hoặc CLI gọi mô hình. Chỉ một tác tử writer được ghi repo trong giai đoạn này. Giai đoạn 1 chỉ sửa ba tệp planning. Sau khi root chấp nhận cửa kiểm kế hoạch, quyền giai đoạn 2 gồm HTML Bài 05, ghi chú, SVG, ba tệp planning, CSS scoped `.lecture-minhash` và mục Bài 5 của index. Không commit hoặc push trong lượt writer.

## Nguồn và quyết định trước khi soạn

Đã đọc `sources/source.md` trước học liệu chi tiết: Bài 05 theo thứ tự đề xuất, nguồn từ buổi gốc 3 và một phần buổi 12. Đã đối chiếu dòng Bài 05 trong `sources/reference-slides/README.md`, tiêu chuẩn biên soạn, template, lớp chung của CSS và Lecture 02. Skill outline của kho cùng hai tài liệu tham chiếu được dùng cho tám phân tích. Mặc định năm 3 của skill được thay bằng đối tượng năm 2 theo chỉ dẫn học phần.

Tác tử nguồn đã mở sách và kiểm kê cả ba bộ slide cục bộ được ánh xạ. Tác tử đối chiếu đã đọc nguồn Stanford, CMU và UMass; các trang xem trực tiếp và giới hạn truy cập được ghi trong hồ sơ riêng. Writer đọc các hồ sơ đã được duyệt, planner và các trang sách liên quan; không tự nhận đã xem tất cả ảnh do tác tử khác xem.

| Nội dung | Bằng chứng | Quyết định trước writer |
|---|---|---|
| Sườn sách | B §§3.1–3.3, tr. 73–91 | Giữ Jaccard → shingling → ma trận → MinHash → chữ ký → tính chữ ký; bỏ khuôn dàn bài cũ |
| So sánh MMDS/Stanford | Bảng cụm trong source/external dossiers | Ưu tiên sách và MMDS khi tương đương; dùng cảnh báo giá trị/hạng ở ST03 tr. 28 |
| Bố cục đại học | ST03 tr. 27, 28, 32, 33; CMU tr. 14, 16, 19, 20; UMass tr. 6–8; MMDS tr. 35 đã được tác tử đối chiếu xem | Giữ dữ kiện và trạng thái đồng thời; không sao chép raster, CSS, ma trận 7 hàng hoặc mũi tên chéo dày |
| Truy cập MMDS | Trang chủ HTTP/HTTPS timeout; PDF chính thức cục bộ đầy đủ | Ghi giới hạn truy cập, tiếp tục dùng nguồn cục bộ; ghi công bằng liên kết `http://www.mmds.org` |
| Topic map | Hai đề xuất độc lập nguồn/planner và quyết định điều phối | Hợp nhất thành n05-01…n05-14; bảng chi tiết ở outline mục 8 |
| Bổ sung | Phương sai, bất biến, mô hình chi phí | Thêm để khép căn cứ chất lượng, tính đúng và chi phí; suy ra được ghi rõ, không gán như trích sách |
| Đọc thêm | Đa tập, từ dừng, §§3.3.6–3.3.7 | Chỉ trong ghi chú với giả thiết; không là tiên quyết tuyến chính |
| Ranh giới | LSH từ §3.4 trở đi; ANN thuộc Bài 07 | Chỉ nêu nhu cầu ứng viên ở kết luận; không dạy banding ở Bài 05 |

## Sai khác có chủ ý và hiệu chỉnh nguồn

| Vị trí | Vấn đề hoặc nhu cầu | Quyết định và tác động |
|---|---|---|
| Toàn bài | Ký hiệu sách có thể dùng cùng tên cho độ dài shingle, hàng hoặc hai loại hàm | Khóa $\ell,k,R,C,n,L$, $h_\pi$ nhận tập, $f_i$ nhận mã hàng; SIM là giá trị thật, ước lượng có dấu mũ; tác động toàn HTML/notes/SVG/bài tập khi triển khai |
| Trang 12 | Lát cắt có thể bị hiểu theo cú pháp ngôn ngữ chưa học | Ghi chỉ số bắt đầu từ 0 và đoạn gồm i,…,i+k−1; đầu phải không được lấy |
| Trang 24–26 | Định lý có thể bị dùng cho tập rỗng hoặc các thứ tự riêng | Nêu tập không rỗng, U hữu hạn, cùng hoán vị và chọn đều; chứng minh đủ hai chiều |
| Trang 28–29 | Định nghĩa chữ ký tổng quát xuất hiện trước ví dụ sẽ tăng mức trừu tượng | Đưa hai thứ tự suy từ Ví dụ 3.8 lên trang 28; trang 29 mới định nghĩa vector và ma trận. Cả hai thứ tự cố định, không gọi là mẫu ngẫu nhiên |
| B tr. 84; trang 31 | Sách ghi kỳ vọng “số hàng trùng” bằng Jaccard | Sửa số đếm thành ns; kỳ vọng tỷ lệ là s. Đã xác nhận trên hình trang sách, không phải lỗi trích xuất |
| Trang 32 | “Tăng n tốt hơn” thiếu đại lượng và điều kiện | Suy ra Var=s(1−s)/n dưới các hoán vị đều độc lập; không bảo đảm mọi lần chạy gần hơn |
| B tr. 85; trang 45 | Câu “chỉ có thể vì 5 nguyên tố” quá mạnh | Dùng điều kiện hệ số khả nghịch modulo R; ví dụ modulo 6 ở bài tập cho trường hợp không nguyên tố. Song ánh không được đồng nhất với chọn đều mọi hoán vị |
| Trang 41–44 | Cận thời gian có thể bỏ khởi tạo hoặc duyệt ô0 | Đếm nC,nR,RC,nL trước cận; đặc/thưa tách riêng; bộ nhớ đầu ra/đệm/đầu vào tách riêng |
| Trang 44 | n<R không chứng minh tiết kiệm byte | Phân biệt ma trận bit với từ máy; ví dụ nhỏ để theo cơ chế, quy mô byte lấy từ B tr. 81 |
| Trang 46 | Kiểm tra chưa đo phép đếm vừa học | Thêm nhiệm vụ nL=18 bằng dữ liệu Hình 3.4; giữ ba nhóm yêu cầu, không sửa recitation |
| Bài 3.2.3 | n trong đề xung đột độ dài chữ ký | Đổi n→ℓ, giữ đơn vị byte và giả thiết bảng chữ cái; không thêm dãy de Bruijn |
| Bài 3.3.2–3.3.3 | h_i của nguồn có hai kiểu dùng | Đổi tên thành f_i cho băm hàng; giữ mọi hệ số, modulo, ma trận và yêu cầu |
| Bài 3.3.1, 3.3.3 | Dữ liệu và nhiệm vụ nhiều | Tách mỗi bài thành hai trang; giữ tổng 15 phút cho từng bài, không nhân đôi thời lượng |

## Kiểm số và đặc tả ở giai đoạn planning

Bằng chứng tính độc lập đã được điều phối viên chấp nhận: `/tmp/lec05-rebuild/root-math-check.json` và `recomputed.json` của tác tử nguồn. Writer đối chiếu các giá trị vào phiếu slide; chưa tuyên bố phần hiển thị đã đạt.

| Phạm vi | Bằng chứng số/đặc tả | Kết quả và cách dùng |
|---|---|---|
| Hình 3.2 | 9 ô1; sáu Jaccard 0,1/4,2/3, 0, 1/3,1/5 | Giữ cùng dữ kiện xuyên bài, kiểm số bằng tập hợp |
| Vét cạn hoán vị | 120 hoán vị; số trùng 0, 30, 80,0, 40, 24 | Đáp án 3.3.1 khớp; phép kiểm không thay chứng minh |
| Hai thứ tự trang 28 | (e,a,b,c,d),(d,a,c,e,b) | Hai hàng định danh (a,c,e,a),(d,c,d,d); cặp 1–4 trùng 2/2 nhưng thật 2/3 |
| Ví dụ 3.8 | Năm trạng thái sau hàng 0–4 | Kết quả f1:(1, 3, 0, 1), f2:(0, 2, 0, 0); các trang 38–40 không bỏ bước quyết định |
| Chi phí ví dụ | R=5,C=4,n=2,L=9 | 8 khởi tạo,10 tính băm,20 kiểm ô đặc,18 min; không đếm chỉ các ô giảm |
| Bài 3.3.2 | Hai bảng f3/f4 | Hàng chữ ký (0, 3, 0, 0),(3, 0, 1, 0); phần dư−1 modulo 5 là 4 |
| Bài 3.3.3 | Sáu hàng, ba hàm modulo 6 | Chữ ký (5, 1, 1, 1),(2, 2, 2, 2),(0, 1, 4, 0); chỉ f3 là hoán vị; sáu tỷ lệ/giá trị thật đã đối chiếu |
| Thời lượng/mã | Script cục bộ đếm bản đặc tả | 57 mã duy nhất; 57 phiếu có nội dung, notes, bố cục và lý do; 7 phần; tổng theo phần 18, 22, 22, 17, 31, 10, 60; giảng 120, bài tập 60 |

## Rà sáu nhóm tiêu chuẩn tại mốc planning

| Nhóm | Bằng chứng trong bản planning | Trạng thái hiện tại |
|---|---|---|
| Đối tượng/ngôn ngữ | Mục tiêu, tiên quyết năm 2; không thêm cơ sở dữ liệu/LSH như tiên quyết | Đã tự rà nội dung dự kiến |
| Mục đích/mạch | Mỗi phiếu có vai trò, câu chốt, vào–ra; chu trình cụm và 7 phần; sáu nhiệm vụ cuối bài | Đã tự rà; chờ cửa kiểm độc lập |
| Thuật toán | Tạo shingle 13; quét 35–46 có đặc tả, vết, giả mã, bất biến, dừng, biên, chi phí | Đủ đặc tả dự kiến; chờ reader toán và bản dựng |
| Ví dụ | Dữ kiện sách; bảng vai trò VD1–VD9; trạng thái tĩnh, phép min đầu đủ | Đã đối chiếu số; chưa kiểm SVG/HTML |
| Chi phí | Mô hình trước bảng; đếm nC,nR,RC,nL; bộ nhớ từ và ví dụ byte tách | Đã tự rà; chưa kiểm khả năng đọc trang 43 |
| Trực quan | Mỗi trang có vùng/tỷ lệ, trọng tâm, thứ tự đọc, lý do năm 2 và phương án quá tải | Đã chốt đặc tả; chưa render, chưa đánh giá kích thước thật |

`gate-preflight.md` là tiêu chí chuẩn bị. Báo cáo độc lập `storyboard-plan-review.md` đã yêu cầu sửa G01–G06 trước triển khai; điều phối viên chấp nhận cả sáu điểm. Writer đã sửa theo bảng dưới và chờ cửa kiểm tái kiểm. Chỉ sau chấp nhận mới được viết HTML, ghi chú và SVG. Năm báo cáo sau bản nháp chưa có, vì bản nháp sản phẩm công khai chưa được dựng.

## No-ai-slop Edit và Quill

Writer đã đọc `no-ai-slop/SKILL.md` và `eval.md`, dùng chế độ Edit trên tiêu đề, câu chốt, nội dung công khai dự kiến, notes và đáp án. Văn phong học thuật của học phần ưu tiên hơn gợi ý giữ giọng nói. Đã tự đối chiếu các nhóm eval và sửa trước bàn giao:

| Nhóm eval | Bằng chứng chỉnh sửa/giữ | Kết quả trong phạm vi planning |
|---|---|---|
| Bảo toàn nội dung và giọng học thuật | Giữ giả thiết, ký hiệu, dữ kiện cố định, kết luận có điều kiện; không thêm thống kê/tình huống ngoài nguồn | Đạt tự kiểm |
| Trực tiếp, cụ thể, không rỗng | Tiêu đề gọi khái niệm/thao tác; câu chốt gắn dữ liệu hoặc điều kiện; bỏ lời bình về độ “kỳ diệu” trong nguồn | Đạt tự kiểm |
| Không đối lập kịch tính, câu hỏi tu từ hoặc ca ngợi | Không kế thừa “A Subtle Point”, “Implementation Trick”, “We achieved our goal!”; dùng quy ước giá trị, quét hàng, dung lượng | Đạt tự kiểm |
| Không chỉ dẫn biên soạn trong công khai | Các câu “hiển thị”, “vẽ lại”, “đặt bên…” được giữ ở trường bố cục; trường công khai dùng nội dung cụ thể | Đạt tự kiểm; vẫn cần rà bản dựng |
| Không đổi thuật ngữ để tránh lặp | Dùng nhất quán tập shingle, MinHash, chữ ký, Jaccard; tách hai kiểu hàm hπ và f_i | Đạt tự kiểm |
| Định dạng và dấu câu | Chuẩn hóa khoảng trắng giữa từ/số; bảng dùng để so dữ kiện, công thức không biến thành ảnh; sửa delimiter trị tuyệt đối trong bảng | Đạt tự kiểm |
| Đọc lại và bàn giao | Writer tự đọc bản đã xuất, kiểm eval; toàn văn sửa nằm trong ba tệp, thay đổi chính ghi ở bảng sai khác | Đạt trong giai đoạn planning |

Không dùng điểm bộ phát hiện AI hay suy đoán tác giả. Bảng trên là tự kiểm biên tập, không thay năm báo cáo độc lập.

Quill Outline/Revise được dùng để rà chủ đề, thứ tự, ký hiệu và nối phần, không tạo `quill.json`. Đầu bài đặt hai giới hạn; trang 33, 44,47–48 thu hồi chúng. Cặp S1,S4 đi từ giao/hợp tới hoán vị, chữ ký, kỳ vọng và kiểm tra. Đổi định danh sang giá trị băm có ánh xạ tại 37. Nhánh đọc thêm không cung cấp tiên quyết bắt buộc cho recitation. Ghi chú có chu trình riêng định nghĩa trước ví dụ, được khóa bằng note-topic-id trong outline và storyboard.

## Các bước còn lại được ghi tại mốc trước tái kiểm

- Tái kiểm độc lập G01–G06 và các vùng ảnh hưởng; điều phối viên chốt trước khi triển khai.
- Dựng HTML, ghi chú độc lập, SVG và lớp bố cục cần thiết; cập nhật index sau kiểm định ghi chú.
- Năm báo cáo độc lập: sinh viên; chuyên gia; toán/thuật toán; phản biện học thuật; kết nối/mạch viết.
- Chỉnh sửa riêng, rà lại toán/mạch theo phạm vi, kiểm mọi trang RevealJS ở khung rộng/hẹp, công thức, ghi chú, đường dẫn, SVG, bàn phím và tài nguyên cục bộ.
- Kiểm viewer ghi chú rộng/hẹp/in, khối gập và bàn phím; hồi quy Lecture 02/03 nếu CSS chung thay đổi.
- Rà Codex Slides theo khả năng công cụ thực tế; không gọi chức năng sinh mô hình. Giới hạn Browser/Codex Slides sẽ được ghi theo kết quả kiểm thật.
- Kiểm diff, commit đúng phạm vi và push origin main sau mọi cửa kiểm. Giữ nguyên thay đổi ngoài phạm vi của người dùng.

Bản này không tuyên bố sản phẩm công khai hoàn tất, không tuyên bố render đạt và không kế thừa trạng thái commit/push của phiên trước.

Kiểm cuối giai đoạn 1: script đọc bản Markdown xuất ra xác nhận 57 heading trang, 57 mã duy nhất, 57 thời lượng, 57 khối notes, 57 đặc tả bố cục và 57 lý do sư phạm; tổng giảng 120 phút, recitation 60 phút. Đã quét trường công khai/notes: không còn câu hướng dẫn dựng thuộc mẫu “hiển thị”, “vẽ lại”, “người soạn”, “chúng ta”. Không có delimiter công thức kiểu ngoài `$...$`/`$$...$$`. `git diff --check` được chạy sau khi bỏ khoảng trắng cuối dòng. Writer dừng ở ba tệp planning để chờ cửa kiểm.


## Sửa theo báo cáo cửa kiểm G01–G06

Điều phối viên đã đọc và chấp nhận sáu đề xuất trong `/tmp/lec05-rebuild/storyboard-plan-review.md`. Writer sửa cục bộ trên Markdown chuẩn, không chạy lại script sinh bản nháp. Trạng thái của cả sáu mục là **đã sửa, chờ cửa kiểm tái kiểm**; chưa có kết luận đạt độc lập hoặc phê duyệt triển khai HTML.

| Mã, mức độ | Bằng chứng trước sửa | Quyết định đã thực hiện | Phạm vi writer đọc lại |
|---|---|---|---|
| G01, trung bình | Trang 17 suy từ 5 shingle sang 5 mã mà chưa nói điều kiện va chạm; mâu thuẫn nguy cơ vừa nêu ở 16 | Thêm “nếu không xảy ra va chạm” trên mặt, nhãn bảng, thứ tự đọc và notes; phân biệt số mã với số shingle, không gán dữ liệu băm mới | 15–19: khoảng trắng → mã có va chạm → giới hạn số mã → kiểm tra → nhu cầu bộ nhớ |
| G02, trung bình | Trang 28 còn phương án dùng liên kết thay dữ kiện bốn tập | Chốt bốn tập trên mặt; bảng hai thứ tự cố định và bốn cột kết quả; phép so sánh cặp 1–4 ở cuối. Bỏ phương án thay dữ kiện bằng liên kết hoặc ma trận nhỏ | 26–30: định lý → một phép thử → hai phép chọn trên cùng tập → vector → tỷ lệ tọa độ trùng |
| G03, nghiêm trọng | Trang 36 thiếu miền i, miền giá trị có thứ tự và hậu điều kiện cho cột rỗng | Định nghĩa $i=1,\ldots,n$, $f_i:\{0,\ldots,R-1\}\to V$, $V$ hữu hạn có thứ tự toàn phần; min trên tập giá trị hợp $\{+\infty\}$. Cột rỗng trả $+\infty$ ngay trên mặt. Đồng bộ bảng ký hiệu, HT8 và notes 42; công thức dùng vùng rộng toàn trang | 34–38 và 40–44: lý tưởng → đặc tả → giá trị cụ thể → vòng lặp → bất biến → thời gian/bộ nhớ; không đổi vết chạy |
| G04, trung bình | Trang 43 dùng nnz trước khi giải nghĩa công khai | Viết $L=\operatorname{nnz}(M)$ là tổng số ô 1; giữ đầu vào đã có, mô hình O(1), bốn phép đếm và điều kiện danh sách cột theo hàng đã xây sẵn | 41–46: vòng lặp cung cấp ô 1; 43 đặt tên L; 46 dùng lại nL=18 |
| G05, trung bình | Notes 52 có câu “Không yêu cầu xây dãy de Bruijn”; notes 55 có câu “Không thêm nhiệm vụ tính ước lượng sau bổ sung” | Bỏ hai câu khỏi notes và đặt vào trường chỉ dẫn nội bộ của đúng bài. Giữ giả thiết Bài 3.2.3 là ít nhất ℓ **chuỗi** độ dài k, không tăng thành ℓ ký tự | 50–57: notes chỉ giữ dữ kiện, phép suy luận, lời giải, nguồn và thời lượng; yêu cầu toán học nguồn không đổi |
| G06, nhẹ | Trang 49–57 gắn mục tiêu rộng; Hình 3.4 bị dẫn tr. 86; một số từ/số dính nhau | Gắn mục tiêu cụ thể cho từng phiếu và bảng MT; đồng bộ trang 46 với MT4,MT5 đã nêu trong nhiệm vụ. Dẫn Hình 3.4 tr. 85, Ví dụ 3.8 tr. 85–86 ở các nơi liên quan. Sửa “ở 120/q”, “là (…)”, “khớp ý” và khoảng trắng trong danh sách số | 49–57, bảng MT, nguồn 37/40/55; không đổi dữ kiện hoặc thời lượng |

No-ai-slop Edit/eval được áp dụng lại vào các đoạn thay đổi. Hai câu G05 chứng minh lượt quét mẫu từ ban đầu chưa đủ phát hiện mọi chỉ dẫn biên soạn; kết quả tự kiểm ban đầu không được dùng để bác báo cáo độc lập. Writer đã chuyển đúng các câu sang trường nội bộ và đọc lại notes 50–57. Quill được dùng để đối chiếu các kết nối vào–ra trong phạm vi ở bảng; không khởi tạo `quill.json`.

Kiểm cấu trúc sau sửa: giữ 57 mã trang duy nhất, 7 phần, 50 trang giảng/120 phút và 7 trang bài tập/60 phút. Chưa dựng hoặc kiểm HTML/SVG, chưa có năm báo cáo bản nháp. Writer dừng sau ba tệp planning và chờ kết quả cửa kiểm tái kiểm.


## Chấp nhận cửa kiểm kế hoạch và quyền triển khai

Điều phối viên đã đọc và chấp nhận toàn bộ `/tmp/lec05-rebuild/storyboard-plan-recheck.md`. Kết luận độc lập **PASS** áp dụng cho kế hoạch sau G01–G06: 57 phiếu, 7 phần và thời lượng 120 + 60 phút. Cả sáu mục được tái kiểm trên các vùng 15–19, 26–30, 34–38, 40–46, 49–57. Trạng thái “chờ tái kiểm” ở bảng sửa trước đó là mốc lịch sử, đã được thay bằng kết quả này.

Root giao giai đoạn 2 theo `/tmp/lec05-rebuild/implementation-brief.md`. Writer đọc trực tiếp ba Markdown cuối cùng, không chạy lại script hoặc JSON planning cũ để ghi đè. Kết quả PASS của kế hoạch không được dùng làm kết quả cửa kiểm sản phẩm thực.

## Bản nháp công khai giai đoạn 2

| Thành phần | Nội dung đã triển khai | Trạng thái bàn giao |
|---|---|---|
| HTML | Viết lại 57 trang; 7 section ngoài với [9, 9, 9, 7, 12, 4, 7] trang; 57 `id` trùng `data-slide-id`; 57 notes học thuật; giữ thư viện cục bộ, cấu hình và footer | Đủ bản nháp; chờ kiểm định bản thực |
| Ghi chú | 14 chủ đề theo n05-01…n05-14; định nghĩa trước ví dụ, chứng minh đầy đủ, vết quét, chi phí, hai nhánh đọc thêm, năm bài sách và lời giải | Đủ bản nháp độc lập; chờ viewer và năm báo cáo |
| SVG | 8 tệp XML tự viết: hai tài liệu, ba vùng Jaccard, cửa sổ, thứ tự MinHash, hai thừa số công việc, các loại hàng, quét theo hàng và quy trình biểu diễn | Có role, title, desc, alt trong nơi dùng; không dùng raster |
| CSS | Chỉ thêm các selector bắt đầu bằng `.reveal.lecture-minhash`; điều chỉnh lưới, vùng hình, độ rộng và ngắt dòng của nhãn bảng | Dùng nguyên thang chữ, bảng, mã, công thức và nguồn của thành phần chung; cần hồi quy 02/03 theo quy trình |
| Index | Cập nhật mô tả Bài 5, giữ liên kết deck và đổi tài nguyên ghi chú thành “Đang kiểm định” | Chưa công bố liên kết ghi chú; root khôi phục sau kiểm viewer |

Không đổi số trang, thời lượng, dữ kiện bài tập hoặc trình tự của sườn đã duyệt. Công thức trang 36 dùng miền chỉ số đã nêu ở đầu trang để rút phần lặp điều kiện hàng trong tập lấy min; vẫn có cùng hậu điều kiện và cột rỗng trên mặt. Ghi chú ghi đầy đủ miền hàng ngay trong công thức. Tài liệu tự học dùng các tiểu mục học thuật, không hiện mã quy trình.

Chỉnh nguồn trong lượt tự rà: thứ tự `b,e,a,d,c` thuộc **Ví dụ 3.7**, không phải Ví dụ 3.6; đã sửa nhãn nguồn và notes HTML trang 23, cùng hai chỗ trong ghi chú. Theo đối chiếu của root, Ví dụ 3.4 thuộc **tr. 78**, đã sửa nhãn nguồn và notes trang 15, ghi rõ trang trong tài liệu tự học. Storyboard đã ghi đúng hai nguồn. Dữ kiện và bố cục không đổi; ảnh cuối của trang 15 và 23 cần được cập nhật sau sửa nhãn.

## Tự kiểm bản nháp của writer

- Kiểm cấu trúc bằng `/tmp/lec05-rebuild/audit_static.py`: PASS; 57 trang, 57 notes, đúng phân bố section, không ID trùng, không style block/inline style, không fragment; tài nguyên lõi cục bộ và SVG đều tồn tại. Đây là kiểm cấu trúc, không phải cửa kiểm học thuật.
- Đối chiếu trực tiếp ba công thức trung tâm: xác suất bằng SIM với hai tập không rỗng và hoán vị đều dùng chung; kỳ vọng số trùng là ns còn tỷ lệ là s; phương sai chỉ được suy dưới độc lập.
- Tính lại bằng tập hợp và vét cạn 120 hoán vị: sáu Jaccard, sáu số đếm, hai hàng chữ ký Ví dụ 3.8, hai hàng bổ sung Bài 3.3.2, ma trận và sáu sai lệch Bài 3.3.3 đều khớp bản nháp. Kết quả lưu ở `/tmp/lec05-rebuild/writer-selfcheck.json`.
- Kiểm Markdown: 14 heading chủ đề; 18 khối exercise, 21 solution, 3 example và 2 proof; khối đóng đủ và không lồng nhau, chỉ delimiter công thức `$...$`/`$$...$$`, hình đúng đường dẫn, không mã nội bộ trong văn bản công khai.
- Kiểm 635 biểu thức của ghi chú bằng KaTeX cục bộ với `throwOnError: true`: không lỗi cú pháp. Kiểm không bật strict cho Unicode; một số dấu tiếng Việt trong `text` dùng ký tự dự phòng và cần đọc trên viewer. Đây không thay kiểm hiển thị công thức trong trang thật.
- `git diff --check` không phát hiện lỗi khoảng trắng tại lần tự kiểm cuối. Chưa commit hoặc push.

No-ai-slop **Edit** được áp dụng cho toàn bộ bản nháp: giữ ngôn ngữ học thuật, cắt lời dẫn và nhận định rỗng; không có chỉ dẫn người viết/giảng viên trong slide, SVG, notes hoặc ghi chú. Tự rà `eval.md`: bảo toàn giả thiết/thuật ngữ và dữ kiện nguồn; câu dẫn nêu đối tượng và phép suy luận; các đoạn phủ định chỉ giữ khi cần phân biệt toán học; không câu hỏi tu từ hoặc giọng quảng bá. Đã sửa lỗi nguồn 3.6/3.7 và khoảng trắng trong lớp công khai. Định dạng bảng dùng cho so sánh dữ kiện; công thức và giả mã vẫn là văn bản, không raster. Kết quả là tự kiểm biên tập, không thay báo cáo đọc độc lập.

Quill Outline/Revise được dùng để đối chiếu bản đồ 14 chủ đề, ký hiệu, đầu vào/đầu ra của từng phần và các dữ kiện nối xuyên bài. Ghi chú đặt định nghĩa trước ví dụ; slide giữ ví dụ trước hình thức hóa ở các cụm đã duyệt. Các phần đọc thêm chỉ nối sau giới hạn của tuyến chính, không cung cấp tiên quyết còn thiếu cho năm bài tập. Không tạo `quill.json` hoặc tệp dự án sách.

## Những bước còn lại sau bàn giao nháp

Writer dừng ghi để root thực hiện cửa kiểm storyboard trên sản phẩm thực và tổ chức đủ năm báo cáo độc lập, rồi giao editor riêng. Cần hoàn tất kiểm RevealJS/ghi chú diễn giả, mọi SVG, viewer ở màn hình rộng/hẹp/in, khối gập, bàn phím, liên kết và hồi quy CSS; chỉ công bố liên kết ghi chú sau đó.

Root đã thông báo kiểm hiển thị sơ bộ HTML ở 57 trang × hai kích thước không có lỗi JS/HTTP/KaTeX, ảnh hỏng hoặc tràn, và kiểm SVG không có nhãn vượt viewBox. Đây là kết quả sơ bộ do root báo, chưa phải xác nhận đạt cuối của writer. Root cũng phát hiện phím S mở Speaker View làm main deck lùi một trang; lỗi phối hợp hash một-based/receiver đang được root giữ cho bước editor, chưa sửa trong lượt writer. Các phát hiện biên tập và hiển thị khác sẽ được hợp nhất sau đủ báo cáo.

Trạng thái bàn giao: **bản nháp đầy đủ, sẵn sàng kiểm định độc lập**. Chưa qua cửa kiểm bản thực, chưa có năm báo cáo được chấp nhận, chưa công bố ghi chú, chưa commit/push.

Bổ sung đối chiếu trước bàn giao: storyboard có bảng “Đối chiếu bố cục của bản nháp giai đoạn 2”, ghi rõ những bố trí thực tế khác phiếu đã duyệt. Các thay đổi không chỉ là tỷ lệ lưới: một số hình/bảng tham chiếu ở 21, 24, 29–30, 37 và trạng thái vào ở 39–40 chưa được lặp trên cùng mặt như dự kiến; các bài tập dùng mô tả sản phẩm thay bảng trống. Đây là các điểm cần gate đánh giá về tính tự đủ dữ kiện và tải ghi nhớ, không được che bằng kết quả không tràn. Bản nháp vẫn chứa dữ kiện trong cùng cụm và lời giải, nhưng chưa coi tương đương sư phạm là đã được xác nhận.


## Hợp nhất năm báo cáo độc lập và lượt editor riêng

Ngày 28-09-2026. Root xác nhận đã nhận, đọc và hợp nhất đủ năm báo cáo sau bản nháp công khai, báo cáo gate bản thực và quan sát kỹ thuật trước khi giao `/root/lec05_editor`. Editor khác writer ban đầu, là tác tử duy nhất được ghi kho trong lượt chỉnh sửa. Quyền được mở thêm `material-viewer.css` chỉ cho Bài 05 theo quyết định rõ của root; không sửa JavaScript viewer, vendor, deck khác hoặc thay đổi riêng của người dùng. Không commit/push trong lượt editor.

| Tác tử | Vai trò độc lập | Cấu hình được điều phối viên chỉ định | Phạm vi thật của báo cáo |
|---|---|---|---|
| `/root/lec05_student_review` | Góc nhìn sinh viên năm 2 | `gpt-6-astra`, `xhigh`, cơ chế tác tử gốc | 57 slide/57 notes, 14 chủ đề và lời giải, 8 SVG; 57 ảnh rộng qua contact sheets, 9 ảnh rộng riêng, 6 ảnh hẹp; tự thao tác viewer 390px, kiểm cuộn ảnh bằng bàn phím; 36 trang in qua contact sheets và 5 trang riêng. Không kiểm toàn bộ tương tác hay Codex Slides. |
| `/root/lec05_expert_review` | Chuyên gia giải thuật và khoa học dữ liệu | Cùng cấu hình được chỉ định | 57 slide/notes, 14 chủ đề, planning và 8 SVG; trực tiếp sách tr. 73–91 cùng nguồn slide liên quan; 57 ảnh rộng qua contact sheets, ảnh riêng 25/39/40; tự tính các kết quả. Không tự vận hành toàn bộ trình duyệt. |
| `/root/lec05_math_review` | Toán học và thuật toán | Cùng cấu hình được chỉ định | 57 slide/notes, toàn ghi chú, 8 SVG đã render; sách tr. 73–91, ảnh nguồn tr. 80, ba PDF slide; tính độc lập vết chạy, 120 hoán vị và bài tập. Không xác nhận hiển thị mọi slide, viewer hoặc bàn phím. |
| `/root/lec05_academic_review` | Phản biện học thuật và giảng dạy | Cùng cấu hình được chỉ định | 57 slide/notes, 14 chủ đề, nhãn 8 SVG; 57 ảnh rộng qua contact sheets, ảnh riêng 25/32/36/37/39/46 và hẹp 36; sách/slide liên quan; viewer và 36 trang in qua ảnh tổng hợp. Không kiểm tương tác. |
| `/root/lec05_flow_review` | Kết nối và mạch viết | Cùng cấu hình được chỉ định | 57 slide/notes, 14 chủ đề, ba planning files, nhãn 8 SVG; 57 ảnh rộng qua contact sheets và ảnh riêng 05/35/37/39/40; viewer/in qua ảnh; đọc mã dựng mục lục. Không tự vận hành viewer. |
| `/root/lec05_storyboard_gate` | Cửa kiểm storyboard trên bản thực, riêng với năm vai trên | Cùng cấu hình được chỉ định | Đối chiếu đủ 57 phiếu với bản HTML/notes/ghi chú và 8 SVG; ảnh rộng tổng hợp, ảnh riêng 11/30/39/40 và hẹp 36; tự tính các bảng. Kết luận trước editor: cần sửa IG01–IG09. |
| `/root/lec05_editor` | Chỉnh sửa riêng sau hợp nhất | Native `gpt-6-astra`, reasoning `xhigh` theo chỉ định trong brief của root | Đọc các quyết định, bảy báo cáo/quan sát được giao, quy định, nguồn/plan và sản phẩm; sửa cục bộ; tự kiểm hình/bảng thay đổi, dựng lại PDF in, đồng bộ planning. Không nhận thay các kiểm rộng và Codex Slides của root. |

Bảng chỉ ghi cấu hình được chỉ định trong quy trình mà root xác nhận; không khẳng định backend thực thi hay tuyến xác thực từ lời tự khai. Tất cả vai chỉ đọc áp dụng no-ai-slop Detect; editor áp dụng Edit và tự kiểm eval. Quill dùng cho mạch/thuật ngữ, không tạo `quill.json`. Không dùng OpenRouter, `.env` hoặc lời gọi mô hình API/CLI.

### Quyết định từng nhóm phát hiện

Bằng chứng nguyên báo cáo được lưu đầy đủ ở các phụ lục dưới đây để nhật ký không phụ thuộc các đường dẫn tạm. Mã trùng nhau được xử lý một lần trên sản phẩm và ánh xạ trong bảng này. “Đã sửa” là kết quả lượt editor, không thay kết luận tái kiểm độc lập hoặc phát hành của root.

| Mã và mức độ gốc | Vị trí, bằng chứng | Quyết định, kết quả cụ thể và phạm vi tác động |
|---|---|---|
| IG01 major; E02, AR-01, F02 trung bình | 37–40: thiếu incidence ở 37, trạng thái vào tại 39/40 và dấu ô đổi | Chấp nhận. Bảng37 có đủ phần tử/mã hàng, cột có1 và hai giá trị băm. Bảng39 giữ sau r0/r1/r2, bảng40 giữ sau r2/r3/r4; đầu vào từng hàng hiện trên mặt. Gạch dưới đúng từng giá trị vừa giảm; giữ các phép min không đổi cột4. Bảng38 đánh viền bốn ô hữu hạn đầu. Đồng bộ các phiếu và ghi chú9. |
| IG02 major | 30: tổng (1+1)/2 thiếu hai chữ ký đang so | Chấp nhận. Bảng hai tọa độ của chữ ký S1/S4 với a=a, d=d tạo hai chỉ báo1; kết quả1 đối chiếu2/3. Notes và phiếu30 có cùng dữ kiện. |
| IG03 minor | 23/24: ô1 đầu chưa đánh dấu, argmin chưa giải nghĩa và thiếu cặp a/3 | Chấp nhận. Bốn ô đầu viền/chữ đậm; trang24 giải nghĩa trả phần tử và đặt hπ(S1)=a, rankπ(a)=3. Bổ sung notes và phiếu, không đổi định nghĩa. |
| IG04 minor | 13/33: mô hình thời gian chỉ có trong ghi chú hoặc chưa nêu | Chấp nhận. Trang13 nêu tạo/băm/chèn khóa dài k tốn O(k) kỳ vọng, tổng O(1+wk) kể khởi tạo. Trang33 nêu từ máy và so bằng O(1) trước cận. Ghi chú3/7 đã có mô hình này, giữ nhất quán. |
| IG05 minor; SV05 nhẹ; R05 | 09,18,27,34,46,49–57 thiếu nhãn đúng quy ước | Chấp nhận. Thêm “Câu hỏi:” trước nhóm nhiệm vụ; ở recitation ghép cùng dòng yêu cầu để không tăng chiều cao vô ích. Không đưa đáp án lên mặt. |
| IG06 minor; M07, E03, AR-05, SV09 nhẹ; R03/R09 phần nguồn | Hình3.1 tr75; mua hàng §3.1.3; Ví dụ3.7 đã dùng định danh | Chấp nhận. Dẫn Hình3.1 tr75, cả văn bản/mua hàng dùng §§3.1.2–3.1.3; ghi chú khách hàng §3.1.3 tr76. Bỏ mô tả “ghi định danh thay hạng”, ghi bổ sung bảng định danh/vị trí. Xác minh R03 và số ví dụ R09 đã được writer sửa đúng: Ví dụ3.4 tr78; Ví dụ3.7 tr82–83. |
| IG07 minor; M01, AR-02, F03 trung bình; R01 | 39/40/46 và ghi chú9 đồng nhất tập/hàm với giá trị chữ ký | Chấp nhận. Tên S_c chỉ tập cố định; các câu cập nhật đều chỉ chữ ký của tập. Trang40 dùng f1(3),f2(3),f1(4),f2(4). Notes46 không còn S4=(1,1). Sau tái kiểm toán, sửa thêm đúng hai câu “Hàng3 hạ thành phần...” và “cung cấp(4,0)...” thành thành phần/ứng viên của chữ ký; đã thông báo root và đồng bộ phiếu40. |
| IG08 minor; SV02 nhẹ; R08 trung bình | Mũi tên cua-so-shingle.svg cắt chữ Cửa sổ | Chấp nhận. Dời nhãn sang vùng trống và đổi tuyến nối từ cửa sổ đầu vào ô ab; giữ sáu cửa sổ, chỉ số0–6 và hai ab. Xem lại ảnh11 thực xác nhận nét không cắt chữ. |
| IG09 minor | Ghi chú13: chưa nêu cách chọn phần đầu và miền m | Chấp nhận. Chọn đều một hoán vị của U, m nguyên và 1≤m<R; giữ bảng hữu hạn/vô cực và cảnh báo không tự áp phương sai s(1−s)/n cho mẫu số hữu ích ngẫu nhiên. Đồng bộ n05-13. |
| M02, SV03 trung bình | Bài3.2.3: byte trong đề nhưng định nghĩa dùng ký tự | Chấp nhận. Giữ nguyên đề; công khai quy ước tính mỗi ký tự một byte ở slide52, notes và lời giải. Nêu trong ghi chú rằng độ dài byte không tự bằng số ký tự nhiều byte. |
| M03, E01, SV01 trung bình; AR-04 nhẹ; R10 trung bình | SVG X/Y gán trùng/khác thiếu điều kiện đầu hợp | Chấp nhận. Điều kiện nhìn thấy “Xét loại của phần tử đầu tiên trong hợp”; Y ghi “thuộc đúng một tập”. Quan hệ X/Y/Z và dữ kiện a,d/c/b,e giữ nguyên. SVG dùng chung tự đồng bộ deck và ghi chú6. |
| M04, SV04 trung bình; E04 nhẹ | Ghi chú12 bỏ dấu chín vị trí từ dừng, không tính lại được | Chấp nhận. Đánh nghiêng đúng A,for,the,that,have,it,is,for,to theo PDF; liệt kê bảng chín cụm ba từ. Không bổ sung danh sách từ dừng ngoài sách. |
| M05 nhẹ; R14 nhẹ | Công thức đa tập chưa loại mẫu số0 và C trùng ký hiệu số tài liệu | Chấp nhận. Hai đa tập hữu hạn B1/B2, tổng bội dương; không định nghĩa tỷ số cho cả hai rỗng. Giữ hợp cộng của nguồn, tỷ số1/3 và tự so1/2. |
| M06 nhẹ | Đếm vị trí chỉ là cận trên, chưa chứng minh tồn tại chuỗi đạt cận | Chấp nhận quyết định root. Nhãn “Đáp số và cận trên”; giữ max(0,ℓ−k+1) và giả thiết ít nhấtℓ chuỗi dài k. Nêu rõ phác thảo không chứng minh phần đạt cận. Không áp dụng đề xuất mở một kiến tạo mới: de Bruijn ngoài phạm vi; không tăng giả thiết thànhℓ ký tự khác nhau. Đồng bộ notes52, lời giải, outline/storyboard. |
| AR-03 trung bình | 32: phương sai đúng nhưng thiếu bước cộng dưới độc lập | Chấp nhận. Chuỗi Var(tổng)/n² → tổng Var/n² có nhãn độc lập → s(1−s)/n. Chuyển SD sang notes, giữ một trọng tâm trên mặt. Không thêm định lý sai số. |
| F01 trung bình | Ranh giới4→5: (a,d) thành(1,0) chưa nối công khai | Chấp nhận. Trang35 nêu không va chạm và bảo toàn phép so bằng;37 có hai thứ tự tăng,40 có a↔0,d↔3 và (a,d)^T→(f1(0),f2(3))^T=(1,0)^T. Notes/ghi chú9 làm rõ cùng hàng thắng và phân biệt song ánh với chọn đều. |
| F04 nhẹ | 05: C xuất hiện trước định nghĩa | Chấp nhận. Thêm kho C tài liệu và cặp không thứ tự trước công thức. Không thay luận điểm hoặc tình huống mở bài. |
| F05, SV07 nhẹ | Mục lục viewer có hai bộ số cạnh nhau | Chấp nhận. CSS chỉ Bài05 bỏ list-style tự sinh, giữ số heading và thụt h3; không sửa JS hoặc thứ tự14 chủ đề. Root kiểm hồi quy viewer03/04. |
| SV06 nhẹ | In: heading3/10/11 và bài3.3.1 tách khỏi nội dung | Chấp nhận. CSS chỉ Bài05 tránh ngắt sau h2/h3/h4, giữ h3 cùng đoạn nguồn và khối tiếp theo. DựngPDF hai lượt, xem các trang5/21/23/32 và trích xuất đầu/cuối trang: tiêu đề được giữ cùng nội dung. Không thu nhỏ chữ; không tuyên bố đã in giấy. |
| SV08 nhẹ | Hình quy trình900px vượt vùng808px trên khung rộng | Chấp nhận. Riêng hình quy trình Bài05 co theo vùng nội dung từ viewport1200px trở lên; màn hình nhỏ hơn giữ cuộn ngang. Root yêu cầu nâng breakpoint từ900 lên1200 để không làm nhãn quá nhỏ ở bố cục hai cột. |
| R02/R07 nhẹ | 28: câu ngượng và σ trước định nghĩa29 | Chấp nhận. Câu “Hai thứ tự được chọn cố định để minh họa phép tính”; ghi chữ ký cụ thể bằng tên, giữ σ ở29. |
| R04 nhẹ | MMDS chưa được giải thích lần đầu | Chấp nhận. Tên sách đầy đủ kèm MMDS ở notes bìa, nguồn công khai đầu và đầu ghi chú. |
| R06 cần xem hình | 36: chevron sát chữ f_i | Chấp nhận theo ảnh. Dùng vùng an toàn28px hai bên tại36, giữ thang chữ. Áp dụng cùng lớp ở24 sau tự xem vì argmin cũng sát điều khiển; không đổi cấu hình controlsLayout. |
| R11 nhẹ | Đoạn nối đầu trong sơ đồ quét thiếu đầu mũi tên | Chấp nhận. Tách đường thành hai path có marker-end riêng; giữ hướng và vòng lặp. |
| R12/R13 nghiêm trọng | Speaker View đổi main index và thiếu CSS/font KaTeX | Chấp nhận giải pháp đã được root thử. HTML Bài05 dùng hashOneBasedIndex=true ở trình chiếu chính, false riêng receiver; listener cùng origin/namespace/connected/opener thêm link id lecture-katex-style và chia sẻ FontFace sau load. Không document.close, không sửa vendor. Root chạy lại Speaker View thực trên57trang. |

Không có đề xuất nào đòi thay sườn, tăng số phần hay đổi đề recitation. Những sai khác layout tại21,29,51–57 được gate/root chấp nhận vì vẫn đủ dữ kiện hoặc quan hệ vai trò; không tự phục hồi một bảng trống chỉ vì bố cục dự kiến ban đầu. Bảng phương sai32 được sửa theo AR-03 dù gate xem bản cũ là chấp nhận được: quyết định root ưu tiên bước suy luận hiện ngay trên mặt.

### Tự kiểm của editor và giới hạn

- Kiểm cấu trúc cuối bằng script hiện hành: PASS, 57 trang, 57 notes, bảy section phân bố9/9/9/7/12/4/7, đủ8SVG; giữ cùng ID và thời lượng120 + 60. `git diff --check` không báo lỗi khoảng trắng. Các phiếu bị sửa được đồng bộ công khai/notes/bố cục; không chạy script sinh planning cũ.
- Tự render19 trang thay đổi ở1280×720; sau hiệu chỉnh vùng an toàn và ngắt trang, render lại10/11/24/46. Tổng23ảnh,21trang riêng. Kiểm bounds/horizontal/footer/KaTeX trong hai lượt không báo lỗi. Ảnh ở thư mục tạm là bằng chứng bổ sung; kết luận cụ thể được ghi ở bảng quyết định, không chỉ dẫn đường dẫn.
- Đã xem nguyên cỡ trực tiếp các trang11,13,23,24,25,30,32,35,36,37,38,39,40,46,52,56. Dữ kiện, công thức, mũi tên và dấu ô ở các vùng sửa đọc được; không giảm font. Không tuyên bố editor xem lại toàn bộ57ảnh rộng/hẹp.
- Dựng lại PDF ghi chú hai lần bằng Chromium; trích xuất văn bản theo trang để kiểm đầu/cuối. Sau quy tắc h3+p, Bài3.3.1/3.3.2/3.3.3 đi cùng nguồn+đề. Xem trực tiếp trang in5,21,23,32: heading3, heading10 cùng proof, heading11, Bài3.3.1 cùng đề đều liền nội dung. Kiểm này trước hai sửa từ “chữ ký” cuối; root dựng lại bản cuối.
- Ghi chú viewer tiếp tục là bề mặt tự học trên điện thoại. Reveal390px co cả khung16:9; báo cáo sinh viên ghi chữ thân khoảng7–9px, không gọi là dễ đọc ở kích thước đó. Hình/công thức viewer có cuộn ngang khi cần.
- Editor không tự chạy lại toàn bộ kiểm bàn phím, invalid paths, Speaker View57trang, hồi quy02/03, viewer03/04 hoặc Codex Slides; root đang phụ trách sau mốc đóng public. Không nhận kết quả bản nháp là bằng chứng bản cuối.

No-ai-slop Edit/eval được tự kiểm sau sửa: bảo toàn nghĩa, giả thiết, nguồn và giọng học thuật; cắt đúng câu ngượng tại28; không đổi thuật ngữ theo lối xoay từ; giữ các phủ định có chức năng phân biệt kiểu/điều kiện; không thêm ca ngợi, lời dẫn rỗng, câu hỏi tu từ hoặc chỉ dẫn biên soạn vào học liệu. Các nhóm Editing principles, Words, Patterns và Final read đều đạt trong phạm vi chỉnh sửa. Bản sửa đầy đủ nằm trong sản phẩm, bảng trên nêu thay đổi; không dùng điểm phát hiện AI hoặc suy đoán tác giả.

Quill Outline/Revise kiểm mạch: trang28 định danh →29ký hiệu →30chỉ báo →31kỳ vọng →32phương sai với độc lập →33mô hình chi phí →35không va chạm/đổi cách lưu →37dữ liệu →38–40vết →41giả mã →42bất biến →43/44chi phí. Chuỗi này không đổi thứ tự hoặc mở/kết bài. Cặp S1/S4 và mãa↔0,d↔3 khép cầu nối; các nhánh12/13 giữ vị trí đọc thêm. C chỉ số tập/tài liệu; B1/B2 dành riêng đa tập. Phạm vi math tái kiểm gồm23–26,28–34,35–46, n05-09 đến14; flow gồm các trang sửa, hai trang lân cận và ranh giới4→5→6; gate kiểmIG01–IG09 cùng bố cục mới.

### Hồ sơ độc lập nguyên báo cáo

Các bản dưới đây là báo cáo tại mốc bản nháp, trước lượt editor. Mức độ, phạm vi xem ảnh và giới hạn được giữ để tránh chuyển một kết quả kiểm cục bộ thành chứng nhận toàn bộ. Quyết định xử lý hiện hành là bảng hợp nhất ở trên; các câu “cần sửa” trong báo cáo lưu trữ không có nghĩa editor chưa sửa.


### Bản lưu: Góc nhìn sinh viên

### Rà soát độc lập Bài 05 — góc nhìn sinh viên năm 2

Ngày rà: 28-09-2026. Tác tử: `lec05_student_review`. Bản được rà là bản nháp đã hoàn tất trước cửa kiểm triển khai. Chỉ đọc kho; báo cáo và ảnh kiểm tra riêng nằm trong `/tmp/lec05-rebuild/`. Không đọc báo cáo của reviewer khác hoặc `root-draft-observations`; không tạo tác tử, không dùng OpenRouter, `.env` hoặc API/CLI mô hình.

#### Kết luận theo vai trò

Không phát hiện lỗi **chặn bàn giao** hoặc **nghiêm trọng** trong phạm vi đã kiểm. Tuyến chính phù hợp sinh viên năm 2 có tiên quyết đã nêu; các ví dụ tính lại được, các bài nguồn đủ dữ kiện và có lời giải. Có **3 phát hiện trung bình** về điều kiện đọc hình, đơn vị trong bài tập và dữ kiện của ví dụ đọc thêm; **6 phát hiện nhẹ** về hình, nguồn và cách đọc học liệu. Các quyết định giữ hoặc sửa thuộc điều phối viên sau khi hợp nhất đủ báo cáo.

Báo cáo này không thay kết luận kiểm định kỹ thuật toàn bộ hay kiểm tra bằng Codex Slides. Thời lượng dưới đây là đánh giá trên kế hoạch và nhiệm vụ; chưa có buổi dạy thử với sinh viên.

#### Phạm vi đã đọc và quan sát

- Đọc brief, AGENTS.md, chuẩn biên soạn slide, mục tiêu/phạm vi Bài 05 trong `sources/source.md`, dòng 5 của `sources/reference-slides/README.md`.
- Đọc **toàn bộ 57 slide và toàn bộ 57 notes** trong `2627-1/lecture-05-bieu-dien-tuong-dong-shingling-va-minhash.html`; **toàn bộ 14 chủ đề** và các lời giải trong `2627-1/materials/lec-05/lecture-note.md`.
- Rà outline về mục tiêu, tiên quyết, ký hiệu, đồ thị khái niệm và 7 phần; đối chiếu bảng thời lượng, các phiếu trọng tâm và toàn bộ dữ liệu thời lượng 57 trang trong storyboard. Không coi trạng thái PASS của kế hoạch là bằng chứng bản triển khai đạt.
- Đọc trực tiếp sách PDF MMDS 3e Chương 3, trang in **73–91** qua trích xuất văn bản; xem ảnh trang in **80** để kiểm định dấu nghiêng chỉ từ dừng trong Ví dụ 3.5. Đối chiếu trực tiếp slide MMDS trang **14–39**, Stanford `03-lsh.pdf` trang **14–33**, Stanford `04-lsh_theory.pdf` trang **1–7**. Đây là phạm vi nội dung liên quan trực tiếp Bài 05; không tuyên bố đã rà hình của toàn bộ ba PDF nguồn.
- Xem đủ **57 ảnh wide** qua 10 contact sheets 2 cột × 3 hàng, mỗi slide 640 × 360: `contact-wide-01-06.png`, `07-12`, `13-18`, `19-24`, `25-30`, `31-36`, `37-42`, `43-48`, `49-54`, `55-57` trong `draft-renders/`.
- Xem ảnh wide riêng ở độ phân giải gốc cho các trang **20, 28, 36, 41, 42, 43, 45, 56, 57**. Xem ảnh narrow riêng cho **13, 20, 38, 43, 56, 57**. Không tuyên bố đã xem đủ 57 ảnh narrow.
- Xem đủ **8 ảnh render SVG** trong `svg/`: `cua-so-shingle`, `phan-tu-dau-hop`, `tai-lieu-gan-trung`, `quet-ma-tran-thua`, `quy-trinh-bieu-dien`, `minhash-hoan-vi`, `quy-mo-so-sanh-cap`, `jaccard-ba-vung`.
- Xem `note-1440-top.png`, `note-390-top.png`; xem **36 trang in** qua cả ba contact sheets trong `draft-materials/`, rồi xem riêng trang in **4, 20, 22, 29, 33**. Quan sát contact sheets kiểm bố cục/ngắt trang; việc đọc đầy đủ nội dung dựa trên Markdown, không dựa vào chữ nhỏ trong contact sheets.
- Tự mở Chromium cục bộ tại đúng máy chủ IPv6 `http://[::1]:8765/2627-1/`. Ở viewport 390 × 844, chụp và xem riêng phần đầu chủ đề **3, 8, 9, 10, 11, 14** cùng lời giải **3.3.3(a,b)**. Kiểm vùng cuộn ảnh Jaccard và quy trình bằng focus/ArrowRight; kiểm ảnh quy trình ở viewport 1440 × 900. Ảnh riêng: `/tmp/lec05-rebuild/student-qa/`. Các ảnh mang tên `note-narrow-topic-*.png` đã được chụp lại sau khi tắt cuộn mượt để đúng vị trí.

#### Phát hiện

##### SV01 — Thiếu điều kiện quyết định khi đọc hình phân loại hàng

- **Mức độ:** trung bình.
- **Vị trí:** `lec05-s03-07`; `img/lec-05/phan-tu-dau-hop.svg`; ghi chú chủ đề 6.
- **Vấn đề:** nhãn hình có thể bị đọc thành “có phần tử chung thì MinHash trùng”, trong khi kết luận chỉ đúng khi phần tử đang xét là phần tử đầu tiên của hợp theo hoán vị chung.
- **Bằng chứng:** hình đặt “X: thuộc cả hai”, `a, d`, “MinHash trùng” trong cùng hộp; hộp Y đặt `c`, “MinHash khác”. Trên hình không có nhãn “phần tử đầu trong hợp”. Mặt trang `s03-07` cũng chỉ có bảng X/Y/Z và số đếm; điều kiện nằm trong notes và trang trước/sau. Một sinh viên chép riêng hình phân loại mất điều kiện quyết định phép suy luận.
- **Đề xuất sửa:** thêm ngay trong hình hoặc chú thích sát hình câu “Xét phần tử đầu tiên trong hợp”; diễn đạt kết quả X/Y dưới điều kiện đó. Giữ nguyên phân hoạch và dữ liệu. Đây là bổ sung điều kiện đã có trong nguồn/notes, không thêm mệnh đề.

##### SV02 — Đường nối chồng lên nhãn cửa sổ

- **Mức độ:** nhẹ.
- **Vị trí:** `lec05-s02-01`, `lec05-s02-02`; `img/lec-05/cua-so-shingle.svg`; ghi chú chủ đề 3.
- **Vấn đề:** đường gấp khúc và đầu mũi tên đi qua chữ “Cửa sổ”.
- **Bằng chứng:** thấy trực tiếp trên `svg/cua-so-shingle.png` và contact sheet `07-12`; đoạn ngang đè phần trên chữ, đầu mũi tên nằm sát/đè vùng chữ bên trái. Nội dung sáu cửa sổ vẫn đúng nhưng nhãn khó đọc.
- **Đề xuất sửa:** dịch nhãn khỏi tuyến mũi tên hoặc thay tuyến nối để đường nối đi vào ô `ab` mà không cắt chữ. Giữ nguyên chuỗi, chỉ số và phép gộp hai cửa sổ `ab`.

##### SV03 — Chưa nối đơn vị byte của bài nguồn với định nghĩa shingle theo ký tự

- **Mức độ:** trung bình.
- **Vị trí:** `lec05-s07-02`; ghi chú mục 14, Bài 3.2.3; liên hệ định nghĩa ở `lec05-s02-03` và ghi chú mục 3.
- **Vấn đề:** phần giảng dùng độ dài ký tự, còn đề bài dùng độ dài byte; lời giải thay thẳng vào công thức số cửa sổ mà không nêu đơn vị phần tử đang xét.
- **Bằng chứng:** định nghĩa: “Một k-shingle là một đoạn gồm k ký tự liên tiếp.” Bài tập: “Một tài liệu dài ℓ byte.” Lời giải cho số cửa sổ `max(0,ℓ−k+1)`. Không có câu xác lập trong bài nguồn rằng một ký tự/đơn vị chuỗi đang tương ứng một byte. Sinh viên áp dụng cho văn bản mã hóa nhiều byte có thể dùng sai độ dài.
- **Đề xuất sửa:** giữ nguyên dữ kiện byte của MMDS 3.2.3 và thêm quy ước diễn giải theo mô hình byte/ký tự một byte của bài nguồn ngay trong notes và ghi chú, tốt nhất có một dòng ngắn trên đề. Nêu rõ công thức cần độ dài và k đo trên cùng đơn vị; không thay đề thành một bài mới về mã hóa.

##### SV04 — Thiếu dữ kiện để tự tái tạo chín shingle từ từ dừng

- **Mức độ:** trung bình.
- **Vị trí:** ghi chú mục 12, “Shingle bắt đầu bằng từ dừng”.
- **Vấn đề:** ví dụ cho kết quả chín shingle nhưng không giữ dấu nhận diện hoặc danh sách từ dừng của nguồn, nên không thể kiểm lại con số chỉ từ tài liệu công khai.
- **Bằng chứng:** ghi chú dẫn nguyên câu tiếng Anh, nêu ba shingle đầu, rồi viết “Theo cách chọn từ dừng trong ví dụ sách, câu có chín shingle”. Câu trích không đánh dấu từ dừng. Ảnh trực tiếp sách tr. 80 (`student-qa/book-p80.png`) đánh nghiêng các vị trí `A`, `for`, `the`, `that`, `have`, `it`, `is`, `for`, `to`; chính chín vị trí này quyết định chín cửa sổ. Ghi chú có câu yêu cầu quy tắc phải nhất quán, nhưng không cung cấp quy tắc của ví dụ đang tính.
- **Đề xuất sửa:** khôi phục dấu nghiêng ở đúng các từ của nguồn hoặc liệt kê rõ các vị trí/từ dừng được dùng trong ví dụ. Có thể bổ sung bảng chín cửa sổ nếu cần, nhưng chỉ đánh dấu đúng dữ kiện nguồn đã đủ để người học tự tính. Không thay bằng danh sách từ dừng khác.

##### SV05 — Nhãn nhiệm vụ kiểm tra chưa theo quy ước học phần

- **Mức độ:** nhẹ.
- **Vị trí:** `lec05-s01-09`, `s02-09`, `s03-09`, `s04-07`, `s05-12`, `s06-03`, `s06-04`.
- **Vấn đề:** các danh sách nhiệm vụ rõ nghĩa nhưng thiếu nhãn **“Câu hỏi:”** được chuẩn slide yêu cầu.
- **Bằng chứng:** chẳng hạn `s03-09` có danh sách “Tính Jaccard…”, “Xác định hai MinHash…”, “Tính xác suất…” dưới tiêu đề “Câu hỏi kiểm tra”; không có nhãn `Câu hỏi:`. Storyboard của cùng trang có nhãn này, HTML đã lược.
- **Đề xuất sửa:** thêm một nhãn chung trước nhóm nhiệm vụ, giữ nguyên danh sách và lời giải; không cần lặp nhãn ở từng ý.

##### SV06 — Một số tiêu đề bị tách khỏi nội dung ở bản in

- **Mức độ:** nhẹ.
- **Vị trí:** bản in ghi chú, trang **4, 20, 22, 29**; CSS in của viewer.
- **Vấn đề:** người học gặp tiêu đề cuối trang nhưng nội dung chỉ bắt đầu ở trang sau.
- **Bằng chứng:** tr. 4 kết bằng “3. Shingling: chuyển chuỗi thành tập”; tr. 20 có “10. Bất biến…” và “Chứng minh thuật toán tính đúng cực tiểu” nhưng toàn khối chứng minh ở trang sau; tr. 22 kết bằng tiêu đề mục 11; tr. 29 kết bằng tiêu đề Bài 3.3.1. Không mất chữ, nhưng nhịp đọc và định vị phần suy luận bị ngắt.
- **Đề xuất sửa:** giữ heading với khối nội dung đầu kế tiếp khi in bằng quy tắc tránh ngắt sau heading, rồi dựng lại để xác nhận với các khối `proof`/`solution`. Nếu chỉnh CSS dùng chung, phải kiểm các ghi chú khác bị ảnh hưởng; có thể giới hạn thay đổi vào Bài 05 nếu có cơ chế phù hợp.

##### SV07 — Mục lục viewer tạo hai hệ số thứ tự cạnh nhau

- **Mức độ:** nhẹ; thuộc hạ tầng dùng chung.
- **Vị trí:** viewer ghi chú, màn hình rộng và hẹp.
- **Vấn đề:** số tự sinh của danh sách mục lục xung đột với số chủ đề đã có trong heading; các tiểu mục được đánh số liên tục như mục lớn.
- **Bằng chứng:** ảnh `note-1440-top.png` có “1. 1. Tài liệu…”, “9. 4. Ma trận…”, “10. 5. MinHash…”. Có 47 liên kết trong một danh sách đánh số; trên viewport390, khối mục lục cao khoảng 1657 px và thân tài liệu bắt đầu ở tọa độ dọc khoảng2167 px. Cấu trúc vẫn có thụt lề cho h3, nhưng số mục sinh thêm gây nhiễu khi tìm mục 9 hay10.
- **Đề xuất sửa:** dùng hệ mục lục phản ánh cấu trúc h2/h3 và tránh số ngoài khi tiêu đề đã có số; có thể chỉ đổi cách đánh dấu danh sách. Không sửa hàng loạt nội dung heading của bài để chạy theo số mục lục. Đây là đề xuất hạ tầng, cần rà ảnh hưởng các bài khác nếu áp dụng.

##### SV08 — Hình quy trình vẫn phải cuộn ngang ở màn hình rộng

- **Mức độ:** nhẹ; không phải mất nội dung.
- **Vị trí:** viewer ghi chú mục14, `quy-trinh-bieu-dien.svg`; quy tắc `.markdown-body img[src^="img/lec-"]`.
- **Vấn đề:** phần kết quy trình bị khuất ở vị trí cuộn ban đầu ngay trên viewport1440, làm người đọc phải cuộn ngang để đọc hộp đầu ra.
- **Bằng chứng:** ảnh `student-qa/note-wide-quy-trinh-bieu-dien.png`; ảnh có chiều rộng900px trong vùng808px, hộp “Tỷ lệ trùng cùng tọa độ” bị che phần bên phải. Quy tắc `min-width:900px` áp dụng cho mọi hình bài giảng. Vùng này cuộn được; trên viewport390, focus vùng ảnh rồi ArrowRight tăng `scrollLeft` từ0 lên40px. Không có bằng chứng nội dung bị cắt mất vĩnh viễn.
- **Đề xuất sửa:** cân nhắc cho riêng hình Bài05 này co theo vùng nội dung ở khung rộng: 808/1100 ×28px cho nhãn khoảng20,6px, vẫn đọc được. Không ép hình này co xuống317px ở điện thoại vì nhãn khi đó chỉ khoảng8px; màn hình hẹp nên giữ cuộn hoặc có bố cục hình phù hợp. Không bỏ `min-width` toàn bộ các bài một cách máy móc.

##### SV09 — Một số chỉ dẫn vị trí nguồn chưa đúng nơi chứa đối tượng

- **Mức độ:** nhẹ.
- **Vị trí:** nguồn hình Jaccard ở `lec05-s01-06`, `s01-07`, `s01-09`, ghi chú mục2; nguồn ví dụ khách hàng ở `lec05-s01-08`, ghi chú mục2.
- **Vấn đề:** người học tra theo số hình/mục sẽ phải tự tìm thêm vì nhãn nguồn không chỉ đúng vị trí.
- **Bằng chứng:** sách tr.74 định nghĩa và nhắc Hình3.1, nhưng **hình thực nằm tr.75**; học liệu ghi “Hình3.1, tr.74”. Tình huống tập mặt hàng của khách hàng thuộc **§3.1.3, tr.76**, trong khi học liệu ghi §3.1.2. Đã kiểm trực tiếp văn bản các trang PDF2–6 của sách.
- **Đề xuất sửa:** khi dẫn hình ghi Hình3.1 tr.75, có thể giữ §3.1.1 tr.74 cho định nghĩa; đổi mục nguồn ví dụ khách hàng thành §3.1.3 tr.76. Đồng bộ SVG/mô tả và hồ sơ nếu những nơi ấy cũng chứa cùng vị trí sai.

#### Các phần đã đạt trong phạm vi sư phạm

##### Tiên quyết và mạch khái niệm

Theo cách rà khái niệm của Quill, đường đi là: tài liệu gần trùng → giao/hợp và Jaccard → tập shingle → ma trận → thứ tự chung → MinHash → biến cố trùng → chữ ký nhiều thành phần → thuật toán lấy cực tiểu → chi phí/giới hạn. Mỗi đầu ra được dùng ở phần kế tiếp. Không cần kiến thức cơ sở dữ liệu, hệ phân tán, LSH hoặc framework để làm bài tập.

Các phân biệt quan trọng đã được giữ: ký tự với byte mã; cửa sổ với phần tử tập; định danh với vị trí và giá trị băm; kỳ vọng số đếm với tỷ lệ; đều với độc lập; tính đúng phép min với bảo đảm xác suất. Bernoulli được nối từ biến chỉ báo 0/1; phần phương sai trong ghi chú có bước $X_i^2=X_i$ và cộng phương sai dưới độc lập. Điều kiện không rỗng của định lý và quy ước $+\infty$ của thuật toán được tách rõ.

Hai mục đọc thêm12–13 được đánh dấu, không là tiên quyết ngầm của recitation. Khối đọc thêm không đưa LSH/phân dải vào Bài05.

##### Chạy tay và lời giải

- Các cửa sổ `ab,bc,cd,da,ab,bd` cho năm phần tử; bảng trạng thái trong ghi chú giải thích rõ lần chèn không tăng kích thước.
- Ma trận5×4 được dùng xuyên suốt. Thứ tự `b,e,a,d,c` cho định danh `(a,c,b,a)` và vị trí `(3,5,1,3)`; bảng tách hai đại lượng tránh học vẹt tên “hàng”.
- Bảng quét theo hàng có trạng thái hữu hạn đầu tiên, bước min giữ nguyên, bước thay một thành phần và kết quả cuối. Giả mã và bất biến dùng cùng ký hiệu.
- Tự tính lại bằng Python với `Fraction` và liệt kê120 hoán vị: sáu Jaccard là `0,1/4,2/3,0,1/3,1/5`; số hoán vị trùng `0,30,80,0,40,24`. Hai hàng bổ sung Bài3.3.2 là `(0,3,0,0)` và `(3,0,1,0)`. Bài3.3.3 cho ma trận chữ ký `[(5,1,1,1),(2,2,2,2),(0,1,4,0)]`, sáu ước lượng/sai lệch khớp notes và ghi chú. Phương sai với $s=2/3,n=100$ là $1/450$.
- Đề Bài3.3.1–3.3.3 đều cung cấp lại ma trận; Bài3.3.3(c) kế thừa sản phẩm ý(a) ở trang liền trước, là phụ thuộc rõ. Không phải tìm một hình không có trong học liệu mới làm được.
- Mọi câu kiểm tra trong slide có đáp án hoặc hướng giải trong notes; bài tập công khai có lời giải gập trong ghi chú. Phần dư âm trong Bài3.3.2 được giải thích.

##### Tải nhận thức và nhịp120+60

Kiểm tổng của57 trường “Thời lượng” trong storyboard bằng script: **50 trang đầu =120 phút; 7 trang cuối =60 phút**. Phần giảng phân bố18/22/22/17/31/10 phút. Phần quét chữ ký được31 phút, có9 phút cho ba trang trạng thái và thời gian riêng cho giả mã, bất biến, chi phí; đây là phân bổ hợp lý cho thao tác mới. Các trang chứng minh hoặc phương sai được khoảng3 phút và có diễn giải tự học dài hơn.

Recitation có năm bài nguồn theo8/10/15/12/15 phút, tăng từ đếm giao/hợp đến truy vết, phân biệt hoán vị và đánh giá ước lượng. Không có nhiệm vụ lập trình hoặc công cụ chưa được chuẩn bị. Tổng thời gian không được tăng giả bằng cách cộng lại toàn bài sau khi tách thành hai slide.

##### Ngôn ngữ và no-ai-slop Detect

Đã đọc `no-ai-slop/SKILL.md` và `eval.md`; áp dụng Detect trên toàn bộ tiêu đề, nội dung hiển thị, notes và ghi chú. Không phát hiện đoạn đủ căn cứ để gắn nhãn các mẫu lời dẫn rỗng, phô trương, ca tụng hoặc suy đoán tác giả. Các câu đối chiếu về “số đếm/tỷ lệ”, “định danh/vị trí”, “thuật toán/giả thiết xác suất” có chức năng toán học nên được giữ. Mục tiêu, câu kiểm tra và tổng kết phục vụ đầu ra học tập, không coi là lời lặp cần cắt cơ học. SV05 là lỗi nhãn theo chuẩn riêng của học phần, không phải kết luận văn bản do AI viết.

#### Giới hạn và điều kiện khi hợp nhất

- Wide1280×720: trên toàn bộ contact sheets và chín ảnh chi tiết đã xem, không thấy mất công thức/bảng, tràn khung hoặc chữ thân quá dày làm không đọc được. SV02 là lỗi chồng nhãn cụ thể trong hình, không phải tràn bố cục HTML.
- Narrow390×844 của RevealJS: sáu trang đã xem co toàn bộ khung16:9 rất nhỏ; chữ thân/mã ở kích thước ảnh gốc khoảng7–9px, không thuận tiện để tự học mà không phóng lớn hoặc xoay màn hình. Không ghi nhận đây là một bản chữ lớn đọc thoải mái trên điện thoại. Đây là giới hạn của bề mặt trình chiếu chung; ghi chú viewer là bề mặt tự học dễ đọc hơn.
- Viewer390: đoạn văn, heading, bảng số nhỏ và lời giải3.3.3(a,b) đọc được; công thức dài và SVG dùng vùng cuộn ngang. Đã kiểm cuộn hai SVG bằng bàn phím, chưa kiểm mọi vùng cuộn và mọi tương tác chạm. Không đồng nhất “phải cuộn” với “mất nội dung”. Không đề nghị ép tất cả SVG về317px vì nhãn sẽ quá nhỏ.
- Bản in: xem đủ36 trang qua contact sheets và năm trang chi tiết; không thấy khối lời giải bị gập trong bản in, nhưng có tiêu đề mồ côi như SV06. Chưa in trên giấy.
- Chưa tự kiểm lại toàn bộ điều hướng bàn phím57slide, toàn bộ21khối lời giải, tất cả liên kết hay an toàn viewer; các việc ấy thuộc kiểm định kỹ thuật tổng hợp. Chưa dùng Codex Slides trong lượt độc lập này.
- Không sửa repo, CSS, HTML, Markdown, SVG hoặc nhật ký. Những phát hiện liên quan hạ tầng dùng chung cần được điều phối viên phân định phạm vi và kiểm ảnh hưởng trước khi sửa.


### Bản lưu: Chuyên gia giải thuật

### Rà độc lập chuyên gia giải thuật và khoa học dữ liệu — Bài 05

Ngày 28-09-2026. Vai trò: reviewer chỉ đọc sản phẩm; không sửa kho. Báo cáo này dựa trên bản nháp hoàn chỉnh được giao trong `review-brief.md`.

#### Kết luận

Tuyến chính đạt về phạm vi Bài 05, độ sâu giải thuật và tính đúng của các phép tính đã kiểm. Chưa phát hiện lỗi chặn bàn giao hoặc lỗi nghiêm trọng trong định lý MinHash, ước lượng, thuật toán quét hàng hay lời giải recitation. Có **hai phát hiện trung bình và hai nhóm phát hiện nhẹ** cần xử lý dưới đây. Hai phát hiện trung bình liên quan đến điều kiện của nhãn hình và dữ kiện cần thiết để tự tái tạo vết chạy trên mặt slide.

Không dùng kết quả kế hoạch đã PASS làm bằng chứng bản dựng đạt. Không mở báo cáo của gate, reviewer khác, `root-math-check.json`, `root observations` hoặc báo cáo tự kiểm writer. `review-log.md` được đọc như một sản phẩm quy trình theo nhiệm vụ; các đoạn trong đó thuật lại nhận xét của tác tử khác không được dùng làm căn cứ cho kết luận độc lập này.

#### Phạm vi thực sự đã kiểm

- Đọc toàn bộ HTML: 57 mặt slide và 57 khối notes; đối chiếu toàn bộ 14 mục chính của `materials/lec-05/lecture-note.md`, gồm hai mục đọc thêm và năm bài tập có lời giải.
- Đọc toàn bộ `outline.md` và `review-log.md`; kiểm bảng mạch, thời lượng, quyết định khác nguồn và các trường mục đích, câu chốt, vào–ra, nguồn, thời lượng, kiểm tra của cả 57 phiếu trong `storyboard.md`. Nội dung công khai/notes được kiểm từ bản HTML; không coi việc có một phiếu là bằng chứng đã triển khai đủ.
- Đọc mã XML của cả tám SVG và nhìn thấy cả tám hình trong các ảnh slide. Đọc phần CSS `.lecture-minhash` và mục Bài 5 trong `index.html`.
- Đọc yêu cầu học phần liên quan trong `AGENTS.md`, `sources/source.md`, dòng Bài 5–6 của `reference-slides/README.md`, cùng `slide_authoring_standard.md`. Đọc skill no-ai-slop và eval, dùng Detect; đọc Quill và workflow Outline/Revise, chỉ áp dụng kiểm tính liên tục, không tạo dự án sách.
- Đọc trực tiếp bản trích xuất theo trang của sách MMDS 3e Chương 3, tr. 73–91, bao gồm §§3.1–3.3 và các bài tập đã chọn. Mở ảnh trang in 80 để kiểm dấu nhận diện từ dừng trong Ví dụ 3.5.
- Mở ba PDF slide cục bộ bằng `pdftotext`, kiểm kê tiêu đề/nội dung đầu trang của 59 trang MMDS, 54 trang Stanford 03, 60 trang Stanford 04. Đọc nội dung đầy đủ các cụm liên quan: MMDS tr. 14–39, Stanford 03 tr. 14–33, Stanford 04 tr. 3–7. Không nhận đã xem bằng mắt toàn bộ 173 trang PDF nguồn.
- Quan sát bằng mắt 10 ảnh `contact-wide-*`, bao phủ cả 57 slide. Xem thêm ảnh riêng 1280 × 720 của trang 25 (`lec05-s03-07`), 39 (`lec05-s05-05`) và 40 (`lec05-s05-06`). Đây là ảnh render được giao, không phải một lượt tự vận hành trình duyệt.
- Quan sát mẫu viewer ở `note-1440-top.png`, `note-390-top.png` và ba contact sheet của 36 trang in. Chỉ kiểm bố cục tổng thể qua các contact sheet; không nhận đã đọc đủ mọi chữ nhỏ trong chúng hoặc đã thử bàn phím, liên kết, khối gập và Speaker View.
- Tự tính độc lập bằng Python: phân bố section, số notes, thời lượng từng phiếu; sáu Jaccard của Hình 3.2; số trùng trên toàn bộ 120 hoán vị; năm trạng thái Ví dụ 3.8; hai hàng bổ sung Bài 3.3.2; ma trận chữ ký, sáu Jaccard, sáu ước lượng và sai lệch Bài 3.3.3. Bằng chứng: `/tmp/lec05-rebuild/expert-qa/independent-checks.json`. Không dùng kết quả của tác tử khác để xác nhận số.

#### Phát hiện

##### E01 — Trung bình — Nhãn SVG bỏ mất điều kiện phần tử đứng đầu hợp

**Vị trí:** `lec05-s03-07` (trang 25); `img/lec-05/phan-tu-dau-hop.svg`, dòng 8–9; hình dùng lại trong ghi chú mục 6.

**Vấn đề:** Hình phân loại hàng gắn trực tiếp “MinHash trùng” vào hộp X và “MinHash khác” vào hộp Y. Mặt slide không có câu nào cho biết hai kết luận này chỉ đúng khi phần tử thuộc loại đang xét là **phần tử đầu tiên của hợp trong hoán vị**. Đây là điều kiện quyết định, không phải diễn giải phụ.

**Bằng chứng:** Ảnh `wide-25-lec05-s03-07.png` hiện đồng thời hộp `X: thuộc cả hai / a,d / MinHash trùng` và hộp `Y: thuộc một tập / c / MinHash khác`, nhưng không hiện thứ tự hoặc điều kiện đứng đầu. Notes và trang 26 phát biểu đúng điều kiện; title/desc của SVG cũng đúng nhưng không hiển thị như nhãn trên hình. Theo MMDS §3.3.3, tr. 83, cần xét hàng đầu tiên khác Z, rồi mới phân loại X/Y. Với chính $S_1,S_4$, sự có mặt của $c$ thuộc Y không tự làm hai MinHash khác; thứ tự ở trang 23 vẫn cho cả hai chọn $a$.

**Đề xuất:** Thêm câu hiển thị “Nếu là phần tử đầu tiên trong hợp” làm điều kiện chung cho hai hộp X/Y, hoặc đổi nhãn kết quả thành “Đứng đầu hợp → trùng” và “Đứng đầu hợp → khác”. Giữ Z là “Không được chọn”. Đồng bộ SVG dùng trong ghi chú; không cần thay chứng minh hay dữ kiện.

##### E02 — Trung bình — Vết chạy hàng 1–2 thiếu dữ kiện để tái tạo phép cập nhật ngay trên mặt slide

**Vị trí:** `lec05-s05-03` đến `lec05-s05-06`, trọng tâm `lec05-s05-05` (trang 39); HTML khoảng dòng 239–263.

**Vấn đề:** Trang 37 có bảng hàm băm nhưng chỉ dẫn bằng chữ “Dùng ma trận đặc trưng Hình 3.2”, không lặp ma trận hay danh sách cột chứa từng hàng. Trang 39 trình bày hai trạng thái **sau** hàng 1 và hàng 2, nhưng không cho các cột có 1 ở hai hàng này. Vì vậy sinh viên nhìn thấy kết quả mà phải nhớ dữ kiện cách nhiều slide để giải thích vì sao chỉ cột 3 nhận $(2,4)$ ở hàng 1, và vì sao cột 2,4 được xét ở hàng 2.

**Bằng chứng:** Trong `wide-39-lec05-s05-05.png`, nội dung ngoài hai bảng chỉ là “$S_4$ đang có $(1,1)$; hàng 2 cung cấp $(3,2)$” và hai phép min. Không có thông tin $r=1\to\{3\}$, $r=2\to\{2,4\}$. Các thông tin này có trong notes và ghi chú mục 9, nên kết quả toán học không sai; vấn đề là dữ kiện công khai phục vụ vết chạy. Ma trận đầy đủ ở trang 20/23 và các tập ở trang 28 đã nằm trước cụm triển khai. Trang 40 có dữ kiện các cột cần cập nhật tốt hơn, nhưng trạng thái trước hàng 3 chỉ nằm ở trang trước.

**Đề xuất:** Ở trang 37, dùng lại bảng dữ kiện Hình 3.4 với cột “Các cột có 1”, hoặc đưa danh sách hai hàng đang xử lý vào trang 39. Tối thiểu hiện rõ $r=1$: cột $3$, giá trị $(2,4)$; $r=2$: cột $2,4$, giá trị $(3,2)$. Đánh dấu các ô đổi và thêm trạng thái vào của thành phần đang giải thích khi cần. Giữ font chung; tách bước nếu thêm dữ kiện khiến trang quá tải. Không cần thay thuật toán hoặc số liệu.

##### E03 — Nhẹ — Một số chú dẫn không trỏ đúng mục/trang hoặc mô tả sai sự khác biệt với sách

**Vị trí và bằng chứng:**

1. `lec05-s01-06`, `lec05-s01-09` và notes đi kèm ghi “Hình 3.1, tr. 74”; ghi chú mục 2, dòng 50 cũng ghi như vậy. Ví dụ 3.1 được diễn giải ở tr. 74, nhưng **hình và chú thích Hình 3.1 nằm ở trang in 75**, PDF trang 4. Outline/storyboard đã dùng khoảng 74–75 chính xác hơn.
2. `lec05-s01-08` và notes dẫn “§3.1.2, tr. 74–76”; ghi chú mục 2, dòng 62 viết “Trong ví dụ khách hàng của §3.1.2”. Ví dụ tập mặt hàng đã mua thuộc **§3.1.3, On-Line Purchases, tr. 76**, không phải §3.1.2. Storyboard trang 08 đã ghi §§3.1.2–3.1.3.
3. `lec05-s03-05` và notes ghi “Ví dụ 3.7 …; ghi định danh thay hạng”. Sách tr. 82–83 vốn ghi $h(S_1)=a$, $h(S_2)=c$, $h(S_3)=b$, $h(S_4)=a$: đây đã là định danh. Việc đổi quy ước hạng liên quan đến slide Stanford 03, tr. 27–28, không phải một thay đổi của Ví dụ 3.7 trong sách.

**Đề xuất:** Dẫn Hình 3.1 ở tr. 75 hoặc “Ví dụ 3.1 và Hình 3.1, tr. 74–75”; đổi dẫn ví dụ khách hàng sang §3.1.3; bỏ cụm “ghi định danh thay hạng” sau nguồn sách hoặc thay bằng “bổ sung bảng đối chiếu định danh và hạng”. Không thay các phép tính đúng đang có.

##### E04 — Nhẹ — Ví dụ từ dừng mất dấu nhận diện cần để kiểm tra con số chín

**Vị trí:** ghi chú mục 12, “Shingle bắt đầu bằng từ dừng”, dòng 629–637.

**Vấn đề:** Ghi chú giữ câu nguồn, ba shingle đầu và kết luận “câu có chín shingle”, nhưng không nêu danh sách từ dừng của ví dụ hoặc đánh dấu các vị trí được chọn. Người đọc độc lập không thể tái tạo chín cửa sổ theo một quy tắc đã xác định.

**Bằng chứng:** Bản Markdown dòng 633 là trích dẫn thuần chữ; dòng 635 viện dẫn “Theo cách chọn từ dừng trong ví dụ sách”. Ảnh nguồn trang in 80 (`expert-qa/book-page80.png`) đánh dấu bằng chữ nghiêng các từ dừng và nói rõ tác dụng của dấu này. Nguồn xác định các vị trí bắt đầu là `A`, `for`, `the`, `that`, `have`, `it`, `is`, `for`, `to`; `for` xuất hiện hai lần. Dấu nhận diện ấy đã bị mất khi chuyển nguồn.

**Đề xuất:** Khôi phục dấu nhấn đúng chín vị trí trong câu nguồn và giải thích quy ước, hoặc ghi danh sách từ dừng dùng cho ví dụ là `{A, for, the, that, have, it, is, to}` với cả hai lần `for` đều được xét. Có thể thêm bảng chín shingle trong khối ví dụ; không thay câu tiếng Anh hoặc tự chọn lại tập từ dừng.

#### Đánh giá nội dung và quyết định phạm vi

| Trục kiểm | Kết quả độc lập |
|---|---|
| Bài 05 và ranh giới Bài 06 | Đúng số bài, chủ đề, nguồn §§3.1–3.3. Bắt đầu bằng tài liệu gần trùng, kết thúc bằng giới hạn số cặp. LSH chỉ xuất hiện như bước kế tiếp; không có banding, đường cong ngưỡng hay độ đo ngoài phạm vi chen vào tuyến chính. |
| Thứ tự theo sách | Jaccard → shingling → ma trận → MinHash → chữ ký → tính chữ ký được giữ. Đưa hai hoán vị suy từ Ví dụ 3.8 lên trước định nghĩa chữ ký có lý do sư phạm và công khai là ví dụ cố định. Không trộn ma trận 7 hàng của slide tham khảo với ma trận 5 hàng trong sách. |
| Bao phủ và chiều sâu | Đủ định nghĩa, kiểu/miền, ví dụ chạy tay, chứng minh xác suất hai chiều, bất biến khởi tạo–duy trì–kết thúc, trường hợp rỗng, thời gian và bộ nhớ. Ghi chú giải thích được độc lập, không chỉ chép mặt slide. E01/E02 là các điểm rút gọn trên mặt slide cần sửa. |
| Hai loại băm | Phân biệt băm shingle trên chuỗi con, $h_\pi$ trên tập và $f_i$ trên mã hàng. Có phân biệt định danh, hạng và giá trị băm; không gán bảo đảm hoán vị đều cho mọi họ hàm affine. |
| Chất lượng ước lượng | Kỳ vọng số đếm $ns$, tỷ lệ $s$; tính tuyến tính không đòi độc lập. Phương sai $s(1-s)/n$ có giả thiết độc lập, nêu rõ là hệ quả suy ra. Không coi chữ ký dài hơn luôn giảm sai số của một mẫu cụ thể. |
| Thuật toán và khả năng triển khai | Giao diện ma trận/danh sách theo hàng, miền $f_i$, giá trị canh và hậu điều kiện đầy đủ. Giả mã đủ khởi tạo/vòng lặp/dừng/trả kết quả. Từ đặc tả và ghi chú có thể triển khai bản quét; không hứa bảo đảm xác suất cho bộ hàm tùy ý. |
| Chi phí | Đếm riêng $nC,nR,RC,nL$ trước cận; phân biệt ma trận đặc và danh sách đã xây sẵn; số min không đồng nhất với số lần ô đổi. Bộ nhớ đầu ra/đệm/đầu vào tách rõ; không suy giảm byte từ riêng $n<R$. Không dùng phép đếm RAM như một cận I/O chưa có mô hình. |
| Bổ sung | Phương sai, bất biến, điều kiện $\gcd(a,R)=1$ và chi phí khép những lập luận còn thiếu; suy ra có thể kiểm trực tiếp từ đặc tả và tiên quyết. Việc sửa phát biểu kỳ vọng tr. 84 và câu “chỉ vì 5 nguyên tố” tr. 85 là đúng. Không cần tăng phạm vi sang Hoeffding hoặc một họ băm mới. |
| Lược/gộp | Đa tập, shingle từ dừng, §§3.3.6–3.3.7 đặt vào nhánh đọc thêm có ghi lý do; không cung cấp tiên quyết bắt buộc cho recitation. Phần nhóm hàng giữ ví dụ Hình 3.5 và tránh suy trung bình các tỷ số luôn bằng tỷ số toàn cục. Nội dung đọc thêm này là giải thích ý tưởng và giới hạn, không được coi là đặc tả đủ của một triển khai tăng tốc. |
| Recitation | Cả năm đề đối chiếu đúng sách: 3.1.1, 3.2.3, 3.3.1(a,b), 3.3.2(a,b), 3.3.3(a,b,c). Giữ hệ số, modulo, ma trận và yêu cầu. Đổi tên $n\to\ell$, $h_i\to f_i$ hợp lý. Bảng sai lệch tuyệt đối cụ thể hóa yêu cầu “how close” của 3.3.3(c), không tạo một bài mới. |
| Thời lượng | Tự đếm được 57 ID riêng, 57 notes, 7 mạch với số slide `[9,9,9,7,12,4,7]`. Tổng từ từng phiếu: 120 phút cho 50 slide giảng, 60 phút cho 7 slide/5 bài tập. Phân bổ hợp lý trên giấy; chưa phải bằng chứng đã dạy thử đúng thời lượng. |

Các kết quả số độc lập khớp bản nháp: Jaccard Hình 3.2 là $0,1/4,2/3,0,1/3,1/5$; số trùng trên 120 hoán vị là $0,30,80,0,40,24$; Bài 3.3.2 cho hai hàng $(0,3,0,0)$ và $(3,0,1,0)$; Bài 3.3.3 cho ba hàng $(5,1,1,1)$, $(2,2,2,2)$, $(0,1,4,0)$ và các sai lệch đúng như notes.

#### No-ai-slop Detect và Quill continuity

No-ai-slop Detect không tìm thấy một mẫu lời dẫn rỗng, ca ngợi, câu hỏi tu từ hoặc suy đoán tác giả cần lập thành lỗi riêng trong toàn bộ mặt slide, notes và ghi chú đã đọc. Các câu đối chiếu “định danh/hạng”, “kỳ vọng/sai số quan sát”, “số cặp/chi phí một cặp” có chức năng toán học rõ và cần giữ. E01 là thiếu điều kiện học thuật, không phải lý do để bỏ phân biệt; E03 cần sửa cách dẫn nguồn, không thay giọng viết. Không dùng điểm phát hiện AI.

Quill continuity: chuỗi khái niệm và ký hiệu xuyên bài ổn định; $\ell,k,R,C,n,L$ có vai trò riêng, $h_\pi$ và $f_i$ không bị nhập làm một. Cặp $S_1,S_4$ nối được từ ma trận tới xác suất, chữ ký và chi phí. Hai nhánh đọc thêm được tách rõ. Điểm đứt cần xử lý là dữ kiện công khai của vết chạy ở E02; ghi chú tự học đã có bảng đầy đủ để dùng làm căn cứ sửa. Chưa phát hiện thay đổi giả thiết ngầm ở ranh giới sang Bài 06.

Sau E01–E04, cần rà lại các slide/hình/đoạn ghi chú bị sửa trên render thực. Kết luận ở đây chỉ xác nhận nội dung học thuật trong phạm vi đã nêu; không thay kiểm trình duyệt, bàn phím, in, liên kết hoặc nghiệm thu chung của điều phối viên.


### Bản lưu: Toán học và thuật toán

### Rà độc lập độ chính xác toán học và thuật toán — Bài 05

Tác tử: `lec05_math_review`. Vai trò: chỉ đọc sản phẩm; không sửa kho. Bản rà ngày 2026-09-28. Dấu vân tay các tệp được lưu trong `math-reviewed-snapshot.json` cùng thư mục để xác định đúng bản nháp đã đọc.

#### Kết luận theo phạm vi

Không tìm thấy lỗi số học hoặc lỗi định lý ở mức **chặn bàn giao/nghiêm trọng** trong 57 slide, 57 khối ghi chú diễn giả, 14 mục ghi chú bài giảng và 8 SVG đã rà. Định lý MinHash, kỳ vọng, phương sai, thuật toán quét, bất biến, các cận thời gian và toàn bộ kết quả số của Ví dụ 3.8 cùng năm bài tập nguồn đều đúng trong các mô hình đã nêu.

Có **4 phát hiện trung bình** cần sửa cục bộ để không lẫn kiểu đối tượng hoặc bỏ mất điều kiện khi đọc trực tiếp hình/lời giải. Có **3 phát hiện nhẹ** về trường hợp biên, độ đầy đủ của lập luận và truy nguyên nguồn. Đây không phải kết luận rằng toàn bộ deck đã vượt kiểm định hiển thị hay có thể phát hành: phạm vi lượt này là tính đúng học thuật.

#### Phạm vi và cách kiểm

- Đọc toàn bộ HTML `2627-1/lecture-05-bieu-dien-tuong-dong-shingling-va-minhash.html`, gồm mọi slide và notes; đếm độc lập được 57/57.
- Đọc toàn bộ 919 dòng `2627-1/materials/lec-05/lecture-note.md`, đủ 14 mục, mọi bảng, khối bài tập và lời giải.
- Đọc nhãn, mô tả, cấu trúc nội dung của đủ 8 SVG và quan sát 8 bản render SVG trong `/tmp/lec05-rebuild/svg/`. Không nhận đã xem render từng slide/viewer ở mọi kích thước.
- Đọc quy định AGENTS, bản đồ nguồn học phần, hàng Bài 5 của `sources/reference-slides/README.md`, `slide_authoring_standard.md`; đối chiếu thuật ngữ của outline với sản phẩm. Không dùng báo cáo planner hay hồ sơ nguồn làm chứng minh.
- Trực tiếp trích xuất từ PDF sách MMDS 3e, đọc §§3.1–3.3, tr. 73–91; đối chiếu Hình 3.2–3.6, Ví dụ 3.3–3.9, Bài 3.1.1, 3.2.3, 3.3.1–3.3.3. Đã quan sát trực tiếp trang in 80 để kiểm dấu từ dừng, thay vì đoán từ văn bản trích xuất mất chữ nghiêng.
- Mở/trích xuất ba slide nguồn được ánh xạ; đối chiếu phần shingling/MinHash và phân biệt định danh–hạng của Stanford 03, phần tóm lược MinHash của Stanford 04 và cụm tương ứng trong slide MMDS. Không đánh giá lại cơ chế LSH nằm ngoài Bài 05.
- Viết và chạy phép tính xác định độc lập trong `math-check-independent.py`; kết quả ở `math-check-independent.json`. Không đọc `root-math-check.json`, `root-draft-observations.md`, kết quả tính của writer hoặc báo cáo reviewer khác.
- Đọc `no-ai-slop/SKILL.md`, `eval.md`, dùng Detect. Đọc Quill và workflow liên quan, áp dụng rà sự liên tục của khái niệm/ký hiệu theo ngoại lệ học phần; không tạo `quill.json`.

#### Phát hiện

##### M01 — Trung bình — Tập, hàm và trạng thái chữ ký bị dùng lẫn kiểu ở một số câu

**Vị trí:** `lec05-s05-05`, `lec05-s05-06`, đặc biệt `lec05-s05-12`; HTML dòng 252, 254, 258, 260, 300, 302. Ghi chú bài giảng mục 9, nhất là dòng 462, 470, 500–504.

**Vấn đề:** Ký hiệu đã được phân loại đúng ở phần đầu nhưng câu hỏi sau lại viết `$S_4=(1,1)$`, trong khi $S_4=\{a,c,d\}$ là tập đầu vào cố định. Các câu “$S_2$ thay đổi”, “$S_2$ còn hai giá trị $+\infty$” tiếp tục gán trạng thái bộ nhớ cho tập. Trên `lec05-s05-06`, `$(f_1,f_2)=(4,0)$` và `$(f_1,f_2)=(0,3)$` dùng tên hai hàm như hai giá trị.

**Bằng chứng:** Ở `lec05-s03-02`, $S_c$ là tập tương ứng một cột. Ở `lec05-s05-02`, trạng thái đầu ra là $\mathrm{SIG}(i,c)$, còn $f_i$ là hàm nhận mã hàng. MMDS Ví dụ 3.8 tr. 86 nói các giá trị trong *cột chữ ký của* $S_4$, không đồng nhất tập với vector. Số học $(1,1)$, $(3,2)$, $(4,0)$, $(0,3)$ đều đúng; lỗi thuộc loại đối tượng được gán giá trị.

**Đề xuất sửa:** Viết “chữ ký hiện tại của $S_4$ là $(1,1)^{\mathsf T}$”; “giải thích vì sao chữ ký của $S_2$ thay đổi còn chữ ký của $S_4$ giữ nguyên”. Dùng $(f_1(3),f_2(3))=(4,0)$ và $(f_1(4),f_2(4))=(0,3)$. Rà tương tự toàn cụm vết chạy để mọi động từ “cập nhật/nhận/giảm” chỉ đúng thành phần chữ ký, không gán cho tập đầu vào. Không đổi bảng kết quả.

##### M02 — Trung bình — Lời giải bài shingle chuyển byte thành ký tự mà chưa chốt mô hình

**Vị trí:** `lec05-s07-02`, HTML dòng 340–342; ghi chú mục 14, Bài 3.2.3, dòng 744–750. Liên quan định nghĩa ở `lec05-s02-03` và ghi chú mục 3.

**Vấn đề:** Định nghĩa $k$-shingle trước đó dùng $k$ **ký tự**, còn đề Bài 3.2.3 giữ đúng nguồn là tài liệu dài $\ell$ **byte**. Lời giải suy ngay số vị trí bắt đầu là $\ell-k+1$, tức đã dùng $\ell$ làm số đơn vị ký tự. Điều này đúng trong mô hình một byte cho một ký tự, hoặc khi tạo shingle trực tiếp trên byte; không đúng như một phát biểu không điều kiện cho chuỗi có ký tự nhiều byte.

**Bằng chứng:** Đề gốc tr. 81 thực sự dùng “bytes”, nên không đề nghị đổi dữ kiện nguồn. Tuy nhiên, tài liệu tự học đã hình thức hóa chỉ số ký tự ở mục 3 và phân biệt rất kỹ đơn vị ký tự/byte ở các mục khác. Khoảng trống nằm ở câu chuyển mô hình, không phải số học $\max(0,\ell-k+1)$.

**Đề xuất sửa:** Giữ nguyên đề nguồn, thêm quy ước trong notes và lời giải: “Trong mô hình của bài này, mỗi ký tự chiếm một byte; vì vậy tài liệu có $\ell$ vị trí ký tự.” Hoặc nêu rõ đang lấy shingle trên byte cho riêng bài này. Không âm thầm áp công thức lên ký tự Unicode đã giải mã khi chỉ biết độ dài tệp theo byte.

##### M03 — Trung bình — Nhãn hình phân hoạch bỏ điều kiện “phần tử đầu trong hợp”

**Vị trí:** `phan-tu-dau-hop.svg`, dòng 8–9; được dùng ở `lec05-s03-07` và ghi chú mục 6.

**Vấn đề:** Hộp $X$ ghi “MinHash trùng”, hộp $Y$ ghi “MinHash khác”. Các kết luận chỉ đúng khi **phần tử đầu tiên của hợp** thuộc loại tương ứng. Với dữ liệu trong chính hình, $X$ và $Y$ đồng thời không rỗng, nên chỉ sự hiện diện của hàng $X$ hoặc $Y$ không quyết định kết quả.

**Bằng chứng:** Chọn thứ tự có $c$ đứng đầu hợp cho $h_\pi(S_1)\ne h_\pi(S_4)$ dù $a,d\in X$. Chọn thứ tự có $a$ đứng đầu cho kết quả trùng dù $c\in Y$. Điều kiện đúng có trong mô tả thay thế và notes nhưng chưa hiện trên nhãn hình; slide hiện dùng tiêu đề “Các hàng chung và riêng”. Định lý và chứng minh sau đó phát biểu đúng.

**Đề xuất sửa:** Thêm nhãn nhìn thấy “Loại của phần tử đầu trong hợp”, hoặc đổi kết luận trong hộp thành “Đứng đầu hợp ⇒ trùng” và “Đứng đầu hợp ⇒ khác”. Đổi “thuộc một tập” thành “thuộc đúng một tập”. Giữ nguyên dữ kiện và phân hoạch $X,Y,Z$.

##### M04 — Trung bình — Con số chín shingle từ dừng thiếu dữ kiện để người đọc tính lại

**Vị trí:** ghi chú mục 12, dòng 629–637, Ví dụ 3.5.

**Vấn đề:** Ghi chú dẫn nguyên câu tiếng Anh và kết luận có chín shingle, nhưng không đánh dấu các từ dừng hoặc liệt kê tập từ dừng dùng cho phép đếm. Định nghĩa “những từ xuất hiện thường xuyên” không xác định một tập duy nhất. Con số đúng theo nguồn nhưng chưa tái tạo được từ dữ kiện công khai.

**Bằng chứng:** Trang in 80 của PDF đánh dấu các từ dừng và nói rõ cách đánh dấu này. Những vị trí tạo chín shingle là: `A`, `for`, `the`, `that`, `have`, `it`, `is`, `for`, `to`. Bản Markdown bỏ dấu phân biệt ấy. Ba shingle đầu đang có đều đúng.

**Đề xuất sửa:** Phục hồi dấu từ dừng theo đúng nguồn hoặc liệt kê chín vị trí bắt đầu. Có thể bổ sung bảng chín kết quả: `A spokesperson for`; `for the Sudzo`; `the Sudzo Corporation`; `that studies have`; `have shown it`; `it is good`; `is good for`; `for people to`; `to buy Sudzo`. Không dùng danh sách từ dừng ngoài nguồn để làm đủ chín.

##### M05 — Nhẹ — Công thức đa tập thiếu điều kiện mẫu số khác không

**Vị trí:** ghi chú mục 12, dòng 617–625.

**Vấn đề và bằng chứng:** Công thức tỷ số đa tập được nêu cho $B,C$ mà chưa nói ít nhất một đa tập không rỗng. Với cả hai rỗng, tử và mẫu đều bằng 0. Tuyến chính đã xử lý rõ cùng vấn đề cho tập thường. Kết quả $1/3$ của ví dụ và $1/2$ khi một đa tập không rỗng so với chính nó đều đúng.

**Đề xuất sửa:** Nêu $B,C$ là các đa tập hữu hạn và $\sum_u(m_B(u)+m_C(u))>0$ trước công thức. Nếu cả hai rỗng, để ngoài định nghĩa hoặc cần quy ước riêng; không đưa vào định lý MinHash tập hợp.

##### M06 — Nhẹ — Phần đạt cận trong Bài 3.2.3 là khẳng định, chưa là chứng minh

**Vị trí:** notes `lec05-s07-02`; ghi chú lời giải Bài 3.2.3, dòng 748.

**Vấn đề:** Đếm vị trí chứng minh đúng cận trên $\ell-k+1$. Câu “dưới giả thiết ... giá trị lớn nhất đạt được khi các cửa sổ đều khác nhau” mới mô tả điều kiện đạt; chưa chứng minh tồn tại một chuỗi có các cửa sổ **chồng lấn** đều khác nhau. Số chuỗi độ dài $k$ khả dĩ đủ lớn không tự nó là một lập luận ghép các chuỗi ấy thành các cửa sổ liên tiếp.

**Bằng chứng và giới hạn:** Đáp số cực đại là đúng theo mô hình của nguồn. Đây không phải phản ví dụ với đáp án; là giới hạn độ đầy đủ của lời giải. Outline hiện chủ ý không thêm chuỗi de Bruijn, nên không đề nghị editor tự mở thêm một thuật toán ngoài phạm vi.

**Đề xuất sửa:** Ghi rõ trong hồ sơ đây là đáp án kèm chứng minh cận trên, phần đạt theo giả thiết và kết quả của bài nguồn được nêu chứ không chứng minh đầy đủ. Nếu root yêu cầu lời giải đầy đủ về tính đạt, phải duyệt thêm lập luận kiến tạo có nguồn trước khi writer thêm; không đổi giả thiết thành “có ít nhất $\ell$ ký tự khác nhau”, vì đó là giả thiết mạnh hơn đề gốc.

##### M07 — Nhẹ — Một số tham chiếu mô tả sai vị trí hoặc cách dùng ký hiệu của sách

**Vị trí:** `lec05-s01-08` và ghi chú mục 2 dòng 62; `lec05-s03-05` phần nguồn.

**Vấn đề và bằng chứng:** Ví dụ khách hàng/mặt hàng nằm ở §3.1.3 (tr. 76), không phải §3.1.2. Dòng nguồn `lec05-s03-05` ghi “ghi định danh thay hạng”, nhưng sách Ví dụ 3.7 đã dùng $h(S_1)=a$, $h(S_2)=c$, $h(S_3)=b$, $h(S_4)=a$. Bản nháp đang dùng cùng định danh với sách; sự khác biệt hạng/định danh được Stanford slide 28 giải thích nhưng không phải một đổi mới so với Ví dụ 3.7.

**Đề xuất sửa:** Sửa §3.1.2 thành §3.1.3 ở ví dụ mua hàng. Thay chú thích bằng “giữ định danh như Ví dụ 3.7; bổ sung hàng vị trí để phân biệt hai kiểu giá trị”. Ngoài ra, Hình 3.1 nằm trên trang in 75, còn định nghĩa/Ví dụ 3.1 trên trang 74; nguồn dẫn chính hình nên ghi tr. 74–75 hoặc tr. 75.

#### Những phần đã kiểm và đạt trong bản nháp

| Cụm | Kết quả kiểm độc lập |
|---|---|
| Jaccard và tập rỗng | Định nghĩa dùng hợp khác rỗng; định lý chỉ dùng hai tập không rỗng; không suy định lý từ hai giá trị canh bằng nhau. Hình $2+3+3$ và tỷ số $3/8$ đúng. |
| Shingling | `abcdabd`: 6 cửa sổ, 5 shingle; `touch down`: 2 cửa sổ dài 9; `touchdown`: 1. Chỉ số lát cắt và trường hợp $\ell<k$ đúng. Bất biến đúng; mô hình trực tiếp $O(1+wk)$ kỳ vọng ở ghi chú phân biệt rõ chi phí theo độ dài khóa. |
| MinHash lý tưởng | $h_\pi$ trả định danh; thứ tự chung; xác suất trên một hoán vị chọn đều. Chứng minh song ánh/đối xứng của phần tử đầu hợp và tương đương biến cố đúng, xử lý giao rỗng và hai tập bằng nhau. |
| Chữ ký | Hai thứ tự cố định suy từ Ví dụ 3.8 là $(e,a,b,c,d)$ và $(d,a,c,e,b)$. Các chữ ký định danh đều đúng; so bằng cùng tọa độ, không lấy Jaccard của tập giá trị. |
| Kỳ vọng/phương sai | $\mathbb E[\sum_iX_i]=ns$, $\mathbb E[\widehat{\mathrm{SIM}}]=s$ không cần độc lập. Phương sai $s(1-s)/n$ có độc lập. Với $s=2/3,n=100$: $200/3$, $2/3$, $1/450$. Ghi chú nêu đúng phương sai bằng 0 ở $s=0,1$. |
| Băm hàng và bất biến | Đặc tả miền hữu hạn có thứ tự toàn phần, giá trị canh lớn hơn mọi giá trị băm, chỉ số $r,c,i$ đầy đủ. Thuật toán dừng sau $R$ hàng và chứng minh đúng cả cột rỗng. Không biến chứng minh tính cực tiểu thành chứng minh chất lượng thống kê. |
| Chi phí | $L$ là tổng số ô 1; khởi tạo $nC$, băm $nR$, kiểm ô $RC$, min $nL$. Cận đặc và danh sách đã xây sẵn đúng; không giấu chi phí xây danh sách. Đầu ra $\Theta(nC)$ từ và bộ đệm $\Theta(n)$ tách khỏi dữ liệu đầu vào. Mô hình không tuyên bố cận I/O hoặc tốc độ thực. |
| Affine | Điều kiện $\gcd(a,R)=1$ đúng; chứng minh chiều đủ và chiều cần ở ghi chú đúng. Không nhầm $R$ nguyên tố là điều kiện cần. Phân biệt song ánh của một hàm với phân phối chọn hàm đều là đúng. |
| Đọc thêm | Quy ước đa tập của sách được giữ đúng, không trộn với mẫu số max. Quy tắc hai vô cực bị bỏ khỏi mẫu số khi cắt lượt tìm đúng theo nguồn. Hình 3.5: Jaccard toàn cục $1/2$, hai nhóm $0,2/3$, trung bình $1/3$ đúng; không khẳng định chia cố định bảo toàn tỷ số. |

##### Kết quả số của Ví dụ 3.8 và recitation

- Ví dụ 3.8: bảng băm $f_1=(1,2,3,4,0)$, $f_2=(1,4,2,0,3)$; toàn bộ năm trạng thái trung gian và đầu ra cuối $\bigl[(1,3,0,1);(0,2,0,0)\bigr]$ đúng. Số phép min là 18, khác số ô thực sự giảm.
- Bài 3.1.1: ba Jaccard $1/3,2/5,1/6$ đúng; giao/hợp trong notes và ghi chú đúng.
- Bài 3.3.1: sáu Jaccard $0,1/4,2/3,0,1/3,1/5$. Liệt kê độc lập đủ $5!=120$ hoán vị cho sáu số đếm $0,30,80,0,40,24$, đúng mọi lời giải.
- Bài 3.3.2: hai bảng giá trị và hai hàng chữ ký $(0,3,0,0)$, $(3,0,1,0)$ đúng; phần dư âm được xử lý đúng.
- Bài 3.3.3: dữ kiện Hình 3.6 khớp PDF; chữ ký $\bigl[(5,1,1,1);(2,2,2,2);(0,1,4,0)\bigr]$ đúng. Chỉ $f_3$ là hoán vị. Sáu ước lượng $1/3,1/3,2/3,2/3,2/3,2/3$, Jaccard thật $0,0,1/4,0,1/4,1/4$ và các sai lệch tuyệt đối $1/3,1/3,5/12,2/3,5/12,5/12$ đều đúng.
- Phép đếm cặp $C=10^6$ và $27^5$ khớp; không có số thực nghiệm bị bịa vào kết luận.

#### Detect và tính liên tục

Không tìm thấy kiểu lời dẫn rỗng, khẳng định phô trương hay suy diễn “thống kê cho thấy” thiếu nguồn trong phần toán học đã đọc. Không sử dụng điểm bộ phát hiện AI hoặc suy đoán tác giả. M01 là chỗ cần sửa để giữ thuật ngữ/đối tượng ổn định; M02 là cầu nối đơn vị bị thiếu. Các phủ định về “không đồng nhất kỳ vọng với một mẫu”, “không suy hoán vị đều từ song ánh” có chức năng toán học và cần giữ, không cắt chỉ để tránh cấu trúc đối lập.

Quill: chuỗi tập hợp → Jaccard → shingle → ma trận → MinHash → chữ ký → kỳ vọng/phương sai → quét hàng → chi phí/giới hạn liên tục. Hai nhánh đọc thêm được đánh dấu riêng, không thành tiên quyết ngầm của thuật toán chính. Không có yêu cầu thay thứ tự toàn bài từ lượt rà toán học này.

#### Giới hạn và phạm vi tái kiểm đề nghị

Không kiểm hành vi JavaScript/viewer, bàn phím, CSS chung, in hay xuất PDF; không xác nhận đã xem render toàn bộ 57 slide. Chỉ quan sát 8 SVG đã render và một trang sách để kiểm dữ kiện phụ thuộc kiểu chữ. Phép liệt kê hữu hạn chỉ là kiểm số học bổ trợ; kết luận định lý dựa trên đọc chứng minh, không suy từ kiểm thử.

Sau chỉnh sửa, tái kiểm M01–M05 trực tiếp trên HTML/Markdown/SVG và xác nhận không đổi dữ kiện các bài nguồn. M06 cần quyết định biên tập của root về mức chứng minh, M07 chỉ sửa tham chiếu. Nếu editor thay định lý, giả mã hoặc phân tích chi phí thay vì chỉ sửa câu, cần giao lại toàn cụm liên quan cho reviewer toán học.


### Bản lưu: Học thuật và giảng dạy

### Rà độc lập học thuật và giảng dạy — Bài 05

Ngày rà: 28-09-2026. Vai trò: phản biện học thuật và giảng dạy, chỉ đọc sản phẩm. Báo cáo này không dựa vào báo cáo gate, báo cáo reviewer khác hoặc quan sát của root. Không sửa tệp trong kho.

#### Kết luận trong phạm vi đã rà

Không phát hiện vấn đề mức **chặn bàn giao** hoặc **nghiêm trọng**. Xương sống Jaccard → shingling → MinHash → chữ ký → tính chữ ký → chi phí và giới hạn phù hợp MMDS 3e, Chương 3. Có **3 vấn đề trung bình** và **2 vấn đề nhẹ** cần xử lý cục bộ trước khi chốt chất lượng giảng dạy. Các điểm này không đòi đổi dữ kiện hoặc xây lại toàn bộ mạch.

Văn phong học thuật nhìn chung đạt: không thấy lời trò chuyện, câu hỏi tu từ, lời ca ngợi, lời điều phối giảng viên hoặc việc phải làm của người soạn trong 57 mặt slide, 57 notes, nhãn SVG và toàn bộ ghi chú đã đọc. Các câu hỏi yêu cầu người học tính hoặc giải thích là nhiệm vụ đánh giá hợp lệ. Những đối chiếu phủ định như “không bảo đảm sai số quan sát giảm” có chức năng toán học, không phải mẫu đối lập rỗng cần cắt bằng no-ai-slop.

#### Phạm vi và cách rà

- Đọc `review-brief.md`, các quy định áp dụng trong `AGENTS.md`, `sources/source.md`, dòng Bài 5 của `sources/reference-slides/README.md`, và sáu nhóm tiêu chuẩn trong `slide_authoring_standard.md`.
- Đọc toàn bộ HTML Bài 05: **57 slide và 57 khối notes**. Đọc toàn bộ **919 dòng, 14 chủ đề** của `materials/lec-05/lecture-note.md`. Đọc nhãn, title và desc của **8 SVG**.
- Đối chiếu sách cục bộ bằng văn bản trích xuất trực tiếp từ PDF, §§3.1–3.3, tr. in 73–91; kiểm lại các ví dụ 3.1–3.9, Hình 3.1–3.6 và năm bài được chọn. Đã mở ba PDF slide tham khảo qua `pdftotext` và đọc các cụm liên quan: MMDS khoảng slide 14–39; Stanford `03-lsh.pdf` slide 18–33; `04-lsh_theory.pdf` slide 3–7. Không nhận đã kiểm ảnh của toàn bộ các PDF tham khảo.
- Đọc bản đồ mạch, ký hiệu, quyết định nguồn và chu trình trong outline/storyboard; kiểm riêng phiếu slide 32, 36, 37–40 và 45. Không dùng lời xác nhận PASS trong tài liệu quy trình làm bằng chứng bản triển khai đạt.
- **Đã xem ảnh thực:** toàn bộ 10 ảnh `draft-renders/contact-wide-*.png`, bao phủ đủ 57 slide; xem thêm ảnh riêng `wide-25`, `wide-32`, `wide-36`, `wide-37`, `wide-39`, `wide-46` và `narrow-36` trong thư mục `lec05/`. Các nhận xét về slide 25, 32, 36, 37, 39, 46 có cả bằng chứng mã và ảnh riêng.
- **Ghi chú trên web/in:** xem `note-1440-top.png`, `note-390-top.png` và ba ảnh `print-contact-1.png` đến `print-contact-3.png`, bao phủ bố cục 36 trang in ở mức ảnh tổng hợp. Không kiểm tương tác bàn phím, không đọc mọi trang in ở độ phân giải riêng, không tuyên bố viewer đạt kiểm định kỹ thuật toàn diện.
- Đọc skill `no-ai-slop/SKILL.md` và `eval.md`; dùng **Detect**, không viết lại hay chấm điểm tác giả. Đọc Quill và phần workflow sửa để kiểm tính liên tục của khái niệm, giả thiết và ký hiệu; không tạo `quill.json`.

#### Các phát hiện

##### AR-01 — Dữ kiện vào của vết quét chưa hiện đủ tại nơi tính

- **Mức độ:** trung bình.
- **Vị trí:** `lec05-s05-03` đến `lec05-s05-06`, rõ nhất `lec05-s05-03` và `lec05-s05-05`; HTML dòng 238–265; ảnh riêng `wide-37-lec05-s05-03.png`, `wide-39-lec05-s05-05.png`.
- **Vấn đề:** Các bảng trạng thái đúng, nhưng người học chưa tự tái tạo đầy đủ vết chạy chỉ từ dữ kiện hiện trên cụm slide này. Khi bắt đầu ví dụ, bảng chỉ chứa mã hàng và hai giá trị băm; ma trận hiện diện hoặc danh sách cột chứa từng hàng nằm ở phần trước, cách 16–17 slide. Tại bước hàng 1, 2, các cột cần cập nhật không được nhắc lại trên mặt slide.
- **Bằng chứng:** Slide 37 chỉ có câu **“Dùng ma trận đặc trưng Hình 3.2.”** cạnh bảng $r,f_1(r),f_2(r)$. Slide 39 hiện hai bảng **“Sau hàng $r=1$”**, **“Sau hàng $r=2$”**, nhưng không hiện đầu vào hàng 1 chỉ thuộc cột 3 và hàng 2 thuộc cột 2, 4. Hai thông tin này có trong notes. Slide 38 đã làm tốt hơn khi ghi các cột có 1 là 1, 4; slide 40 cũng chỉ rõ các cột được cập nhật.
- **Ảnh hưởng học tập:** Vết chạy là bước nối từ đặc tả cực tiểu sang giả mã. Thiếu danh sách cột khiến người học thấy kết quả số nhưng phải nhớ dữ liệu cũ hoặc nhận lời giải bằng lời mới biết vì sao một cột được cập nhật. Điều này làm yếu tiêu chí “tính lại được trạng thái tiếp theo từ dữ kiện hiển thị”.
- **Đề xuất sửa:** Bổ sung cột “Các cột có 1” vào bảng slide 37, như bảng đã có trong ghi chú §9; tại slide 39 thêm dữ kiện ngắn cho hàng 1 và 2, hoặc đặt danh sách hàng tương ứng cạnh từng trạng thái. Giữ số liệu nguồn. Không cần đưa toàn bộ ma trận lên mọi slide hoặc thêm slide mới. Rà lại các trang 35–42 sau khi sửa.

##### AR-02 — Dùng ký hiệu tập để chỉ trạng thái chữ ký

- **Mức độ:** trung bình.
- **Vị trí:** `lec05-s05-12`, nhiệm vụ 2, HTML dòng 300; các diễn đạt liên quan ở `lec05-s05-05`, notes `lec05-s05-12`, ghi chú §9.
- **Vấn đề:** Một câu trên mặt slide đồng nhất trực tiếp tập $S_4$ với một cặp giá trị chữ ký. Đây là vấn đề kiểu đối tượng và tính liên tục ký hiệu, không phải lỗi phép min.
- **Bằng chứng:** Nhiệm vụ viết **“Giải thích cập nhật $S_4=(1,1)$ bằng $(3,2)$.”** Trong cả bài, $S_4=\{a,c,d\}$ là tập cố định; $(1,1)$ là trạng thái hai thành phần chữ ký trước khi xử lý hàng 2. Ảnh `wide-46-lec05-s05-12.png` xác nhận đẳng thức này hiện trực tiếp cho người học. Slide 39 viết “$S_4$ đang có $(1,1)$”; ghi chú §9 có “$S_2$ nhận $(3,2)$ … còn $S_4$ đã có $(1,1)$”. Những cách nói sau có thể hiểu là lược “chữ ký”, nhưng cùng đẳng thức sai kiểu ở slide 46 dễ tạo sự đồng nhất.
- **Ảnh hưởng học tập:** Phần trước dành nhiều công sức phân biệt phần tử, hạng, giá trị băm, tập và vector. Nhiệm vụ kiểm tra cuối cụm lại dùng cùng tên cho đầu vào cố định và trạng thái được cập nhật, làm suy yếu chính phân biệt ấy.
- **Đề xuất sửa:** Gọi rõ “chữ ký hiện tại của $S_4$ là $(1,1)$” và “ứng viên từ hàng 2 là $(3,2)$”; hoặc dùng cột $\mathrm{SIG}(:,4)$ sau khi đã giải thích ký hiệu. Rà các câu “tập nhận/giữ/thay đổi” trong vết chạy và notes, đổi thành “chữ ký của tập” nơi đang nói về trạng thái. Không cần đổi các nhãn cột $S_1,\ldots,S_4$ trong bảng vì đó là nhãn đối tượng được biểu diễn.

##### AR-03 — Công thức phương sai đúng nhưng bước suy ra bị rút khỏi mặt slide

- **Mức độ:** trung bình.
- **Vị trí:** `lec05-s04-05`, HTML dòng 206–211; ảnh `wide-32-lec05-s04-05.png`; storyboard phiếu 32.
- **Vấn đề:** Slide trình bày hai công thức kết quả cho phương sai và độ lệch chuẩn ngay sau điều kiện độc lập, nhưng thiếu bước cho thấy tính độc lập được dùng ở đâu. Công thức đúng và được giải thích đủ trong notes/ghi chú §8; vấn đề nằm ở mức hỗ trợ suy luận trên lớp của mặt slide.
- **Bằng chứng:** Mặt slide chuyển từ **“Nếu các hoán vị còn độc lập, $X_i$ là các biến Bernoulli độc lập có tham số $s$.”** thẳng tới $\operatorname{Var}(\widehat{\mathrm{SIM}})=s(1-s)/n$ rồi công thức SD. Storyboard dự kiến có **“một chuỗi suy ra ngắn Var(tổng)/n²”** và thứ tự đọc “Độc lập → phương sai tổng → chia $n^2$”; chuỗi này không có trong bản HTML/ảnh.
- **Ảnh hưởng học tập:** Slide trước dùng tính tuyến tính của kỳ vọng, vốn không cần độc lập. Nếu bước cộng phương sai bị ẩn, sinh viên dễ coi điều kiện độc lập là nhãn kèm công thức, hoặc không phân biệt được hai lập luận. Tiêu chuẩn slide yêu cầu bước suy luận quyết định còn hiện trên mặt ngay cả khi chứng minh chi tiết chuyển sang notes.
- **Đề xuất sửa:** Giữ một chuỗi ngắn $\operatorname{Var}(n^{-1}\sum_iX_i)=n^{-2}\sum_i\operatorname{Var}(X_i)=s(1-s)/n$ và nhãn ngắn cho bước dùng độc lập. Có thể chuyển công thức SD sang notes hoặc lời giải bằng chữ để giữ một trọng tâm. Không cần thêm định lý sai số mới. Không áp dụng nhận xét này cho ghi chú §8: phần đó đã có lập luận đủ.

##### AR-04 — Nhãn kết quả trong hình phân hoạch thiếu điều kiện “đầu tiên trong hợp”

- **Mức độ:** nhẹ.
- **Vị trí:** `phan-tu-dau-hop.svg` dòng 8–9, dùng tại `lec05-s03-07` và ghi chú §6; ảnh `wide-25-lec05-s03-07.png`.
- **Vấn đề:** Trong hình đang phân loại các phần tử, ô $X$ ghi “MinHash trùng”, ô $Y$ ghi “MinHash khác”, nhưng nhãn nhìn thấy không nêu rằng kết quả phụ thuộc loại của **phần tử đầu tiên trong hợp**. Title/desc của SVG và notes có điều kiện đúng, song chúng không thay cho nhãn nhìn thấy khi trình chiếu.
- **Bằng chứng:** Hình hiển thị **“X: thuộc cả hai / a, d / MinHash trùng”** và **“Y: thuộc một tập / c / MinHash khác”**. Hình không chọn hay đánh dấu hàng đầu. Chỉ có việc tồn tại hàng thuộc giao không đủ suy hai MinHash trùng. Điều kiện được viết đúng ở slide 22 và slide 26 nên đây là sự thiếu rõ tại hình, không phải lỗi định lý toàn bài.
- **Đề xuất sửa:** Thêm một câu chú thích ngắn: “Loại của phần tử đầu trong hợp quyết định kết quả”; hoặc sửa hai nhãn thành kết quả có điều kiện. Dùng cùng SVG đã sửa cho ghi chú để giữ nhất quán.

##### AR-05 — Hai dẫn chiếu cục bộ chưa đúng vị trí trong sách

- **Mức độ:** nhẹ.
- **Vị trí:** `lec05-s01-08`, nguồn trên mặt và notes; `lec05-s01-06`, `lec05-s01-09`; ghi chú §2, dòng 50, 62.
- **Vấn đề:** Nội dung đúng nhưng địa chỉ tra cứu chưa chính xác.
- **Bằng chứng:** Ghi chú viết **“Trong ví dụ khách hàng của §3.1.2, phần tử có thể là mặt hàng đã mua.”** Sách đặt phần *On-Line Purchases* trong **§3.1.3, tr. 76**; §3.1.2 là tương đồng tài liệu. Slide 08 cũng dẫn riêng §3.1.2 cho cả hai ứng dụng. Ngoài ra, câu **“Hình 3.1 của sách, tr. 74”** và nguồn slide 06/09 ghi tr. 74, trong khi hình cùng chú thích nằm **tr. 75**; Ví dụ 3.1 và công thức ở tr. 74.
- **Đề xuất sửa:** Dẫn §3.1.3 cho ví dụ khách hàng; nếu một slide gồm cả văn bản và khách hàng, ghi §§3.1.2–3.1.3. Dẫn Hình 3.1 ở tr. 75, hoặc ghi “Ví dụ 3.1 và Hình 3.1, tr. 74–75”. Sửa đồng thời nguồn lặp trong notes và Markdown.

#### Kiểm mạch hình thức hóa và tính liên tục theo Quill

| Cụm | Kết quả rà |
|---|---|
| Jaccard, slide 04–09; chủ đề 1–2 | Tình huống và chi phí cặp đi trước ví dụ giao/hợp 3 và 8; công thức đến sau ví dụ; có điều kiện mẫu số, biên, ứng dụng và kiểm tra. Ghi chú đặt định nghĩa trước ví dụ là đúng loại tài liệu. |
| Shingling, slide 10–18; chủ đề 3 | Có cửa sổ cụ thể, lặp `ab`, đặc tả chỉ số, thuật toán và bất biến. Giới hạn bộ nhớ nối sang chữ ký. Không cần tạo thuật toán mới ngoài nguồn. |
| Ma trận, hoán vị và định lý, slide 19–27; chủ đề 4–6 | Ma trận có vai trò cầu nối; trực giác dùng cùng thứ tự và ví dụ `b,e,a,d,c` đi trước argmin. Phân loại X/Y/Z chuẩn bị đúng chứng minh. Công thức xác suất xuất hiện đúng chỗ. AR-04 chỉ làm rõ hình. |
| Chữ ký và ước lượng, slide 28–34; chủ đề 7–8 | Ví dụ hai thứ tự cho kết quả hữu hạn khác Jaccard thật đi trước vector/tổng chỉ báo; giả thiết đều và độc lập được phân biệt. AR-03 là thiếu cầu nối trên mặt slide, không phải lỗi thứ tự toàn cụm. |
| Quét hàng, slide 35–46; chủ đề 9–11 | Đặc tả đứng trước vết chạy chi tiết là sai khác đã có lý do trong storyboard: phép min và chọn đầu đã được dựng ở phần trước, slide 35 giải thích thao tác theo hàng. Không coi riêng thứ tự này là lỗi bắt buộc. Tính đúng, dừng, rỗng, chi phí và giới hạn đều có; AR-01/02 làm yếu bước cụ thể hóa chứ không làm thuật toán sai. |
| Đọc thêm, chủ đề 12–13 | Đa tập, từ dừng, lấy phần đầu và nhóm hàng được đánh dấu rõ, không trở thành tiên quyết ngầm cho recitation. Không ép chúng vào deck. Ví dụ nhóm hàng phân biệt trung bình các tỷ số với tỷ số toàn cục. |
| Kết luận và vận dụng, slide 47–57; chủ đề 14 | Quy trình thu hồi nhu cầu biểu diễn; giới hạn số cặp trở lại cùng công thức mở bài; sáu nhiệm vụ tự kiểm có đáp án. Bài tập nguồn áp dụng trực tiếp Jaccard, hoán vị, min và đánh giá ước lượng. Bảy mạch ngoài khớp mục lục; tổng 120+60 phút được ghi ở storyboard và notes recitation. |

Các phân biệt được bảo toàn xuyên bài gồm $k$ với số byte mã, $R$ với $C$ và $n$, định danh với hạng và giá trị băm, xác suất với kết quả một phép thử, kỳ vọng số đếm với tỷ lệ, độ không chệch với phương sai, tính đúng của phép min với bảo đảm của phân phối hàm. AR-02 là ngoại lệ cục bộ cần sửa trong hệ ký hiệu này.

#### Kết quả Detect về văn phong

Đã kiểm tiêu đề, mặt slide, notes, nhãn hình, toàn bộ prose và lời giải theo no-ai-slop/eval. Không phát hiện mẫu tu từ rỗng đủ rõ để ghi thành lỗi văn phong riêng. Không suy đoán tác giả hoặc nguồn sinh văn bản. Các câu có “không” chủ yếu giữ phân biệt cần thiết về kiểu, đơn vị, giới hạn và giả thiết; không đề nghị cắt vì hình thức đối lập. Những câu “Tính”, “Xác định”, “Giải thích”, “Sản phẩm” thuộc nhiệm vụ người học; thời lượng trong notes recitation là ngoại lệ được brief cho phép. Không phát hiện chỉ dẫn người soạn hoặc giảng viên phải nói/làm gì.

Các phát hiện AR-01 đến AR-05 là vấn đề học tập, ký hiệu, nhãn có điều kiện hoặc truy nguyên nguồn; không gán chúng thành dấu hiệu văn bản do AI tạo. Sau khi sửa, nên rà lại cụm 31–34, 35–46 và SVG/ghi chú bị tác động, không cần biên tập lại hàng loạt những câu đã rõ.


### Bản lưu: Kết nối và mạch viết

### Rà độc lập kết nối và mạch viết — Bài 05

Ngày 28-09-2026. Tác tử `/root/lec05_flow_review`. Vai trò chỉ đọc; không sửa sản phẩm. Áp dụng **no-ai-slop Detect** và **Quill Outline/Revise theo chế độ đề xuất**, không tạo `quill.json`.

#### Kết luận trong phạm vi vai trò

Xương sống bài đã rõ và bám MMDS 3e §§3.1–3.3: đại lượng Jaccard → biểu diễn văn bản → ma trận tập → một MinHash → xác suất trùng → nhiều thành phần → ước lượng → phép quét tính được → chi phí và giới hạn. Không phát hiện lỗi **chặn bàn giao** hoặc **nghiêm trọng** về mạch toàn bài. Có **ba phát hiện trung bình** và **hai phát hiện nhẹ** dưới đây; chúng có thể xử lý cục bộ, không cần đổi sườn sách hoặc thêm phần lớn.

Kết luận này không thay kiểm toán toán học, kiểm tải nhận thức, cửa kiểm storyboard hoặc cửa kiểm phát hành. Việc đủ 57 mã/7 phần không tự chứng minh chất lượng mạch.

#### Phạm vi và bằng chứng đã xem

- Đọc brief chung, AGENTS.md và chuẩn slide; đối chiếu mục Bài 05 trong `sources/source.md` và dòng tương ứng trong `sources/reference-slides/README.md`. Nguồn trục đã đọc trực tiếp dưới dạng văn bản trích từ PDF cục bộ: phần mở Chương 3 và toàn bộ §§3.1–3.3, tr. 73–91, gồm các bài 3.1.1, 3.2.3, 3.3.1–3.3.3. Ba PDF slide ánh xạ đã được mở/trích văn bản; đọc đối chiếu trực tiếp phần ôn 3–7 của ST04. Lượt này không tự nhận đã xem hình của toàn bộ ba bộ slide tham khảo, không làm lại vai phân tích nguồn.
- Đọc **toàn bộ 57 slide và 57 notes**, **toàn bộ 14 chủ đề của lecture-note.md**, ba tệp `outline.md`, `storyboard.md`, `review-log.md`, cùng chữ/nhãn của tám SVG. Đã đọc các lý do thay thứ tự trong planning, nhưng không dùng các tuyên bố PASS/tự kiểm ở đó làm bằng chứng bản dựng đạt.
- Không mở báo cáo của reviewer khác, báo cáo gate hoặc tệp observations của root. Nhật ký sản phẩm bắt buộc đọc có tóm tắt lịch sử kiểm định; các tóm tắt ấy không được dùng để kết luận trong báo cáo này.
- Xem bằng mắt **10 ảnh contact-wide**, phủ đủ trang 01–57. Xem thêm ảnh riêng 1280×720 của trang **05, 35, 37, 39, 40** để kiểm các phát hiện. Ảnh riêng thuộc `draft-renders/lec05/wide-…`. Không tự nhận đã mở 57 ảnh riêng hoặc mọi ảnh hẹp.
- Viewer: xem `draft-materials/note-1440-top.png`, `note-390-top.png`; ba `print-contact-*.png` phủ 36 trang in. Các contact sheet bản in dùng để kiểm sự tiếp nối và phân chia mục, không để xác nhận từng glyph nhỏ. Chưa thao tác trực tiếp viewer/bàn phím, chưa rà từng trang in ở độ phân giải đầy đủ.
- Đọc cục bộ đoạn dựng mục lục trong `material-viewer.js` và kiểu `.toc-level-3` trong `material-viewer.css` để xác định nguyên nhân F05; không chạy lại bộ kiểm tương tác của root.
- Đếm độc lập bằng HTMLParser: 7 section ngoài, phân bố **[9, 9, 9, 7, 12, 4, 7]**, 57 mã duy nhất, 57 notes. Storyboard phân bổ 18+22+22+17+31+10=120 phút giảng; 8+10+7+8+12+8+7=60 phút bài tập. Đây là kiểm phép cộng kế hoạch, không phải thử giảng thực tế.

Bản HTML đọc có SHA-256 `5314061b1c1471f86c9c892c0ff8eb2cd1aa2c0e6341b201642c6f9de26a3beb`; Markdown có SHA-256 `d12bd50feb03dc0d2f29ecb1c2e3d1693f8d9b8d0b371bf21dc45d7357762e18`.

#### Bảy mạch và các ranh giới

| Phần | Chức năng và kết nối vào | Đầu ra cho phần sau; mục tiêu | Đánh giá |
|---|---|---|---|
| 1, 01–09 | Đặt kho gần trùng, số cặp; nhận tập hợp/xác suất tiên quyết | Jaccard đã xác định nhưng còn thiếu cách chọn phần tử văn bản; MT1 | Trang 09 chuyển đúng sang shingle. Cần F04 về ký hiệu đầu vào |
| 2, 10–18 | Nhận yêu cầu biểu diễn tập; cửa sổ tạo phần tử rồi quy định độ dài, khoảng trắng và băm | Tập phần tử có quy ước, vẫn có thể lớn; MT2 | 17–19 nối có căn cứ từ số phần tử sang bộ nhớ. Không xem bước băm shingle như đã có chữ ký cố định |
| 3, 19–27 | Nhận giới hạn dung lượng; biểu diễn ma trận giúp chọn cùng một phần tử theo thứ tự | Biến cố trùng có xác suất bằng Jaccard; MT3 | Ma trận/thưa là cầu nối, không phải tuyến thuật toán phụ. 27 phân biệt lần thử cố định và xác suất, tạo nhu cầu nhiều phép thử |
| 4, 28–34 | Nhận một phép thử; ví dụ hai thứ tự rồi vector, chỉ báo, kỳ vọng và phương sai | Ước lượng, điều kiện và đánh đổi theo độ dài; MT4 | 28→29→30 tiến triển rõ. 33 thu hồi thừa số số cặp; 34→35 chuyển sang tính chữ ký. Cầu nối đổi kiểu cần F01 |
| 5, 35–46 | Nhận chữ ký lý tưởng; thay cách biểu diễn thứ tự bằng giá trị băm và phép min | Chữ ký tính được, bất biến, số thao tác, bộ nhớ, điều kiện của hàm; MT5 | Không bị tách khỏi tuyến chính. Vết chạy cần F02; ký hiệu tập/chữ ký cần F03 |
| 6, 47–50 | Nhận toàn bộ kết quả để thu hồi bài toán gần trùng | Chuỗi→tập→chữ ký→ước lượng, điều kiện bảo đảm, sáu nhiệm vụ và ranh giới Bài 06 | Thu hồi đúng hai giới hạn khi đọc cùng notes. Không hứa MinHash tự giảm số cặp |
| 7, 51–57 | Nhận kiến thức tuyến chính; dùng năm bài nguồn | Tính tập, cận cửa sổ, đếm hoán vị, tạo chữ ký và đối chiếu sai lệch | 53→54 và 56→57 truyền đúng kết quả bài trước. Không cần đọc thêm để giải recitation |

Từng trang đều có một chức năng xác định. Các cụm dùng lại dữ kiện nhưng không lặp nguyên chức năng: 06 đếm, 07 đặt tỷ số, 08 xác định nghĩa phần tử, 09 kiểm; 22 chọn trực quan, 23 chạy đủ bốn cột, 24 chốt kiểu, 25 phân loại, 26 chứng minh, 27 phân biệt xác suất/quan sát; 31 tính kỳ vọng, 32 thêm độc lập để đo dao động, 33 trả chi phí; 41 khái quát vết chạy, 42 chứng minh, 43 đếm thao tác, 44 đếm bộ nhớ, 45 giới hạn bảo đảm, 46 kiểm. Mở bài 01–03 định vị chủ đề; 04–05 đưa tình huống và quy mô. 49–50 là tự kiểm tổng hợp, không thay phần bài tập nguồn.

Không có kết quả trọng tâm bị bỏ lại: danh sách theo hàng ở 21 được dùng tại 35/41/43; phần tử đầu của hợp ở 22/25 đi vào 26; cặp S1,S4 đi qua 27/28/30/34/46; chi phí từng cặp tại 05 được dùng lại 33/48/50; nhu cầu bộ nhớ tại 19 thu hồi 44 và notes 48. Hai giới hạn không cùng xuất hiện bằng tên trên mặt trang 05: số cặp được đặt ở 05, dung lượng tập được cụ thể hóa ở 19. Ghi chú tự học đặt cả hai ngay mục 1. Đây là sự triển khai dần theo sách, không phải mâu thuẫn mở–kết.

#### Phát hiện cần quyết định

##### F01 — Trung bình — Cầu nối định danh thắng sang giá trị băm chưa hiện rõ trên cụm slide

- **Trang chiếu:** `lec05-s04-01`, `lec05-s05-01`–`lec05-s05-03`, `lec05-s05-06`; ranh giới phần 4→5. Vị trí đối chiếu: HTML dòng 182,226–242,256–260; ghi chú mục 9 đã có cầu nối tốt.
- **Vấn đề:** bài đổi từ chữ ký lưu định danh sang chữ ký lưu giá trị băm. Sự khác kiểu được nói trong notes, nhưng mặt slide chưa chỉ ra chính xác điều gì được giữ khi đổi cách lưu. Sinh viên thấy $(a,d)^{\mathsf T}$ ở 28 rồi $(1,0)^{\mathsf T}$ ở 40; quan hệ giữa hai kết quả cùng ví dụ bị để cho người học tự nối.
- **Bằng chứng:** 28 ghi “$\sigma(S_1)=\sigma(S_4)=(a,d)^{\mathsf T}$”; 35 chuyển sang “Gán giá trị $f_i(r)$ cho hàng $r$; mỗi tập giữ giá trị nhỏ nhất…”; 37 chỉ có mã hàng và hai bảng hàm, notes nói “Hai thứ tự ấy chính là dữ kiện đã dùng ở trang 28” nhưng không viết lại chúng hay nối hai loại kết quả. 40 kết bằng chữ ký số. Ngược lại, lecture-note mục 9 giải thích rõ rằng khi hàm song ánh, so cực tiểu tương đương so định danh thắng.
- **Vai trò trong mạch:** chuyển kết quả xác suất đã chứng minh thành đối tượng thuật toán sẽ tính. **Kết nối vào:** MinHash theo cùng thứ tự và vector định danh ở phần 4. **Kết nối ra:** SIG chứa cực tiểu và vẫn dùng phép so cùng tọa độ ở 46.
- **Đề xuất sửa cục bộ:** ở 35 hoặc 37 nêu ngắn rằng sắp hàng theo $f_i(r)$ tăng dần tạo thứ tự, hàng thắng là hàng có giá trị nhỏ nhất; khi hàm không va chạm, đổi định danh thành giá trị của hàng ấy giữ quan hệ so bằng. Dùng ngay ví dụ nguồn: tọa độ đầu thắng ở $a\leftrightarrow r=0$ nên lưu $f_1(0)=1$; tọa độ thứ hai thắng ở $d\leftrightarrow r=3$ nên lưu $f_2(3)=0$. Một đối chiếu $(a,d)\mapsto(1,0)$ tại 40 nối trực tiếp về28. Giữ điều kiện song ánh/va chạm và phân biệt nó với phân phối chọn đều; không gán thêm bảo đảm xác suất cho hai hàm cố định.
- **Rà lại:** 26–30 để đối chiếu chữ ký định danh; 33–42 và ranh giới phần 4→5; 44–48 nếu sửa cách diễn giải ước lượng ở 46. Không cần thay sườn hoặc mở/kết.

##### F02 — Trung bình — Dữ kiện truyền vào vết quét không đầy đủ trên mặt trang

- **Trang chiếu:** `lec05-s05-03`–`lec05-s05-06`, trọng tâm37 và 39; HTML dòng 238–260. Ảnh riêng37/39/40 đã được xem.
- **Vấn đề:** trang 37 chuẩn bị phép chạy nhưng chỉ dẫn “Dùng ma trận đặc trưng Hình 3.2”, trong khi ma trận đầy đủ gần nhất ở trang 23 là một thứ tự khác, và ma trận gốc ở 20 cách 17 trang. Trang 39 đưa hai trạng thái sau $r=1$ và$r=2$ mà không hiện tập cột cần cập nhật của hai hàng. Điều này làm chuỗi đầu vào→thao tác→trạng thái bị yếu đúng nơi sinh viên phải khái quát thành vòng lặp 41.
- **Bằng chứng:** mặt 37 có bảng $r,f_1(r),f_2(r)$ nhưng không có quan hệ hàng→cột có 1. Trang 38 có đủ “các cột có 1 là 1,4”, nên bước đầu theo được. Mặt39 cho kết quả cột 3 là $(2,4)$ và cột 2 là $(3,2)$ nhưng chỉ giải thích hai phép min giữ nguyên chữ ký cột 4; dữ kiện “hàng 1 chỉ thuộc S3, hàng 2 thuộc S2,S4” nằm trong notes. Trang 40 lại nêu rõ các cột cập nhật, cho thấy chính loại dữ kiện ấy có thể đặt trên mặt mà không cần đổi nội dung.
- **Vai trò trong mạch:** vết chạy làm căn cứ cho giả mã, bất biến và phép đếm $nL$. **Kết nối vào:** ma trận/thưa ở 20–21 và các hàm ở 37. **Kết nối ra:** vòng “mỗi c có M(r,c)=1” ở 41, trạng thái min ở 42, đếm mỗi ô 1 ở 43.
- **Đề xuất sửa cục bộ:** đặt lại ma trận gốc hoặc danh sách đầy đủ các cột có 1 theo hàng ngay cạnh bảng hàm ở 37; có thể dùng bảng ghép năm hàng của lecture-note mục 9. Trên 39 ghi trực tiếp hai hàng đầu vào “$r=1$: cột 3, giá trị $(2,4)$; $r=2$: cột 2,4, giá trị $(3,2)$”. Nêu/đánh dấu rõ trạng thái vào của bước đầu trên 39 và 40 khi rút gọn bảng, hoặc giữ bảng trước–sau như storyboard. Không cần lặp toàn bộ dữ liệu nguồn trên mọi slide; cần đủ để biết mỗi ô kết quả đến từ đâu.
- **Rà lại:** 35–43, đối chiếu 46 và bài 55–57. Nếu tách thêm trang, cập nhật thời lượng và toàn bộ ánh xạ số trang; ưu tiên sửa tại chỗ.

##### F03 — Trung bình — Ký hiệu S4 bị chuyển từ tập sang vector chữ ký

- **Trang chiếu:** `lec05-s05-05`, `lec05-s05-12`; notes tương ứng và các đoạn diễn giải trạng thái trong lecture-note mục 9. HTML dòng 253,300–301; storyboard 39,46.
- **Vấn đề:** $S_4$ đã được định nghĩa là tập $\{a,c,d\}$. Công thức “$S_4=(1,1)$” ở 46 và cách viết “$S_4$ đang có $(1,1)$” ở 39 khiến cùng ký hiệu nhận một kiểu dữ liệu khác ngay trong cụm muốn phân biệt tập và chữ ký.
- **Bằng chứng:** nhiệm vụ 46 là “Giải thích cập nhật $S_4=(1,1)$ bằng $(3,2)$”. Trong đặc tả 36, đối tượng được cập nhật lại là $\mathrm{SIG}(i,c)$. Tập nguồn không thay đổi ở bất cứ bước quét nào.
- **Vai trò trong mạch:** trạng thái cần truyền xuyên vết chạy để suy ra bất biến. **Kết nối vào:** tập/cột đã cố định từ 20 và đầu ra SIG ở 36. **Kết nối ra:** bất biến 42 và việc so chữ ký 46 yêu cầu giữ riêng đầu vào bất biến với trạng thái thay đổi.
- **Đề xuất sửa cục bộ:** viết “chữ ký của $S_4$ đang là $(1,1)$” hoặc dùng cột 4 củaSIG; nhiệm vụ 46 chỉ cập nhật chữ ký, không viết đẳng thức giữa tập và vector. Đồng bộ notes/Markdown/storyboard nơi diễn đạt này xuất hiện. Không đổi số, thuật toán hoặc định nghĩa tập.
- **Rà lại:** 37–41,44–48 và lecture-note mục 9–10. Có thể sửa cùng F01 nhưng phải kiểm riêng tính nhất quán kiểu.

##### F04 — Nhẹ — C xuất hiện trước câu định nghĩa số tài liệu

- **Trang chiếu:** `lec05-s01-05`, HTML dòng 35–39; đối chiếu `n05-01`.
- **Vấn đề và bằng chứng:** mặt 05 bắt đầu bằng $\binom C2=C(C-1)/2$ và $C=10^6$, không có câu “$C$ là số tài liệu”; trang 04 chỉ nói “kho…”. Người đọc có thể suy từ bối cảnh, nhưng ký hiệu tham số chưa được giới thiệu trước công thức. Outline/storyboard và lecture-note mục 1 đã định nghĩa rõ.
- **Vai trò trong mạch:** lượng hóa hạn chế mọi cặp. **Kết nối vào:** kho văn bản ở 04. **Kết nối ra:** cùng $C$ được dùng trong so sánh mọi chữ ký ở 33 và kết 48/50.
- **Đề xuất sửa:** thêm một dòng ngắn “Kho gồm $C$ tài liệu; xét các cặp không thứ tự” trước công thức. Giữ nguyên bài toán, số liệu và luận điểm hai thừa số.
- **Rà lại:**03–07 và các lần dùng $C$ ở 33,48,50; vì sửa phần mở đầu, áp dụng quy tắc rà lại toàn bộ deck nếu editor thay đổi cách đặt vấn đề hoặc luận điểm mở. Bổ sung riêng định nghĩa không cần thiết kế lại tuyến chính.

##### F05 — Nhẹ — Mục lục viewer có hai hệ đánh số xung đột

- **Vị trí:** viewer ghi chú, ảnh `note-1440-top.png`, `note-390-top.png`; `material-viewer.js:222–245`, `material-viewer.css:114–126`.
- **Vấn đề và bằng chứng:** mục lục dùng một danh sách đánh số chung cho cả h2 và h3, đồng thời giữ số đã có trong h2. Ảnh cho thấy “1. 1. Tài liệu gần trùng…”, rồi sau các tiểu mục của phần 3 là “9. 4. Ma trận đặc trưng…”. CSS có thụt tiểu mục 14px, nhưng bộ đếm vẫn không tương ứng bản đồ 14 chủ đề.
- **Vai trò trong mạch:** mục lục là bản đồ tự học của tài liệu dài. **Kết nối vào:** người học chọn một trong 14 chủ đề. **Kết nối ra:** tìm đúng tiểu mục và giữ quan hệ phần → bước lập luận; hiện bộ đếm phụ làm hai cấp trở nên khó nhận diện.
- **Đề xuất sửa:** giữ số trong tiêu đề nguồn và bỏ bộ đếm tự động của mục lục, hoặc dựng danh sách phân cấp h2/h3 đúng nghĩa. Không đổi thứ tự/đánh số 14 chủ đề trong Markdown chỉ để bù hành vi viewer. Đây là hạ tầng dùng chung; nếu sửa JS/CSS cần root xác định phạm vi hồi quy các ghi chú khác.
- **Rà lại:** mục lục rộng/hẹp, đích neo quanh chủ đề 3→4 và 9→10; không yêu cầu đổi nội dung slide hay nguồn toán.

#### Ghi chú tự học, Quill và no-ai-slop

Mười bốn chủ đề tạo chuỗi liên tục: 1 đặt hai giới hạn;2 định nghĩa số đo;3 tạo phần tử;4 tạo biểu diễn chung;5 định nghĩa phép chọn;6 chứng minh;7 gom phép thử thành ước lượng;8 định lượng dao động;9 tính chữ ký;10 chứng minh và đếm;11 phân biệt mô hình/biên;12–13 là hai nhánh đọc thêm;14 tổng hợp và vận dụng. Các chủ đề đọc thêm có nhãn rõ, không là tiên quyết ẩn của bài tập. Việc đặt đa tập và tăng tốc sau tuyến chính không làm gián đoạn một chứng minh đang dở.

Không áp chu trình slide cho ghi chú: Jaccard, shingling, MinHash và chữ ký trong Markdown đều có định nghĩa trước ví dụ. Ở slide, 06→07,11→12,23→24,28→29 giữ trực giác/ví dụ trước hình thức. Cụm quét hàng đặt đặc tả 36 trước vết 37–40 đã có lý do cụ thể trong outline/storyboard: phép min và phần tử thắng đã được xây ở 22–24, trực giác triển khai ở 35. Không đề nghị đảo cụm chỉ để máy móc đồng nhất hai loại tài liệu; F01/F02 tăng cầu nối trong trình tự hiện có.

No-ai-slop Detect đã áp dụng vào tiêu đề, nội dung hiển thị, toàn bộ notes/Markdown và nhãn SVG. Không tìm thấy mẫu văn nói, khẩu hiệu, ca ngợi, câu hỏi tu từ hoặc dẫn nguồn mơ hồ cần lập phát hiện riêng. Các câu phủ định như “Một giá trị ước lượng bằng 1 không đủ suy hai tập bằng nhau” và “Song ánh… không bảo đảm phân phối chọn đều…” có chức năng phân biệt toán học cụ thể, nên giữ; không coi chúng là đối lập tu từ để cắt. Các câu tổng hợp ở 47–50 và mục 14 thực hiện chức năng học tập được yêu cầu, nên cũng giữ. F03 là lỗi chính xác thuật ngữ/kiểu, không phải bằng chứng suy đoán tác giả. Không chấm điểm hoặc suy đoán văn bản do AI viết.

#### Phạm vi sửa và tái kiểm đề nghị

Ưu tiên sửa F01–F03 cùng một lượt cục bộ ở 35–46, đồng bộ tài liệu quy trình và câu liên quan trong ghi chú. Sau sửa, rà các trang bị đổi, hai trang lân cận mỗi phía và ranh giới phần 4→5→6; kiểm lại mối nối 28↔37/40. Nếu thêm/bớt/đổi thứ tự trang, cập nhật đủ ánh xạ và thời lượng. Nếu đổi mở bài, kết bài hoặc luận điểm hai giới hạn, giao rà lại toàn bộ 57 trang. F05 là cải thiện mục lục có phạm vi dùng chung; không cho phép sửa hạ tầng mà bỏ kiểm các ghi chú chịu ảnh hưởng.

Báo cáo này kết thúc ở đề xuất; không có tệp sản phẩm nào được chỉnh sửa.


### Bản lưu: Gate bản thực

### Cửa kiểm storyboard trên bản thực — Bài 05

Ngày 2026-09-28. Reviewer độc lập, chỉ đọc kho; báo cáo này chưa phải một trong năm lượt reader. Không gọi mô hình ngoài, không đọc `.env`, không sửa sản phẩm.

**Kết luận: CẦN SỬA.** Không phát hiện lỗi blocking về định lý, dữ kiện hoặc đáp án. Có **2 lỗi major về khả năng tái tạo phép tính ngay trên trang**, và **7 lỗi minor** về cầu nối ký hiệu, mô hình chi phí, nhãn, nguồn và hình. Kế hoạch vẫn phù hợp; không cần mở lại sườn bài. Sau editor, tái kiểm những vùng nêu dưới đây trước khi coi bản thực đã qua cửa kiểm.

#### Phạm vi và bằng chứng đã đọc

- Đối chiếu ba Markdown hiện hành trong `2627-1/planning/lec-05/` với `lecture-05-bieu-dien-tuong-dong-shingling-va-minhash.html`: đủ 57 trang và 57 notes; 7 phần, phân bố 9/9/9/7/12/4/7. Thời lượng trong planning vẫn 120 + 60 phút; notes bảy trang recitation cộng đúng 60 phút.
- Đọc toàn văn 919 dòng `materials/lec-05/lecture-note.md`, đối chiếu 14 chủ đề với n05-01…n05-14 và đọc XML của cả 8 SVG.
- Đọc `gate-preflight.md`, `implementation-brief.md`, các quyết định điều phối và bảng sai khác bố cục cuối storyboard. Không dùng JSON/script cũ làm đặc tả.
- Dùng trực tiếp sách cục bộ MMDS 3e Chương 3, §§3.1–3.3; trong lượt này mở lại tr. 74–78 và 90–91 để xác minh nguồn và yêu cầu recitation. Dữ kiện §§3.3.1–3.3.5 đã được đọc trực tiếp trong hai lượt gate kế hoạch, được đối chiếu lại với nội dung bản thực.
- Xem contact sheet của toàn bộ 57 ảnh rộng trong `draft-renders/lec05`; xem riêng ảnh rộng 11, 30, 39, 40 và ảnh hẹp 36. Contact sheet phục vụ đối chiếu bố cục, không được coi là kiểm hết chi tiết chữ ở mọi kích thước. Không dùng kết quả không tràn của root làm bằng chứng đạt sư phạm.
- Tính độc lập từ bảng HTML hiện tại: sáu Jaccard của Hình 3.2, vét cạn 120 hoán vị, bốn hàng chữ ký của Ví dụ 3.8/Bài 3.3.2, chữ ký và sáu sai lệch Bài 3.3.3. Kết quả ở `gate-actual-math-check.json`; tất cả khớp bản thực.
- Áp dụng no-ai-slop Detect cho phần công khai và notes; Quill cho mạch, thuật ngữ và ký hiệu. Không thấy lời chỉ dẫn người viết/giảng viên lọt vào học liệu. Những câu về soạn hình ở trường nguồn được hiểu là ghi công, không là việc còn phải làm. Không dùng điểm phát hiện AI.

#### Các lỗi cần sửa

##### IG01 — major — Cụm 37–40 thiếu dữ kiện và trạng thái vào của vết chạy

**Vị trí:** `lec05-s05-03` đến `lec05-s05-06`; HTML dòng 238–260; storyboard phiếu 37–40, nhất là dòng 996, 1048, 1074. Ảnh `wide-39-lec05-s05-05.png`, `wide-40-lec05-s05-06.png` xác nhận bố cục thực.

**Bằng chứng:** Trang 37 chỉ có bảng r/f1/f2 và câu “Dùng ma trận đặc trưng Hình 3.2.”, không có quan hệ hàng–cột. Ma trận đầy đủ gần nhất ở trang 23, các tập đầy đủ gần nhất ở 28. Trang 39 chỉ cho trạng thái sau r=1 và r=2; dữ kiện r=1 thuộc cột 3, r=2 thuộc cột 2/4 nằm trong notes. Trang 40 chỉ có sau r=3 và r=4, không có trạng thái sau r=2 để đối chiếu ba giá trị giảm ở bước r=3. Không bảng nào có dấu nhận diện ô thay đổi.

**Tác động:** Người học phải nhớ cả quan hệ hiện diện lẫn các giá trị cũ để kiểm tra phép min. Bảng kết quả đúng chưa đủ cho mục tiêu truy vết. Đây là đúng nội dung mà storyboard đã giữ đồng thời để giảm tải ghi nhớ; §4 của chuẩn yêu cầu dữ kiện, thao tác, trạng thái trước/sau và khả năng tự tái tạo vết chạy từ dữ kiện hiển thị.

**Điều kiện sửa:**

1. Ở 37, cung cấp lại đầy đủ incidence bằng ma trận hoặc thêm cột “phần tử / các cột có 1” vào bảng hàm. Bảng trong mục 9 của ghi chú là một phương án gọn, đủ dữ kiện; không bắt buộc lặp một ma trận thứ hai.
2. Ở 39, cho thấy trạng thái vào sau r=0 và dữ kiện hai hàng: r=1 → (2,4), cột 3; r=2 → (3,2), cột 2/4. Giữ phép min của cột 4 và đối chiếu cột 2 từ vô cực.
3. Ở 40, cung cấp trạng thái sau r=2 trước bước r=3. Có thể dùng bảng vết chạy ba trạng thái hoặc ghi giá trị cũ→mới đủ rõ, không nhất thiết ba bảng lớn. Đánh dấu các ô giảm bằng chữ/viền; phân biệt các phép min giữ nguyên. Ghi rõ bảng là trạng thái sau hàng nào.

**Rà lại:** 35–42; phép đếm “min không đồng nghĩa ô đổi” ở 43/46; mục 9–10 ghi chú. Giữ nguyên các kết quả và tổng thời lượng, không thu nhỏ chữ để nhét bảng.

##### IG02 — major — Trang 30 mất cầu nối từ tọa độ cụ thể sang chỉ báo

**Vị trí:** `lec05-s04-03`, HTML dòng 194–198; storyboard phiếu 30 dòng 808. Ảnh `wide-30-lec05-s04-03.png`.

**Bằng chứng:** Trang hiện công thức tổng chỉ báo và kết quả `(1+1)/2=1`, nhưng không có hai chữ ký đang được so. Chúng chỉ xuất hiện ở 28; 29 đã chuyển sang vector tổng quát. Notes 30 cũng không ghi lại hai vector. Bố cục được duyệt yêu cầu hai chữ ký cùng đường nối theo tọa độ để các số 1 có căn cứ nhìn thấy.

**Tác động:** Đúng lúc giới thiệu ký hiệu chỉ báo, trang yêu cầu nhớ dữ kiện hai trang trước. Người học không kiểm được số hạng nào đến từ tọa độ nào trên chính trang này.

**Điều kiện sửa:** Khôi phục `σ(S1)=(a,d)^T`, `σ(S4)=(a,d)^T` bằng bảng hai tọa độ hoặc hai vector căn hàng; chỉ rõ a=a và d=d tạo hai chỉ báo 1, rồi mới nối tới tổng/chia n. Giữ quy tắc so đúng chỉ số và phân biệt ước lượng với SIM thật. Không cần lặp cả bốn tập hoặc bốn chữ ký.

**Rà lại:** 28–32 và n05-07. Chấp nhận bảng vai trò hàng/cột hiện tại của trang 29; không bắt buộc khôi phục ma trận ví dụ ở cả 29 lẫn 30.

##### IG03 — minor — Trang 24 chưa giải nghĩa argmin ngay trên mặt; trang 23 thiếu tín hiệu chọn ô đầu

**Vị trí:** `lec05-s03-05/06`, HTML dòng 150–160; storyboard 23–24.

**Bằng chứng:** Trang 24 giới thiệu `argmin` chỉ bằng công thức. Ví dụ `hπ(S1)=a` đối chiếu `rankπ(a)=3` đã được duyệt bị bỏ. Bảng sai khác cuối storyboard nói ví dụ nằm trong notes, nhưng notes 24 thực tế chỉ nói tổng quát về kiểu trả về, không có a/3. Trang 23 có đủ ma trận và kết quả nhưng tất cả ô 1 cùng hình thức.

**Điều kiện sửa:** Thêm một dòng giải thích argmin trả phần tử đạt vị trí nhỏ nhất, cùng cặp a/3 dưới thứ tự b,e,a,d,c. Đánh viền/ký hiệu chữ ở bốn ô 1 đầu của trang 23; không dùng riêng màu. Sửa ghi nhận sai khác để phản ánh đúng nơi ví dụ xuất hiện.

**Rà lại:** 22–26, mục 5 ghi chú. Các số đang đúng; đây là phục hồi cầu nối cho năm 2, không phải sửa định nghĩa.

##### IG04 — minor — Mô hình chi phí chưa đầy đủ trên mặt trang 13/33

**Vị trí:** `lec05-s02-04`, HTML dòng 85–92; `lec05-s04-06`, dòng 212–216; ghi chú mục 3 dòng 128 và mục 7 đã có mô hình tốt hơn.

**Bằng chứng:** Trang 13 nói “Tạo và băm trực tiếp đoạn dài k: O(wk) kỳ vọng” nhưng giả thiết chèn kỳ vọng theo độ dài khóa chỉ nằm trong notes. Chưa rõ dòng này đang tính toàn thuật toán hay chỉ xử lý cửa sổ khi w=0. Trang 33 đặt Θ(n) bên cạnh n phép so bằng nhưng bỏ dòng mô hình từ máy/O(1) mà storyboard đã chỉ định; notes 33 cũng không nêu giả thiết này.

**Điều kiện sửa:** Trang 13 ghi ngắn mô hình tạo/băm/chèn khóa dài k tốn O(k) kỳ vọng; gọi O(wk) là phần xử lý w cửa sổ hoặc dùng tổng O(1+wk). Trang 33 thêm “mỗi thành phần vừa một từ máy; so bằng O(1)” trước cận thời gian, hoặc ghi rõ đang đếm số phép so bằng thay vì thời gian. Đừng dời căn cứ về trang 43 sau đó mười trang.

**Rà lại:** 11–15, 31–35, mục 3/7. Giữ phân tích 43–44 hiện tại: mô hình, bốn phép đếm và phạm vi đầu vào đã có đều đúng.

##### IG05 — minor — Thiếu nhãn “Câu hỏi:” theo chuẩn

**Vị trí:** Trang 09, 18, 27, 34, 46, 49–50 và 51–57; toàn HTML không có chuỗi `Câu hỏi:`.

**Bằng chứng:** Các trang có nhiệm vụ cụ thể và đáp án trong notes, nhưng dùng tiêu đề “Câu hỏi kiểm tra” hoặc chỉ danh sách động từ. Chuẩn dòng 54 yêu cầu nhãn “Câu hỏi:”; nội dung dự kiến của storyboard vẫn có nhãn này.

**Điều kiện sửa:** Thêm nhãn đúng trước khối nhiệm vụ trên các trang kiểm tra/bài tập, không thêm đáp án lên mặt. Có thể giữ nguyên các tiêu đề hiện tại.

**Rà lại:** Các trang vừa nêu, nhất là 46/56 vốn có nhiều dữ kiện; kiểm lại bố cục sau thêm nhãn.

##### IG06 — minor — Sai vị trí nguồn Jaccard và ví dụ khách hàng

**Vị trí:** Trang 06/09, HTML dòng 44–45 và 62–63; trang 08 dòng 56–57; ghi chú dòng 50 và 62.

**Bằng chứng trực tiếp từ sách:** Định nghĩa/Ví dụ 3.1 ở tr. 74 nhưng **Hình 3.1 ở tr. 75**. Phần mua hàng nằm trong **§3.1.3, tr. 76**, không phải §3.1.2. Bản thực gắn Hình 3.1 với tr. 74 và gọi ví dụ khách hàng của §3.1.2. Nội dung và số 3/8 đúng.

**Điều kiện sửa:** Dẫn hình tr. 75 hoặc “Ví dụ 3.1/Hình 3.1, tr. 74–75”; trang 08 dẫn §§3.1.2–3.1.3, tr. 74–76; ghi chú khách hàng đổi thành §3.1.3. Đồng bộ notes, storyboard và mọi chỗ dẫn cùng hình, không thay nhầm nguồn định nghĩa Jaccard tr. 74 vốn đúng.

**Rà lại:** 04–10, n05-01/02, nhãn nguồn SVG nếu bổ sung. Nguồn mới của trang 15 (Ví dụ 3.4, tr. 78) và 23 (Ví dụ 3.7, tr. 82–83) đã đúng.

##### IG07 — minor — Một số biểu thức đồng nhất tập/hàm với giá trị chữ ký

**Vị trí:** Trang 46, HTML dòng 300: “Giải thích cập nhật S4=(1,1) bằng (3,2).” Trang 40, dòng 258: “Hàng 3: (f1,f2)=(4,0)” và tương tự hàng 4.

**Vấn đề:** S4 đã là một tập phần tử, không phải vector; f1/f2 đã là hàm, không phải giá trị tại hàng đang xét. Ngữ cảnh giúp đoán ý nhưng ký hiệu viết ra đổi kiểu đối tượng, trái mục tiêu phân biệt kiểu xuyên bài.

**Điều kiện sửa:** Dùng “chữ ký cột S4 đang có (1,1), nhận ứng viên (3,2)” ở 46; dùng `(f1(3),f2(3))=(4,0)` và `(f1(4),f2(4))=(0,3)` ở 40. Cụm “S4 đang có” ở 39 cũng nên đổi thành “chữ ký của S4”.

**Rà lại:** 37–46, bảng ký hiệu, mục 9 và lời giải. Không đổi hπ trả định danh thành giá trị băm.

##### IG08 — minor — Mũi tên SVG cửa sổ đè nhãn

**Vị trí:** `img/lec-05/cua-so-shingle.svg`, dòng 8–9; trang 10/11 và hình trong mục 3 ghi chú.

**Bằng chứng:** Đường `M320 112V140H95V172` đi qua vùng chữ “Cửa sổ” đặt ở x=75,y=155. Ảnh riêng trang 11 cho thấy nét và đầu mũi tên cắt chữ, mặc dù mọi đối tượng vẫn nằm trong viewBox. Vì vậy kiểm biên viewBox không phát hiện lỗi này.

**Điều kiện sửa:** Dời nhãn hoặc đường nối để nét không đi qua chữ và vẫn trỏ từ cửa sổ đầu đến ô ab đầu tiên. Giữ sáu cửa sổ, chỉ số 0–6 và liên kết hai ab.

**Rà lại:** Cả hai slide 10/11, viewer mục 3 và bản in; xem lại hình thật sau sửa, không chỉ kiểm bounding box.

##### IG09 — minor — Nhánh đọc thêm chưa phát biểu cụ thể cách lấy phần đầu ngẫu nhiên

**Vị trí:** Ghi chú mục 13, dòng 653 và đoạn “Cách chọn phần đầu phải gắn với mô hình lấy mẫu của nguồn.”; outline n05-13 yêu cầu nêu ngẫu nhiên.

**Bằng chứng:** Đoạn mở chỉ nói “m hàng đầu của một hoán vị, với m<R”, còn câu sau dẫn chung về mô hình nguồn. Người đọc độc lập chưa biết chọn hoán vị thế nào và miền m. Bảng xử lý hai vô cực là đúng; đoạn không đưa ra bảo đảm sai số sai.

**Điều kiện sửa:** Nêu rõ trong nhánh đang mô tả: chọn hoán vị đều của U và lấy m hàng đầu, với m nguyên, 1≤m<R. Nếu nhiều phép thử dùng độc lập, nêu khi dùng tính chất đó; không tự áp công thức phương sai có mẫu số n cho số phép thử hữu ích ngẫu nhiên. Có thể bỏ câu nhắc chung về “mô hình nguồn” sau khi đã phát biểu điều kiện cụ thể.

**Rà lại:** Mục 11–14 ghi chú và n05-13 trong planning; không thêm tăng tốc vào core deck.

#### Những sai khác bố cục được chấp nhận

| Sai khác | Quyết định và căn cứ |
|---|---|
| Không lặp ma trận gốc ở 21 | Chấp nhận. Danh sách năm hàng đã chứa đầy đủ quan hệ hiện diện; phép cộng 2+1+2+3+1 và số 20 đủ cho mục tiêu nhận diện biểu diễn thưa. Không cần nhìn ma trận gốc để tái tạo dữ liệu. |
| Trang 12 dùng đặc tả toàn chiều rộng, ví dụ số ở notes | Chấp nhận. Trang 11 liền trước đã có đủ cửa sổ; 12 giải thích cú pháp lát cắt và trường hợp rỗng, không trình bày một phép tính mới thiếu đầu vào. |
| Bảng chữ thay hộp ký tự ở 15; phép mã hóa bằng công thức ở 16 | Chấp nhận. `touch down`/`touchdown`, độ dài và cửa sổ đều hiện rõ; kiểu chữ giữ dấu cách. Độ dài k và byte vẫn được phân biệt. |
| Chứng minh dạng chữ ở 26 | Chấp nhận. Hai bước và tỷ số cùng trang; hình phân loại ở 25 đã xây đối tượng. Notes chứng minh hai chiều, chỉ rõ vai trò hoán vị đều. |
| Bảng vai trò của hai loại ma trận ở 29 | Chấp nhận, với IG02 sửa ở 30. Bảng truyền đạt đúng kiểu hàng và giữ C cột; không có phép thay số thiếu dữ kiện trên 29. |
| Hai thẻ số đếm/tỷ lệ ở 31; thêm độ lệch chuẩn ở 32 | Chấp nhận. Các đại lượng cùng s,n, chứng minh nằm trong notes/ghi chú; tính độc lập xuất hiện trước phương sai. Không hứa từng lần tăng n đều chính xác hơn. |
| Sơ đồ quét 35; bảng chi phí 43/44; danh sách 45/48 | Chấp nhận. Vai trò dữ liệu, giả thiết, bốn phép đếm, đầu ra/đệm và giới hạn xác suất vẫn đầy đủ. |
| Hai thẻ băm bên dưới sơ đồ 47 | Chấp nhận. Thẻ ghi rõ miền thao tác “từng chuỗi con” và “cực tiểu của tập”; sơ đồ có các kiểu dữ liệu. Không có mũi tên gán nhầm bảo đảm. |
| Thẻ sản phẩm thay bảng trống ở 51–57; không vẽ dải vị trí ở 52 | Chấp nhận. Đây là giai đoạn vận dụng sau khi đã học bảng/vết chạy. Dữ kiện nguồn hiện đầy đủ, sản phẩm nêu rõ cột cần nộp; không cần cung cấp sẵn khung đáp án. Riêng 57 dùng kết quả do người học vừa tính ở 56 là phụ thuộc hợp lý của cùng Bài 3.3.3, không tương đương việc giấu dữ kiện một ví dụ giảng mới. |

#### Nội dung đã đạt trong phạm vi gate

Mạch sách và hai giới hạn đầu bài được giữ: Jaccard → shingle → ma trận → MinHash một thành phần → định lý → chữ ký → tính chữ ký, chi phí và giới hạn. 28 là ví dụ cố định trước định nghĩa 29 đúng quyết định điều phối; có đủ bốn tập, hai thứ tự, bốn cột kết quả và phân biệt ước lượng 1 với SIM=2/3. Các chu trình trọng tâm đều còn thành phần cần thiết ở cấp cụm; IG01/02 yêu cầu phục hồi chất lượng hiện thực hóa, không thêm mục mới.

Các sửa G01–G06 của gate kế hoạch vẫn được bảo toàn về nội dung: điều kiện không va chạm ở 17; dữ kiện đầy đủ của 28; đặc tả miền f_i/V/chỉ số/vô cực ở 36; L được định nghĩa công khai ở 43; không còn hai câu chỉ dẫn biên soạn trong notes 52/55; ánh xạ mục tiêu và nguồn Hình 3.4 đã sửa. Các định lý/phép đếm/các biên quan trọng đều đúng: hữu hạn và không rỗng, cùng hoán vị đều, ns so với s, độc lập cho phương sai, cột rỗng trả vô cực nhưng không mở rộng định lý, điều kiện gcd cho affine, bốn phép đếm 8/10/20/18, bộ nhớ tách đầu vào.

Ghi chú 14 chủ đề có thể đọc độc lập ở tuyến chính; định nghĩa đứng trước ví dụ, có vết trạng thái đầy đủ, bất biến ba bước, mô hình chi phí và lời giải. Hai nhánh đọc thêm được tách rõ; công thức đa tập giữ đúng hợp cộng của sách; ví dụ phân nhóm không bị diễn giải thành bảo đảm cho phân hoạch tùy ý. IG09 làm cụ thể giả thiết còn viết chung.

Năm bài recitation giữ dữ kiện/yêu cầu sách. Thêm bảng sai lệch tuyệt đối ở 3.3.3(c) là cách cụ thể hóa yêu cầu “How close…” của nguồn, không là bài toán mới. Tách 3.3.1 và 3.3.3 qua hai trang không nhân thời lượng. Lời giải HTML/Markdown khớp các tính toán độc lập. Bài cuối có tải tính lớn nhất trong 15 phút nhưng dữ kiện ma trận nhỏ, ba hàm và sản phẩm đều rõ; không có căn cứ để thay dữ kiện hoặc tăng thời lượng ở gate này.

#### Điều kiện đóng cửa kiểm

Editor sửa IG01–IG09, ghi quyết định cùng phạm vi tác động vào review-log, và cập nhật đặc tả bố cục thực trong storyboard. Tái kiểm 28–32, 35–46 và hình cửa sổ bằng ảnh mới; rà cục bộ nguồn/nhãn/mô hình/ghi chú theo từng mục. Không cần viết lại sườn 7 phần hoặc đổi 57 trang nếu vẫn giữ được chữ đủ lớn. Lỗi Speaker View, kiểm viewer bàn phím/in, hồi quy CSS và phát hành là các cửa kiểm kỹ thuật riêng của root; báo cáo này không chứng nhận thay các cửa kiểm ấy.


### Bản lưu: Quan sát kỹ thuật của điều phối viên

### Quan sát sơ bộ của điều phối viên trên bản HTML đầu

Ngày 28-09-2026. Đây là quan sát bổ sung, không thay năm báo cáo độc lập. Writer đã báo HTML/SVG/CSS ổn định để root kiểm trong lúc đang viết ghi chú. Chưa sửa sản phẩm theo các phát hiện này; chờ đủ bản nháp, gate và năm báo cáo trước lượt editor riêng.

#### Bằng chứng tự động

- `/tmp/lec05-rebuild/draft-renders/report.json`: 57 trang × rộng 1280×720 / hẹp 390×844 = 114 ảnh; không tràn khung, tràn ngang, chồng footer, KaTeX error, công thức dollar chưa render, ảnh hỏng, lỗi JS/HTTP hoặc request ngoài localhost.
- Reveal có width1280, height720, controlsLayout edges, slideNumber/hashOneBasedIndex/hash true; plugin markdown/highlight/notes/katex. ArrowDown/ArrowRight trên màn rộng, PageDown trên hẹp hoạt động.
- `/tmp/lec05-rebuild/svg/report.json`: 8 SVG, đủ role=img, không có bbox nhãn vượt viewBox.
- Đã xem trực tiếp ảnh nguyên cỡ các trang 28,36,43,46. Dữ kiện và công thức chính đọc được; không thấy cắt nội dung.

#### Phát hiện để editor hợp nhất sau năm báo cáo

| Mã | Mức độ | Vị trí | Vấn đề và bằng chứng | Đề xuất |
|---|---|---|---|---|
| R01 | Trung bình | Trang46, lec05-s05-12, HTML khoảng dòng300; storyboard và notes cùng nhiệm vụ | Câu “Giải thích cập nhật S4=(1,1) bằng (3,2)” dùng S4 (vốn là tập) để chỉ vector chữ ký. Hai kiểu đối tượng bị đồng nhất. | Viết “Giải thích phép cập nhật chữ ký của S4 từ (1,1)^T bằng các giá trị (3,2)^T”, hoặc dùng SIG(:,4) nếu đã định nghĩa. Đồng bộ notes/storyboard và kiểm chỗ tương tự. |
| R02 | Nhẹ | Trang28, lec05-s04-01, HTML khoảng dòng184 | Câu “không là mẫu chứng minh tính ngẫu nhiên đều” không phải cách diễn đạt học thuật rõ; bảng đã ghi hai thứ tự cố định. | Chú thích trực tiếp “Hai thứ tự được chọn cố định để minh họa phép tính”; giả thiết ngẫu nhiên đều thuộc phần định nghĩa/định lý. Giữ điều kiện, bỏ diễn đạt “mẫu chứng minh”. |
| R03 | Trung bình | Trang15, lec05-s02-06, source và notes, HTML khoảng dòng103 | Dẫn Ví dụ3.4 tr79, nhưng bản PDF nguồn đặt toàn bộ ví dụ ngay trước page break sang79, tức trang in78. Root kiểm trực tiếp book-root.txt dòng248–295. | Đổi riêng số trang của Ví dụ3.4 thành78 và đồng bộ ghi chú/planning; phân biệt §3.2.2 (chọn k) nằm79. |
| R04 | Nhẹ | Lần dùng MMDS đầu: notes bìa và source trang4 | Dùng viết tắt MMDS từ đầu; tên đầy đủ Mining of Massive Datasets mới xuất hiện cuối phần giảng. | Giới thiệu tên sách đầy đủ kèm (MMDS) ở notes bìa và nguồn đầu tiên công khai, rồi dùng dạng rút gọn. |
| R05 | Cần reviewer sinh viên/academic xác định | Các trang kiểm tra, ví dụ46 | Trang46 có tiêu đề “Câu hỏi kiểm tra”, nhưng các yêu cầu trực tiếp không có nhãn đúng “Câu hỏi:” theo AGENTS. | Rà toàn bộ trang tương tác/bài tập và thống nhất nhãn; không coi tiêu đề có chữ Câu hỏi là nhãn có dấu hai chấm nếu quy định đang được áp dụng đúng nghĩa đen. |
| R06 | Cần rà thị giác | Trang36, lec05-s05-02 | Ảnh wide36: chevron trái ở mép gần vị trí đầu dòng f_i khi dòng nằm ngang giữa trang. Bbox tổng không tràn, nhưng có thể chạm phần nét chữ f. | Rà hình thật ở nguyên cỡ; nếu che nét, chỉnh cục bộ bố cục để tránh vùng controls, giữ controlsLayout edges và thang chữ chung. Không đổi CSS chung của các bài khác. |
| R07 | Cần gate/flow xác định | Trang28 và29 | Writer thêm σ(S1)=σ(S4) trên ví dụ28, trong khi ký hiệu σ tổng quát được định nghĩa ở29; storyboard28 chỉ cần vector cụ thể. | Có thể hiển thị “Chữ ký S1 và S4: (a,d)^T” ở28 rồi đặt σ ở29 để giữ ví dụ trước ký hiệu tổng quát; nếu giữ, phải định nghĩa rõ ký hiệu tại nơi dùng. |

Bố cục thực của43/46 dùng hai cột và đọc được trên ảnh rộng; nếu khác đặc tả vùng trong storyboard, cần ghi quyết định triển khai và đồng bộ, không tự coi là sai nội dung. Chưa kiểm viewer của ghi chú mới vì writer đang viết.

#### Rà thêm tám SVG và nguồn ví dụ

Đã xem trực tiếp cả tám ảnh SVG ở thư mục `/tmp/lec05-rebuild/svg/`. Các quan hệ giao/hợp, hai thứ tự và số phần tử đúng dữ kiện; kiểm tự động viewBox không thay việc rà đường nối với chữ.

- **R08 — Trung bình — cua-so-shingle.svg, dùng ở trang 11:** đường mũi tên gấp khúc từ cửa sổ đầu đi ngang qua nhãn “Cửa sổ”. Ảnh SVG nguyên cỡ cho thấy nét xanh chạm phần chữ. Dời nhãn hoặc đường nối để tách rõ; giữ vị trí sáu cửa sổ và hai ab. Rà cả slide lẫn viewer sau sửa.
- **R09 — Trung bình — trang 23, lec05-s03-05, source và notes:** HTML dẫn “Ví dụ 3.6, Hình 3.3”. Sách dùng Ví dụ 3.6 cho ma trận Hình 3.2; thứ tự beadc và Hình 3.3 thuộc Ví dụ 3.7 (book-root.txt dòng434–464). Đổi số ví dụ, đối chiếu nguồn ở ghi chú/planning. Cụm “ghi định danh thay hạng” cũng cần tránh gợi ý sách trả hạng: Ví dụ 3.7 đã viết h(S1)=a. Có thể mô tả rõ “định danh phần tử và vị trí được tách riêng trong bảng”.
- **R10 — Trung bình — phan-tu-dau-hop.svg và trang 25, lec05-s03-07:** các thẻ X/Y có kết luận “MinHash trùng/MinHash khác” nhưng trên mặt trang chưa nêu điều kiện **hàng đầu tiên trong hợp** thuộc loại tương ứng. Notes và trang26 có điều kiện đúng; riêng hình25 có thể bị đọc thành có hàng chung thì MinHash luôn trùng. Thêm câu điều kiện ngay trên mặt hoặc trong nhãn hình, giữ vai trò phân loại X/Y/Z và quan hệ của ví dụ. Đối chiếu với math/flow reader trước quyết định cuối.
- **R11 — Nhẹ — quet-ma-tran-thua.svg:** đường nối khối “Tính n giá trị băm” sang khối danh sách chỉ là đoạn thẳng, trong khi đường kế tiếp và vòng lặp có đầu mũi tên. Cân nhắc thêm đầu mũi tên đầu để thống nhất hướng dữ liệu; không đổi cơ chế.

#### R12 — Nghiêm trọng: mở Speaker View làm đổi trang chính

**Vị trí:** phần cấu hình RevealJS cuối HTML Bài 05; plugin Notes cục bộ. Không phải lỗi nội dung.

**Bằng chứng:** `/tmp/lec05-rebuild/speaker-popup-check.json` ghi trước khi nhấn S ở `lec05-s01-09`, index v=8, sau khi mở popup bị lùi sang `lec05-s01-08`, v=7. Đã tái hiện cả sau khi chờ trang sẵn sàng. Popup hiển thị notes của trang8 thay vì trang9.

**Nguyên nhân từ mã cục bộ:** Notes dựng hash receiver bằng `data.state.indexh/indexv` bắt đầu0, nhưng iframe receiver đọc hash theo cấu hình `hashOneBasedIndex:true`. Trạng thái bị trừ1 rồi receiver gửi lại cho cửa sổ chính.

**Giải pháp đã được root thử và chấp nhận để editor triển khai:** chỉ trong HTML Bài 05, dùng `hashOneBasedIndex: !new URLSearchParams(location.search).has("receiver")`. Trình chiếu chính vẫn true; iframe nhận của Speaker View dùng chỉ số0 đúng với URL do plugin sinh. Đây là thích ứng tích hợp cho receiver nội bộ; không sửa vendor, không tác động các deck khác, không thay mạch nội dung.

**Thử nghiệm trước khi sửa repo:** `/tmp/lec05-rebuild/check_speaker_receiver.py` dùng route trong bộ nhớ, không ghi HTML. Kết quả ở `speaker-receiver-prototype.json`: main giữ trang9 khi mở S; notes khớp Jaccard; main→speaker sang trang10 và speaker→main sang trang11 đồng bộ; main hashOneBasedIndex=true, receiver=false. Root cần chạy lại cùng kiểm chứng trên tệp thực sau editor, bỏ route thay HTML trong bộ nhớ.

#### R13 — Nghiêm trọng: công thức trong cửa sổ diễn giả bị lặp hoặc mất nét

**Bằng chứng:** popup của plugin Notes nhận HTML KaTeX đã render nhưng không có CSS KaTeX. Ảnh `speaker-prototype.png` cho thấy “3/83/8” (MathML và HTML cùng hiện). Chỉ thêm stylesheet chưa đủ trong môi trường Chromium này: FontFace của tài liệu `about:blank` do `document.write` tạo còn ở trạng thái loading, công thức bị để trắng. Đóng luồng document không giải quyết nên không áp dụng cách đó.

**Bản thử đã đạt:** `check_speaker_receiver.py` (route chỉ trong bộ nhớ) chèn listener nhận `reveal-notes/connected`, chỉ chấp nhận cùng origin và `event.source.opener === window`. Listener thêm đúng một link `vendor/katex/dist/katex.min.css` (đường dẫn tuyệt đối được giải từ `document.baseURI`) vào head popup; khi stylesheet tải xong, đưa các FontFace của tài liệu bài giảng vào `target.fonts` bằng `for (const face of document.fonts) target.fonts.add(face)`. Không sửa thư viện, không tải mạng, không đưa kiểu tự viết vào JS.

Ảnh `speaker-prototype-fixed.png` đã được root xem: chỉ một công thức 3/8, đúng kiểu chữ, đầy đủ nét. FontFaceSet có status loaded, không còn face đang loading. MathML được ẩn đúng (absolute, clip1px). Đồng bộ hai chiều tiếp tục đạt cùng R12. Mã thử hiện tại trong `/tmp/lec05-rebuild/check_speaker_receiver.py` là phiên bản dùng CSS + chia sẻ FontFace, KHÔNG gọi document.close. Editor có thể lấy khối `popup_css` để triển khai trong HTML Bài05; root sẽ kiểm lại tệp thực cùng các trang công thức phức tạp.

#### Cập nhật trạng thái bản nháp đầy đủ

Writer tự sửa R03 (trang15 nguồn78) và phần dẫn số Ví dụ của R09 (trang23 thành3.7) trước bàn giao; editor xác minh, không lặp sửa không cần thiết. Render draft đã chạy lại sau hai sửa nguồn:114ảnh sạch và kiểm thêm công thức `$...$`/`$$...$$` chưa render. Static audit57IDs/57notes/7sections/8SVG PASS. Viewer1440/390:635KaTeX,21details,47TOClinks; bàn phím, in mở tất cả, sau in đóng lại, invalidpaths từ chối, không lỗi JS/HTTP/ngoại mạng. Root xem toàn bộ36trang in qua3contact sheets: không thấy cắt công thức/bảng/ảnh, lời giải hiện trong in. Các quan sát đọc hiểu vẫn giao reviewer độc lập; ảnh thu nhỏ không thay kiểm nội dung.

#### R14 — Nhẹ: ký hiệu C trong nhánh đa tập

Ghi chú mục12 dùng B,C cho hai đa tập, trong khi bảng ký hiệu toàn bài dùng C cho số tập/tài liệu. Có thể phân biệt từ ngữ cảnh cục bộ, không làm công thức sai, nhưng nên đổi riêng hai đa tập thành B1,B2 và các hàm bội tương ứng khi sửa M05. Điều này giữ một vai trò cho C xuyên tài liệu và không đổi dữ kiện hay quy ước hợp cộng. Reviewer toán cần đối chiếu sau sửa cùng M05.


## Bàn giao sau lượt editor

Editor đã hoàn tất các quyết định được giao, đồng bộ sản phẩm và planning. Sau mốc đóng public, chỉ có hai sửa rõ kiểu đối tượng theo math recheck trong notes trang40 và ghi chú9; đã thông báo root ngay khi thực hiện. Trạng thái: **đã sửa, chờ root tổng hợp tái kiểm cuối và phát hành**. Năm báo cáo độc lập đã có đầy đủ; kết quả math/flow/gate tái kiểm và QA cuối cần được root bổ sung sau khi các lượt đó kết thúc. Không tự ghi PASS thay tác tử chỉ đọc; chưa commit/push trong lượt editor.


## Chốt tái kiểm nội dung của điều phối viên

Ngày 28-09-2026. Editor đã dừng ghi trước lượt này. Điều phối viên đã đọc toàn bộ ba báo cáo tái kiểm cuối: toán học, mạch viết và cửa kiểm storyboard. Cả ba kết luận PASS trong phạm vi được giao; tất cả phát hiện hợp nhất đã được đóng. Không yêu cầu một vòng viết lại hoặc thêm nội dung ngoài sách. Kết luận dựa trên bản HTML có SHA-256 `37983375fc5ca8f923bc1ccf28af755a3dbe2c47af1eb23df8f8993cad61c3ae` và ghi chú có SHA-256 `fef08ee7eeb2a1cf91a5ef92ef84c59b1d871c8312302ff96707ac7c8878b287`.

Mạch cuối lấy MMDS 3e Chương 3, §§3.1–3.3 làm sườn: Jaccard → shingling → ma trận đặc trưng → MinHash theo hoán vị → chữ ký và ước lượng → thuật toán tính chữ ký, tính đúng, chi phí và giới hạn. Các nguồn slide bổ trợ bố cục hoặc cách biểu diễn, không quyết định lại sườn bài. Phần phương sai, bất biến và phép đếm được ghi là suy luận bổ sung có giả thiết; LSH giữ ở Bài 06. Văn phong học thuật, ký hiệu nhất quán và việc không có chỉ dẫn cho người soạn đã qua editor cùng các reviewer độc lập.

Giới hạn học thuật được giữ công khai: lời giải Bài 3.2.3 nêu đáp số và chứng minh cận trên; không tuyên bố phép đếm cửa sổ đã chứng minh tồn tại chuỗi đạt cận. Dữ kiện sách không bị thay để né giới hạn này.


### Bản lưu cuối: Tái kiểm toán học

### Tái kiểm toán học và thuật toán — Bài 05

Tác tử: `lec05_math_review`, tiếp tục tác tử native của lượt rà độc lập. Ngày 2026-09-28. Chỉ đọc kho; chỉ ghi báo cáo và công cụ kiểm trong `/tmp/lec05-rebuild/`.

#### Phạm vi tái kiểm

Đọc `math-review.md`, quyết định điều phối `review-decisions.md`, các đoạn HTML/notes/Markdown/SVG hiện tại liên quan M01–M07, R14, IG04, IG09, AR03, F01. Kiểm lại các trang 13, 23–27, 29–40, 41–46 và 51–57 cùng các mục ghi chú 3, 5–13, 14 trong phạm vi bị ảnh hưởng. Không đọc báo cáo reviewer khác hoặc dùng hồ sơ nguồn thay cho sản phẩm.

Quan sát bảy ảnh render cuối rộng 1280 × 720: trang 25, 32, 35, 37, 38, 39, 40 trong `final-renders/lec05/`. Đây là kiểm trực quan các công thức, điều kiện và dấu trên bảng của cụm thay đổi, không phải kiểm hiển thị lại toàn bộ 57 trang hoặc bản hẹp/in.

Tiếp tục dùng no-ai-slop Detect và Quill để kiểm diễn đạt điều kiện và sự liên tục của loại đối tượng; không sửa văn phong, không tạo dự án sách. Không thêm nguồn, bài toán hay chứng minh kiến tạo ngoài quyết định đã duyệt.

#### Kết quả từng mục

| Mã | Kết quả trên bản công khai | Bằng chứng tái kiểm |
|---|---|---|
| M01 | **Đạt.** | `lec05-s05-05` nói chữ ký của $S_4$; `lec05-s05-06` dùng $(f_1(3),f_2(3))$ và $(f_1(4),f_2(4))$; `lec05-s05-12` không còn viết $S_4=(1,1)$. Câu hỏi/lời giải mục 9 phân biệt chữ ký thay đổi với tập đầu vào cố định. Sau xác nhận editor, đã đọc lại notes trang 40 (HTML dòng 260): “Hàng 3 hạ thành phần thứ hai của chữ ký của ...”; mục 9 (Markdown dòng 470): “Hàng $3$ cung cấp ứng viên $(4,0)$ cho chữ ký của ...”. Cả hai câu còn sót đã gọi đúng loại đối tượng. |
| M02 | **Đạt.** | Trang 52 nêu công khai “mỗi ký tự chiếm một byte”; notes và mục 14 giải thích $\ell$ vị trí ký tự theo mô hình ấy, không áp ngầm vào ký tự nhiều byte. Đề nguồn và giả thiết số chuỗi độ dài $k$ được giữ. |
| M03 | **Đạt.** | SVG thêm nhãn nhìn thấy “Xét loại của phần tử đầu tiên trong hợp”; loại $Y$ là “thuộc đúng một tập”. Ảnh trang 25 hiển thị đủ điều kiện này. Phân hoạch vẫn là $X=\{a,d\},Y=\{c\},Z=\{b,e\}$. |
| M04 | **Đạt.** | Mục 12 phục hồi chín vị trí in nghiêng `A, for, the, that, have, it, is, for, to`, phân biệt hai vị trí `for`, kèm bảng chín shingle ba từ. Các hàng khớp đúng Ví dụ 3.5, không thay danh sách từ dừng bằng nguồn ngoài. |
| M05 | **Đạt.** | Trước tỷ số đa tập, mục 12 nêu hai đa tập hữu hạn và $\sum_u(m_{B_1}(u)+m_{B_2}(u))>0$. Không mở rộng định lý MinHash tập hợp cho công thức đa tập. |
| M06 | **Đạt theo quyết định phạm vi của root.** | Notes trang 52 và khối “Đáp số và cận trên” ở mục 14 phân biệt đáp số $\max(0,\ell-k+1)$ với lập luận đếm cửa sổ chỉ chứng minh cận trên. Cả hai nói rõ phần tồn tại chuỗi đạt cận không được chứng minh trong phác thảo. Không thêm de Bruijn; không đổi giả thiết thành $\ell$ ký tự khác nhau. |
| M07 | **Đạt.** | Ví dụ khách hàng dẫn §3.1.3; trang 23 ghi “bổ sung bảng đối chiếu định danh và vị trí”, không còn gọi đây là thay hạng của Ví dụ 3.7. Tham chiếu Hình 3.1 đã sửa trang in 75; định nghĩa vẫn dẫn trang 74. |
| R14 | **Đạt.** | Hai đa tập được đổi nhất quán sang $B_1,B_2$ trong định nghĩa số lần, giả thiết, công thức và ví dụ. Ký hiệu $C$ giữ vai trò số tập/tài liệu. Tỷ số $3/9=1/3$ và tự tương đồng $1/2$ không đổi. |
| IG04 | **Đạt.** | Trang 13 nêu tạo, băm, chèn khóa dài $k$ tốn $O(k)$ kỳ vọng mỗi cửa sổ, tổng $O(1+wk)$ kỳ vọng; trường hợp $w=0$ vẫn có khởi tạo. Trang 33 nêu mỗi thành phần vừa một từ máy, so bằng $O(1)$ trước kết luận $\Theta(n)$ và $nC(C-1)/2$. Các giả thiết tương ứng có trong ghi chú mục 3 và 7. |
| IG09 | **Đạt.** | Mục 13 chọn đều một hoán vị của $U$, rồi xét $m$ hàng đầu với $m$ nguyên và $1\le m<R$. Ba trường hợp hữu hạn/vô cực giữ đúng; hai vô cực bị loại khỏi tử và mẫu, mẫu bằng 0 thì chưa xác định. Không áp lại $s(1-s)/n$ khi số phép thử hữu ích ngẫu nhiên. |
| AR03 | **Đạt.** | Trang 32 hiển thị đủ hệ số $1/n^2$, phương sai tổng, bước chuyển sang tổng phương sai gắn nhãn “độc lập”, rồi $ns(1-s)/n^2=s(1-s)/n$. Giả thiết các hoán vị đều kế thừa trang 31; độc lập thêm ở trang 32. SD chuyển sang notes đúng công thức; câu về sai số của từng mẫu vẫn được giới hạn. |
| F01 | **Đạt.** | Trang 35 nêu không va chạm ⇒ sắp giá trị băm tăng dần xác định hàng thắng ⇒ lưu giá trị của hàng đó bảo toàn so bằng định danh, cùng các hàm cho mọi cột. Trang 37 cho lại mã hàng, danh sách cột và hai thứ tự cố định. Trang 40 công khai $(a,d)^{\mathsf T}\mapsto(f_1(0),f_2(3))^{\mathsf T}=(1,0)^{\mathsf T}$. Notes/mục 9 nêu $a\leftrightarrow0$, $d\leftrightarrow3$ và không suy tính chọn đều từ không va chạm. |

#### Bảng vết chạy và bảo toàn dữ kiện

Đã đối chiếu trực tiếp các bảng HTML mới với `math-check-independent.json` của lượt tính độc lập trước, bằng `math-recheck-tables.py`. Tệp kết quả `math-recheck-tables.json` ghi **PASS**. Không chạy lại phép liệt kê 120 hoán vị khi dữ kiện không thay đổi.

- Trang 37: năm hàng mã $a/0$ đến $e/4$, danh sách cột có 1 và hai cột giá trị băm không đổi. Hai thứ tự tăng vẫn là $(e,a,b,c,d)$ và $(d,a,c,e,b)$.
- Trang 38: chỉ bốn ô $(i,c)$ với $i\in\{1,2\},c\in\{1,4\}$ nhận 1 từ $+\infty$; viền đậm đánh dấu đúng cả bốn ô.
- Trang 39: sau $r=1$, chỉ hai thành phần của cột 3 giảm từ vô cực xuống $(2,4)$; sau $r=2$, chỉ hai thành phần cột 2 giảm xuống $(3,2)$. Cột 4 giữ $(1,1)$, không gạch dưới. Chú giải nói rõ mỗi ô là hai thành phần chữ ký và $\infty$ viết gọn cho $+\infty$.
- Trang 40: sau $r=3$, chỉ tọa độ hai của cột 1, 3, 4 được gạch dưới tại 0; sau $r=4$, chỉ tọa độ một của cột 3 được gạch dưới tại 0. Mọi giá trị còn lại giữ nguyên. Hàng nền đầu mỗi bảng không đánh dấu một lần cập nhật mới.
- Các đầu vào recitation trang 53–57 giữ nguyên hai ma trận của Hình 3.2/3.4 và Hình 3.6. Đã đọc lại notes recitation và lời giải chữ ký/ước lượng ở mục 14: các hàm modulo 5, modulo 6, ma trận chữ ký, sáu ước lượng, Jaccard thật và sai lệch tuyệt đối không thay so với bản đã tính độc lập.
- Phân tích chi phí quét vẫn là $\Theta(nC+nR+RC+nL)$ với ma trận đặc và $\Theta(nC+nR+nL)$ với danh sách hàng đã có; số đếm $8,10,20,18$ giữ nguyên. Đầu ra và bộ đệm vẫn tách khỏi dữ liệu đầu vào. Không có bước cập nhật mới làm thay đổi bất biến hoặc điều kiện dừng.

#### Giới hạn

Kết luận M06 chỉ xác nhận cách công bố đúng mức phác thảo đã được root duyệt. Lập luận đếm vị trí **không được xem là chứng minh tính đạt cận**. Lượt này không bổ sung chứng minh tồn tại.

Không rà JavaScript, bàn phím, viewer, bản in, Codex Slides hoặc toàn bộ CSS chung. Bảy ảnh đã quan sát chứng minh các điều kiện, công thức và dấu bảng của cụm sửa có hiện trên bản render rộng; không suy kết quả QA ngoài phạm vi ấy.

#### Kết luận cuối

**PASS theo phạm vi tái kiểm.** M01–M07, R14, IG04, IG09, AR03 và F01 đã đạt; không còn lỗi toán học hoặc thuật toán chưa xử lý trong các thay đổi được giao kiểm. Các bảng vết chạy, dấu đánh dấu cập nhật và dữ kiện số được bảo toàn. Giới hạn của M06 và phạm vi kiểm hiển thị được giữ rõ như trên. Không sửa tệp sản phẩm trong kho.


### Bản lưu cuối: Tái kiểm mạch viết

### Tái kiểm mạch viết sau editor — Bài 05

Ngày 28-09-2026. Tác tử `/root/lec05_flow_review`. Chỉ đọc sản phẩm; áp dụng no-ai-slop Detect và Quill để kiểm sự liên tục, không tạo `quill.json`.

#### Kết luận

**PASS theo phạm vi tái kiểm mạch viết.** F01–F05 đã được xử lý. Những thay đổi tại 24, 28, 30, 32, 35–40 và 46 khép các bước suy luận hoặc làm rõ kiểu dữ liệu; không đổi luận điểm chính, sườn MMDS 3e §§3.1–3.3, thứ tự phần hay mục tiêu học tập. Không còn phát hiện cần editor sửa trong phạm vi đã đọc và xem dưới đây.

Đây là tái kiểm của vai mạch viết, không thay kiểm toán toán học, cửa kiểm storyboard, kiểm hiển thị toàn bộ hay quyết định phát hành của điều phối viên.

#### Phạm vi và bằng chứng

- Đọc lại `flow-review.md`, `review-decisions.md`, bản HTML hiện tại và các đoạn Markdown/planning liên quan. Không đọc báo cáo tái kiểm của reviewer khác, báo cáo gate hoặc observations riêng của root.
- Đọc trực tiếp toàn bộ chữ hiển thị và notes của **03–07, 22–50**: gồm các trang sửa được giao, hai trang lân cận mỗi phía, các ranh giới 4→5→6, và đối chiếu xa 28↔40. Đã đọc đầy đủ 57 slide/notes, 14 chủ đề và ba planning files trong lượt độc lập trước; lượt này không tự nhận đọc lại toàn bộ 57 slide hoặc toàn bộ ba planning files.
- Trong lecture-note, đọc lại mục 1, phần định nghĩa/ví dụ của mục 5, mục 7–13, phần tổng hợp và lời giải Bài 3.2.3 ở mục 14; đối chiếu các câu liên quan trạng thái chữ ký trong mục 9–10. Đọc bảng hành trình, chu trình cụm, phiếu/các quyết định hiện hành liên quan trong outline và storyboard. Phần ghi nhận bố cục cũ trong storyboard được gắn rõ là hồ sơ trước editor; không nhầm với đặc tả hiện hành.
- Xem sáu contact sheet do tác tử ghép từ ảnh cuối, phủ **03–07 và 22–50**, tại `flow-qa/final-03-07.png`, `final-22-27.png`, `final-28-33.png`, `final-34-39.png`, `final-40-45.png`, `final-46-50.png`. Xem thêm ảnh riêng 1280×720 của **32, 37, 39, 40** trong `final-renders/lec05/`.
- Viewer: xem `final-materials/note-1440-top.png` và `note-390-top.png`; đọc quy tắc mục lục hiện hành trong `material-viewer.css`. Xác nhận cách đánh số và phân cấp bằng ảnh; không kiểm lại hành vi neo/bàn phím, không mở lại toàn bộ ảnh hẹp của slide hay bản in cuối. Ảnh viewer sẵn có được dùng cho mục lục; các câu notes-only mới nhất được kiểm từ nguồn hiện tại, không tuyên bố ảnh viewer đã phản ánh lần dựng lại sau chúng.
- Nền đối chiếu nguồn là phần mở Chương 3 cùng §§3.1–3.3, tr. 73–91 đã đọc trực tiếp từ PDF cục bộ ở lượt đầu. Lượt này kiểm việc giữ dữ kiện, điều kiện và nhãn nguồn của các vùng sửa; không thực hiện lại vai kiểm toán nguồn toàn phần.

Bản HTML được đọc có SHA-256 `37983375fc5ca8f923bc1ccf28af755a3dbe2c47af1eb23df8f8993cad61c3ae`; lecture-note có SHA-256 `fef08ee7eeb2a1cf91a5ef92ef84c59b1d871c8312302ff96707ac7c8878b287`.

#### Đóng các phát hiện F01–F05

| Mã | Vai trò, kết nối vào → ra | Bằng chứng sửa và kết luận |
|---|---|---|
| F01 | Chuyển MinHash định danh ở phần 4 thành giá trị mà thuật toán phần 5 lưu; nhận cùng thứ tự, trả SIG dùng để so tọa độ ở 46 | **Đã đóng.** 35 nêu sắp tăng giá trị xác định hàng thắng và không va chạm bảo toàn so bằng định danh. 37 có đủ phần tử/mã hàng, hai thứ tự sắp tăng đúng 28. 40 ghi công khai $(a,d)^{\mathsf T}\mapsto(f_1(0),f_2(3))^{\mathsf T}=(1,0)^{\mathsf T}$. Notes 37/40 và mục 9 nêu $a\leftrightarrow0$, $d\leftrightarrow3$. Điều kiện không va chạm được giữ riêng với điều kiện phân phối chọn đều; không biến ví dụ cố định thành bảo đảm xác suất. |
| F02 | Vết chạy nối dữ kiện ma trận/thưa và các hàm với vòng lặp, bất biến, phép đếm $nL$ | **Đã đóng.** 37 có đủ năm hàng, cột chứa 1 và hai giá trị băm. 38 có khởi tạo và sau $r=0$. 39 giữ trạng thái vào sau $r=0$, dữ kiện $r=1,2$ và hai trạng thái ra. 40 giữ trạng thái vào sau $r=2$, ứng viên/cột của $r=3,4$ và kết quả. Dấu gạch dưới phân biệt thành phần giảm; ví dụ giữ nguyên ở cột 4 vẫn dẫn đúng sang lập luận “mỗi phép min không nhất thiết đổi ô” tại 43/46. |
| F03 | Giữ tập đầu vào bất biến, phân biệt với trạng thái chữ ký thay đổi; nhận đặc tả 36, trả đối tượng cho bất biến 42 và kiểm tra 46 | **Đã đóng.** 39 viết “Chữ ký của $S_4$ giữ $(1,1)$”; 46 yêu cầu phép min của chữ ký của $S_4$, không còn đẳng thức tập = vector. Notes và mục 9–10 giữ cách gọi tương ứng, kể cả các câu mô tả cập nhật $S_3$, $S_2$ và $S_4$. Bảng vẫn dùng tên tập để gọi cột; chú giải nói mỗi ô chứa hai thành phần chữ ký nên không gây đổi kiểu ngầm. |
| F04 | Đặt tham số của giới hạn số cặp; nhận kho ở 04, trả $C$ cho chi phí 33 và tổng kết 48/50 | **Đã đóng.** Trước công thức ở 05 đã có “Kho gồm $C$ tài liệu; xét các cặp không thứ tự.” Ví dụ một triệu, phép đếm và luận điểm hai thừa số không đổi. Ghi chú mục 1 đồng bộ. |
| F05 | Mục lục là bản đồ vào 14 chủ đề và các bước bên trong mỗi chủ đề | **Đã đóng trong phạm vi hiển thị mục lục.** Ảnh rộng/hẹp cho một dãy số chủ đề gốc; các h3 thụt vào và không chen số tự sinh. Chuyển chủ đề 3→4 còn đúng số 4. Quy tắc `list-style: none` giới hạn vào ghi chú lec-05; giữ quy tắc thụt h3. Không đổi thứ tự hay số chủ đề Markdown. Việc tương tác với đích neo thuộc bộ kiểm kỹ thuật riêng. |

#### Những cầu nối bổ sung và ranh giới

| Vùng | Đầu vào → chức năng mới được phục hồi → đầu ra | Kết quả |
|---|---|---|
| 22–26, trọng tâm 24 | Trực giác và ví dụ 23 → argmin trả phần tử, đối chiếu $a$ với hạng 3 → đối tượng của biến cố trùng ở 26 | PASS. Ví dụ ngay dưới định nghĩa làm rõ kiểu trả về; không đổi quy ước MinHash. Mục 5 của ghi chú vẫn đặt định nghĩa trước ví dụ, còn slide vẫn 23 trước 24. |
| 27–30, trọng tâm 28/30 | Một lần trùng không đủ kết luận → ví dụ hai tọa độ cụ thể → vector ở 29 và hai chỉ báo ở 30 | PASS. 28 không dùng $\sigma$ trước định nghĩa 29. 30 có bảng $a/a$, $d/d$ và chỉ báo tương ứng; phép cộng $(1+1)/2$ có dữ liệu để kiểm. Không bị biến thành một công thức đứng riêng. |
| 30–34, trọng tâm 32 | Chỉ báo và kỳ vọng ở 30–31 → dùng độc lập để cộng phương sai → đánh đổi độ dài/chất lượng/chi phí ở 33–34 | PASS. Chuỗi hệ số $n^{-2}$, phương sai tổng, tổng phương sai có nhãn độc lập và kết quả $s(1-s)/n$ hiện trên mặt 32. Độ lệch chuẩn ở notes không là bước cần để hiểu kết luận. Mục 8 dùng cùng điều kiện và giải thích hiệp phương sai. |
| Phần 4→5, 33–37 | Chi phí so sánh và kiểm tra chữ ký → nhu cầu tính chữ ký trong thực hành → đặc tả và dữ liệu chạy | PASS. 35/36 nói rõ đại lượng được tính là giá trị min. Các phân biệt xác định/ngẫu nhiên và định danh/giá trị được giữ. |
| Phần 5→6, 44–50 | Bộ nhớ, giới hạn hàm và kiểm tra thuật toán → quy trình biểu diễn → thu hồi giới hạn số cặp và chuyển Bài 06 | PASS. 46 dùng trực tiếp kết quả ở 40, phép min ở 39 và đếm $nL$ ở 43. 47 tổng hợp các phép đổi biểu diễn; 48/50 giữ số cặp bậc hai. Không có kết quả vừa sửa bị bỏ lại. |

#### Ghi chú, nguồn và mức ảnh hưởng

Mục 9 hiện tạo đúng chuỗi định nghĩa đầu ra → dữ kiện đầy đủ → hai thứ tự liên hệ mục 7 → vết chạy → giả mã. Mục 10 nhận đúng SIG để chứng minh và đếm; mục 11 phân biệt tính đúng của phép min với bảo đảm xác suất. Các câu vừa sửa về “chữ ký của tập” nhất quán với dữ liệu đầu vào không thay đổi. Không áp máy móc tiêu chí trực giác-trước-hình-thức của slide lên ghi chú.

Nguồn và dữ kiện đi cùng các sửa: 24 theo §§3.3.2–3.3.3 với quy ước định danh được công khai; 28 dùng Hình 3.2 và hai thứ tự suy từ Ví dụ 3.8; 30/31 theo §3.3.4; 32 được ghi là hệ quả suy bằng phương sai của chỉ báo độc lập; 37–40 giữ Hình 3.4/Ví dụ 3.8, tr. 85–86. Các bảng trạng thái của note và slide cho cùng kết quả cuối. Outline/storyboard hiện hành ghi cùng cầu nối và vai trò.

Nhánh đọc thêm vẫn tách khỏi tiên quyết tuyến chính: mục 12 đổi đa tập thành $B_1,B_2$, không chiếm lại $C$; danh sách chín vị trí từ dừng đi cùng bảng chín shingle của ví dụ nguồn. Mục 13 định nghĩa cách chọn và miền của $m$ trước bảng ba trường hợp, giữ cảnh báo mẫu số hữu ích ngẫu nhiên. Bài 3.2.3 ghi đúng mức “đáp số và cận trên”, không dùng phần đạt cận chưa chứng minh làm tiên quyết cho bài sau. Các sửa này không kéo thêm một chủ đề bắt buộc vào hành trình slide.

**Mở/kết và phạm vi toàn bài:** bổ sung định nghĩa $C$ ở 05 là sửa tiên quyết ký hiệu cục bộ. Tình huống tài liệu gần trùng ở 04, phép tách số cặp × chi phí một cặp ở 05, giới hạn dung lượng triển khai ở 19/44 và kết luận 47–50 không đổi ý nghĩa. Notes 48 tiếp tục thu hồi cả bộ nhớ được giảm và số cặp chưa giảm; ghi chú mục 1 đặt hai giới hạn ngay từ đầu. Do không đổi mở bài theo nghĩa bài toán/luận điểm, không đổi kết bài hay mục tiêu, không phát sinh yêu cầu làm lại toàn bộ review 57 trang trong lượt này. Bảy chức năng section và cấu trúc 120 + 60 phút vẫn như báo cáo độc lập trước.

No-ai-slop Detect trên các đoạn vừa tái kiểm không phát hiện câu rỗng, lời dẫn giảng viên, khẩu hiệu hoặc câu hỏi tu từ mới. Các câu phủ định về va chạm, kỳ vọng và sai số có chức năng phân biệt giả thiết/kết luận nên được giữ. Quill xác nhận mỗi đoạn sửa có đầu vào đã chuẩn bị và đầu ra được dùng ở bước kế; không tạo thuật ngữ hoặc ký hiệu trọng tâm chưa được giải nghĩa trong vùng kiểm.

Không sửa tệp sản phẩm. Các công cụ trích chữ và contact sheet chỉ nằm trong `/tmp/lec05-rebuild/flow-qa/`.


### Bản lưu cuối: Tái kiểm storyboard trên bản thực

### Tái kiểm cửa kiểm storyboard trên bản thực — Bài 05

Ngày 2026-09-28. Vai trò: reviewer độc lập của cửa kiểm storyboard, chỉ đọc sản phẩm và planning; không sửa kho, không gọi mô hình ngoài. Báo cáo này kiểm bản sau editor theo `review-decisions.md`, tiếp nối `storyboard-implementation-review.md`.

**Kết luận: PASS.** IG01–IG09 đã được xử lý đúng trên bản thực. Không còn điều kiện sửa mở trong phạm vi cửa kiểm này. Hai bổ sung được điều phối viên giao kiểm thêm — AR-03 tại trang 32 và F01 tại ranh giới phần 4→5 — cũng đạt. Có thể đóng cửa kiểm storyboard; việc phát hành vẫn theo các kết quả kỹ thuật và tái kiểm chuyên môn riêng do root tổng hợp.

#### Phạm vi kiểm trực tiếp

- Đọc quyết định hợp nhất của root và bảng quyết định sau editor trong `review-log.md` dòng 192–237. Các báo cáo cũ được lưu với nhãn lịch sử rõ; không coi câu “cần sửa” trong bản lưu là trạng thái hiện hành.
- Đọc HTML/notes hiện tại của các trang bị IG01–IG09 tác động, toàn cụm 22–46 cùng các trang kiểm tra/recitation, và đối chiếu phiếu storyboard tương ứng. Đọc lại các đoạn ghi chú mục 2–3, 7–14 có sửa về nguồn, chi phí, ký hiệu, cầu nối và nhánh đọc thêm.
- Xem trực tiếp 16 ảnh rộng nguyên cỡ tại `final-renders-notes/lec05`: **11, 13, 23, 24, 25, 30, 32, 33, 35, 36, 37, 38, 39, 40, 46, 52**. Các nhận xét về dữ kiện đồng thời và dấu thay đổi bên dưới dựa trên ảnh thật, không suy từ phép kiểm không tràn.
- Đọc phần tổng hợp của `final-renders-notes/report.json`: 114 ảnh, không lỗi trang/tài nguyên/request ngoài máy cục bộ. Đây là bằng chứng kỹ thuật do root tạo, chỉ dùng bổ trợ; reviewer không tự nhận đã xem lại toàn bộ 114 ảnh.
- Kiểm trực tiếp 57 slide, 57 notes, 57 thời lượng trong storyboard; cộng được 120 phút giảng và 60 phút recitation. Kiểm đủ 14 nhãn “Câu hỏi:” trong các trang được yêu cầu.
- Kiểm bảy liên kết ảnh Markdown trong storyboard: đều dùng `../../img/lec-05/...` và đều trỏ tới tệp tồn tại khi giải từ thư mục chứa storyboard.

#### Kết quả từng mục

| Mã | Kết quả | Bằng chứng bản thực và phạm vi tái kiểm |
|---|---|---|
| **IG01** | **PASS** | Trang 37 có bảng đủ phần tử/mã hàng, các cột có 1, giá trị hai hàm; không còn phụ thuộc câu dẫn “dùng ma trận Hình 3.2” để biết incidence. Trang 39 hiện sau r=0/1/2, ứng viên (2,4), (3,2) và cột nhận. Trang 40 hiện sau r=2/3/4 cùng dữ kiện r=3/4. Mỗi ô giữ cặp thành phần theo cùng thứ tự; chú giải nói rõ cách đọc và quy ước vô cực. Gạch dưới đánh dấu đúng các thành phần vừa giảm: hai thành phần cột 3 ở r=1; hai thành phần cột 2 ở r=2; thành phần thứ hai cột 1/3/4 ở r=3; thành phần thứ nhất cột 3 ở r=4. Trang 38 đánh viền đúng bốn ô từ vô cực thành 1. Phép min không đổi của cột 4 vẫn hiện trên 39. Đọc lại 35–46 và mục 9–10: vết chạy, giả mã, bất biến và số 18 phép min tiếp tục khớp. |
| **IG02** | **PASS** | Trang 30 đã có bảng hai tọa độ của chữ ký S1/S4, a=a và d=d, mỗi dòng tạo chỉ báo 1, rồi tổng/chia 2. Công thức, bảng và kết quả cùng nhìn thấy trên ảnh rộng. Notes nêu lại hai vector và SIM thật 2/3. Phiếu 30 ghi đúng bố cục này. Vùng 28–32 vẫn giữ ví dụ cố định → định nghĩa vector → chỉ báo → kỳ vọng → phương sai. |
| **IG03** | **PASS** | Ảnh 23 có bốn ô 1 đầu viền đậm đúng vị trí, kèm chú giải không dựa riêng vào màu. Trang 24 giải nghĩa argmin trả phần tử; thứ tự (b,e,a,d,c), hπ(S1)=a và rankπ(a)=3 cùng hiện. Notes 24 có tập S1={a,d} và giải thích hai kiểu giá trị; phiếu đã đồng bộ. Rà 22–26 không phát hiện bước suy luận bị mất hoặc đảo. |
| **IG04** | **PASS** | Trang 13 công khai giả thiết tạo/băm/chèn khóa dài k tốn O(k) kỳ vọng cho mỗi cửa sổ, tổng O(1+wk) kể khởi tạo. Notes phân biệt phần xử lý cửa sổ O(wk); mục 3 ghi tổng gồm khởi tạo. Trang 33 đặt mô hình mỗi thành phần vừa một từ máy, so bằng O(1) trước Θ(n); notes và mục 7 cùng giả thiết. Các phép đếm 43–44 giữ nguyên mô hình, đầu vào đã có, nC/nR/RC/nL và bộ nhớ tách đầu vào. |
| **IG05** | **PASS** | Có nhãn đúng “Câu hỏi:” ở 09,18,27,34,46,49–57: đủ 14 trang. Recitation ghép nhãn vào dòng yêu cầu, không đưa lời giải lên mặt. Ảnh 46 và 52 cho thấy nhãn không làm mất dữ kiện hoặc sản phẩm cần nộp. |
| **IG06** | **PASS** | Trang 06/09 và ghi chú mục 2 dẫn Hình 3.1 tr. 75; trang 07 tách đúng định nghĩa §3.1.1 tr. 74 với hình tr. 75. Trang 08 dẫn §§3.1.2–3.1.3; đoạn khách hàng ở ghi chú dòng 62 dẫn §3.1.3, tr. 76. Phiếu và outline giữ nguồn phù hợp. Nguồn Ví dụ 3.4 tr. 78 và Ví dụ 3.7 tr. 82–83 vẫn đúng; 23 không còn nói sách trả hạng rồi bị đổi sang định danh. |
| **IG07** | **PASS** | Trang 39/46 và notes dùng “chữ ký của S4”, không còn S4=(1,1). Trang 40 ghi f1(3),f2(3) và f1(4),f2(4), phân biệt hàm với giá trị tại một hàng. Notes 40 và mục 9 đã đổi các câu cập nhật sang “thành phần/ứng viên của chữ ký”; các tập đầu vào giữ nguyên. Rà 37–46 và mục 9 thấy sự phân biệt kiểu được duy trì. |
| **IG08** | **PASS** | SVG đổi đường nối thành `M320 112V132H112V172`, nhãn “Cửa sổ” chuyển sang vùng trống. Ảnh rộng 11 xác nhận nét không cắt chữ, đầu mũi tên vẫn trỏ ô ab đầu; sáu cửa sổ và nối hai ab giữ nguyên. Trang 10/11 và ghi chú mục 3 dùng cùng tệp SVG đã sửa, không còn một bản hình cũ riêng. |
| **IG09** | **PASS** | Ghi chú mục 13 dòng 667 nêu chọn đều một hoán vị của U, m nguyên, 1≤m<R. Đã bỏ câu dẫn chung thay cho giả thiết. Bảng bỏ cả hai vô cực khỏi số trùng/mẫu số, trường hợp không có phép thử hữu ích và cảnh báo phương sai với mẫu số ngẫu nhiên vẫn đầy đủ. Outline n05-13 và phần cập nhật cuối storyboard khớp. Nhánh giữ vị trí đọc thêm; không đưa vào phần giảng hoặc thành tiên quyết recitation. |

#### Hai yêu cầu bổ sung

**AR-03 — PASS.** Ảnh và HTML trang 32 đều có chuỗi ba bước: hệ số $n^{-2}$ nhân phương sai tổng; chuyển sang tổng phương sai với nhãn “độc lập”; thay $\operatorname{Var}(X_i)=s(1-s)$ để ra $s(1-s)/n$. Trang 31 đã đặt $X_i,s$ và tính đều; 32 nêu thêm độc lập. Công thức độ lệch chuẩn chuyển vào notes, không chiếm trọng tâm hình. Kết luận về phương sai không bị biến thành bảo đảm sai số giảm ở từng lần chạy. Phiếu 32 và mục 8 nhất quán.

**F01 — PASS.** Trang 35 phát biểu điều kiện không va chạm và phép lưu giá trị của hàng thắng bảo toàn phép so bằng; vẫn nói bảo đảm xác suất phụ thuộc cách chọn hàm. Trang 37 đặt tên phần tử cạnh mã hàng và hai giá trị, rồi nối thứ tự tăng với hai thứ tự cố định đã dùng ở 28. Trang 40 có cầu nối công khai

$$
(a,d)^{\mathsf T}\mapsto(f_1(0),f_2(3))^{\mathsf T}=(1,0)^{\mathsf T}.
$$

Notes 37/40 và mục 9 giải thích a↔0, d↔3 và điều kiện không va chạm. Trang 45 tiếp tục tách song ánh của từng hàm khỏi phân phối chọn đều; không dùng ví dụ affine cố định làm chứng minh xác suất. Cầu nối này giữ thứ tự sư phạm và dữ kiện sách.

#### Kiểm vùng lân cận và quyết định giữ

Điều kiện trên hình phân loại trang 25 nay hiện ngay trong SVG: “Xét loại của phần tử đầu tiên trong hợp”; Y ghi “thuộc đúng một tập”. Vì vậy kết luận trùng/khác trong hình đã có điều kiện trên mặt. Định lý ở 26 và kiểm tra 27 vẫn nối đúng tới hình.

Trang 28 đã bỏ ký hiệu σ trước định nghĩa 29, giữ vector cụ thể và câu minh họa cố định. Cặp S1/S4 không đổi khi đi qua 28–30 và 37–40. Giữ các sai khác đã được chấp nhận ở 21,29,51–57: không cần khôi phục ma trận hoặc bảng trống trùng lặp vì sản phẩm học tập và dữ kiện vẫn đủ.

Trang 46 tiếp tục kiểm ba thao tác: tỷ lệ trùng, min giữ nguyên, nL=18. Thời lượng 120+60 không đổi. Bài 3.2.3 hiện ghi quy ước một ký tự/một byte, và lời giải mang nhãn “Đáp số và cận trên” cùng giới hạn chứng minh đạt cận đúng quyết định M06 của root; không lén tăng giả thiết bảng chữ cái hoặc thêm kiến tạo ngoài phạm vi.

No-ai-slop Detect và rà Quill trong các đoạn đã sửa không phát hiện chỉ dẫn người soạn/giảng viên lọt vào mặt trang hoặc notes. Các nhãn “viền đậm”, “gạch dưới” là chú giải học thuật cho người đọc hình. Cầu nối, ký hiệu và các phủ định về giới hạn vẫn có chức năng cụ thể.

#### Dấu vết bản đã kiểm và giới hạn

SHA-256 tại lúc tái kiểm:

- HTML: `37983375fc5ca8f923bc1ccf28af755a3dbe2c47af1eb23df8f8993cad61c3ae`.
- `lecture-note.md`: `fef08ee7eeb2a1cf91a5ef92ef84c59b1d871c8312302ff96707ac7c8878b287`.
- `storyboard.md`: `1ea797c2c61f08a4fe73cd07e19b7409e2e6f36a922b0b2704e2768a1168ce1a`.

PASS ở đây xác nhận xử lý IG01–IG09, AR-03/F01 và tính nhất quán storyboard–bản thực trong vùng ảnh hưởng. Không thay việc root kiểm Speaker View, toàn bộ ảnh hẹp, viewer bàn phím/in, hồi quy CSS hoặc quyết định phát hành. Không cần thêm lượt sửa do cửa kiểm này yêu cầu.


## Kiểm định kỹ thuật cuối của điều phối viên

Các kiểm tra sau chạy trên tệp thật trong kho; riêng thử nghiệm Speaker View trước editor là lịch sử và không được dùng thay kết quả sau sửa. Sau hai sửa câu về “chữ ký của” cuối cùng, HTML Bài 05, viewer và Speaker View đã được chạy lại; 13 tệp công khai có SHA-256 không đổi từ lúc bắt đầu lượt kiểm cuối.

| Phạm vi | Bằng chứng và kết quả |
|---|---|
| Cấu trúc và tài nguyên | 57 `data-slide-id` duy nhất, 57 notes, 7 phần với số trang 9/9/9/7/12/4/7; 50 trang giảng/120 phút và 7 trang recitation/60 phút; 8 SVG. Kiểm đường dẫn, vai trò ảnh và cú pháp cấu trúc đạt. |
| RevealJS Bài 05 | Dựng đủ 57 trang ở 1280 × 720 và 390 × 844: 114 ảnh; không tràn biên nội dung, công thức lỗi, tài nguyên hỏng, lỗi JavaScript hoặc yêu cầu tài nguyên ngoài máy cục bộ. Bàn phím và cấu hình trình chiếu chính đạt. Điều phối viên xem đủ 57 trang qua 5 ảnh tổng hợp, cùng ảnh nguyên cỡ các cụm sửa và ảnh hẹp tiêu biểu. Các ảnh tổng hợp chỉ là kiểm bố cục, không thay đọc nội dung hoặc ảnh nguyên cỡ. |
| SVG | Tám hình có mô tả/role và không vượt viewBox. Đã xem lại ba hình sửa đường nối/điều kiện; mũi tên không cắt nhãn, hình X/Y nêu rõ điều kiện phần tử đầu tiên trong hợp. |
| Speaker View | Tệp HTML thật: notes của cả 57 trang khớp; main → receiver và receiver → main đồng bộ, đóng/mở lại không đổi trang; công thức nhận CSS/phông cục bộ. Tám ảnh popup kiểm các trang 09/26/33/36/38/42/54/57; điều phối viên xem công thức bất biến ở 42. Trình chiếu chính giữ hash bắt đầu 1, receiver nội bộ dùng hash bắt đầu 0 đúng hợp đồng plugin; không sửa vendor. |
| Ghi chú rộng/hẹp | 1440 × 900 và 390 × 844: mỗi bản có 648 công thức KaTeX, không lỗi, không tràn thân trang hoặc ảnh hỏng. 47 liên kết mục lục đều có đích; 21 khối gập đóng mặc định và đóng/mở được bằng Enter. Mục lục hết đánh số kép. Hình quy trình vừa cột rộng; bản hẹp giữ vùng cuộn của hình. |
| Bản in | 39 trang A4, 21 khối lời giải mở khi in và trở về trạng thái trước in. Điều phối viên xem toàn bộ qua 4 ảnh tổng hợp và trang đề bài nguyên cỡ; không cắt bảng, công thức hoặc hình. Các tiêu đề 3/10/11 và đầu bài 3.3.1–3.3.3 đi cùng nội dung/đề bài. |
| Viewer và liên kết | Từ chối đường dẫn ra ngoài thư mục tài liệu và doc/deck khác số bài; index Bài 05 trỏ đúng HTML và viewer. Không lỗi JavaScript, HTTP hay tải tài nguyên cốt lõi ngoài máy cục bộ. |
| Hồi quy CSS slide | Dựng lại đủ Bài 02 (81 trang) và Bài 03 (63 trang) ở hai khung: 288 ảnh, không lỗi biên/công thức/tài nguyên. Đối chiếu kiểu tính toán của các thành phần tương ứng trước/sau: giống nhau. CSS mới giới hạn bởi `.lecture-minhash`. |
| Hồi quy CSS viewer | So sánh mục lục, heading và ảnh của ghi chú Bài 03/04 ở 1440/390, cả screen/print: 8 trường hợp giống bản trước. Không nhận đã kiểm ghi chú Bài 02 vì bài này chưa có tệp ghi chú tương ứng. CSS sửa viewer chỉ áp dụng doc Bài 05. |

Giới hạn khung hẹp: RevealJS thu nhỏ toàn bộ khung 16:9 để vừa màn hình dọc; ảnh không tràn nhưng chữ nhỏ, không được coi là đạt khả năng đọc như bản máy chiếu. Người đọc trên điện thoại có bản ghi chú đáp ứng theo chiều rộng; khi dùng deck cần xoay ngang hoặc phóng to. Không giảm thang chữ chung để xử lý tải nội dung.

Bằng chứng máy cục bộ ở `/tmp/lec05-rebuild/`: `final-renders/report.json`, `final-renders-notes/report.json`, `final-materials/report.json`, `speaker-final/report.json`, `svg/report.json`, `common-styles-before.json`, `common-styles-after.json`, `viewer-regression-before/report.json` và `viewer-regression-after/report.json`. Các số liệu và giới hạn cần lưu bền vững đã được chép vào bảng này.


## Codex Slides và quyết định phát hành

Dự án bền vững: `20260827173151-b-i-5-bi-u-di-n-t-ng-ng-shingling-v-minh-3rca`. Điều phối viên nhập thủ công 57 ảnh PNG từ lần dựng RevealJS cuối, lưu 57 tiêu đề và 57 ghi chú diễn giả lấy từ HTML đã duyệt. Các thao tác `upload_slide_image`, `update_speaker_notes` và cập nhật stage `deck` chỉ lưu dữ liệu cục bộ; không dùng chức năng sinh, nghiên cứu, sửa bằng mô hình hoặc kết nối OpenRouter. Ảnh PNG phục vụ kiểm trên Codex Slides, không đưa vào Git hay thay các SVG trong deck.

`get_project` xác nhận 57/57 ảnh, tiêu đề và notes khớp. Trên ứng dụng Codex Slides thật bằng Chromium cục bộ, kiểm cả 57 trang: mã băm ảnh tải trong canvas bằng ảnh gốc, canvas đúng cỡ chính, notes bằng văn bản đã nhập; không lỗi JavaScript. Đã chụp 11 trang đại diện và panel notes cuối, điều phối viên trực tiếp xem trang 01, 38 và 57 với panel notes. Handoff cuối giữ đúng project, trang 57, panel `speaker-notes`, mode `workspace`, checkpoint `deck`:

[Codex Slides — trang 57 và ghi chú](http://127.0.0.1:4311/project/20260827173151-b-i-5-bi-u-di-n-t-ng-ng-shingling-v-minh-3rca?slide=57&panel=speaker-notes&mode=workspace&checkpoint=deck).

Lượt tự động đầu bị hộp thiết lập Codex xuất hiện muộn che nút canvas. Đã đọc skill `codex-slides-known-errors`, giữ nguyên dự án, đợi hộp hiện rồi đóng bằng nút bỏ qua; không đăng nhập hoặc gọi mô hình. Lượt kiểm sau đạt. Trong kiểm chỉ đọc, mọi request ghi và request mô hình/ngoại mạng bị chặn; 27 request chat tự lưu của giao diện bị chặn và không được dùng để sinh nội dung. Dòng chat cũ về bản nháp và chi phí lịch sử còn trên sidebar không là bằng chứng cho một lượt sinh mới; trạng thái canonical 57 ảnh và canvas được kiểm trực tiếp.

Giới hạn công cụ: phiên này không cung cấp Browser tích hợp trong trình soạn thảo Codex. Đã mở handoff qua công cụ plugin và kiểm ứng dụng bằng Chromium cục bộ, nhưng không tuyên bố đã xem trong Browser tích hợp. Không xuất PPTX/PDF từ Codex Slides và không tuyên bố một durable render run đã chạy. HTML, Markdown, outline, storyboard, nhật ký và hai CSS được lưu thêm làm Design Files; bản nguồn có thể chỉnh sửa vẫn ở kho.

Điều phối viên chấp nhận bản công khai sau năm báo cáo độc lập, editor, ba lượt tái kiểm cuối và QA kỹ thuật ở trên. Không còn phát hiện bắt buộc sửa. Chỉ 16 tệp sản phẩm Bài 05 và hạ tầng liên quan được đưa vào commit; giữ nguyên thay đổi riêng của người dùng trong AGENTS, tiêu chuẩn, cấu hình và các thư mục ngoài phạm vi. `git diff --check` sạch trước phát hành. Commit và push `origin main` là bước cuối; kết quả cùng mã commit được đối chiếu từ Git khi bàn giao, không suy từ trạng thái của Codex Slides.

## Duyệt từng trang ngày 01/10/2026

Yêu cầu của người dùng: duyệt lần lượt từng trang, xác định trang muốn nói gì, đề xuất rồi sửa để tiêu đề ngắn gọn, học thuật; lập luận chặt; khái niệm không xuất hiện đột ngột. Sau mỗi trang, sửa mục tương ứng của `lecture-note.md` (theo `note-topic-id`), commit và push.

Cách làm: điều phối viên (phiên Claude Code, Opus 5.5, effort `high`) trực tiếp biên tập từng trang theo tiền lệ lượt duyệt Bài 04, tự kiểm theo `no-ai-slop`/`eval.md`, tính lại phép tính bằng phân số. Sau mỗi phần, một tác tử rà chỉ đọc (loại `fork`, kế thừa Opus 5.5) kiểm độ chính xác và mạch trên các trang đã sửa; phát hiện và quyết định ghi ở bảng rà lại cuối mục. Kiểm hiển thị: Playwright Chromium, 1600 × 900 và 390 × 844 cho deck; 1440 × 900, 390 × 844 và in cho ghi chú. Cổng 8765 đang bị máy chủ của dự án khác chiếm nên máy chủ của kho chạy ở cổng 8775 từ gốc kho.

| Trang | Trang muốn nói | Quyết định | Thay đổi deck và storyboard | Ghi chú tự học |
|---|---|---|---|---|
| lec05-s01-01 | Tên bài, học phần và học kỳ; phạm vi MMDS §§3.1–3.3. | giữ | Tiêu đề và ghi chú đạt. | Không đổi; phần mở đầu ghi chú đã nêu cùng phạm vi. |
| lec05-s01-02 | Bảy phần và quan hệ giữa chúng. | sửa | Mục 1 “Giới thiệu và tương đồng tập hợp” → “Tài liệu gần trùng và độ tương đồng Jaccard”; mục 5 “Tính chữ ký và giới hạn” → “Tính chữ ký bằng hàm băm”. Ghi chú viết lại thành chuỗi quan hệ giữa các phần (Jaccard → tập shingle → MinHash → chữ ký → tính bằng hàm băm). Tên phần đồng bộ trong storyboard và outline. | Không đổi; ghi chú không có mục lục theo phần của deck. |
| lec05-s01-03 | Bốn năng lực đầu ra và kiến thức đầu vào. | sửa | “Giải thích xác suất trùng MinHash” → “Chứng minh xác suất trùng MinHash bằng Jaccard” (deck có chứng minh ở s03-08); thêm “Ước lượng Jaccard từ chữ ký” (sản phẩm phần 4); “phân tích chi phí” → “đếm chi phí”. Storyboard đồng bộ. | Không đổi; đoạn mục tiêu đầu ghi chú đã nêu đủ năm năng lực tương ứng. |
| lec05-s01-04 | Bài toán: từ kho văn bản lớn, đo tương đồng văn bản của từng cặp; tài liệu gần trùng làm phép so từng ký tự mất tác dụng. | sửa | Tiêu đề “Tài liệu gần trùng” → “Bài toán tài liệu gần trùng”. Đưa câu “So sánh từng ký tự chỉ phát hiện hai tài liệu trùng hoàn toàn” lên mặt trang (nhu cầu của bài toán, trước chỉ có trong ghi chú); thêm tình huống đạo văn của MMDS §3.1.2; đầu vào ghi “kho văn bản lớn như trang Web hoặc bản tin”. Ghi chú nêu đủ ba tình huống và giới hạn mức ký tự. Storyboard đồng bộ. | Mục 1: thêm tình huống đạo văn; câu về tương đồng ngữ nghĩa ghi rõ “mức ký tự”. |
| lec05-s01-05 | Số cặp không thứ tự $C(C-1)/2$; tổng công việc = số cặp × chi phí một cặp. | sửa | Tiêu đề “Chi phí so sánh từng cặp” (dễ hiểu là chi phí một cặp) → “Chi phí so sánh mọi cặp”. Thêm câu chốt “Bài này giảm chi phí một cặp; số cặp chỉ giảm khi có bước chọn cặp ứng viên” để nối sang các phần sau. Ghi chú nêu con số “nửa nghìn tỷ cặp” của sách cạnh phép tính chính xác. | Không đổi; mục 1 đã tách hai giới hạn và nói rõ Bài 05 giảm chi phí một cặp. |
| lec05-s01-06 | Khi tài liệu là tập, phần văn bản chung là giao; đếm giao 3, hợp 8 trên Hình 3.1; lượng chung cần so với hợp. | sửa | Tiêu đề “Phần tử chung của hai tập hợp” → “Giao và hợp của hai tập”. Thêm câu nối đầu trang “Khi mỗi tài liệu được biểu diễn bằng một tập phần tử…” (trước đó trang chuyển từ tài liệu sang tập hợp mà không nêu lý do). Câu chốt đổi thành “Lượng chung cần được so với kích thước hợp” để dẫn vào tỷ số Jaccard. Ghi chú thêm đối chiếu $|S|+|T|=11$. | Mục 2: thêm câu so sánh $|S|+|T|=11$ với $|S\cup T|=8$. |
| lec05-s01-07 | Định nghĩa Jaccard với điều kiện hợp khác rỗng; $3/8$; miền giá trị. | sửa nhẹ | Giữ tiêu đề. Câu chốt nêu cách đọc hai biên: 0 khi hai tập rời, 1 khi $S=T$ (trước chỉ có trong ghi chú). Ghi chú bỏ hai câu lặp mặt trang, giữ lý do tỷ số không vượt 1 và điều kiện $0/0$. | Không đổi; mục 2 đã có miền giá trị, hai biên và trường hợp $0/0$. |
| lec05-s01-08 | Jaccard dùng cho mọi dữ liệu biểu diễn được bằng tập; ý nghĩa giá trị phụ thuộc cách chọn phần tử và ứng dụng. | sửa | Tiêu đề “Tập hợp trong ứng dụng” → “Ứng dụng của độ tương đồng Jaccard”. Thay hai thẻ chung chung bằng dữ kiện MMDS §3.1.3: trang phản chiếu được dự kiến trên 90%, khách hàng 20% đã có thể có ý nghĩa. Bỏ công thức lặp lại từ s01-07. Câu chốt: “Ý nghĩa của một giá trị Jaccard phụ thuộc cách chọn phần tử và ứng dụng.” | Mục 2: thêm câu so sánh ngưỡng 90% và 20% theo nguồn. |
| lec05-s01-09 | Kiểm tra cách tính Jaccard (mẫu số là hợp) và nhu cầu quy tắc tạo tập cho văn bản. | sửa | Tiêu đề “Câu hỏi kiểm tra” → “Câu hỏi về độ tương đồng Jaccard”. Câu 1 cũ hỏi $3/8$ đã hiện ở s01-07; thay bằng tính lại sau khi thêm hai phần tử riêng vào $T$ ($3/10$). Thêm câu 2 chỉ ra lỗi $3/(5+6)$. Giữ câu nối sang văn bản. Ghi chú có lời giải ba câu; thẻ kiểm tra storyboard đồng bộ. | Mục 2: bài tự kiểm thêm ý (a) tính lại Jaccard sau khi mở rộng $T$, có lời giải. |
| lec05-s02-01 | Định nghĩa $k$-shingle và lý do tập shingle giữ phần văn bản chung của tài liệu gần trùng. | sửa | Tiêu đề “Shingle của văn bản” → “Biểu diễn văn bản bằng tập shingle”. Bỏ hình `cua-so-shingle.svg` (trùng trọng tâm với s02-02); định nghĩa đặt trong thẻ. Thêm hai ý trực giác lên mặt trang: thay một ký tự đổi nhiều nhất $k$ cửa sổ (suy từ định nghĩa, ghi rõ ở dòng nguồn); câu giữ nguyên tạo shingle chung kể cả khi đổi thứ tự (mở §3.2). Bỏ dòng khoảng trắng (thuộc s02-06). | Mục 3: thêm lập luận “nhiều nhất $k$ cửa sổ” và dẫn mở đầu §3.2 về câu đổi thứ tự. |

**Rà lại phần 1 (tác tử chỉ đọc, `subagent_type: "fork"`, kế thừa Opus 5.5 của điều phối viên).** Độ chính xác đạt ($499\,999\,500\,000$, $3/8$, $3/10$, $|S|=5$, $|T|=6$); khẳng định không mạnh hơn nguồn (“half a trillion”, “might expect” trên 90%, 20% “might be unusual enough”). Không có phát hiện chặn bàn giao hoặc nghiêm trọng.

| Trang | Phát hiện rà lại | Quyết định | Thay đổi |
|---|---|---|---|
| lec05-s01-09 | (trung bình) Câu 3 có một phần đáp án trên mặt s01-08 và câu nối s01-06. | sửa | Câu 3 đổi thành: hai văn bản cùng dài 1000 ký tự, giải thích vì sao chưa xác định được Jaccard. Lời giải trong ghi chú và thẻ storyboard đồng bộ. |
| storyboard 06, 08, 09 | (trung bình) Trường Bố cục, Trọng tâm, Mục đích còn mô tả bản cũ. | sửa | Viết lại ba trường theo bản hiện tại. |
| lec05-s01-09, ghi chú mục 2 | (nhẹ) Câu 1 chưa nói hai phần tử là mới; câu 2 khó hiểu. | sửa | “hai phần tử mới, không thuộc $S$”; “Một lời giải lấy mẫu số $5+6$ và cho $3/11$. Chỉ ra đại lượng bị đếm sai.” Ý (a) trong ghi chú tự học sửa tương ứng. |
| lec05-s01-06 | (nhẹ) “cần” biến lựa chọn định nghĩa thành bắt buộc; ghi chú có dấu hai chấm mở ý. | sửa | Câu chốt → “Jaccard đặt lượng chung trong quy mô của hợp.”; ghi chú → “…chưa đủ, vì ba phần tử chung…”. |
| lec05-s01-02 | (nhẹ) Ghi chú dùng “hàng” trước khi có ma trận đặc trưng. | sửa | “hoán vị thật của các hàng” → “hoán vị thật của các phần tử”. |
| lec05-s02-01 | Điều phối viên phát hiện: commit 7c30725 sửa storyboard nhưng lệnh `sed` không áp vào HTML câu “đọc qua một cửa sổ dài $k$”. | sửa | Áp lại vào HTML trong commit này; storyboard và deck khớp. |
| lec05-s02-02 | Chạy tay Ví dụ 3.3: `abcdabd`, $k=2$, sáu cửa sổ cho năm shingle. | sửa nhẹ | Tiêu đề “Ví dụ tạo shingle” → “Tập 2-shingle của một chuỗi”. Câu chốt về cửa sổ lặp đã nằm trong nhãn hình (“Hai cửa sổ ab → một phần tử của tập”), không thêm câu lặp. Ghi chú giữ nguyên. | Không đổi; mục 3 đã có bảng vết chạy sáu vị trí và câu về cửa sổ lặp. |
| lec05-s02-03 | Định nghĩa $S_k(D)$ bằng chỉ số, quy ước nửa mở $D[i:i+k]$, trường hợp $\ell<k$. | sửa tiêu đề | “Đặc tả tập shingle” → “Định nghĩa tập shingle” (trang nêu định nghĩa; “đặc tả” dành cho bài toán, thuật toán; không đặt $k$ trong tiêu đề vì CSS viết hoa thành “K”). Nội dung và ghi chú đạt. | Không đổi; mục 3 “Định nghĩa và quy ước” đã khớp. |
| lec05-s02-04 | Giả mã tạo $S_k(D)$, bất biến, số lần lặp $w$, chi phí $O(1+wk)$ kỳ vọng. | sửa | Thêm dòng đầu vào/đầu ra (thiếu trên bản cũ). Bất biến viết thành công thức $S=\{D[j:j+k]:0\le j<t\}$ thay câu “chứa đúng các cửa sổ đã xét”. Dòng $w$ nêu số lần lặp và trường hợp $\ell<k$ trả $\varnothing$. Ghi chú viết lại theo khởi tạo, duy trì, kết thúc rồi chi phí. Giữ tiêu đề. | Không đổi; mục 3 đã có bất biến cùng dạng và chi phí $O(1+wk)$. |
| lec05-s02-05 | Tiêu chí chọn $k$ và quy tắc kinh nghiệm 5 / 9 của nguồn. | sửa | Tiêu đề “Độ dài shingle” → “Chọn độ dài shingle”. Đặt tiêu chí của MMDS §3.2.2 lên đầu trang (trước chỉ có con số $27^5$ không rõ để kiểm điều gì); thêm trường hợp cực đoan $k=1$; câu $27^5$ ghi rõ phép so với độ dài một thư điện tử (viết bằng văn bản, không đặt chữ tiếng Việt trong KaTeX). Giữ bảng 5/9 và câu “quy tắc kinh nghiệm”. Ghi chú nêu lý do $20^k$. | Mục 3: thêm tiêu chí chọn $k$ và trường hợp $k=1$; câu $27^5$ nêu phép so sánh với độ dài thư điện tử. |
| lec05-s02-06 | Cách xử lý khoảng trắng thay đổi tập shingle; quy tắc của sách và hệ quả khi xóa khoảng trắng. | sửa | Tiêu đề “Khoảng trắng trong shingle” → “Xử lý khoảng trắng”. Dòng đầu nêu quy tắc của MMDS §3.2.1 (thay mỗi dãy ký tự trắng bằng một dấu cách). Câu chốt thay “xử lý theo cùng một quy tắc” bằng hệ quả kiểm được trên bảng: xóa hết khoảng trắng thì cả hai chuỗi tạo `touchdown`. Ghi chú nêu hai câu nguồn và lý do của quy tắc. | Mục 3: thêm quy tắc thay dãy ký tự trắng bằng một dấu cách và lý do. |
| lec05-s02-07 | Băm 9-shingle thành mã 4 byte: giảm dung lượng phần tử, phân biệt tốt hơn 4-shingle cùng dung lượng; va chạm có thể lệch Jaccard. | viết lại | Giữ tiêu đề. Thay hai thẻ chung chung và câu chốt “Độ dài shingle vẫn là $k=9$” (chi tiết phụ, đồng thời là đáp án câu hỏi s02-09) bằng bảng so sánh của MMDS §3.2.3: 4-shingle khoảng $20^4=160\,000$ giá trị so với mã của 9-shingle phủ gần như $2^{32}$. Câu chốt: “Cùng 4 byte, mã của 9-shingle phân biệt tài liệu tốt hơn 4-shingle.” Dòng va chạm giữ. Ý $k$ vẫn là 9 chuyển vào ghi chú. | Mục 3: thêm đoạn so sánh 4-shingle với mã của 9-shingle và câu về phép toán một từ máy. |
| lec05-s02-08 | Băm rút ngắn từng phần tử; số phần tử vẫn tăng theo độ dài tài liệu. | gộp | Trùng luận điểm với s03-01 và lặp số liệu `abcdabd` 6/5/5 của s02-02, s02-04. Xóa trang khỏi deck; cận $|S_k(D)|\le w$ và câu về băm chuyển sang s03-01 (sửa trong cùng commit). Phần 2 còn 8 trang, 21 phút; phần 3 nhận 1 phút (23 phút). Deck còn 56 trang (49 giảng, 7 bài tập). Phiếu 17 trong storyboard ghi quyết định gộp; số thứ tự phiếu giữ theo bản 28-09. Outline và bảng phần cập nhật. | Mục 4: câu mở thêm cận $|S_k(D)|\le\max(0,\ell-k+1)$ và ý “có thể không vừa bộ nhớ chính”. Mục 3 giữ đoạn `abcdabd` về số mã khi không va chạm. |
| lec05-s03-01 | Tập shingle có tới $w$ phần tử, cỡ bốn lần dung lượng tài liệu; cần chữ ký độ dài cố định. | sửa (nhận nội dung gộp) | Tiêu đề “Tập shingle và bộ nhớ” → “Kích thước tập shingle”. Thêm cận $|S_k(D)|\le w$ và câu “băm làm mỗi phần tử còn 4 byte, nhưng số phần tử vẫn có thể gần bằng số ký tự” từ s02-08. Bỏ dòng ghi chú nhỏ về chi phí cấu trúc (chuyển vào ghi chú). Câu chốt nêu yêu cầu chữ ký ngắn ước lượng được Jaccard. Ghi chú thêm câu “khoảng bốn lần” và “có thể không vừa bộ nhớ chính” của MMDS mở §3.3. | Như dòng trên. |
| lec05-s02-09 | Kiểm tra tạo tập shingle, tác động của một thay đổi cục bộ lên Jaccard, và lý do băm 9-shingle. | sửa | Tiêu đề “Câu hỏi kiểm tra” → “Câu hỏi về shingling”. Ba câu cũ có đáp án trên mặt s02-02 (6 cửa sổ, 5 shingle, nhãn hình về `ab`) và s02-07 bản cũ ($k$ vẫn là 9). Thay bằng: tập $S_3$ của `abcdabd` (5 cửa sổ, 5 phần tử); Jaccard của `abcdabd` và `abcdabc` với $k=2$ ($4/5$, tính lại bằng chương trình); so sánh 4-shingle với mã của 9-shingle. Chuỗi `abcdabc` ghi rõ là dữ kiện do người soạn tạo từ Ví dụ 3.3. | Mục 3: bài tự kiểm viết lại thành ba ý (a) số cửa sổ/mã, (b) Jaccard `abcdabd`/`abcdabc`, (c) 4-shingle và mã 9-shingle; bỏ ý “độ dài sau mã hóa”. |
| lec05-s03-02 | Ma trận đặc trưng của Hình 3.2: hàng là phần tử, cột là tập; ma trận thưa chỉ lưu vị trí ô 1. | sửa | Giữ tiêu đề. Thêm câu dẫn nêu lý do dùng ma trận (xét mọi tập trên cùng các hàng). Câu chốt “Ma trận có kích thước $R\times C$” → “Hàng là phần tử của $U$, cột là tập.” Thêm dòng “Ma trận thực tế rất thưa; khi lưu chỉ ghi vị trí các ô 1” (MMDS §3.3.1), nhận ý chính của s03-03. Định nghĩa $M(r,c)$ viết bằng câu văn thay công thức `cases` chứa chữ tiếng Việt trong KaTeX (dấu hiển thị lệch). Ghi chú nêu vai trò mã hàng $r$ cho phần tính chữ ký. | Không đổi; mục 4 đã có ma trận, mã hàng và danh sách theo hàng. |

**Rà lại phần 2 và s03-01 (tác tử chỉ đọc, `subagent_type: "fork"`, kế thừa Opus 5.5).** Độ chính xác đạt: “nhiều nhất $k$ cửa sổ” đúng cho phép thay ký tự; $20^4=160\,000$; “vượt xa $2^{32}$” khớp “many more than $2^{32}$”; “bốn lần” khớp “roughly four times”; cận $|S_k(D)|\le w$; $|S_3(\texttt{abcdabd})|=5$; Jaccard $4/5$. Không khái niệm nào dùng trước khi định nghĩa sau khi gộp s02-08. Không có phát hiện chặn bàn giao hoặc nghiêm trọng.

| Trang | Phát hiện rà lại | Quyết định | Thay đổi |
|---|---|---|---|
| lec05-s02-09 | (trung bình) Câu 3 có đáp án trên mặt s02-07 (bảng $20^4$ / $2^{32}$ và câu chốt). | sửa | Câu 3 thay bằng phép tính: tài liệu 50.000 ký tự, $k=9$, mã 4 byte, mọi cửa sổ khác nhau → $49\,992$ mã, $199\,968$ byte (cận trên). Câu này chuẩn bị con số của s03-01. Ghi chú, thẻ kiểm tra storyboard đồng bộ; ghi chú tự học mục 3 thêm ý (d) cùng lời giải, giữ ý (c) về 4-shingle. |
| storyboard 16 | (trung bình) Trường kết nối trỏ tới trang 17 đã gộp. | sửa | “trang 18 kiểm tra; trang 19 chỉ ra mã ngắn vẫn có nhiều phần tử”. |
| storyboard 10, 12, 14, 15, 16, 18 | (trung bình/nhẹ) Bố cục, Trọng tâm, Mục đích mô tả bản cũ. | sửa | Viết lại các trường theo bản hiện tại. |
| lec05-s02-07 | (nhẹ) “gần như mọi giá trị trong $2^{32}$” thiếu danh từ. | sửa | Thêm “mã” ở deck và storyboard. |
| lec05-s03-01 | (nhẹ) Trang mở phần 3 nhưng nội dung còn là shingle. | sửa ghi chú | Giữ trang; câu đầu ghi chú nêu kết quả kế thừa (tập mã 4 byte của phần 2) và giới hạn còn lại (số phần tử). |
| lec05-s03-03 | Ma trận chỉ lưu vị trí ô 1 theo danh sách cột của mỗi hàng; 9 ô 1 trong 20 ô. | gộp | Ý chính đã thành dòng “Ma trận thực tế rất thưa; khi lưu chỉ ghi vị trí các ô 1” ở s03-02. Ghi chú cũ phải nhắc “giá trị băm của một phần tử” trước khi băm hàng được giới thiệu (phần 5), nên trang đứng sai chỗ trong mạch. Danh sách cột có 1 theo hàng xuất hiện khi cần ở s05-03 và s05-09 ($L=\operatorname{nnz}(M)$). Xóa trang; deck còn 55 trang (48 giảng, 7 bài tập). 2 phút chuyển sang s03-04; phần 3 giữ 23 phút. Phiếu 21 ghi quyết định gộp; outline, bảng phần, ánh xạ ghi chú cập nhật. | Không đổi; mục 4 giữ bảng danh sách theo hàng và $L=\operatorname{nnz}(M)$ cho người tự học. |
| lec05-s03-04 | Mỗi tập giữ phần tử đứng đầu theo một thứ tự chung; trùng khi và chỉ khi phần tử đầu của hợp thuộc giao. | sửa | Tiêu đề “Trực giác MinHash” → “Ý tưởng của MinHash”. Thêm câu dẫn “Đại diện mỗi tập bằng một phần tử, chọn theo cùng một quy tắc” để nối với nhu cầu chữ ký của s03-01 (trước đó “thứ tự” xuất hiện không có lý do). Gạch thứ ba phát biểu đủ hai chiều (“đúng khi”). Ghi chú mở bằng nhu cầu, kết bằng câu nối sang định lý. | Mục 5: câu mở thêm nhu cầu chữ ký ngắn giữ liên hệ với Jaccard. |
| lec05-s03-05 | Ví dụ 3.7: với thứ tự $(b,e,a,d,c)$, MinHash của bốn tập là a, c, b, a; định danh khác vị trí. | sửa nhẹ | Tiêu đề “Ví dụ hoán vị” → “Ví dụ MinHash theo một hoán vị”. Câu cuối ghi chú (“không trộn chúng trong cùng bảng kết quả”) mâu thuẫn với bảng hai hàng trên mặt trang; viết lại thành “giá trị MinHash là định danh, còn vị trí chỉ cho biết phép quét dừng ở hàng nào”. Dữ kiện kiểm lại đúng. | Không đổi; mục 5 đã có bảng hoán vị và bảng định danh/hạng. |
| lec05-s03-06 | Định nghĩa $h_\pi(S)=\arg\min_{u\in S}\operatorname{rank}_\pi(u)$; trả định danh, không trả hạng. | sửa nhẹ | Giữ tiêu đề và công thức. Thẻ cuối bỏ dòng “Định lý xác suất dùng $\pi$ chọn đều” (giả thiết của định lý, đã phát biểu ở s03-08), thay bằng lý do $h_\pi$ xác định duy nhất (các hạng khác nhau). Ghi chú bỏ câu lặp ví dụ, sắp lại: kiểu hàm → điều kiện xác định → định danh khác hạng → nối sang định lý. | Không đổi; mục 5 đã nêu định nghĩa, tính duy nhất và quy ước định danh. |
| lec05-s03-07 | Với một cặp cột, hàng thuộc X $(1,1)$, Y (đúng một cột có 1) hoặc Z $(0,0)$; $x=|S\cap T|$, $x+y=|S\cup T|$. | sửa tiêu đề | “Các hàng chung và riêng” → “Ba loại hàng của một cặp cột” (gọi đúng đối tượng của phép phân loại). Nội dung, ví dụ $S_1,S_4$ ($x=2$, $y=1$) và ghi chú đạt. | Không đổi; mục 6 có bảng X/Y/Z và ví dụ cùng dữ kiện. |
| lec05-s03-08 | Định lý $\Pr[h_\pi(S)=h_\pi(T)]=\mathrm{SIM}(S,T)$ và chứng minh hai bước. | sửa | Tiêu đề “Xác suất trùng MinHash” → “Định lý xác suất trùng MinHash”. Đặt tên $u$ cho phần tử đầu của hợp; bước 1 thêm lý do quyết định trên mặt trang (“mọi hoán vị đồng khả năng”); bước 2 viết bằng ký hiệu. Dòng cuối “Pr[trùng]” (chữ tiếng Việt trong KaTeX) thay bằng chuỗi $\Pr[h_\pi(S)=h_\pi(T)]=\Pr[u\in S\cap T]=x/(x+y)$. Ghi chú giữ chứng minh chi tiết. | Không đổi; mục 6 có chứng minh đầy đủ (song ánh đổi tên phần tử) và cùng ký hiệu $u$. |
| lec05-s03-09 | Kiểm tra điều kiện trùng của MinHash, áp dụng định lý cho một cặp mới, vai trò hàng loại $Z$. | sửa | Tiêu đề “Câu hỏi kiểm tra” → “Câu hỏi về MinHash”. Ba câu cũ có đáp án trên mặt s03-05 (MinHash theo $(b,e,a,d,c)$), s03-07 ($x=2,y=1$) và s03-08. Thay bằng: tìm thứ tự làm hai MinHash khác nhau; $\Pr[h_\pi(S_1')=h_\pi(S_4)]$ với $S_1'=S_1\cup\{e\}$ ($1/2$, kiểm bằng liệt kê 120 hoán vị); vai trò của $b$ (loại $Z$). $S_1'$ ghi là biến thể ở dòng nguồn. | Mục 6: bài tự kiểm thêm ý (b) với $S_1'$ và lời giải. |
| lec05-s04-01 | Một MinHash chỉ cho 0/1; hai thứ tự cố định tạo chữ ký $(a,d)$ cho $S_1,S_4$, tỷ lệ trùng 1 so với Jaccard $2/3$. | sửa | Tiêu đề “Ví dụ chữ ký MinHash” → “Chữ ký từ nhiều thứ tự”. Thêm câu dẫn nêu lý do cần nhiều thứ tự (một phép thử chỉ cho trùng/không trùng), nối từ định lý của phần 3; trước đó trang mở thẳng bằng bảng. Bảng, ví dụ và ghi chú giữ. | Không đổi; mục 7 mở bằng “Một thành phần MinHash chỉ là một phép thử”. |
| lec05-s04-02 | Định nghĩa $\sigma(S)$ từ $n$ hoán vị dùng chung; ma trận chữ ký $n\times C$ so với ma trận đặc trưng $R\times C$; mô hình lý tưởng đều và độc lập. | sửa nhẹ | Tiêu đề “Vector và ma trận chữ ký” → “Định nghĩa chữ ký MinHash”. Ghi chú thêm cỡ $n$ của MMDS §3.3.4 (khoảng 100 đến vài trăm) so với $R$ là số shingle của cả kho; số trong ghi chú viết bằng KaTeX. | Mục 7: thêm câu về cỡ $n$ theo nguồn. |

**Rà lại phần 3 (tác tử chỉ đọc, `subagent_type: "fork"`, kế thừa Opus 5.5).** Độ chính xác đạt: định lý và hai bước chứng minh khớp MMDS §3.3.3; thứ tự $(c,a,b,d,e)$; $\Pr=1/2$ cho $S_1'$; số liệu mở §3.3. Sau khi gộp s03-03, $L$ được định nghĩa tại s05-09 nơi dùng lần đầu. Không có phát hiện chặn bàn giao hoặc nghiêm trọng.

| Trang | Phát hiện rà lại | Quyết định | Thay đổi |
|---|---|---|---|
| lec05-s03-09 | (trung bình) Câu 3 có đáp án trên nhãn hình s03-07 (“Z: ngoài hợp / b, e”). | sửa | Câu 3 đổi sang cặp $S_1,S_3$ và phần tử $c$ (ngoài $\{a,b,d,e\}$). Ghi chú, thẻ storyboard đồng bộ. |
| lec05-s03-02 → s05-09 | (trung bình) “Ma trận đặc” xuất hiện ở s05-09 mà chưa được định nghĩa sau khi bỏ s03-03; (nhẹ) “rất thưa” mạnh hơn “almost always sparse”. | sửa | Dòng ở s03-02: “Ma trận thực tế hầu như luôn thưa; thay vì lưu ma trận đặc đủ $RC$ ô, chỉ ghi vị trí các ô 1.” |
| storyboard 20, 22, 26, 27 | (trung bình/nhẹ) Trường kết nối, bố cục, trọng tâm, lý do, nguồn còn mô tả bản cũ; phiếu 26 thiếu dòng nguồn ghi chú. | sửa | Viết lại các trường; thêm “Nguồn: MMDS 3e, §3.3.3, tr. 83.” vào ghi chú phiếu 26. |
| lec05-s03-06 | (nhẹ) “vị trí” và “hạng” dùng lẫn mà không định nghĩa “hạng”. | sửa | “$\operatorname{rank}_\pi(u)$ là hạng, tức vị trí, của $u$…”; “$\arg\min$ trả phần tử đạt hạng nhỏ nhất.” |
| lec05-s03-04 | (nhẹ) “đúng khi” dễ đọc sai. | sửa | “khi và chỉ khi”. |
| lec05-s03-07 | (nhẹ) Câu ghi chú khó hiểu. | sửa | “bỏ chúng khỏi thứ tự không làm đổi phần tử được chọn”. |
| ghi chú mục 4 | (nhẹ) Nhắc giá trị băm, tính chữ ký trước khi giới thiệu; “Ma trận đặc là cách mô tả” dễ nhầm. | sửa | Thêm “(xem mục 9)”; câu đổi thành “Ma trận đặc trưng là cách mô tả dữ liệu; thực tế nó hầu như luôn thưa…”; bài tự kiểm hỏi danh sách cột của hàng $d$, phần tính chữ ký chuyển về mục 9. |
| lec05-s04-02 | Điều phối viên ghi nhận: máy chủ kiểm hiển thị dừng (hết giới hạn chạy nền) trong lúc kiểm s04-02; commit 1ff2769 chạy trước khi kiểm khung hẹp và ghi chú xong. | kiểm lại | Khởi động lại máy chủ cổng 8775; chạy lại: 1600 × 900, 390 × 844 và ghi chú (1440, 390, in) đều không lỗi. |
| lec05-s04-03 | Ước lượng $\widehat{\mathrm{SIM}}$ là tỷ lệ tọa độ trùng theo cùng chỉ số; với $n$ nhỏ có thể lệch cả hai phía. | sửa | Tiêu đề “Ước lượng Jaccard” → “Ước lượng Jaccard từ chữ ký”. Ví dụ $S_1,S_4$ ($1\ne2/3$) lặp kết luận của s04-01; thay bằng $S_2,S_4$ trên cùng hai thứ tự: $(c,c)$ và $(a,d)$ cho ước lượng 0 so với Jaccard $1/3$ (tính lại). Ghi chú so hai cặp để nêu lệch hai phía. | Mục 7: thêm cặp $S_2,S_4$ và câu “có thể lệch về cả hai phía”. |
| lec05-s04-04 | $\mathbb E[X_i]=s$ theo định lý; tuyến tính kỳ vọng cho $\mathbb E[\sum X_i]=ns$ và $\mathbb E[\widehat{\mathrm{SIM}}]=s$. | sửa | Tiêu đề “Kỳ vọng số lần trùng” → “Kỳ vọng của ước lượng” (kết quả trung tâm là tính không chệch). Dòng giả thiết ghi căn cứ “định lý MinHash cho $\mathbb E[X_i]=\Pr[X_i=1]=s$”. Thêm câu chốt “Ước lượng không chệch; tính tuyến tính của kỳ vọng không cần các hoán vị độc lập” (đối chiếu với giả thiết độc lập của s04-05); câu tương ứng trong ghi chú bỏ để không lặp. Khối công khai storyboard chép lại theo HTML. | Không đổi; mục 7 đã có phép suy ra và câu “không cần độc lập”. |
| lec05-s04-05 | Với hoán vị độc lập, $\operatorname{Var}(\widehat{\mathrm{SIM}})=s(1-s)/n$. | sửa | Tiêu đề “Sai số của chữ ký” → “Phương sai của ước lượng” (đại lượng được tính là phương sai). Câu chốt “Tăng $n$ làm giảm phương sai” → “Độ lệch chuẩn $\sqrt{s(1-s)/n}$: giảm một nửa cần tăng $n$ gấp bốn” (định lượng đánh đổi). Phép suy ra giữ nguyên. | Mục 8: thêm “giảm theo $1/\sqrt n$… tăng $n$ gấp bốn”. |
| lec05-s04-06 | Một cặp chữ ký: $n$ phép so bằng, $\Theta(n)$; mọi cặp: $nC(C-1)/2$. | sửa nhẹ | Giữ tiêu đề và phép đếm. Thẻ “Một cặp chữ ký” thêm “không phụ thuộc độ dài tài liệu” để nối với nhu cầu ở s03-01 (lợi ích chính của chữ ký so với tập shingle). “$n$ phép so bằng” chuyển ra văn bản thường (chữ tiếng Việt trong KaTeX hiển thị lệch dấu). Câu chốt trong storyboard cập nhật. | Mục 7: câu chi phí thêm “không phụ thuộc độ dài hai tài liệu hay kích thước hai tập shingle”. |
| lec05-s04-07 | Kiểm tra kỳ vọng số lần trùng và dùng độ lệch chuẩn để chọn $n$. | sửa | Tiêu đề “Câu hỏi kiểm tra” → “Câu hỏi về chữ ký MinHash”. Câu 2 cũ (kỳ vọng tỷ lệ $=s$) có đáp án trên s04-04; câu 3 cũ (tác dụng của $n$) có đáp án trên s04-05, s04-06. Giữ câu 1 ($200/3$); câu 2 mới: độ lệch chuẩn với $n=100$ ($\sqrt{1/450}\approx0{,}047$); câu 3 mới: $n$ nhỏ nhất để độ lệch chuẩn $\le0{,}02$ ($n=556$, tính bằng phân số) và số phép so bằng một cặp. | Mục 8: bài tự kiểm thêm ý (b) tìm $n=556$, có lời giải. |
| lec05-s05-01 | Không hoán vị thật được hàng triệu hàng; hàm băm trên mã hàng đóng vai hoán vị, giá trị nhỏ nhất đóng vai phần tử đứng đầu. | sửa | Tiêu đề “Hoán vị lớn và hàm băm” → “Mô phỏng hoán vị bằng hàm băm”. Đưa nhu cầu (chọn, sắp xếp $n$ hoán vị của hàng triệu hàng) lên mặt trang, trước chỉ có trong ghi chú; câu thứ hai nêu vai trò của $f_i$ trước khi nói tới va chạm. Câu điều kiện “không va chạm” chuyển vào ghi chú. Ghi chú viết lại theo §3.3.5 (“hàng $r$ được đưa tới vị trí $f_i(r)$”). | Mục 9: đoạn mở nêu cách mô phỏng hoán vị bằng $f_i$ và vai trò của giá trị nhỏ nhất. |

**Rà lại phần 4 (tác tử chỉ đọc, `subagent_type: "fork"`, kế thừa Opus 5.5).** Độ chính xác đạt: $\sigma(S_2)=(c,c)$, $\sigma(S_4)=(a,d)$, $\mathrm{SIM}=1/3$; $200/3$; $\sqrt{1/450}\approx0{,}0471$; $n=556$; “khoảng 100 đến vài trăm” khớp “Perhaps 100 permutations or several hundred”. s04-07 không có đáp án trên mặt trang trước. Không có phát hiện chặn bàn giao hoặc nghiêm trọng.

| Trang | Phát hiện rà lại | Quyết định | Thay đổi |
|---|---|---|---|
| storyboard 34 | (trung bình) Ký tự điều khiển BEL làm hỏng `\approx` trong thẻ kiểm tra (chuỗi Python không đặt `r`). | sửa | Thay lại `\approx`; quét cả năm tệp bằng grep ký tự `\a \b \f \v` và tab trên các dòng đã thêm từ đầu lượt: không còn. |
| storyboard 30, 32, 34 | (trung bình) Bố cục, Trọng tâm, Lý do còn mô tả bản cũ. | sửa | Viết lại theo HTML hiện tại (cặp $S_2,S_4$; dòng độ lệch chuẩn trên mặt trang; ba câu $200/3$, $\sqrt{1/450}$, $n=556$). |
| lec05-s04-05 | (nhẹ) Ghi chú sai ngữ pháp, công thức viết thường; “còn độc lập” mơ hồ. | sửa | Ghi chú viết lại với KaTeX (“Hệ số $1/n$ của trung bình được bình phương khi đưa ra ngoài phương sai…”); mặt trang: “Thêm giả thiết các hoán vị độc lập: …”. |
| lec05-s04-06 | (nhẹ) Ghi chú viết công thức thường. | sửa | Dùng $C(C-1)/2$, $n$ trong KaTeX. |
| ghi chú mục 7 | (nhẹ) Câu chèn làm “Đây” chỉ sai đối tượng. | sửa | Đưa câu về cỡ $n$ ra sau câu “Đây là một kiểu hàng khác…”. |
| lec05-s05-01 | (nhẹ, ngoài phạm vi) Ranh giới s04-07 → s05-01 đột ngột. | đã xử lý | Sửa ở commit 1a450cc (nhu cầu và vai trò $f_i$ lên mặt trang). |
| lec05-s05-02 | Đặc tả: đầu vào $M$, $f_1,\ldots,f_n$ dùng chung; đầu ra $\mathrm{SIG}(i,c)$ là cực tiểu trên các hàng có 1, cột rỗng nhận $+\infty$. | sửa | Tiêu đề “Đặc tả tính chữ ký” → “Đặc tả bài toán tính chữ ký”. Ba dòng rời (tham số, miền chỉ số, hàm) gộp thành hai dòng có nhãn “Đầu vào”, “Đầu ra” theo mục 3 của tiêu chuẩn soạn slide. Công thức và quy ước $+\infty$ giữ. | Không đổi; mục 9 đã có đặc tả với cùng miền, hàm và quy ước. |
| lec05-s05-03 | Dữ kiện Hình 3.4: $f_1=(r+1)\bmod5$, $f_2=(3r+1)\bmod5$; sắp tăng cho hai thứ tự đã dùng ở s04-01. | sửa nhẹ | Tiêu đề “Ví dụ các hàm băm hàng” → “Hai hàm băm hàng”. Ghi chú thêm câu giải thích cột “Các cột có 1” (danh sách vị trí ô 1 theo hàng), vì sau khi gộp s03-03 đây là lần đầu danh sách này hiện trên mặt trang. Bảng kiểm lại đúng. | Không đổi; mục 9 có bảng cùng cột “Các cột có 1” và mục 4 giải thích danh sách theo hàng. |
| lec05-s05-04 | Vết chạy bước đầu: khởi tạo $+\infty$; hàng 0 ($a$) cập nhật cột 1 và 4. | sửa nhẹ | Tiêu đề “Khởi tạo và giá trị hữu hạn” → “Khởi tạo và hàng 0” (đồng dạng với hai trang vết chạy sau). Thêm câu chốt rút ra từ bước này (trước chỉ có trong ghi chú): chỉ các cột chứa $a$ được cập nhật, cột 2 và 3 giữ $+\infty$. Bảng giữ nguyên. | Không đổi; mục 9 có đoạn “Ở hàng 0, chỉ $S_1,S_4$ chứa $a$…”. |
| lec05-s05-05 | Hàng 1 và 2: cột 3 rồi cột 2 nhận giá trị hữu hạn đầu tiên; cột 4 giữ $(1,1)$ dù vẫn thực hiện phép min. | sửa nhẹ | Tiêu đề “Cập nhật cột mới” → “Quét hàng 1 và 2”. Dòng cuối về cột 4 chuyển thành câu chốt, nêu rõ hai phép min vẫn được thực hiện dù không ô nào đổi (chuẩn bị cho phép đếm $nL$ ở s05-09). Bảng vết kiểm lại đúng. | Không đổi; mục 9 có đoạn về hàng 2 và câu “số phép min không bằng số lần giá trị lưu giảm xuống”. |
| lec05-s05-06 | Hàng 3 và 4 hạ từng thành phần độc lập; chữ ký cuối của $S_1,S_4$ là $(1,0)$, ứng với $(a,d)$. | sửa nhẹ | Tiêu đề “Cập nhật từng thành phần” → “Quét hàng 3 và 4”. Dòng cuối dùng ký hiệu $\mapsto$ khó đọc; viết lại thành câu chốt “Chữ ký của $S_1$ và $S_4$ là $(f_1(0),f_2(3))^{\mathsf T}=(1,0)^{\mathsf T}$, ứng với chữ ký định danh $(a,d)^{\mathsf T}$”. Bảng vết kiểm lại đúng. | Không đổi; mục 9 nêu cùng tương ứng $(a,d)\leftrightarrow(1,0)$. |
| lec05-s05-07 | Giả mã quét hàng: khởi tạo $+\infty$, tính $n$ giá trị băm một lần mỗi hàng, cập nhật min ở các cột có 1, dừng sau $R$ hàng. | giữ | Tiêu đề gọi đúng thuật toán; giả mã khớp đặc tả s05-02 và vết s05-04…06; ghi chú nêu cách duyệt với danh sách hoặc ma trận đặc và tính bất biến của thứ tự quét. | Không đổi; mục 9 có cùng giả mã. |
| lec05-s05-08 | Bất biến: sau tập hàng $A$, $\mathrm{SIG}(i,c)$ là cực tiểu trên $A$; khởi tạo, duy trì, kết thúc cho đúng đặc tả. | sửa | Tiêu đề “Bất biến giá trị nhỏ nhất” → “Tính đúng của phép quét hàng” (gọi kết quả thay vì công cụ). Bước duy trì viết đẳng thức quyết định trên mặt trang: cực tiểu mới bằng $\min(\mathrm{SIG}(i,c),f_i(r))$, khớp dòng cập nhật của giả mã. | Không đổi; mục 10 có chứng minh bất biến đầy đủ ba bước. |
| lec05-s05-09 | Đếm thao tác theo giả mã: $nC$, $nR$, $RC$, $nL$; tổng $\Theta(nC+nR+RC+nL)$ hoặc $\Theta(nC+nR+nL)$ khi có danh sách. | sửa nhẹ | Tiêu đề “Số phép tính chữ ký” → “Chi phí tính chữ ký” (đồng dạng với “Chi phí so sánh chữ ký”). Nhãn “Kiểm ô đặc” → “Kiểm ô (ma trận đặc)”, khớp định nghĩa ma trận đặc ở s03-02. Phép đếm kiểm lại: 8, 10, 20, 18. | Không đổi; mục 10 có bảng chi phí và hai tổng. |
