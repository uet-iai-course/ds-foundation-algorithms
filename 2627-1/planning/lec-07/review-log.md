# Nhật ký rà soát Bài 7

## Quyết định nguồn và biên tập

- Vòng ghi chú tự học 2026-09-02 dùng ba worker OpenRouter với `z-ai/glm-5.3-flash` để lập kế hoạch, ánh xạ nguồn và bản đồ chủ đề. Lượt bản đồ đầu chạm giới hạn tool-call; lượt thử lại cùng model trên hồ sơ hẹp hoàn tất.
- Codex chính giữ 11 chủ đề `L07-N01`–`L07-N11`, tách nhánh đồ thị và nhánh PQ/IVF-PQ rồi hội tụ ở bảng so sánh. Không thêm bài HNSW vào recitation vì runbook không có dữ kiện nguồn.
- Bổ sung quy tắc phá hòa, phân biệt `nok/|xq|` với recall@K tổng quát và chi phí IVF-PQ dưới nhãn suy ra. Không dùng tỷ lệ hiệu năng BIODS/Princeton thiếu điều kiện.

- Đọc `sources/source.md` và dòng Bài 7 trong `sources/reference-slides/README.md` trước khi soạn.
- Stanford BIODS 271 trang 17–18 chỉ đặt bối cảnh. Giữ dữ kiện $N=10^{10}$, $D=3072$, đoạn 6 chiều và mã tâm 8 bit; bỏ tuyên bố giảm độ chính xác 20–30% vì không có tập dữ liệu, phép đo hoặc cấu hình đi kèm.
- Suy ra 122,88 TB dữ liệu thô và 5,12 TB mã PQ theo hệ thập phân. Các số này chưa gồm mã định danh, bộ mã, danh sách đảo hoặc véc-tơ gốc; giới hạn được ghi ngay trong notes.
- Không dùng các con số so sánh thư viện ở Princeton như kết luận phổ quát. Mọi kết quả chạy phụ thuộc dữ liệu, phần cứng, số luồng và tham số.
- `recall@K` được đặc tả bằng giao của tập kết quả với tập $K$ hàng xóm thật. Khi có hòa, cần một quy tắc thứ tự cố định.
- `SEARCH-LAYER` chỉ bảo đảm $W$ trên phần đồ thị đã phát hiện. Tính lại phần tử xa nhất của $W$ sau mỗi lần cập nhật trong vòng lặp lân cận; bất biến và điều kiện dừng không được diễn giải thành chứng minh tìm đúng toàn cục.
- Không tuyên bố HNSW có $O(\log N)$ cho mọi dữ liệu. Bài báo dẫn xuất dưới giả thiết về tầng và khả năng điều hướng, đồng thời nêu giới hạn khi số chiều cao.
- Quy tắc chọn lân cận đa dạng được giữ theo Thuật toán 4 của bài báo; các cờ mở rộng ứng viên và giữ cạnh bị loại nằm ngoài phạm vi.
- Công thức PQ ghi rõ điều kiện $D$ chia hết cho $m$, cùng $k^*$ ở mọi đoạn, không gian $(k^*)^m$ véc-tơ tái dựng, $mk^*$ tâm con, $k^*D$ số vô hướng và $\lceil mb/8\rceil$ byte mỗi mã; chưa gồm phụ phí.
- ADC giữ truy vấn đầy đủ và lượng tử hóa phía cơ sở dữ liệu. Ví dụ Q06 dùng số tự dựng từ cơ chế nguồn và được ghi nhãn. PQ đơn thuần vẫn quét $N$ mã; IVF mới giảm số mã được xét.
- IVF-PQ mã hóa véc-tơ dư. Mỗi danh sách $L_i$ phải dùng truy vấn dư $q-\mu_i$ và bảng ADC riêng; đầu ra truy vấn là $K$ mã định danh hoặc phần tử, không phải $K$ mã PQ.
- Với IVF, công thức $nprobe\,N/k_c$ chỉ là xấp xỉ khi danh sách cân bằng. Bài giảng không dùng nó như cận bảo đảm.
- Bài tập giữ nguyên notebook Princeton. Dữ liệu có $d=64$, nên ba cấu hình 6 byte có $dsub=16,8,4$. Không ghi kết quả MSE, thời gian hoặc $nprobe$ tốt nhất cố định; sinh viên báo số đo của môi trường.
- Ô 155 đo tổng thời gian của 50 lần tìm trên cùng lô 100 truy vấn. `nok/|xq|` là tỷ lệ đúng hàng xóm hạng 1, không phải `recall@K` tổng quát. R08 chỉ là phiếu báo cáo của phép quét nguồn, không đặt mục tiêu vận hành mới.
- Hậu tố `np` trong chuỗi factory được kiểm chứng bằng tài liệu chính thức của Faiss; tài liệu này chỉ bổ sung cách đọc cú pháp, không thay dữ kiện bài tập.

## Sai khác có chủ ý so với nguồn

- Gộp BIODS và Princeton thành một tình huống xuyên suốt, nhưng không sao chép giao diện hoặc số liệu biểu đồ.
- Vẽ lại ví dụ đồ thị nhỏ có cực tiểu cục bộ thật: tham lam đi $e:9\to a:7\to b:5$; tìm kiếm chùm $ef=3$ còn giữ $s:8$ để tới $t:4,u:2,z:1$. Khoảng cách và trạng thái được kiểm tra lại bằng tay.
- Tách HNSW thành tìm kiếm tầng, phân tầng, truy vấn, chèn, chọn cạnh và tham số; thứ tự này đặt trực giác và ví dụ trước giả mã.
- Tách PQ thành VQ → mã PQ → ví dụ ADC số → không gian mã → ADC hình thức → bảng tra → quét tuyến tính → IVF-PQ, phù hợp quan hệ tiên quyết của công thức.
- Chỉ đưa LSH trên một trang cầu nối. Không dạy DiskANN, NSG, Vamana, OPQ hoặc các biến thể ngoài chuẩn đầu ra.
- Việt hóa mọi tiêu đề và nhãn hình; chỉ giữ tên riêng và tên thuật toán `HNSW`, `PQ`, `IVF-PQ`, `SEARCH-LAYER`, `recall@K`, `Faiss`.

## Xử lý phản biện độc lập

- **Chặn bàn giao — H01–H03:** hình cũ không có cực tiểu cục bộ hợp lệ và một path thiếu `fill="none"`. Đã thay toàn bộ `greedy-beam.svg`, thêm khoảng cách và hai vết chạy; rà lại H00–H05.
- **Chặn bàn giao — R04:** ghi sai $d=128$. Đã đối chiếu ô 2–4 của runbook, sửa thành $d=64$ và $dsub=16,8,4$; rà lại R02–R06.
- **Nghiêm trọng — H05:** ngưỡng $f$ bị giữ cũ trong vòng lặp lân cận. Đã chuyển phép lấy phần tử xa nhất hiện tại vào vòng lặp và nối với bất biến H06.
- **Nghiêm trọng — HNSW:** thiếu truyền điểm vào và đặc tả chèn. H07 nêu $ep_2\to ep_1\to ep_0$; H10 phân biệt tầng chỉ hạ điểm vào với tầng cập nhật cạnh và nêu mất đối xứng sau cắt bậc.
- **Nghiêm trọng — PQ/ADC:** thiếu ví dụ số và chi phí. Q06 tính ADC 0,31 từ mã Q05; Q07–Q10 bổ sung không gian mã, byte làm tròn, chi phí lập/lưu bảng và quét.
- **Nghiêm trọng — IVF-PQ:** công thức thiếu miền, truy vấn dư theo danh sách và kiểu đầu ra. Đã sửa I01–I04 cùng `ivfpq-flow.svg`.
- **Nghiêm trọng — so sánh:** tam giác cũ ngụ ý thứ hạng định lượng không có nguồn. Đã thay bằng bảng vai trò trung tính gồm LSH, HNSW, PQ đầy đủ và IVF-PQ; C00 dùng lại bốn trục A02 và tăng từ 4 lên 8 phút.
- **Nghiêm trọng — recitation:** đã thêm đường dẫn notebook, ánh xạ nhiệm vụ ô 82–99 và 148–155, phân biệt xây dựng/truy vấn, sửa nhãn thời gian và tỷ lệ đúng hạng 1.
- **Không áp dụng — bài HNSW trong recitation:** nguồn được chỉ định không có bài HNSW trực tiếp. Không tự tạo dữ kiện để lấp chỗ trống; các câu kiểm tra HNSW ở phần giảng không tính vào 60 phút bài tập.
- **Không áp dụng — ẩn đáp án khỏi notes:** quy định học phần yêu cầu lời giải hoặc hướng dẫn chấm trong ghi chú diễn giả, nên giữ đáp án ở notes.

### Tái kiểm sau chỉnh sửa

- **Nghiêm trọng — hợp đồng `SEARCH-LAYER`:** bổ sung tầng hữu hạn, $ef\ge1$, $1\le|ep|\le ef$; H05 khởi tạo trung thành bằng $W\leftarrow ep$.
- **Nghiêm trọng — đặc tả chèn HNSW:** hạ mục tiêu từ “chạy tay chèn” xuống “giải thích chèn”. H10 nay bao phủ chỉ mục rỗng; pha tầng trên với $ef=1$; pha cập nhật với `efConstruction`; chọn không quá M; nối hai chiều ban đầu; cắt từng đầu bằng $M_{max,0}\ge M$ hoặc $M_{max}\ge M$; truyền $ep\leftarrow W$; cập nhật điểm vào khi $\ell>L$.
- **Trung bình — ký hiệu mức:** H08 định nghĩa $m_L>0$ là hệ số mức. Lựa chọn $m_L=1/\ln M$ chỉ được nêu trong notes khi $M>1$ và là lựa chọn của bài báo.
- **Nghiêm trọng — chi phí IVF-PQ:** I03 ghi đủ $\Theta(k_cD)+\Theta(nprobe\,k^*D)+\Theta(m\sum|L_i|)$ và tách phụ phí top-K theo cấu trúc. I04 trả $\min(K,\sum|L_i|)$ khi thiếu ứng viên.
- **Nghiêm trọng — bốn trục so sánh:** bản SVG đúng nội dung nhưng chữ bị co quá nhỏ. C00 chuyển thành bảng HTML so chất lượng, truy vấn, xây dựng và bộ nhớ cho cả LSH, HNSW, PQ đầy đủ và IVF-PQ; không xếp hạng hay dùng số hiệu năng phổ quát.
- **Nghiêm trọng — trạng thái notebook:** R00 ghi chuỗi ô nền 0–4, 17, 21–24 và các biến `d,xt,xb,xq,gt`; R01/R04/R06/R07 ghi đúng tên mục nguồn và ô tương ứng. Mỗi sinh viên chạy các ô chuẩn bị trước giờ học trên chính notebook và kernel sẽ dùng; không tạo checkpoint mới. Thời gian máy huấn luyện/tìm được báo riêng, không tính vào 60 phút hoạt động.

## Tài sản và trạng thái rà soát

- Chín hình SVG được tham chiếu từ HTML, có `role="img"`, `title` và `desc`; không dùng raster hoặc tài nguyên mạng. Bản nháp `tradeoff.svg` đã được bỏ sau khi C00 chuyển sang bảng HTML để tăng cỡ chữ.
- Bản chỉnh sửa gồm 38 trang giảng và 9 trang recitation. Mỗi trang có `data-slide-id` duy nhất và ghi chú diễn giả.
- Bản chỉnh sửa không sửa `2627-1/index.html`, `lecture-style.css` hoặc tệp dùng chung.
- Bản chỉnh sửa đã hợp nhất các lỗi chặn bàn giao và nghiêm trọng từ rà storyboard, góc nhìn sinh viên, chuyên gia giải thuật, độ chính xác toán học và phản biện học thuật–giảng dạy. Điều phối viên đã chạy lại kiểm tra tĩnh, hai tái kiểm độc lập và kiểm định trình duyệt sau lượt sửa cuối.

## Kiểm tra tĩnh sau chỉnh sửa

- Xác nhận 47 trang với 47 `data-slide-id` duy nhất: 38 trang giảng và R00–R08; mỗi trang có đúng một khối ghi chú.
- Thứ tự HTML khớp storyboard; tổng thời lượng trong storyboard là 120 phút giảng và 60 phút recitation.
- Chín tham chiếu SVG đều tồn tại; toàn bộ chín tệp SVG đọc được bằng trình phân tích XML và có `role="img"`, `title`, `desc`.
- Không có ảnh raster, URL tài nguyên từ xa hoặc phụ thuộc mạng cốt lõi; mọi liên kết CSS, JavaScript và hình cục bộ đều tồn tại.
- Tự kiểm theo `no-ai-slop/eval.md`: giữ nội dung nguồn, bỏ diễn đạt chung chung, thống nhất “véc-tơ”, không dùng câu hỏi tu từ trong tiêu đề hoặc kết luận phô trương. Rà mạch theo Quill xác nhận dữ kiện được truyền từ ví dụ sang giả mã, bất biến, chi phí và kiểm tra; không tạo `quill.json`.
- Máy chủ `python3 -m reloadserver 8765` không khả dụng vì môi trường thiếu mô-đun; dùng máy chủ HTTP cục bộ đang chạy ở cổng 8765 để kiểm định tương đương.
- Chromium không giao diện đã duyệt đủ 47 trang sau lượt sửa cuối ở khung 1280×720 và 800×600: không có lỗi trình duyệt, tài nguyên hỏng, tràn, chồng lấn hoặc lỗi KaTeX; không có thân bài dưới 18 px. Điều hướng dọc–ngang bằng bàn phím đi đúng P00→P01 và P00→A00. Hai contact sheet được điều phối viên kiểm tra trực quan.
- Hai vòng tái kiểm độc lập sau lượt sửa cuối đều dùng `z-ai/glm-5.3-flash` qua OpenRouter và xác nhận không còn lỗi `chặn bàn giao` hoặc `nghiêm trọng`. Góp ý nhẹ về nhãn cột H03, câu nối đầu H08 và cấp tiêu đề C00 không áp dụng: nhãn hiện tại mô tả trạng thái trước phép lấy tiếp theo; H08 đã có câu nối xuôi sang truy vấn; C00 là trang tổng hợp trong cùng mạch, không phải trang mở mạch mới.
- Dự án Codex Slides `20260827193022-b-i-7-ch-m-c-h-ng-x-m-g-n-ng-4lo7` vẫn là bản nháp 0 trang. HTML cuối đã tải thành công làm material `20260830101640884-jubs.html`, nhưng material không tạo bề mặt 47 trang trong dự án và Codex Browser không khả dụng trong phiên này. Vì vậy chưa thể xác minh trực quan trên bề mặt Codex Slides; không tuyên bố đã rà hình bằng Codex Slides.

## Năm rà soát độc lập của bản nháp hiện tại

Phạm vi rà lại: các trang vừa sửa (A00, A01, H05, H06, Q06, Q07, I01, I02, C00, R00, R01, R04, R06), hai trang lân cận mỗi phía và ranh giới liên quan (P00, Q05, R05, R07). Không đổi cấu trúc, thứ tự 47 trang, thời lượng hay luận điểm trung tâm.

### Góc nhìn sinh viên

- `mức độ`: trung bình
- `trang chiếu`: R00, R01, R04, R06
- `vấn đề`: câu “Thời gian máy không tính vào 60 phút” dễ gây hiểu nhầm là thời lượng được cộng trừ.
- `bằng chứng`: mặt R00 và notes R04/R06 trước sửa chứa cụm “không tính vào 60 phút”.
- `đề xuất sửa`: đổi thành “Thời gian máy được báo riêng” và bỏ mọi câu 60 phút khỏi mặt/notes, giữ quy định hoạt động và báo thời gian máy.
- `quyết định`: đã áp dụng.

### Chuyên gia giải thuật và khoa học dữ liệu

- `mức độ`: trung bình
- `trang chiếu`: H10, R06
- `vấn đề`: hai báo cáo cho rằng `np` trong chuỗi factory nghĩa là tắt bảng tiền tính.
- `bằng chứng`: tài liệu chính thức Faiss “The index factory” (https://github.com/facebookresearch/faiss/wiki/The-index-factory) xác nhận `np` không huấn luyện hoán vị Polysemous, không liên quan bảng tiền tính.
- `đề xuất sửa`: bác bỏ hai báo cáo; giữ diễn đạt hiện tại ở notes R06.
- `quyết định`: đã bác bỏ hai báo cáo, giữ nguyên diễn đạt đúng.

### Độ chính xác toán học và thuật toán

- `mức độ`: nghiêm trọng nếu bỏ sót, đã xử lý hết
- `trang chiếu`: P00, H05, H13, Q00, Q06, H04, H10, A01, I01, R01
- `vấn đề`: kiểm tra từng dữ kiện then chốt trên bản nháp hiện tại.
- `bằng chứng`: P00 ghi đúng nguồn COS579A; H05 điều kiện dừng khớp Thuật toán 2 (chỉ so d(c,q) với d(f,q), không kèm |W|=ef); H13 ghi rõ O(NM) là suy luận §4.2.3 dưới giả thiết bậc trung bình bị chặn; Q00 tách rõ mã, tái dựng và sai số tái dựng; Q06 dùng bình phương khoảng cách nhất quán (0,02+0,29=0,31); H04 nêu ep là dạng tổng quát hóa của điểm vào đơn trong Thuật toán 2; H10 ghi rõ efConstruction≥M là quy ước thiết kế, không phải điều kiện bắt buộc; A01 nay nêu N_K(q) dùng cùng quy tắc phá hòa cố định của quét đúng/argmin nên recall@K xác định khi có hòa; I01 ví dụ nprobe=1 đúng tính toán 2<50; R01 chỉ số 123 và công thức tái dựng khớp runbook.
- `đề xuất sửa`: không cần sửa thêm; bổ sung câu phá hòa vào notes A01 đã thực hiện.
- `quyết định`: đã áp dụng (bổ sung notes A01); các điểm còn lại xác nhận đúng.

### Phản biện học thuật và giảng dạy

- `mức độ`: trung bình
- `trang chiếu`: C00, A00, nhãn SVG
- `vấn đề`: C00 có nguy cơ quá tải với hai đoạn small; một báo cáo cho rằng Q03/Q10/H10/C00/A00 “garbled”.
- `bằng chứng`: hai đoạn small ở C00 trước sửa trùng nội dung giữ cố định; báo cáo “garbled” không có bằng chứng — các trích dẫn là tiếng Việt bình thường, không phát hiện lỗi ký tự hay cú pháp; nhãn SVG (alt, title, desc) đọc được và khớp nội dung.
- `đề xuất sửa`: gộp hai đoạn small ở C00 thành một đoạn ngắn (trả lời bài toán mở đầu theo chất lượng truy vấn, chi phí dựng, bộ nhớ, kèm giữ cố định chuẩn đánh giá/phần cứng/chính sách lưu, không thêm số liệu); bỏ đoạn mặt trang dài về phá hòa ở A00, chuyển nội dung ngắn vào notes A01; bác bỏ báo cáo “garbled”.
- `quyết định`: đã áp dụng hai sửa đầu; đã bác bỏ báo cáo “garbled”.

### Kết nối và mạch viết

- `mức độ`: trung bình
- `trang chiếu`: H05, H06, Q06, Q07, I01, I02, R01, R06
- `vấn đề`: mã nội bộ (H04, H03, Q05, P01, I02, I01, R00) còn xuất hiện trong mặt/notes, làm đứt mạch khi đọc.
- `bằng chứng`: tìm thấy các cụm “H04 bảo đảm”, “Trong H03”, “từ Q05”, “ở P01”, “ở I02”, “Trong I01”, “từ trạng thái R00”, “từ R00” trong bản trước sửa.
- `đề xuất sửa`: thay bằng lời tự nhiên (“Đặc tả trước đó”, “Trong ví dụ tìm kiếm chùm”, “từ ví dụ PQ trước”, “trong tình huống mở bài”, “ở bước kế tiếp”, “Trong ví dụ ngay trước”, “từ trạng thái đã chuẩn bị”, “đã chuẩn bị”); xác nhận 7 mạch (mở đầu; đặc tả và cầu nối LSH; HNSW; PQ; IVF-PQ; kết luận; recitation) vẫn liền mạch.
- `quyết định`: đã áp dụng; không đổi cấu trúc, thứ tự hay luận điểm trung tâm.

### Quyết định phạm vi khác

- Không thêm bài HNSW recitation: nguồn được chỉ định không có bài HNSW; không tự tạo dữ kiện.
- Xóa mã nội bộ và thời lượng khỏi mặt/notes nhưng giữ nguyên thuộc tính `data-slide-id`; thời lượng vẫn giữ trong outline/storyboard/review-log.
- Điều phối viên đã chạy lại kiểm tra tĩnh, hai tái kiểm độc lập và kiểm định trình duyệt sau lượt sửa hiện tại; kết quả và quyết định đối với ba góp ý nhẹ được ghi ở phần “Kiểm tra tĩnh sau chỉnh sửa”.

## Rà soát ghi chú tự học

- Writer `deepseek/deepseek-v4-flash-0731` qua OpenRouter tạo bản nháp trong gốc tạm hẹp. Bản nháp từ mục 2 trở đi bị hỏng Unicode và sai tên nhiều SVG; Codex chính không phát hành bản này.
- Năm reviewer độc lập dùng `z-ai/glm-5.3-flash` qua OpenRouter, lần lượt kiểm nguồn, toán–thuật toán, mạch sư phạm, tính liên tục và khả năng render. Hai lượt đầu chạm giới hạn công cụ được chạy lại cùng model trong gốc chỉ đọc hẹp; metadata runtime đều xác nhận đúng model và provider OpenRouter.
- Đã áp dụng các lỗi có bằng chứng: soạn lại phần Unicode hỏng; bỏ nhãn chủ đề nội bộ khỏi bản công khai; khôi phục đủ chủ đề tham số HNSW; sửa giả mã `SEARCH-LAYER`; viết lại công thức tầng; tách VQ, PQ và ADC; cho đầy đủ dữ kiện của ví dụ ADC 0,31; thêm trường hợp IVF-PQ thiếu ứng viên; chuẩn hóa chín đường dẫn SVG; ghi rõ ba cấu hình notebook cùng ngân sách 6 byte.
- Bác đề xuất đổi cấu hình BIODS thành 6 byte/véc-tơ. Nguồn đặt `Vs=6` là **số chiều mỗi đoạn**, nên $S=3072/6=512$ đoạn; với $C=256$ và $P_c=8$ bit, mã dài 512 byte và kho mã chiếm 5,12 TB. Cấu hình 6 byte chỉ thuộc nhiệm vụ ngân sách ở ô 98–99 của notebook.
- Bác cảnh báo đường dẫn deck, notebook và SVG không tồn tại vì đó là hệ quả của gốc rà soát tạm: trong kho thật, deck và notebook đều có; viewer chủ động chuẩn hóa `img/lec-07/...` theo gốc `2627-1/`.
- `$no-ai-slop` đã được dùng để bỏ câu dẫn rỗng, nhịp liệt kê máy móc và mọi dấu vết quy trình khỏi ghi chú công khai; tự kiểm theo `no-ai-slop/eval.md` không phát hiện lời quảng bá, câu hỏi tu từ trong tiêu đề hay kết luận lặp.
- `$quill` đã được dùng để rà chuỗi quy mô → ANN → ba cơ chế; nhánh tham lam → `SEARCH-LAYER` → HNSW; nhánh VQ → PQ → ADC → IVF-PQ; hai nhánh hội tụ ở bảng so sánh rồi dẫn vào thực hành. Thuật ngữ và ký hiệu thống nhất với deck; không tạo `quill.json`.
- Hai lượt tái kiểm cuối cùng dùng `z-ai/glm-5.3-flash` qua OpenRouter. Lượt toán–thuật toán xác nhận toàn bộ con số, giả mã, công thức chi phí và ranh giới tuyên bố; lượt mạch xác nhận đủ 11 chủ đề, không còn mojibake, nhãn nội bộ hoặc nội dung quy trình trong bản công khai. Ba góp ý nhẹ được xử lý về ký hiệu $k^*$, truy vấn dư $\widetilde q_i$ và từ “khối lượng công việc”; nhận xét ví dụ VQ bị hòa bị bác vì $|3-4|<|3-0|$.
- Viewer thật đạt ở 1280×720 và 390×844: 26 tiêu đề khớp 26 liên kết mục lục, 189 công thức KaTeX không lỗi, chín SVG tải đủ, không lỗi trình duyệt hoặc tràn ngang. Sáu khối đáp án gập mặc định, mở được bằng bàn phím và mở khi in; bản in A4 có 16 trang. Traversal và cặp `doc`/`deck` lệch số bài đều bị từ chối.
- Sau khi các cổng viewer đạt, `index.html` mới được cập nhật. Kiểm tra một lần nhấp từ thẻ Bài 07 mở đúng ghi chú, đúng deck, đủ chín hình và không có lỗi KaTeX.

## Đồng bộ cuối với ghi chú đã phát hành — 2026-09-02

Điều phối viên giữ nguyên 47 trang, 7 mạch, 38 trang giảng + 9 trang thực hành, thời lượng 120+60 phút và 9 SVG. Hai reader OpenRouter đã đối chiếu lại deck–note–nguồn: reader kế hoạch phiên `81520`, reader nguồn phiên `13583`; cả hai dùng đúng `z-ai/glm-5.3-flash` qua OpenRouter. Writer phiên `98265` dùng đúng `deepseek/deepseek-v4-flash-0731` qua OpenRouter và chỉ đề xuất các delta hẹp; Codex chính áp dụng sau khi kiểm bằng nguồn.

### Quyết định nội dung

- Sửa hợp đồng `SEARCH-LAYER`: `ep` là tập với $1\le |ep|\le ef$; khởi tạo $V,C,W\leftarrow ep$ trong ghi chú, thống nhất với deck và Thuật toán 2.
- Chuẩn hóa chỉ số VQ và tâm thô về 0-based; dùng $\widetilde q_i=q-\mu_i$ nhất quán cho truy vấn dư IVF-PQ.
- Sửa cấu hình 48 bit từ $16\times4$ thành $16\times3$; ba cấu hình là $4\times12$, $8\times6$, $16\times3$.
- Tách rõ ô nền 0–4, 17, 21–24; nhiệm vụ PQ đọc 82–97, chạy 83–95 và hoàn thiện 96–97; so sánh mã 6 byte dùng 98–99.
- Sửa vết chạy tìm kiếm chùm trong ghi chú để khớp H03; đổi tiêu đề H02 sang “minh họa”; sửa bảng C00 thành $O(ND)$ số cho véc-tơ gốc.
- Biên tập `$no-ai-slop`: bỏ câu quy trình và siêu bình luận; viết tự nhiên lại P02, H04, H10, Q01, Q06, Q08, I03 và R00. Rà Quill xác nhận chuỗi ANN → HNSW → PQ/ADC → IVF-PQ → so sánh → thực hành liền mạch; không tạo `quill.json`.

### Năm reviewer và hai tái kiểm

- Nguồn, phiên `89063`: `GO`; xác nhận HNSW, PQ, ADC, IVF-PQ và notebook khớp nguồn.
- Toán–thuật toán, phiên `65731`: `GO`; xác nhận recall@K, `SEARCH-LAYER`, phân tầng/chèn HNSW, chi phí PQ/ADC/IVF-PQ và trường hợp thiếu ứng viên.
- Góc nhìn sinh viên, phiên `99088`: phát hiện lỗi $16\times4$ và cách mô tả phần chuẩn bị notebook; đã sửa.
- Văn phong, phiên `82806`: phát hiện vết chạy chùm, chỉ số tâm thô và các câu meta; đã sửa. Phiên `69221` bị loại vì báo lỗi ký tự không tồn tại trên tệp thật.
- Kỹ thuật, phiên `16557`: `GO`; xác nhận 47 ID/notes, cấu trúc RevealJS, KaTeX và 9 SVG. Cảnh báo thiếu runtime trong dossier tạm bị bác vì các thư viện cục bộ tồn tại trong kho thật.
- Tái kiểm toán, phiên `98685`: `GO`; xác nhận cấu hình 48 bit, ranh giới ô notebook, tập `ep` và truy vấn dư.
- Tái kiểm văn phong đầu tiên, phiên `7699`, đọc nhầm bản sao planning cũ trong dossier nên không dùng làm bằng chứng cuối. Dossier đã đồng bộ lại trước lượt tái kiểm cuối.
- Tái kiểm văn phong cuối, phiên `42473`: `GO`; xác nhận vết chạy chùm, chỉ số tâm thô, thuật ngữ “véc-tơ”, Q01, I03 và C00 đều đã đồng bộ, không còn lỗi chặn hoặc trung bình.

### Kiểm định phát hành

- Chromium trên deck thật: 47 trang, 47 notes, không lỗi KaTeX hay tài nguyên; điều hướng bàn phím đạt; PDF có 47 trang. Sau khi giảm nhẹ công thức I03, không còn tràn ở 1280×720, 800×600 và 720×900.
- Viewer ở 1280×720 và 390×844: 26 heading, 19 mục lục, 193 công thức KaTeX, 9 SVG và 6 khối gập; không lỗi, không ảnh hỏng, không tràn ngang. Khối gập mở bằng bàn phím, mở khi in; PDF viewer có 16 trang. Traversal và cặp `doc`/`deck` lệch số bài đều bị từ chối.
- `index.html` có đúng một liên kết Bài 07 với nhãn “Ghi chú bài giảng”; một lần nhấp mở đúng note và deck.
- Dự án Codex Slides `20260827193022-b-i-7-ch-m-c-h-ng-x-m-g-n-ng-4lo7` truy xuất thành công nhưng vẫn ở checkpoint `clarify`, trạng thái draft, 0 slide. Vì vậy kiểm định trực quan cuối dựa trên RevealJS/Chromium thật; không tuyên bố Codex Slides đã render 47 trang.

## Duyệt từng trang ngày 03/10/2026

Yêu cầu của người dùng: duyệt lần lượt từng trang Bài 07; với mỗi trang xác định trang muốn nói gì, vấn đề còn lại và đề xuất sửa; sửa để tiêu đề ngắn gọn, học thuật, lập luận chặt, khái niệm không xuất hiện đột ngột; giảm chữ và giải thích dài; không dẫn chiếu ví dụ ở trang trước mà dùng hình để nhắc lại dữ kiện; sau mỗi trang sửa phần tương ứng của `lecture-note.md`, cập nhật mục Bài 07 trong `index.html`, commit và push. Sau cùng rà lại toàn bài từ góc nhìn sinh viên.

Cách làm như lượt Bài 05–06: điều phối viên (phiên Claude Code, Opus 5.5, effort `high`) biên tập từng trang, tự kiểm theo `no-ai-slop`/`eval.md`, tính lại phép tính bằng chương trình; sau mỗi phần, một tác tử rà chỉ đọc (`subagent_type: "fork"`, kế thừa Opus 5.5) kiểm độ chính xác, mạch và góc nhìn sinh viên. Kiểm hiển thị bằng Playwright Chromium ở 1600 × 900 và 390 × 844 (chế độ cuộn của Reveal), ghi chú ở 1440 × 900, 390 × 844 và in; máy chủ `python3 -m reloadserver 8775` chạy từ gốc kho. Lỗi CSP trong trình xem ghi chú do máy chủ phát triển chèn một script nội tuyến vào trang; tệp `material-viewer.html` trong kho không có script này, nên lỗi được loại khỏi kết quả kiểm. Ảnh chụp lưu ngoài kho tại `/tmp/lec07-work/shots/` vì thư mục scratchpad của phiên không còn dùng được. Quy ước số thập phân: trang nào được sửa thì dùng dấu phẩy (`0{,}25`) như Bài 04–06.

### Bước chuẩn bị: chuyển sang CSS dùng chung và mục index

| Vị trí | Vấn đề | Bằng chứng | Quyết định |
|---|---|---|---|
| `<head>` của deck | (nghiêm trọng) Deck có khối `<style>` riêng, đặt cỡ chữ `.9em`, `.small` `.82em`, `.tiny` `.72em`; vi phạm quy định chỉ dùng `lecture-style.css`. | Khối `<style>` dòng 8–10 bản trước. | Bỏ khối `<style>`. Gốc deck mang `.course-deck.lecture-ann`; trang nội dung dùng `example-slide` và các lớp chung `ex-grid2`, `ex-card`, `ex-equation`, `ex-table`, `ex-code`, `ex-takeaway`. Bố cục riêng (`ann-figure`, `ann-short`, `ann-grid3`, thẻ nhấn `ann-accent`/`ann-good`, hộp `ann-question`, ô trống `ann-blank`, `ann-code-split`) thêm vào `lecture-style.css` trong phạm vi `.reveal.course-deck.lecture-ann`. Nội dung chữ chưa đổi; sửa nội dung làm theo từng trang ở dưới. |
| Giả mã H05, H09, R00, R02, R06 | (trung bình) Giả mã đặt trong `<div class="code">`, không có `data-trim`. | Tiêu chuẩn mục 3, khối mã. | Đổi sang `<pre class="ex-code"><code class="language-plaintext" data-trim>`. |
| P00 | (nhẹ) Trang tiêu đề không theo mẫu chung. | So với Bài 06. | Dùng `title-slide`, `lecture-title`, `supporting-text`, `course-name`, `term-name`, `institution-name`. |
| Mở phần A00, H00, Q00, I00, R00 | (nhẹ) Dùng `<h1>` có cỡ chữ của theme, khác các trang cùng phần. | Bản render. | Đổi sang `<h2>`. |
| I01 | (nghiêm trọng) Công thức miền argmin không render: ký tự `<` thô trong `\min_{0\le i<k_c}` cắt HTML. | Ảnh chụp hiện chuỗi `$$a(y)\in\arg\min_{0\le i`. | Đổi thành `&lt;`. Script kiểm thêm phép dò ký tự `$` còn sót ngoài KaTeX. |
| Cấu hình Reveal | (nhẹ) Thiếu đoạn nạp KaTeX cho cửa sổ ghi chú diễn giả. | So với Bài 06. | Dùng cùng khối script của Bài 06. |
| `index.html` | Bài 07 chưa có mục. | Index dừng ở Bài 6. | Thêm thẻ Bài 7 với liên kết deck và ghi chú theo yêu cầu của người dùng trong lượt này. |

Kiểm định: 47 trang, 1600 × 900 không tràn khung, không `.katex-error`, cỡ chữ nhỏ nhất ngoài KaTeX 23,7 px; 390 × 844 không tràn ngang; không lỗi console, không yêu cầu mạng ngoài máy chủ cục bộ; điều hướng bàn phím hoạt động. Ghi chú render được ở 1440 × 900, 390 × 844 và in, không lỗi KaTeX. Phạm vi CSS chung: chỉ thêm khối `.lecture-ann`; đã mở Bài 02 và Bài 03 ở hai khổ, không lỗi và không phần tử nào khớp `.lecture-ann`.

### Duyệt từng trang

| Trang | Trang muốn nói | Vấn đề | Quyết định và thay đổi deck, storyboard | Ghi chú tự học |
|---|---|---|---|---|
| P00 | Tên bài; ba cấu trúc HNSW, PQ, IVF-PQ; nối từ Bài 06. | Dòng phụ chưa diễn giải PQ, IVF-PQ; ghi chú gọi PQ là “nén khoảng cách”; mã học phần nguồn ghi sai “COS579A”. | sửa nhẹ. Dòng phụ “Đồ thị HNSW, lượng tử hóa tích (PQ) và tệp đảo IVF-PQ”. Ghi chú nêu khác biệt tìm cặp và truy vấn, vai trò từng cấu trúc, nguồn đúng “Princeton COS 597A”. Storyboard thêm mục chi tiết. | Thêm đoạn mở đầu nêu bài toán truy vấn và ba cấu trúc. Sửa liên kết deck `../../lecture-07-…` (trình xem phân giải thành `/lecture-07-…`, lỗi 404) thành đường dẫn tương đối như Bài 06. Tài liệu tham khảo: “COS 597G” → “COS 597A”. |
| P01 | Tình huống: truy hồi ngữ nghĩa trên $10^{10}$ véc-tơ 3072 chiều; quét toàn kho không khả thi. | Hình đưa “mã PQ, 512 đoạn, 8 bit, 5,12 TB” trước khi PQ được định nghĩa (khái niệm đột ngột); không nói véc-tơ đến từ mô hình nhúng; câu hỏi “nén … mười tỷ mã” giả định sẵn khái niệm mã; thiếu con số chi phí quét. | sửa. Hình mới `truy-hoi-ngu-nghia.svg` (sinh bằng `img/lec-07/generate_svg.py`) theo quy trình BIODS tr.16. Bỏ hai thẻ đầu vào/đầu ra (A00 hình thức hóa); hai thẻ số: 122,88 TB và $3{,}07\cdot10^{13}$ tọa độ mỗi truy vấn (tính lại: $10^{10}\cdot3072\cdot4=1{,}2288\cdot10^{14}$ byte; $10^{10}\cdot3072=3{,}072\cdot10^{13}$). Câu hỏi mới: thời gian quét với giả định $10^{12}$ tọa độ/giây (30,72 giây). Ghi chú giải thích mô hình nhúng, nguồn số liệu, đáp án. | Mục 1 đổi tiêu đề “Từ quy mô dữ liệu đến đặc tả ANN” (câu kể tiến trình) thành “Truy hồi ngữ nghĩa và bài toán hàng xóm gần nhất”; thêm đoạn quy trình nhúng, hình mới, chi phí quét. Đoạn 5,12 TB chuyển sang cuối mục 7 (sau khi PQ được định nghĩa); ký hiệu nguồn $P_c$ chưa định nghĩa đổi thành $b=8$. |
| P02 | Mục tiêu học tập của bài. | Không có dàn bài nên sinh viên không thấy cấu trúc buổi học; thẻ “Giải thích: chạy tay tìm kiếm” mơ hồ; “PQ đầy đủ” và “bốn trục” dùng trước khi định nghĩa; tiêu đề “Kết quả học tập” khác mẫu Bài 06. | viết lại. Tiêu đề “Nội dung và mục tiêu”; bố cục `agenda-slide` như Bài 06 (sáu phần + ba mục tiêu có sản phẩm cụ thể). Phần “So sánh và tự kiểm tra” cam kết bổ sung trang tự kiểm ở phần kết. CSS: thêm `.ann-orientation` (hai cột bằng nhau) trong phạm vi `.lecture-ann`. | Không đổi; sáu mục tiêu chi tiết của ghi chú bao phủ ba mục tiêu trên trang. |
| A00 | Đặc tả $K$ hàng xóm gần nhất, chi phí quét, nhu cầu tìm gần đúng. | Tiêu đề “Từ tìm đúng sang tìm gần đúng” là câu kể tiến trình; mặt trang chỉ có bài toán đúng, khái niệm “gần đúng” chỉ ở ghi chú; chi phí $\Theta(ND)$ chưa gắn số quy mô. | sửa. Tiêu đề “Bài toán $K$ hàng xóm gần nhất”; dòng đầu vào; hai thẻ “Tìm đúng” (phá hòa theo mã định danh) và “Tìm gần đúng (ANN)”; dòng chi phí thay số $N=10^{10}$, $D=3072$. Ghi chú: tên đầy đủ ANN, ý nghĩa phá hòa, mô hình đếm tọa độ, nguồn có số trang. | Mục 1: đoạn đặc tả viết lại thành ba đoạn tìm đúng, chi phí quét (thay số), định nghĩa ANN; câu dẫn công thức độ thu hồi nối với $\widehat N_K(q)$. |
| A01 | Định nghĩa độ thu hồi tại $K$. | Tiêu đề “Độ thu hồi tại $K$ đo phần tìm lại được” dài; hình Venn viết tay chữ khoảng 12 px khi chiếu; phép tính 3/5 chỉ có trong hình; không có câu hỏi kiểm tra. | sửa. Tiêu đề “Độ thu hồi tại $K$”. Hình mới `do-thu-hoi.svg` (chữ 30–40 đơn vị, hai tập phân biệt bằng nét liền/nét đứt và màu). Bố cục hai cột: hình; công thức, phép thay số, câu hỏi tập $\{a,c,f,g,h\}$ (đáp án $2/5$). CSS thêm `.ann-figure-split`. `ann-recall.svg` không còn được dùng. | Mục 1: thêm ý nghĩa và trung bình trên tập truy vấn; khối ví dụ, hình mới, bài tự kiểm cùng câu hỏi. |
| A02 | So sánh chỉ mục phải đo bốn trục trong cùng điều kiện. | Tiêu đề “Bốn trục phải đo cùng nhau” mang giọng mệnh lệnh; “thứ tự chèn” (HNSW) xuất hiện trước khi HNSW được giới thiệu; lý do một số đo không đủ chỉ có trong ghi chú. | sửa. Tiêu đề “Bốn trục đánh giá chỉ mục”; bảng gọn ba cột; thêm câu hỏi A/B ($0{,}9$/5 ms và $0{,}7$/2 ms) với đáp án có điều kiện trong ghi chú. Nguồn: chân trang PDF Princeton ghi “COS579A”; giữ mã “COS 597A” theo `sources/reference-slides/README.md`. | Mục 1: bảng thêm cột điều kiện giữ cố định, câu dẫn nêu lý do; lời giải bài tự kiểm nêu cách chọn theo yêu cầu. |
| A03 | Định vị LSH, HNSW, PQ và IVF-PQ trước khi đi vào từng cơ chế. | Tiêu đề kiểu khẩu hiệu “LSH tạo ngăn, HNSW tạo đường, PQ tạo mã”; ba tên cấu trúc xuất hiện không gắn với chi phí $\Theta(ND)$ của A00, nên sinh viên không thấy vì sao cần chúng; “PQ … giảm bộ nhớ” chưa nói giảm thừa số nào. | viết lại. Tiêu đề “Hai cách giảm chi phí truy vấn”; đẳng thức chữ chi phí ≈ (số véc-tơ được đo) × (chi phí một phép đo); thẻ “Giảm số véc-tơ được đo” (LSH, HNSW) và “Giảm chi phí một phép đo” (PQ, mã vài chục đến vài trăm byte); câu chốt IVF-PQ giảm cả hai. Nguồn ghi chú đối chiếu lại Princeton lớp 9 tr.4, 5, 7. | Mục 2 viết lại cùng khung hai thừa số (tiêu đề cũ “Ba cách cắt chi phí”). |
| H00 | Mở phần 3: định nghĩa đồ thị lân cận và ý tưởng tìm trên đồ thị. | Không có hình; thẻ “Trạng thái/Phép tiến” đưa đỉnh đã thăm, ứng viên chưa mở, tập tốt nhất trước khi có thuật toán; “cạnh … hữu ích cho điều hướng” mơ hồ; không nối với hai thừa số chi phí của A03. | viết lại. Tiêu đề “Đồ thị lân cận”. Hình mới `do-thi-vi-du.svg` (sinh bằng `generate_svg.py`, tọa độ thật; tính lại khoảng cách tới gốc: 9,000; 7,001; 5,000; 7,999; 3,996; 1,992; 1,000), dùng chung cho H01–H06 dưới ba biến thể (`do-thi-vi-du`, `do-thi-tham-lam`, `do-thi-chum`). Ba gạch: đỉnh và cạnh; dữ liệu lưu; cách tìm. Câu chốt nối A03. | Mục 3 đổi tiêu đề “Đồ thị lân cận và tìm kiếm tham lam”; thêm đoạn định nghĩa, bộ nhớ, hình ví dụ. |

**Rà lại phần 1–2 (tác tử chỉ đọc, `subagent_type: "fork"`, kế thừa Opus 5.5, effort `high`; bằng chứng: lệnh gọi Agent trong phiên ngày 03/10/2026).** Độ chính xác đạt: $1{,}2288\cdot10^{14}$ byte $=122{,}88$ TB; $3{,}072\cdot10^{13}$; $30{,}72$ s; recall $3/5$ và $2/5$; mệnh đề khớp BIODS tr.16–17, HNSW tr.1, Princeton lớp 8 tr.2, lớp 9 tr.2, 4, 5, 7. Không có phát hiện chặn bàn giao hoặc nghiêm trọng. Không trang nào dẫn chiếu “ví dụ ở trang trước”.

| Trang/vị trí | Phát hiện rà lại | Quyết định | Thay đổi |
|---|---|---|---|
| A00 | (trung bình) Dòng chi phí khẳng định $\Theta(D)$ mỗi khoảng cách nhưng giả thiết Euclid chỉ ở ghi chú. | sửa | Thẻ “Tìm đúng” thêm “Quét đầy đủ với khoảng cách Euclid: … $\Theta(ND)$”. |
| A00 | (trung bình) Thứ tự lập luận: chi phí (lý do cần ANN) đứng sau thẻ ANN. | sửa | Chi phí tiệm cận nằm trong thẻ “Tìm đúng”; câu chốt thay số và nêu “ANN tránh lượt quét này”. |
| A02 | (trung bình) “phụ phí” chưa định nghĩa. | sửa | “byte mỗi véc-tơ, kể cả cấu trúc chỉ mục” (deck và ghi chú). |
| P02 | (trung bình) Cam kết phần “So sánh và tự kiểm tra” nhưng phần kết chỉ có C00. | giữ, mở | Ghi thành việc còn mở: bổ sung trang tự kiểm khi duyệt phần kết. |
| H00 | (trung bình) Trạng thái SEARCH-LAYER xuất hiện đột ngột; không nối A03. | đã sửa | Commit H00 (`e104d73`). |
| P02 | (nhẹ) “Tệp đảo kết hợp PQ” thiếu tên viết tắt. | sửa | Thêm “(IVF-PQ)”. |
| A01 | (nhẹ) recall@R của bài báo PQ ở trang in 8, không phải 7 (trang PDF đầu là bìa HAL nên trang in = trang PDF − 1). | sửa | “tr.8”. |
| A01 | (nhẹ) Câu hỏi ngầm dùng tập đúng trong hình. | sửa | “Với cùng tập đúng, …”. |
| A00 ghi chú | (nhẹ) “ở trang sau” là lời chỉ trang; mẫu “không có nghĩa là … :”; “K-ANN” lệch thuật ngữ nguồn. | sửa | Viết lại hai câu; “bài toán K-NNS và K-ANNS”. |
| P01, A00 | (nhẹ) Đơn vị “tọa độ” dễ hiểu thành số tọa độ trong kho. | sửa | “lượt xử lý tọa độ” (thẻ P01), “lượt tọa độ mỗi giây” (câu hỏi P01). |
| A02 ghi chú | (nhẹ) Lớp 8 tr.5 chỉ là ký hiệu notebook. | sửa | “lớp 8, tr.2–4”. |
| Ghi chú mục 2 | (nhẹ) “Cả ba” mơ hồ khi đoạn nêu bốn cấu trúc. | sửa | “Mọi cấu trúc trên”. |
| H01 + H02 | Tham lam dừng ở cực tiểu cục bộ $b:5$ trong khi $z:1$ gần $q$ hơn. | Hai trang cùng một ý: H01 chỉ có hình và một câu, H02 chỉ có bảng nên phải nhớ hình ở trang trước; “cực tiểu cục bộ” dùng trên tiêu đề H02 nhưng không định nghĩa; bảng H02 ghi lân cận của $a$ chỉ có $b:5$ (thiếu $e:9$); hình cũ không theo tỷ lệ khoảng cách. | gộp. Một trang “Tìm kiếm tham lam”: câu quy tắc một bước, hình `do-thi-tham-lam.svg` cạnh bảng vết ba hàng (đủ lân cận), câu chốt định nghĩa cực tiểu cục bộ. Bỏ H02. Ghi chú: lý do không bảo đảm toàn cục, tính dừng, 4 phép đo (tính lại). CSS thêm `.ann-trace-split`. | Mục 3: định nghĩa tham lam và cực tiểu cục bộ, bảng ba cột khớp trang, hình mới thay `greedy-beam.svg`, đoạn dừng và số phép đo. |
| H03 | Tìm kiếm chùm giữ nhánh $s$ làm đường dự phòng và tới $z$. | $C$, $W$ dùng trước khi định nghĩa (khái niệm đột ngột); không có hình, phải nhớ đồ thị trang trước; vết chỉ tới $s$; câu chốt hai dòng. | sửa. Tiêu đề “Tìm kiếm chùm”; dòng định nghĩa $C$, $W$, $ef$; hình `do-thi-chum.svg` cạnh bảng 7 lần mở (mô phỏng lại theo Thuật toán 2: kết quả $\{z,u,t\}$); câu hỏi $ef=2$ (mô phỏng: trả $\{b,a\}$, dừng vì $8>7$). Ghi chú: quy tắc thêm/bỏ, điều kiện dừng, $ef=1$ trùng tham lam, đáp án. CSS thêm `.ann-compact`. | Mục 4: định nghĩa tìm kiếm chùm, bảng vết đủ, hình, bài tự kiểm $ef=2$ có lời giải. |
| H04 | Đặc tả đầu vào, đầu ra, trạng thái của SEARCH-LAYER. | “Hợp đồng” dịch sát “contract”; tham số tầng $\ell_c$ xuất hiện trước khái niệm tầng; hình cũ chữ nhỏ, không gắn ví dụ; $V$ chưa định nghĩa. | sửa. Tiêu đề “Đặc tả SEARCH-LAYER”; hình mới `search-layer-trang-thai.svg` vẽ $C,W\subseteq V$ bằng trạng thái thật sau khi mở $b$ ($ef=3$); ba dòng đầu vào/đầu ra/trạng thái. Ghi chú: $\ell_c=0$ khi một đồ thị, lý do $1\le|ep|\le ef$, phạm vi đầu ra; bỏ dẫn chiếu “ở trang trước”. `search-layer.svg` cũ không còn dùng. | Mục 4: đoạn đặc tả có danh sách đầu vào/đầu ra/trạng thái, hình mới thay hình cũ. |
| H05 | Giả mã SEARCH-LAYER và vai trò của ngưỡng $f$. | Tiêu đề là câu mô tả; tên dạng `hàng_đợi_gần_nhất`, `lân_cận`; dòng cuối dồn “thêm … ; cắt W còn ef”; không nối với ví dụ. Ghi chú cũ đúng nhưng chưa giải thích lệnh `break`. | sửa. Tiêu đề “Giả mã SEARCH-LAYER”; giả mã 13 dòng khớp Thuật toán 2 (đối chiếu từng dòng với bài báo, tr.4); câu chốt bước mở $s$: $f=s{:}8$, thêm $t{:}4$, bỏ $s$, ngưỡng mới $a{:}7$. Ghi chú thêm lập luận: khi `break`, mọi đỉnh của $W$ đã mở; dừng là đánh đổi nên kết quả gần đúng (bản nháp đầu của câu này khẳng định quá mức “không thể thêm đỉnh nào”, đã sửa trước commit). Xóa `greedy-beam.svg` (không còn tham chiếu sau H01). | Mục 4: giả mã đồng bộ với trang; đoạn ngưỡng $f$ có ví dụ; đoạn lệnh `break` và tính dừng. |
| H06 | Bất biến của SEARCH-LAYER và giới hạn của kết luận. | Chỉ liệt kê tính chất ba tập; thiếu khởi tạo–duy trì–kết luận; phát biểu về $W$ yếu; tiêu đề “Bất biến giới hạn trong vùng đã phát hiện” khó hiểu; ví dụ chỉ trong ghi chú, dẫn chiếu “ví dụ tìm kiếm chùm”. | sửa. Tiêu đề “Bất biến của SEARCH-LAYER”; mệnh đề “$W$ là một tập gồm $\min(ef,|V|)$ đỉnh của $V$ gần $q$ nhất” (kiểm bằng chương trình trên đồ thị ví dụ và 3000 đồ thị ngẫu nhiên); bảng khởi tạo/duy trì/khi dừng; hình mới `do-thi-ef2.svg` nhắc lại lần chạy $ef=2$ ($V=\{e,a,s,b\}$, $W=\{b,a\}$). Bản nháp đặt hình nhỏ dưới bảng (chữ khoảng 10 px) đã được đổi sang bố cục hai cột trước commit. CSS thêm `.ann-mini` (không dùng sau khi đổi bố cục; giữ cho trang có hình phụ) và `th[scope="row"]` không xuống dòng. | Mục 4: đoạn bất biến có chứng minh ba bước, ví dụ $ef=2$ kèm hình, giới hạn. |
| H06B (mới) | Vì sao cần nhiều tầng: cạnh dài giảm số bước. | Bản cũ đi thẳng từ bất biến một tầng sang các tầng HNSW, không nêu lý do; sinh viên chưa thấy giới hạn “số bước” của đồ thị chỉ có cạnh ngắn. | thêm. Trang “Cạnh dài rút ngắn đường đi” với hình mới `canh-dai-mot-chieu.svg` dựng lại ví dụ một chiều của Princeton lớp 9 tr.11–13 (tham lam tính lại: 6 bước và 3 bước; chỉ có $p4$–$p8$ vẫn 6 bước). Câu chốt nối sang các tầng. | Mục 5: đoạn mở đầu về cạnh dài/cạnh ngắn, số phép đo ≈ số bước × bậc, hình mới. |
| H07 | Cấu trúc nhiều tầng và đường đi của truy vấn qua các tầng. | Tiêu đề là câu mô tả; hình cũ chữ nhỏ, không gắn với ví dụ; chuỗi $ep_2\to ep_1\to ep_0$ chưa giải thích; không nói tầng nào chứa điểm nào. | sửa. Tiêu đề “Đồ thị nhiều tầng”; hình mới `do-thi-nhieu-tang.svg` dùng lại 12 điểm của H06B (tầng 1: $s,p2,\ldots,p10$; tầng 2: $s,p4,p8$; vết tính lại: $s\to p4\to p8$, $p8\to p6$, $p6$); hai gạch cấu trúc và cách truy vấn. `hnsw-layers.svg` không còn dùng. | Mục 5: đoạn “Đồ thị nhiều tầng” với ví dụ ba tầng và hình mới; khối công thức rút tầng chuyển xuống sau đoạn truy vấn (theo thứ tự cấu trúc → truy vấn → rút tầng → chèn sẽ áp dụng cho deck ở H08). |
| H08 | Quy tắc rút tầng và vì sao tầng trên thưa dần. | Chỉ có công thức và bảng ký hiệu; không suy ra phân phối nên “hệ số mức” không có nghĩa trực quan; ghi chú dùng $M$ (chưa định nghĩa) và dẫn chiếu “trang sau”; đặt trước giả mã truy vấn dù chỉ dùng khi chèn. | sửa, chuyển sau H09. Tiêu đề “Rút ngẫu nhiên tầng của điểm mới”; suy luận $\Pr[\ell\ge k]=p^k$, $p=e^{-1/m_L}$; thẻ ý nghĩa và ví dụ $m_L=1/\ln16$ ($p=1/16$, tính lại $1/16$, $1/256$; mô phỏng $10^6$ lần: $0{,}0626$, $0{,}0039$); tầng cao nhất $\log_{16}10^{10}\approx8{,}3$. Bản nháp viết “khoảng 8 tầng”, sửa thành “khoảng tầng 8” trước commit. Đối chiếu bài báo mục 4.1: $m_L=1/\ln M$ ứng với $p=1/M$. | Mục 5: đoạn rút tầng có suy luận, khối ví dụ, ghi chú về $m_L=1/\ln M$. |
| H09 | Giả mã truy vấn HNSW. | Tiêu đề “Truy vấn HNSW dùng hai chế độ” mơ hồ; tên dạng `điểm_vào`, `phần_tử_gần_nhất`; thiếu đầu vào/đầu ra; không nối với ví dụ. Bản nháp đầu dùng thẻ chữ “Ví dụ ba tầng” (nhắc bằng chữ), thay bằng hình trước commit theo yêu cầu dùng hình. | sửa. Tiêu đề “Giả mã truy vấn HNSW”; dòng đầu vào/đầu ra; giả mã 6 dòng khớp Thuật toán 5 (đối chiếu bài báo tr.5); hình mới `do-thi-nhieu-tang-gon.svg` (biến thể gọn, chữ lớn của hình H07) và dòng vết $ep=p8$, $p6$. | Mục 5: đoạn truy vấn có đặc tả, giả mã, vết ví dụ, tính dừng. |
| H10 → H10, H10B | Thao tác chèn hai pha và các tham số xây dựng. | Tiêu đề câu mô tả “Chèn HNSW có hai pha theo tầng”; hình `hnsw-insert.svg` bốn hộp chữ khoảng 10 px; một dòng đưa cùng lúc $efConstruction$, $M$, $M_{max}$, $M_{max,0}$; toàn bộ thuật toán nằm trong ghi chú diễn giả; không có ví dụ. | tách. H10 “Chèn một điểm mới”: ví dụ $x=2{,}6$, $\ell=1$, $M=2$, chùm 3 trên đồ thị ba tầng (mô phỏng: $ep=p4$; tầng 1 $W=\{p2,p4,s\}$; tầng 0 $W=\{p3,p2,p4\}$), hình mới `chen-vi-du.svg`. H10B “Giả mã chèn HNSW”: giả mã khớp Thuật toán 1, dòng định nghĩa tham số. Ghi chú: bản nháp nói bài báo “dùng $M_{max}=M$”; đối chiếu mục 4.1 chỉ thấy đề xuất $M_{max,0}=2M$, đã sửa trước commit. `hnsw-insert.svg` không còn dùng. | Mục 5: đoạn chèn có ví dụ (bảng, hình), giả mã, tham số, các trường hợp biên. |
| H11 | Quy tắc chọn lân cận đa dạng. | Ký hiệu $q$ cho điểm mới xung đột với truy vấn $q$; không hình, không ví dụ; tiêu đề “Lân cận đa dạng giữ nhiều hướng thoát” dùng ẩn dụ. | sửa. Tiêu đề “Chọn lân cận đa dạng”; điểm mới ký hiệu $x$ như H10–H10B; ví dụ hai chiều do học phần dựng (tính lại: $d(\cdot,x)$ = 2,022; 2,474; 2,751; 3,041; $d(c3,c1)=0{,}985$, $d(c2,c1)=0{,}849$, $d(c4,c1)=5{,}004$; kết quả $\{c1,c4\}$, chọn gần nhất $\{c1,c3\}$); hình hai khung `lan-can-da-dang.svg`; bảng quyết định. Đổi ví dụ vì trên ví dụ một chiều hai cách chọn trùng nhau (ghi trong ghi chú). | Mục 5: đoạn chọn lân cận đa dạng dùng $x$, khối ví dụ, hình, giải thích (bổ sung ở commit riêng vì lệnh cập nhật ghi chú và storyboard bị bỏ qua ở commit đầu do một lệnh kiểm tra trả mã lỗi). |
| H12 | Ba tham số của HNSW và đánh đổi. | Tiêu đề ẩn dụ “Ba núm điều khiển…”; bảng không phân biệt tham số khi xây và khi truy vấn; không có câu hỏi kiểm tra cho phần 3. | sửa. Tiêu đề “Ba tham số của HNSW”; bảng cột “Dùng khi”; câu hỏi giảm độ trễ không xây lại (đáp án: giảm $efSearch$, giữ $\ge K$). Ghi chú: xu hướng là thực nghiệm; $M$ 6–48 (bài báo tr.8). Đối chiếu số trang bài báo HNSW (trang PDF = trang in): mục 4.1 tr.5–6, mục 4.2.3 tr.8; sửa trích dẫn “tr.5–8” ở H10B. | Mục 6: bảng thêm cột “Dùng khi”, đoạn về tham số khi xây/truy vấn và phạm vi $M$. |
| H13 | Chi phí bộ nhớ, truy vấn, xây dựng và giới hạn của HNSW. | Tiêu đề câu dài; chỉ ký hiệu $O(ND)$, $O(NM)$, không thay số; không nối sang phần PQ. | sửa. Tiêu đề “Chi phí của HNSW”; dòng giả định ($M=16$, $M_{max,0}=32$, $M_{max}=16$, $p=1/16$, mã định danh 8 byte vì $10^{10}>2^{32}$); bảng véc-tơ 12 288 byte/122,88 TB và cạnh cận trên $\approx265$ byte/2,65 TB (tính lại: $32+16/15=33{,}07$; mô phỏng $E[\ell]=0{,}066$; ước lượng của bài báo 302 byte); dòng chi phí truy vấn và điều kiện $\log N$; câu chốt nối sang PQ. | Mục 6: đoạn bộ nhớ có mô hình và khối ví dụ mười tỷ véc-tơ; đoạn truy vấn và xây dựng; câu nối sang lượng tử hóa. |
| Q00 + Q01 | Lượng tử hóa véc-tơ: mã, tái dựng, sai số. | Q00 chỉ có hai thẻ ký hiệu trừu tượng, không hình, không nối với nhu cầu giảm bộ nhớ; Q01 là ví dụ của cùng khái niệm; câu hỏi Q01 “sai số bằng bao nhiêu” có đáp án đã hiện trên trang. | gộp. Trang “Lượng tử hóa véc-tơ”: dòng định nghĩa; hình mới `luong-tu-hoa-vec-to.svg` (ba ô, ranh giới $x_1=1$, $x_2=1$, $x_1=x_2$); phép tính cho $x$; câu hỏi mới $y=(0{,}6;1{,}5)$ (tính lại: mã 2, sai số 0,61). Tọa độ thập phân dùng dấu phẩy, phân cách thành phần bằng dấu chấm phẩy. | Mục 7 đổi tiêu đề “Từ … đến …” thành “Lượng tử hóa véc-tơ và lượng tử hóa tích”; ví dụ một chiều cũ thay bằng ví dụ hai chiều cùng trang, hình, bài tự kiểm; ký hiệu VQ dùng $k$ (PQ dùng $k^*$). |
| Q02 | Đặc tả lượng tử hóa véc-tơ. | Thiếu chi phí mã hóa và lưu bộ mã (Q03 phải tự đưa công thức); k-means chỉ có trong ghi chú; văn xuôi ba dòng khó quét. | sửa. Giữ tiêu đề; công thức argmin; bảng đầu vào (bộ mã học bằng k-means, phá hòa), đầu ra (mã $\lceil\log_2k\rceil$ bit, điều kiện sau), chi phí ($\Theta(kD)$, $kD$ số). Ghi chú: điều kiện Lloyd cần không đủ. | Mục 7: đoạn đặc tả và chi phí thay câu tóm tắt cũ. |

**Rà lại phần 3 (tác tử chỉ đọc, `subagent_type: "fork"`, kế thừa Opus 5.5, effort `high`; bằng chứng: lệnh gọi Agent trong phiên ngày 03/10/2026).** Độ chính xác đạt: chạy lại mọi vết (tham lam; chùm $ef=3$, $ef=2$; trạng thái sau khi mở $b$; ba tầng; chèn $x=2{,}6$; lân cận đa dạng), bất biến H06, $\log_{16}10^{10}=8{,}30$, bộ nhớ 264,5 byte/2,65 TB/97,9%; giả mã khớp Thuật toán 1, 2, 4, 5; trang PDF của bài báo HNSW trùng trang in. Không có phát hiện chặn bàn giao.

| Trang/vị trí | Phát hiện rà lại | Quyết định | Thay đổi |
|---|---|---|---|
| storyboard, outline | (nghiêm trọng) Tổng phần giảng thành 130 phút (phần H 58 phút); outline còn ghi “H00–H13, 48 phút”. | mở | Cân lại thời lượng toàn bài và cập nhật outline sau khi duyệt xong phần 4–6 (các phần này còn gộp/tách trang). Không bàn giao khi chưa đóng mục này. |
| H13, ghi chú mục 6 | (trung bình) Giả thiết của kết luận $\log N$ ghi sai nguồn. Mục 4.2.1 giả thiết mỗi tầng là đồ thị Delaunay chính xác, bậc trung bình bị chặn. | sửa | Mặt trang: “khi mỗi tầng là đồ thị Delaunay chính xác; đồ thị thực tế chỉ xấp xỉ”. Ghi chú diễn giả và ghi chú tự học nêu đủ giả thiết; nguồn “mục 4.2.1, tr.7–8”. |
| H05, H06, H11 (deck và ghi chú) | (trung bình) $e$ vừa là tên đỉnh điểm vào, vừa là biến lân cận/ứng viên. | sửa | Biến đổi thành $y$ (khớp $y\in Y$ của A00). H10B dùng $e\in R$ trong một dòng giả mã: giữ vì ở đó không có đỉnh $e$ của đồ thị ví dụ; ghi nhận. |
| H06B | (trung bình) Đổi từ đồ thị bảy đỉnh sang dãy một chiều không nêu giới hạn kế thừa và lý do. | sửa | Câu dẫn trên trang: số bước tăng theo khoảng cách từ điểm vào tới $q$; xét 12 điểm trên một đường thẳng. Ghi chú: đồ thị bảy đỉnh chỉ có một đường dài tới $z$. Nguồn “mục 3, tr.2–3”. |
| H04 | (nhẹ) $\ell_c$ trước khái niệm tầng. | sửa | “tầng $\ell_c$ (một đồ thị: $\ell_c=0$)”. |
| H08, H13 (deck và ghi chú) | (nhẹ) $p$ trùng tên điểm $p1,\ldots,p11$; “tầng $\ge1$ có $1/16$ số điểm” mơ hồ. | sửa | Đổi thành $\rho=e^{-1/m_L}$; “tầng 1 chứa khoảng $1/16$ số điểm, tầng 2 khoảng $1/256$”. |
| H13 | (nhẹ) Nhãn “cận trên” cho một kỳ vọng. | sửa | “Cạnh, kỳ vọng tối đa”. |
| H10B | (nhẹ) Ràng buộc trình bày như định nghĩa; $ep$ và $\{ep\}$ không thống nhất. | sửa | “$efConstruction$: bề rộng chùm khi chèn, chọn $\ge M$”; ghi chú: ở pha 2, $ep$ là một tập. |
| H10 | (nhẹ) “$ef=3$” chưa gọi tên tham số. | sửa | Câu dẫn: “bề rộng chùm khi chèn $efConstruction=3$”. |
| H07 | (nhẹ) $efSearch$ trước định nghĩa. | sửa | “tầng 0 tìm với chùm rộng $efSearch$”. |
| H11 ghi chú | (nhẹ) Dẫn chiếu “các trang trước”. | sửa | “Trên ví dụ một chiều, hai cách chọn cho cùng kết quả…”. |
| Ghi chú mục 4, 6 | (nhẹ) $\ell$ thay vì $\ell_c$; dòng trống thừa; “recall” lẫn tiếng Anh. | sửa | $\ell_c$; xóa dòng trống; “độ thu hồi”. Hai chỗ “recall” ở mục 9–10 xử lý khi duyệt phần IVF-PQ và kết luận. |
| H08/H13 nguồn | (thông tin) Bài báo tự mâu thuẫn: mục 4.2.1 viết $p=\exp(-m_L)$, mục 4.1 ứng $m_L=1/\ln M$ với $p=1/M$. | ghi nhận | Deck dùng $\rho=e^{-1/m_L}$ suy từ Thuật toán 1 dòng 4, khớp mục 4.1. |
| Q03 | Một bộ mã duy nhất không tạo được mã dài. | Tiêu đề là câu; không nói vì sao cần mã 64 bit; công thức bộ nhớ không thay số. | sửa. Tiêu đề “Giới hạn của một bộ mã lớn”; dòng dẫn theo ví dụ SIFT của bài báo; bảng lưu/mã hóa/học thay số (tính lại $2^{64}\cdot128\cdot4\approx9{,}44\cdot10^{21}$ byte; $2{,}36\cdot10^{21}$ phép toán); câu chốt viết lại tránh mẫu dấu hai chấm. | Mục 7: thêm đoạn “Giới hạn của một bộ mã lớn” với cùng số liệu. |
| Q04 | Định nghĩa lượng tử hóa tích. | Tiêu đề câu “PQ chia không gian…”; hình cũ chữ rất nhỏ; mặt trang thiếu độ dài mã, cách tái dựng, tên đầy đủ. | sửa. Tiêu đề “Lượng tử hóa tích (PQ)”; hình mới `pq-tach-doan.svg` ($D=8$, $m=4$, $k^*=256$, mã 32 bit); ba gạch chia đoạn/mã/tái dựng. Ghi chú: chi phí mã hóa $\Theta(k^*D)$, ký hiệu `M` của Faiss. `pq-split.svg` không còn dùng. | Mục 7: đoạn định nghĩa PQ có công thức tái dựng, chi phí, ví dụ, hình mới. |
| Q05 | Ví dụ mã hóa PQ hai đoạn. | Khoảng cách từng đoạn và sai số chỉ trong ghi chú; không hình; dấu chấm thập phân; tiêu đề không nói thao tác. | sửa. Tiêu đề “Ví dụ mã hóa PQ”; hình mới `pq-vi-du.svg` (biến thể `pq-vi-du-adc.svg` thêm $q$ cho ví dụ ADC); bảng khoảng cách (tính lại 0,08; 6,48; 7,30; 0,10), mã $(0,1)$, tái dựng, sai số 0,18. Bản nháp hình có nhãn đè nhau và nhãn “tâm 1” bị cắt; đã chỉnh trước commit. | Mục 7: khối ví dụ mã hóa PQ và hình. |
| Q06 | Ví dụ khoảng cách bất đối xứng. | Mở bằng dẫn chiếu “từ ví dụ PQ trước” mà không nhắc bộ mã; khái niệm bất đối xứng chưa giải thích; giá trị đúng 0,07 chỉ ở ghi chú; ghi chú tự học dùng một ví dụ ADC khác số liệu deck. | sửa, chuyển sau Q07. Dòng định nghĩa bằng lời; hình `pq-vi-du-adc.svg` nhắc lại bộ mã, $x$ và thêm $q$; bảng hai đoạn (tính lại 0,02; 0,29); so 0,31 với 0,07. Bản nháp hình có nhãn $q$, $x$, “tâm 1” chồng nhau ở đoạn 2, đã chỉnh. | Mục 8: ví dụ ADC thay bằng cùng ví dụ của deck, kèm hình. |
| Q07 | Kích thước mã và bộ mã PQ. | Tiêu đề câu “Không gian mã lớn nhưng bộ mã vẫn nhỏ”; công thức không so với VQ; số liệu 512 byte/5,12 TB chỉ ở ghi chú. | sửa. Tiêu đề “Kích thước mã và bộ mã PQ”; bảng VQ/PQ cùng mã 64 bit (tính lại $256^8=2^{64}$, $256\cdot128=32\,768$) theo Princeton lớp 8 tr.32; câu chốt thay số kho mở đầu ($m=512$, 512 byte, 5,12 TB, nhỏ hơn 24 lần). Xóa `quy-mo-vector.svg` (không còn dùng ở deck lẫn ghi chú). | Mục 7: đoạn kích thước có bảng so sánh và khối ví dụ kho mười tỷ véc-tơ thay đoạn “Áp dụng…” và hình cũ. |
| Q08 | Công thức ADC. | Tiêu đề câu “…giữ truy vấn đầy đủ”; hai thẻ lặp định nghĩa; chưa nêu vì sao tính trước được (cầu nối sang bảng tra). | sửa. Tiêu đề “Khoảng cách bất đối xứng (ADC)”; công thức; hai gạch (dạng của $q$, $y$; số hạng chỉ phụ thuộc $q^{(j)}$, $i_j$); câu chốt $k^*$ giá trị mỗi đoạn. Ghi chú: SDC theo đúng nhận định của bài báo (tr.4: ưu điểm duy nhất của SDC là truy vấn ở dạng mã; ADC sai lệch thấp hơn với độ phức tạp tương tự). Bản nháp ghi “chi phí tương đương (Bảng II)” không kiểm được từ văn bản nguồn, đã thay trước commit. | Mục 8: đoạn định nghĩa ADC dùng cùng ký hiệu deck ($q^{(j)}$, $c^{(j)}_{i}$), giải thích số hạng; đoạn SDC theo bài báo. |
| Q09 | Bảng tra khoảng cách và chi phí. | Tiêu đề câu “Bảng tra biến khoảng cách thành phép cộng”; hình `pq-lut.svg` chữ nhỏ, không có số; chi phí một dòng ký hiệu. | sửa. Tiêu đề “Bảng tra khoảng cách”; bảng HTML 2×2 của ví dụ (tính lại 0,02; 7,22; 6,29; 0,29), ô của mã $(0,1)$ viền đậm (CSS `.ann-selected`); chấm hai mã (0,31; 13,51); bảng chi phí. Xóa `pq-lut.svg`. | Mục 8: đoạn bảng tra với bảng ví dụ, bảng chi phí, câu về quét $\Theta(Nm)$; ký hiệu $q_j$, $c_{j,i}$ cũ đổi sang $q^{(j)}$, $c^{(j)}_i$. |
| Q10 | Giới hạn của PQ quét đầy đủ, nối sang IVF. | Tiêu đề câu; chi phí chỉ ký hiệu; “tầng định tuyến” là thuật ngữ mới không giải thích. | sửa. Tiêu đề “Giới hạn của PQ quét đầy đủ”; bảng quét véc-tơ gốc và quét mã PQ cho $10^{10}$ véc-tơ (tính lại $Nm=5{,}12\cdot10^{12}$; lập bảng $256\cdot3072=786\,432$); câu hỏi thời gian (5,12 s, giả định $10^{12}$ lần tra/giây); câu chốt hai thừa số. | Mục 8: đoạn giới hạn có bảng và bài tự kiểm. |
| I00 | Mở phần 5: tệp đảo và vai trò trong IVF-PQ. | Tiêu đề câu; hai thẻ chữ không hình; “định tuyến”, “véc-tơ dư” chưa giải thích. | viết lại. Tiêu đề “Tệp đảo (IVF)”; ví dụ hai chiều mới dùng cho cả phần 5 (bốn tâm thô, 16 điểm, $q=(6;3{,}5)$; tính lại bình phương khoảng cách tới tâm: 18,25; 6,25; 36,25; 24,25); hình `tep-dao.svg` và `tep-dao-du.svg` (sinh bằng `generate_svg.py`); danh sách đảo là bảng HTML. Bản nháp đặt danh sách trong hình nên chữ khoảng 12 px, đã tách ra trước commit. | Mục 9 đổi tiêu đề thành “Tệp đảo và IVF-PQ”; đoạn định nghĩa, khối ví dụ, hình. |

**Rà lại phần 4 (tác tử chỉ đọc, `subagent_type: "fork"`, kế thừa Opus 5.5, effort `high`; bằng chứng: lệnh gọi Agent trong phiên ngày 03/10/2026).** Độ chính xác đạt: mọi số tính lại khớp (VQ 3,05/0,25/5,45 và 2,61/4,21/0,61; $9{,}44\cdot10^{21}$ byte; $256^8=2^{64}$; 5,12 TB, tỷ lệ 24; PQ 0,08/6,48/7,30/0,10, sai số 0,18; ADC 0,31 và 0,07; bảng tra; $5{,}12\cdot10^{12}$, 5,12 s); số trang trích dẫn khớp nguồn. Không có phát hiện chặn bàn giao hoặc nghiêm trọng.

| Trang/vị trí | Phát hiện rà lại | Quyết định | Thay đổi |
|---|---|---|---|
| Q00 | (trung bình) Trang mở phần không nêu nhu cầu trên mặt trang. | sửa | Dòng đầu: “Véc-tơ gốc chiếm 122,88 TB. Lượng tử hóa thay…”. |
| storyboard “Hành trình khái niệm” | (trung bình) Còn mô tả thứ tự cũ (Q01; Q06 trước Q07); dòng HNSW cũng cũ. | sửa | Viết lại hai dòng HNSW và lượng tử hóa tích theo thứ tự hiện hành. |
| Q00 | (nhẹ) “$\log_2 k$ bit” không khớp ví dụ 2 bit và Q02. | sửa | $\lceil\log_2 k\rceil$. |
| Q00 ghi chú, mô tả SVG, ghi chú mục 7 | (nhẹ) Ranh giới ô viết $x_1$, $x_2$ hoặc “x = 1, y = 1” trùng tên điểm $x$, $y$. | sửa | Viết bằng lời “tọa độ thứ nhất bằng 1…”. |
| Q04 | (nhẹ) Giả thiết $m\mid D$ chỉ ở ghi chú. | sửa | “($m$ chia hết $D$)” trên mặt trang. |
| Q05 | (nhẹ) Cột không nói là bình phương khoảng cách. | sửa | Tiêu đề cột “$\|x^{(j)}-c\|^2$, tâm 0”. |
| Q06→Q08, ghi chú mục 7–8 | (nhẹ) Véc-tơ trong kho đổi tên $x$ → $y$ không nói tương ứng; công thức VQ trong ghi chú dùng $y$ trùng điểm câu hỏi. | sửa | Ghi chú Q08: “$y$ chính là véc-tơ $x$”; ghi chú tự học: công thức VQ dùng $x$, đoạn ADC ghi “ở ví dụ dưới đây là $x$”. |
| Q07 | (nhẹ) Nhãn hàng “Mã hóa” thiếu đối tượng. | sửa | “Mã hóa một véc-tơ”. |
| Q08 ghi chú | (nhẹ) Câu SDC/ADC dài ba mệnh đề. | sửa | Tách hai câu. |
| Q10 ghi chú | (nhẹ) Giả định một lần tra ngang một lượt tọa độ chưa nói ra; “Ý tiếp theo là…” gần lời chuyển trang. | sửa | Nêu giả định; viết lại câu nối. |
| I00 | (nhẹ, ngoài phạm vi) Dạng cũ. | đã sửa | Commit I00 (`bc6f106`). |
| I01 | Gán vào tâm thô và chọn danh sách cần mở. | Tiêu đề câu; ví dụ hai tâm rời rạc, không cho thấy tác dụng của $nprobe$. | sửa. Tiêu đề “Chọn danh sách cần mở”; công thức; hình biến thể `tep-dao-o.svg` (không đánh dấu “mở”, vì câu hỏi dùng $nprobe=1$); bảng bốn tâm; câu hỏi $y_3$ (tính lại 9,49; 15,49; $\|q-y_3\|^2=2{,}34$; $\|q-y_8\|^2=1{,}25$). | Mục 9: đoạn chọn danh sách, công thức, bài tự kiểm có lời giải. |
| I02 | Phần dư và truy vấn dư riêng cho từng danh sách. | Tiêu đề câu; chưa giải thích vì sao cần truy vấn dư riêng; câu “Trong ví dụ ngay trước…” dẫn chiếu bằng lời. | sửa. Tiêu đề “Mã hóa phần dư”; đẳng thức $\|q-y\|=\|(q-\mu_i)-r(y)\|$; hình `tep-dao-du.svg` phóng to hai ô dưới (mũi tên vẽ tay thay marker để tránh đầu mũi tên phóng to theo nét); ví dụ $y_8$ (tính lại 1,25; dùng nhầm bảng 31,25). | Mục 9: đoạn mã hóa phần dư, đẳng thức, khối ví dụ, hình. |
| I03 | Chi phí truy vấn IVF-PQ. | Tiêu đề câu; chưa đếm theo bước; không thay số; giả thiết danh sách cân bằng chỉ ở ghi chú; đặt trước trang thuật toán. | sửa, chuyển sau I04. Tiêu đề “Chi phí truy vấn IVF-PQ”; dòng giả định ($k_c=10^5\approx\sqrt N$ theo Princeton lớp 9 tr.5, $nprobe=64$, cân bằng); bảng ba bước thay số (tính lại $3{,}07\cdot10^8$; $5{,}03\cdot10^7$; $3{,}28\cdot10^9$; tổng $3{,}63\cdot10^9$; tỷ lệ 1409). | Mục 9: đoạn chi phí, khối ví dụ kho mười tỷ véc-tơ; “recall” → “độ thu hồi”. |
| I04 | Thuật toán truy vấn IVF-PQ. | Tiêu đề câu; hình luồng chữ rất nhỏ; danh sách bước thiếu khởi tạo, vòng lặp, cấu trúc giữ $K$ kết quả; không có vết chạy. | sửa. Tiêu đề “Thuật toán truy vấn IVF-PQ”; giả mã 8 dòng theo mục IV-C của bài báo; bảng khoảng cách hai danh sách mở (tính lại; ghi rõ giả định ADC không sai số); câu hỏi $nprobe=1$ (recall@3 $=2/3$). Xóa `ivfpq-flow.svg`. | Mục 9: đoạn thuật toán có giả mã, trường hợp ít hơn $K$, khối ví dụ hai giá trị $nprobe$. |
| C00 | So sánh bốn cấu trúc và trả lời tình huống mở đầu. | Bảng chỉ có ký hiệu; “Trả lời bài toán mở đầu” là lời khuyên chung; không thu hồi tình huống bằng số. | sửa. Tiêu đề “So sánh bốn cấu trúc”; dòng giả định; bảng năm cột (thừa số được giảm, bộ nhớ mỗi véc-tơ, một truy vấn, tham số chất lượng); câu chốt thay số (tính lại 125,5 TB; 5,2 TB). Bản nháp có cụm “giả định như các phần trước”, đã đổi thành liệt kê giả định. | Mục 10: tiêu đề “So sánh bốn cấu trúc”; bảng sáu cột (thêm rủi ro chất lượng), đoạn thu hồi tình huống mở đầu. |
| C01, C02 (mới) | Tự kiểm cuối bài. | Phần kết thiếu nhiệm vụ tự kiểm (tiêu chuẩn mục 2; việc mở từ lượt rà phần 1–2). | thêm. Hai trang “Tự kiểm tra: độ thu hồi và đồ thị”, “Tự kiểm tra: PQ và IVF-PQ”, mỗi trang ba câu với dữ kiện mới; đáp án trong ghi chú diễn giả, kiểm bằng chương trình (mô phỏng Thuật toán 2 cho câu chùm). Đóng việc mở của P02. | Mục 12: thay danh sách 8 câu không đáp án bằng sáu bài tự kiểm có lời giải, khớp hai trang. |
| R00 | Mở phần bài tập: sổ thực hành, dữ liệu, ba nhiệm vụ. | Không nêu dữ liệu (kích thước, vai trò của `xt`, `xb`, `xq`, `gt`); đường dẫn nội bộ `sources/…` trên mặt trang; dòng điều phối “Thời gian máy được báo riêng”. | sửa. Tiêu đề “Sổ thực hành và dữ liệu”; bảng bốn mảng (đối chiếu ô 2: `SyntheticDataset(64, 1000000, 10000, 100)`, ô 21: `faiss.knn` với $k=10$); bảng ba nhiệm vụ. Hướng dẫn chuẩn bị chuyển vào ghi chú diễn giả. | Mục 11 đổi tiêu đề “Thực hành với sổ thực hành Princeton”; phần chuẩn bị có bảng dữ liệu, ánh xạ ký hiệu Faiss, bảng nhiệm vụ. |
| R01 | Nhiệm vụ 1: cấu trúc mã PQ trên dữ liệu thật. | “Sản phẩm: bảng kích thước” không nói điền gì; tham số Faiss không nối với $m$, $b$, $k^*$; liệt kê tên biến không giải thích. | sửa. Tiêu đề “Nhiệm vụ 1: cấu trúc mã PQ”; dòng ô 83 và ánh xạ $D=64$, $m=4$, $b=8$; bảng dự đoán/giá trị in ra cho `code_size`, `pq_centroids.shape`, `xb_codes.shape` (đáp án 4; $(4,256,16)$ theo chú thích ô 94; $(10\,000,4)$). Không đổi dữ kiện hay nhiệm vụ của nguồn; chỉ chia bước. | Mục 11, nhiệm vụ 1: bảng điền và lời giải; câu nối sang ô 96–97. |

**Rà lại phần 5–6 (tác tử chỉ đọc, `subagent_type: "fork"`, kế thừa Opus 5.5, effort `high`; bằng chứng: lệnh gọi Agent trong phiên ngày 03/10/2026).** Độ chính xác đạt: ví dụ bốn ô, $y_3$, $y_8$, phần dư, 1,25/31,25, recall@3 $=2/3$; chi phí I03 ($3{,}634\cdot10^9$, tỷ lệ 1409); C00 (125,53 TB; 5,2 TB); đáp án C01–C02 (mô phỏng); giả mã I04 khớp mục IV-C; số trang đúng. Không có phát hiện chặn bàn giao hoặc nghiêm trọng. Sáu câu tự kiểm phủ ba mục tiêu của P02.

| Trang/vị trí | Phát hiện rà lại | Quyết định | Thay đổi |
|---|---|---|---|
| I02 | (trung bình) Lý do mã hóa phần dư chỉ ở ghi chú. | sửa | Gạch đầu: “Phần dư nhỏ hơn $y$ nên mã PQ cùng số bit chính xác hơn”. |
| I04 | (trung bình) Đầu ra và trường hợp ít hơn $K$ chỉ ở ghi chú. | sửa | Dòng đầu ra dưới khối giả mã. |
| storyboard “Hành trình khái niệm” | (trung bình) Dòng IVF-PQ còn thứ tự cũ. | sửa | Viết lại theo thứ tự hiện hành. |
| C01, C02 ghi chú | (nhẹ) Ánh xạ câu hỏi sang mục tiêu lẫn số. | sửa | “câu 1 → mục tiêu 1…” theo P02. |
| C01 câu 3 | (nhẹ) 265 byte giả định mã định danh 8 byte; đáp án sát ngưỡng phụ thuộc GB/GiB. | sửa | Đề ghi “mã định danh 8 byte” và “1 GB $=10^9$ byte” (deck và ghi chú). |
| I03 ghi chú | (nhẹ) Giả định một lần tra ngang một lượt tọa độ chưa nhắc lại. | sửa | Nêu trong ghi chú diễn giả và ghi chú tự học. |
| I00 | (nhẹ) “thô” chưa giải thích. | sửa | “Lượng tử hóa thô (VQ với ít tâm, $k_c$ tâm)”. |
| C00 ghi chú | (nhẹ) Câu “dùng đồ thị để chọn tâm thô” không có trong nguồn đã đối chiếu; dẫn chiếu “các trang chi phí”. | sửa | Bỏ câu (deck và ghi chú tự học); “phần chi phí HNSW, PQ và IVF-PQ”. |
| I02 ghi chú | (nhẹ) Lời nhấn “sai hoàn toàn”. | sửa | “31,25 thay vì 1,25” (deck và ghi chú). |
| C00 | (nhẹ) Câu chốt chưa nêu kết luận lựa chọn. | sửa | “trong bộ nhớ một máy, IVF-PQ khả thi, với $nprobe$ chọn theo ngưỡng độ thu hồi”. |
| R00 | (ngoài phạm vi) Dạng cũ. | đã sửa | Commit R00 (`b93a48e`). |
| R02 | Hoàn thiện ô tái dựng 96–97. | Khối mã ghi `assert np.all(...)` trong khi ô 97 của nguồn không có `assert`; không nhắc công thức tái dựng; tiêu đề mô tả thao tác. | sửa. Tiêu đề “Tái dựng véc-tơ 123 bằng tay”; chép đúng ô 96–97 (đối chiếu sổ nguồn); dòng gợi ý công thức $\widehat x$; dòng yêu cầu. | Mục 11, nhiệm vụ 1: khối mã ô 96–97 và lời giải. |
| R03 | Ba điều kiện để tái dựng khớp với `decode`. | Không rõ phải lập luận gì; thiếu đáp án mẫu; tiêu đề chưa nói khớp với gì. | sửa. Tiêu đề “Điều kiện để tái dựng khớp”; bảng điều kiện với cột “Nếu vi phạm thì”; chỉ số Python $j=0,\ldots,m-1$ ghi rõ để không lẫn với $x^{(1)},\ldots,x^{(m)}$ của bài; đáp án mẫu và rubric trong ghi chú. | Mục 11, nhiệm vụ 1: bảng điều kiện và lời giải. |
| R04 | Nhiệm vụ 2: ba cấu hình PQ cùng 6 byte. | Bảng điền sẵn `dsub`, `ksub`; không có cột cho MSE và thời gian; ký hiệu $M_{PQ}$ khác $m$ của bài; ghi chú tự học gọi thời gian là “huấn luyện/mã hóa”, sai so với ô 99. | sửa. Tiêu đề “Nhiệm vụ 2: cùng ngân sách 6 byte”; dòng ô 99 với ánh xạ `M`→$m$, `nbits`→$b$; bảng sáu cột, bốn cột để dự đoán/ghi; đáp án dự đoán trong ghi chú (16, 8, 4; 4096, 64, 8). | Mục 11, nhiệm vụ 2: mô tả đúng ô 99, bảng điền, lời giải. |
| R05 | Phân tích ba cấu hình cùng ngân sách. | Yêu cầu chung, chưa gắn với mô hình chi phí của bài và nhận định của nguồn; tiêu đề “Đọc đánh đổi…”. | sửa. Tiêu đề “Phân tích đánh đổi cùng ngân sách”; ba yêu cầu: `code_size`; MSE so với nhận định của Princeton lớp 8 tr.33; thời gian giải thích bằng $k^*D$ (tính lại 262 144; 4 096; 512). Rubric giữ 10 điểm. | Mục 11, nhiệm vụ 2: thêm ba yêu cầu phân tích và yêu cầu kết luận. |
| R06 | Nhiệm vụ 3: xây dựng IVF-PQ từ chuỗi cấu hình. | “Giải thích chuỗi cấu hình” không nói giải thích gì; không nối với $k_c$, $m$, $b$. | sửa. Khối mã ô 149–151; bảng $k_c$, $m$, $b$, byte mã, $|L_i|$ trung bình (đáp án 200; 16; 8; 16 byte; 50); dòng sản phẩm về ô 150, 151. Ý nghĩa `np` giữ theo tài liệu Faiss. | Mục 11, nhiệm vụ 3: khối mã, yêu cầu, lời giải. |
| R07 | Vòng đo $nprobe$ và ý nghĩa đại lượng đo. | Không chép ô 155; $nok/|xq|$ không nối với độ thu hồi (ghi chú cũ nói “không gọi là recall@K”, trong khi với $K=1$ đó là $\operatorname{recall@1}$ theo định nghĩa của bài; trục của Princeton lớp 8 tr.4 cũng là “1-recall@1”); tiêu đề chứa $nprobe$ bị viết hoa. | sửa. Tiêu đề “Độ thu hồi và thời gian theo số danh sách mở”; khối mã ô 155 (đối chiếu sổ nguồn); bảng ba đại lượng; ghi chú: không phải recall@10, thời gian mỗi truy vấn chia 5000, số mã ≈ $50\,nprobe$. | Mục 11, nhiệm vụ 3: khối mã ô 155, bảng đại lượng, đoạn diễn giải. |
| R08 | Phiếu báo cáo nhiệm vụ 3. | Một hàng trống cho năm giá trị; thiếu cột thời gian mỗi truy vấn và số mã được chấm; tiêu đề khó hiểu. | sửa. Tiêu đề “Phiếu báo cáo nhiệm vụ 3”; bảng năm hàng với cột recall@1, tổng ms, ms mỗi truy vấn, số mã được chấm; yêu cầu vẽ và giải thích bằng số mã được chấm. Không thêm giá trị $nprobe$ hay mục tiêu mới. | Mục 11, nhiệm vụ 3: phiếu năm hàng và lời giải phần tính được. |

### Cân lại thời lượng và đồng bộ outline

| Vị trí | Phát hiện | Quyết định | Thay đổi |
|---|---|---|---|
| storyboard, outline | (nghiêm trọng, mở từ lượt rà phần 3) Tổng phần giảng 141 phút sau khi thêm, gộp, tách trang; outline còn dải trang và phút cũ. | sửa, đóng | Cân lại từng trang: mở đầu 6, bài toán 11, HNSW 44, PQ 28, IVF-PQ 16, tổng kết 15 phút; tổng 120 (40 trang giảng). Bài tập giữ 60 phút (R01–R08: 6+9+5+10+10+6+9+5). Bảng storyboard và mục “Thời lượng” của từng trang khớp nhau. Outline: bảng mạch theo thứ tự deck, ghi gộp/tách/thêm/chuyển; ký hiệu mới ($k$, $x$, $y$, $\rho$, ký hiệu IVF); kiểm kê 19 SVG sinh bằng `generate_svg.py`; bảng nguồn thêm H06B, C00–C02. |

**Rà lại phần 7 (tác tử chỉ đọc, `subagent_type: "fork"`, kế thừa Opus 5.5, effort `high`; bằng chứng: lệnh gọi Agent trong phiên ngày 03/10/2026).** Trung thành với nguồn: mọi mã, số ô, tham số và đáp án khớp sổ thực hành (ô 1, 2, 21, 83, 94–97, 99, 149–151, 155); `nok/100` đúng là recall@1 theo A01; ô 99 đo mã hóa cộng giải mã, không gồm huấn luyện; bài tập tổng 60 phút. Không có phát hiện chặn bàn giao hoặc nghiêm trọng.

| Trang/vị trí | Phát hiện rà lại | Quyết định | Thay đổi |
|---|---|---|---|
| R07, R08, ghi chú mục 11 | (trung bình) “ms mỗi truy vấn = tổng/5000” là trung bình theo lô nhiều luồng, không phải độ trễ một truy vấn; ghi chú tự học tự mâu thuẫn. | sửa | Cột “ms trung bình mỗi truy vấn trong lô”; câu nêu không phải độ trễ một truy vấn, phụ thuộc số luồng ô 1. |
| Ghi chú diễn giả R00, R01, R04, R06, R07 | (trung bình) Chỉ dẫn điều phối và thời lượng trong ghi chú diễn giả. | sửa | Bỏ khỏi ghi chú diễn giả; chuyển vào storyboard (mục “Ghi chú điều phối phần bài tập”); yêu cầu kỹ thuật cho sinh viên đưa vào mục 11 ghi chú tự học. |
| R07 ghi chú | (nhẹ) Trích Princeton lớp 8 tr.4 sai; “trang tradeoff”. | sửa | “tr.3 và tr.5”; “trang đánh đổi”. |
| R07 | (nhẹ) Khối mã bỏ dòng `print` của ô 155; thiếu dòng yêu cầu. | sửa | Thêm dòng `print`; “Chạy ô 152–155; ghi kết quả vào phiếu báo cáo.” (deck và ghi chú). |
| R01 | (nhẹ) Ô 95 không in `xb_codes.shape`. | sửa | Cột “Giá trị kiểm bằng mã”; ghi chú nêu cách kiểm. |
| R01, R03 ghi chú | (nhẹ) Thang điểm lệch. | sửa | R01: bảng kèm giải thích 3 điểm, khớp rubric 10 điểm ở R03. |
| R02, R08 ghi chú | (nhẹ) Câu biện minh của người soạn. | sửa | Bỏ khỏi ghi chú diễn giả; ghi trong storyboard. |
| R00, R01, R06, ghi chú mục 11 | (nhẹ) Tên nhiệm vụ không thống nhất. | sửa | “Nhiệm vụ 1: mã và tái dựng PQ”; “Nhiệm vụ 2: cùng ngân sách 6 byte”; “Nhiệm vụ 3: chỉ mục IVF-PQ” ở R00, tiêu đề trang và ghi chú. |
| R00 ghi chú | (nhẹ) Không nhắc số luồng ô 1. | sửa | Thêm câu về 32 luồng và việc ghi lại số luồng. |
| `index.html` | (nhẹ) Mô tả Bài 7 dùng từ “runbook”. | sửa | “sổ thực hành Princeton”; thêm “tệp đảo” trước IVF-PQ. Kiểm: hai liên kết trả 200 ở 1440 và 390 px, không tràn ngang. |

### Duyệt lại toàn bài từ góc nhìn sinh viên

Tác tử chỉ đọc (`subagent_type: "fork"`, kế thừa Opus 5.5, effort `high`; bằng chứng: lệnh gọi Agent trong phiên ngày 03/10/2026) đóng vai sinh viên năm 2, đọc 49 trang, ghi chú diễn giả, ảnh chụp và ghi chú tự học. Không có phát hiện chặn bàn giao; 1 nghiêm trọng, 4 trung bình, 9 nhẹ. Mạch toàn bài được đánh giá chặt: hai thừa số chi phí ở A03 xuyên suốt; mỗi phần kết bằng giới hạn tạo nhu cầu cho phần sau; C00 thu hồi tình huống bằng số; C01–C02 phủ ba mục tiêu. Mỗi dòng dưới đây là một commit riêng.

| Trang/vị trí | Phát hiện | Quyết định | Thay đổi |
|---|---|---|---|
| H01 | (nhẹ) Ký hiệu $e{:}9$ trong bảng chưa giải thích trên trang. | sửa | Câu đầu thêm “Ký hiệu $e{:}9$ nghĩa là $d(e,q)=9$.” Ghi chú tự học đã có câu tương ứng. |
| H03 → H03, H03B | (nghiêm trọng) Quy tắc thêm/bỏ khỏi $W$, nghĩa của “mở” và điều kiện dừng chỉ ở ghi chú; sinh viên không tự tái tạo được vết hay trả lời câu hỏi $ef=2$. | tách | H03 “Tìm kiếm chùm”: ba gạch quy tắc cạnh hình đồ thị ví dụ, câu chốt $ef=1$ trùng tham lam. H03B “Vết tìm kiếm chùm”: dòng điểm vào và ký hiệu, hình đường chùm, bảng (ba lần mở cuối gộp một hàng), câu hỏi. Bản nháp đặt cả quy tắc và bảng trên một trang tràn khung (đáy 774/720). Thời lượng 4 phút chia 2 + 2. Ghi chú tự học đã có quy tắc và bảng đủ bảy lần mở. |
| H06B | (trung bình, nhẹ) Tọa độ ví dụ một chiều không nêu trên trang; mệnh đề “số bước tăng theo khoảng cách” lỏng. | sửa | “Nếu chỉ có cạnh ngắn, số bước tăng theo khoảng cách…”; “$s$ ở tọa độ 0, $p_i$ ở tọa độ $i$, $q$ ở 6,4”. Ghi chú tự học mục 5 nêu cùng tọa độ. |
| H10 | (trung bình) Tọa độ các điểm $p_i$ không có trên trang nên không tự tính được khoảng cách tới $x$. | sửa | Câu dẫn thêm “($s$ ở 0, $p_i$ ở $i$)”. Ghi chú tự học: tọa độ đã nêu ở đoạn cạnh dài (mục 5). |
| H13 | (trung bình, nhẹ) “Đồ thị Delaunay” chưa được giới thiệu; hệ số $\rho/(1-\rho)$ không giải thích trên trang. | sửa | “đồ thị lân cận lý tưởng (đồ thị Delaunay)”; dòng chú thích “$\rho/(1-\rho)$: kỳ vọng số tầng trên của một điểm”. Ghi chú diễn giả và ghi chú tự học định nghĩa đồ thị Delaunay (ô Voronoi kề nhau; tham lam luôn tới điểm gần nhất, bài báo HNSW tr.2). |
| Q09 | (nhẹ) Dữ kiện $q$ và bộ mã chỉ ở ghi chú; không kiểm được các ô 7,22 và 6,29. | sửa | Dòng ví dụ trên trang: $q$ và hai bộ mã con. Ghi chú tự học đã nêu dữ kiện ở ví dụ ADC ngay trước bảng. |
| R02; ghi chú C01, C02, R02, R08, P02 | (nhẹ) Tiêu đề “bằng tay” mang sắc thái khẩu ngữ; còn dẫn chiếu trang trong ghi chú diễn giả; P02 đánh số phần khác số phần trong deck. | sửa | Tiêu đề “Tái dựng thủ công véc-tơ 123”; “mục tiêu học tập của bài”, “phần giải thích điều kiện khớp”, “bảng cấu hình của nhiệm vụ 3”; ghi chú P02 gọi phần theo tên. |
| Ghi chú tự học, mục tiêu và ký hiệu | (trung bình, nhẹ) Bảng ký hiệu còn bản cũ, thiếu $m_L$, $\rho$, $\ell,\ell_c$, `efSearch`, `efConstruction`, $M_{\max},M_{\max,0}$, $k$, $b$, ký hiệu IVF và quy ước $x$/$y$; sáu mục tiêu không ánh xạ sang ba mục tiêu của deck; “Bài 05–06 đã trình bày LSH và phân dải”. | sửa | Mục tiêu gom thành ba mục khớp P02; bảng ký hiệu 15 dòng theo outline; “Bài 06 đã trình bày LSH”. |
| H09, Q05, Q06 (hình) | (nhẹ) Nhãn trong hình khoảng 18–19 px ở 1600 × 900, sát ngưỡng khi chiếu. | sửa | `generate_svg.py`: chữ hình ba tầng gọn 30 → 36; nhãn “tâm” và tiêu đề khung trong hình ví dụ PQ 28 → 32. Đã chụp lại, không chồng chữ. |

**Tái rà sau lượt góc nhìn sinh viên (tác tử chỉ đọc, `subagent_type: "fork"`, kế thừa Opus 5.5, effort `high`).** Quy tắc H03 khớp Thuật toán 2 và đủ để tái tạo H03B, trả lời câu $ef=2$; tọa độ, mệnh đề Delaunay, $\rho/(1-\rho)$, bảng tra Q09 đúng; ranh giới các trang đã sửa nối tự nhiên. Không có phát hiện chặn bàn giao, nghiêm trọng hay trung bình; 5 phát hiện nhẹ, xử lý như sau.

| Trang/vị trí | Phát hiện | Quyết định | Thay đổi |
|---|---|---|---|
| H03 | (nhẹ) Chưa nói vì sao cần chùm; chưa nêu khởi tạo. | sửa | Gạch đầu thêm “ban đầu $C=W=\{\text{điểm vào}\}$”; câu chốt “Giữ nhiều hướng để không kẹt ở cực tiểu cục bộ; …”. |
| H13 ghi chú diễn giả, ghi chú tự học mục 6 | (nhẹ) “số chiều thấp”, “tăng nhanh” lệch nguồn (tr.7: dữ liệu Euclid ngẫu nhiên; bậc Delaunay tăng theo hàm mũ của số chiều). | sửa | Viết lại theo đúng nguồn. |
| R08 ghi chú | (nhẹ) “nhiệm vụ 3 2 điểm” khó đọc. | sửa | “bảng cấu hình (2 điểm)”. |
| Q09 ghi chú | (nhẹ) Lặp dữ kiện đã có trên trang. | sửa | Bỏ câu lặp. |

### Kiểm định cuối lượt duyệt từng trang, 03/10/2026

**Kiểm hiển thị (Playwright Chromium, máy chủ `python3 -m reloadserver 8775`).** Deck 50 trang (41 giảng, 9 bài tập): 1600 × 900 không tràn khung (đáy nội dung lớn nhất 638/720), không `.katex-error`, không ký tự `$` sót ngoài KaTeX, cỡ chữ nhỏ nhất ngoài KaTeX 24 px (khối mã và bảng gọn), không phần tử tràn ngang; 390 × 844 (chế độ cuộn của Reveal) không tràn ngang; không lỗi console hay lỗi trang; không yêu cầu mạng ngoài máy chủ cục bộ; phím mũi tên chuyển trang. Mọi ảnh là SVG có `role="img"` và mô tả; không ảnh raster. Ghi chú tự học ở 1440 × 900, 390 × 844 và in: không lỗi KaTeX, không tràn ngang, ảnh tải đủ, liên kết deck trả 200. Index: hai liên kết Bài 7 trả 200 ở hai khổ. Đã xem ảnh chụp từng trang sau mỗi lần sửa; ảnh lưu ngoài kho tại `/tmp/lec07-work/shots/`.

**Kiểm tĩnh.** Không còn khối `<style>`, không `style=""` nội tuyến, không `fragment`; `data-slide-id` duy nhất (50) và không xuất hiện trên mặt trang hay trong ghi chú diễn giả; khối mã có `data-trim`, ngôn ngữ `plaintext` cho giả mã và `python` cho ô sổ thực hành; `git diff --check` sạch ở mọi commit.

**Phiếu kiểm tra của `slide_authoring_standard.md`.**

| Mục | Kết quả |
|---|---|
| Tiêu đề ngắn, gọi đúng khái niệm; không câu hỏi, không câu kể tiến trình | đạt; đã bỏ “Từ … sang …”, các tiêu đề câu và tiêu đề có ký hiệu bị viết hoa |
| Văn phong học thuật; biên tập và tự kiểm theo `no-ai-slop`/`eval.md` | đạt; đã bỏ mẫu dấu hai chấm kịch tính, lời nhấn “sai hoàn toàn”, dẫn chiếu trang trong ghi chú diễn giả |
| Không văn nói, chỉ dẫn biên soạn hoặc điều phối trên trang và trong ghi chú diễn giả | đạt; chỉ dẫn điều phối phần bài tập chuyển vào storyboard |
| Mỗi trang một mục đích, có vai trò trong storyboard | đạt; mục “Chi tiết từng trang” có đủ 50 trang |
| Mỗi phần mở rõ nhu cầu và nối sang phần sau | đạt; hai thừa số chi phí ở A03 xuyên suốt; H13 → Q00, Q10 → I00 |
| Phần kết thu hồi tình huống ban đầu, có 4–6 nhiệm vụ tự kiểm; thời lượng tách riêng | đạt; C00 thay số, C01–C02 sáu câu; 120 + 60 phút |
| Một trọng tâm mỗi trang; chú thích khớp hình, bảng, mã | đạt |
| Tiên quyết và ký hiệu được thiết lập trước nơi dùng | đạt; $x$/$y$, $\rho$, $\ell_c$, ký hiệu IVF có trong outline và bảng ký hiệu ghi chú |
| Cụm thuật toán đủ đặc tả, ví dụ, giả mã, lập luận đúng, dừng, biên, chi phí | đạt cho SEARCH-LAYER (H03–H06), truy vấn và chèn HNSW (H07–H11, H13), VQ/PQ/ADC (Q00–Q10), IVF-PQ (I00–I03) |
| Ví dụ tính lại được; phân biệt nguồn và phần dựng | đạt; mọi vết và số tính lại bằng chương trình; ví dụ dựng ghi rõ |
| Mô hình chi phí, đơn vị, giả thiết trước phép tính | đạt (P01, A00, H13, Q03, Q07, Q10, I03) |
| Mỗi số hạng chi phí truy được về một bước | đạt (I03 theo các bước của I04) |
| Hình, giả mã, bảng, lời giải dùng cùng dữ kiện và ký hiệu | đạt; không còn dẫn chiếu “ví dụ trước” bằng lời, mỗi trang dùng lại ví dụ có hình hoặc dữ kiện trên trang |
| Câu hỏi đo đúng mục tiêu, có đáp án trong ghi chú | đạt |
| Bản render đọc được, không tràn hay chồng lấn | đạt |
| Khối mã có `data-trim`; công thức render đúng; không `fragment` | đạt |
| Sai khác nguồn và ngoại lệ có lý do trong nhật ký | đạt; xem các bảng duyệt và rà lại ở trên |

**Phân công vai trò trong lượt này.** Điều phối và biên tập: phiên Claude Code, Opus 5.5, effort `high`. Tác tử rà chỉ đọc (`subagent_type: "fork"`, kế thừa Opus 5.5): phần 1–2; phần 3; phần 4; phần 5–6; phần 7; góc nhìn sinh viên toàn bài; tái rà sau lượt góc nhìn sinh viên. Bằng chứng: các lệnh gọi Agent trong phiên. Chỉ một tác nhân ghi tệp (điều phối viên).

**Giới hạn còn lại.** Phần bài tập không có nhiệm vụ HNSW vì sổ nguồn không có (giữ quyết định cũ). Thời gian chạy máy của sổ thực hành phụ thuộc môi trường, không có đáp án số cố định.

## Bổ sung trang tiêu đề mạch 2026-10-14

Căn cứ: `AGENTS.md` mục "Trang tiêu đề mạch" và hai gạch đầu dòng về mạch mở đầu, mạch kết luận trong "Mẫu RevealJS bắt buộc"; yêu cầu người dùng 2026-10-14 bổ sung trang tiêu đề mạch cho các bài đã phát hành theo từng đợt có nhật ký. Đợt 2 gồm Bài 07–15; một tác tử soạn duy nhất ghi tệp (Claude Opus 5.5; loại tác tử và effort do điều phối ghi theo lệnh gọi Agent); không commit.

Trang thêm (6), mỗi trang là `<section>` trong đầu tiên của section ngoài, `class="strand-title"`, `id="mach-N"`. Mã `<tiền tố>00` đã thuộc trang nội dung đầu mạch nên dùng `<tiền tố>T`:

| N | Mã | Tên mạch | Dòng dẫn |
|---:|---|---|---|
| 2 | AT | Bài toán hàng xóm gần đúng | Muốn tránh quét mười tỷ véc-tơ cho mỗi truy vấn, phải đặc tả đầu ra gần đúng và cách đo chất lượng. |
| 3 | HT | Tìm kiếm trên đồ thị HNSW | Muốn đo ít véc-tơ mà vẫn tìm được điểm gần, phải đi trên đồ thị lân cận nhiều tầng. |
| 4 | QT | Lượng tử hóa tích (PQ) | Muốn giảm bộ nhớ và chi phí mỗi phép đo, phải thay véc-tơ bằng mã ngắn và tính khoảng cách qua bảng tra. |
| 5 | IT | Tệp đảo kết hợp PQ (IVF-PQ) | Muốn chỉ chấm một phần kho bằng mã ngắn, phải chia kho thành danh sách đảo và mã hóa phần dư. |
| 6 | CT | So sánh và tự kiểm tra | Muốn chọn chỉ mục cho kho mở đầu, phải đối chiếu thừa số được giảm, bộ nhớ và chi phí truy vấn. |
| 7 | RT | Bài tập thực hành | Muốn kiểm các công thức PQ và IVF-PQ bằng số đo, phải chạy sổ thực hành trên dữ liệu tổng hợp. |

Dòng dẫn 20–24 âm tiết; từ khóa 4–5 cụm; ghi chú diễn giả 86–97 âm tiết, viết từ nội dung các trang trong mạch. Số trang 50 → 56. Các trang nội dung đầu mạch (A00, H00, Q00, I00, C00, R00) đều có nội dung, không phải trang tiêu đề phần một dòng, và tiêu đề khác tên mạch; giữ nguyên.

Trang Nội dung (P02 "Nội dung và mục tiêu"): danh sách `ul` sáu mục thiếu mạch mở đầu; đổi thành `ol` 1–7, thêm mục 1 "Mở đầu", các mục 2–7 trùng từng chữ với tên mạch. Notes thêm một câu cho mạch mở đầu. Trang gộp với ba mục tiêu, mặt trang khoảng 95 âm tiết, vượt trần 80; theo phạm vi đợt này chỉ đánh số, chưa tách. Quyết định: sửa.

Cố ý chưa làm (việc của đợt sau): mạch mở đầu đầy đủ (Tiên quyết và quy ước, Vấn đề trung tâm, câu luận đề trên trang bìa); chuẩn mật độ mặt trang; mạch kết luận theo khuôn mới (bảng tổng kết ba cột, trả lời vấn đề trung tâm, câu hỏi tự kiểm tra, nguồn và tài liệu đọc). Không sửa CSS, SVG, ghi chú bài giảng, index.

Kiểm tra: section mở/đóng 63/63; 56 `data-slide-id` và 6 `id` duy nhất. Chromium Playwright trên máy chủ cục bộ cổng 8771: ở 1600×900, `#/2` … `#/N` mở đúng trang tiêu đề mạch tương ứng (`id`, số thứ tự khớp); khối tiêu đề nằm trong khung (đáy lớn nhất 720 px trên 900 px), không cuộn ngang; 0 lỗi console, 0 `.katex-error`, không yêu cầu mạng ngoài; trang Nội dung đọc ra đúng tên các mạch. Ở 390×844, RevealJS chuyển sang chế độ cuộn và bỏ qua hash khi nạp; các trang được chụp sau khi cuộn tới phần tử, không tràn ngang. Đã tự xem ảnh. `git diff --check` sạch.

### Sửa sau rà lại đợt 2 (2026-10-14)

Theo báo cáo rà lại đợt 2 (không có phát hiện chặn bàn giao, nghiêm trọng hoặc trung bình), viết lại 5 ghi chú diễn giả của trang tiêu đề mạch: bỏ các câu lấy tài liệu hoặc trang làm chủ ngữ ("Phần này …", "Trang đầu …", "trang tiếp …", "Phần cuối …", "ở phần sau") theo `AGENTS.md` "Tiêu chuẩn trang chiếu và ghi chú diễn giả"; chủ ngữ mới là đối tượng, thuật toán hoặc kết quả; giữ ba ý kế thừa, nhiệm vụ, kết quả giao và độ dài 40–100 âm tiết (no-ai-slop, chế độ Edit). Dòng từ khóa: khoảng trắng trong mỗi cụm và trước dấu "·" đổi thành khoảng trắng không ngắt (`&nbsp;`), nên dấu "·" không đứng đầu dòng và không cụm nào bị tách ở 1600×900; không sửa CSS. Kiểm lại: section mở/đóng cân bằng; `#/2` … `#/N` mở đúng trang tiêu đề mạch ở 1600×900; 0 lỗi console, 0 `.katex-error`; `git diff --check` sạch.

## Sửa toàn diện theo chuẩn 2026-10-14

Căn cứ: `AGENTS.md` ("Mẫu RevealJS bắt buộc", "Trang tiêu đề mạch", "Văn phong và mật độ mặt trang chiếu", "Tiêu chuẩn trang chiếu và ghi chú diễn giả"), `slide_authoring_standard.md`, deck mẫu Bài 06; kế hoạch sửa toàn diện Bài 07 do tác tử lập kế hoạch nộp (tệp tạm trong scratchpad của phiên), mục B–F; quyết định của điều phối viên, mục "Bài 07" và "Chung cho mọi bài".

**Phân công.** Điều phối viên: phiên Claude Code, Opus 5.5, effort `high`. Tác tử lập kế hoạch: chỉ đọc, `subagent_type: "fork"` (kế thừa Opus 5.5, effort `high`). Tác tử soạn: `subagent_type: "fork"` (kế thừa Opus 5.5, effort `high`), tác tử duy nhất được ghi; phạm vi ghi là deck Bài 07 và ba tệp planning; không commit. Bằng chứng là lời gọi Agent và tin nhắn giao việc của điều phối viên. Rà rút gọn ba vai (sinh viên kèm mật độ; độ chính xác toán; kết nối và mạch viết) do điều phối viên giao sau, chưa chạy khi ghi mục này.

**Quyết định của điều phối viên đã áp dụng.**

1. Luận đề: "HNSW giảm số véc-tơ được đo, lượng tử hóa tích (PQ) giảm chi phí mỗi phép đo; đổi lại, có thể bỏ lỡ hàng xóm thật." Câu có 26 token theo script (trần 25 của bìa, kế hoạch ghi 25); giữ nguyên chữ vì là quyết định của điều phối viên, chờ điều phối viên xác nhận hoặc rút (ví dụ bỏ "(PQ)" và giải nghĩa PQ ở P03).
2. Mạch 6 đổi tên "Tổng kết và tự kiểm tra" (P04 và CT).
3. C00 đổi sang khuôn `Thuật toán | Đầu vào | Bảo đảm | Chi phí`.
4. Ba mục tiêu học tập giữ nguyên chữ.
5. Không ghi công mmds.org; C05 ghi Malkov–Yashunin (arXiv 1603.09320, bản 2018 theo PDF cục bộ), Jégou–Douze–Schmid (IEEE TPAMI 2011, 33(1)), Princeton COS 597A (2023, lớp 8 Liberty–Douze, lớp 9 Simhadri, sổ thực hành), Stanford BIODS 271 (2025, bài 12) và liên kết viewer ghi chú. Năm và ấn bản kiểm trên trang đầu các PDF cục bộ; không ghi IEEE TPAMI 2020 cho HNSW vì PDF cục bộ là bản arXiv.
6. Bỏ dòng nối Bài 08: `sources/source.md` chỉ nêu thứ tự (Bài 8 mở mạch "Dòng dữ liệu và cửa sổ"), không nêu quan hệ nội dung giữa Bài 7 và Bài 8.
7. Nhãn Thực hành trên R00–R08 bằng `div.slide-badge-row` + `span.practice-badge`, lớp đã có trong `lecture-style.css` (Bài 03 dùng); không thêm CSS.
8. k-means và hàng đợi ưu tiên nằm trong ghi chú diễn giả của P03.
9. Rà rút gọn ba vai: chờ điều phối viên.
10. RT 0,5 phút lấy từ R01 (6 → 5,5); recitation đúng 60 phút.

Chung: "Đáp án" → "Lời giải" (15 chỗ, kể cả "đáp án số cố định"); "Sản phẩm:", "Yêu cầu:", "Trạng thái:", "Giả định:", "Ví dụ:" (dấu hai chấm), "Gợi ý:" không đậm trên mặt trang thay bằng "Câu hỏi:", "Ký hiệu:", "Giả thiết:", "Ví dụ.", "Nhắc lại:"; thuật ngữ và viết tắt giải nghĩa ở lần đầu (HNSW, ANN, recall, beam search, VQ, ADC, IVF, MSE); trang bài tập có một dòng `ex-note` "Nguồn: sổ thực hành Princeton COS 597A lớp 8, ô …" (R07 ghi ô trong dòng Câu hỏi vì trang chật). Ghi chú diễn giả không chứa thời lượng (deck cũ đã không có).

**Thay đổi cấu trúc.** 56 → 65 trang (55 giảng + 10 bài tập); bảy mạch 6/5/18/12/7/7/10; 120 + 60 phút (8/11/42/28/16/15 + 60). Thêm P03, P05, C03, C04, C05; tách P02 → P02 + P04, H13 → H13 + H14, Q09 → Q09 + Q11, I04 → I04 + I05; C00 đổi khuôn. Thêm `aria-label` cho bảy section ngoài. Lớp `.lecture-ann .ann-orientation` không còn được deck dùng; không xóa khỏi CSS chung trong đợt này (sửa CSS chung đòi kiểm Bài 02, 03), để dọn ở đợt CSS. CSS, SVG, viewer, `index.html`, ghi chú bài giảng không sửa.

**Con số mới.** Không có. Mọi số trên trang mới và trang tách lấy từ deck hoặc ghi chú đã kiểm; cột "Đóng góp" của I03 giữ $3{,}1\cdot10^8$, $5{,}0\cdot10^7$, $3{,}3\cdot10^9$, tổng $\approx3{,}6\cdot10^9$ (kiểm lại: $10^5\cdot3072=3{,}072\cdot10^8$; $64\cdot256\cdot3072=5{,}03\cdot10^7$; $64\cdot10^{10}/10^5\cdot512=3{,}28\cdot10^9$; tổng $3{,}63\cdot10^9$; $5{,}12\cdot10^{12}/3{,}63\cdot10^9\approx1410$). Bảng Q11 dùng ký hiệu đếm $n_c$ (số véc-tơ được chấm), định nghĩa trên dòng Mô hình. Ghi chú H14 dẫn đúng mục 4.2.1 của bài báo HNSW cho kết luận số bước mỗi tầng bị chặn (kiểm trên PDF cục bộ); ghi chú H13 dẫn mục 4.2.3 cho bộ nhớ.

**Mật độ trước → sau.** Lệnh: biến thể `m07.py` của `tools/density.py` (cộng trang đầu mỗi section ngoài, bỏ công thức `$...$`), chạy `python3 -I m07.py 2627-1/lecture-07-chi-muc-hang-xom-gan-dung.html`. Deck cũ không có dòng `ex-source` nên cột "trước" không tách nguồn.

| Chỉ số | Trước (56 trang) | Sau (65 trang) |
|---|---:|---:|
| Trung vị âm tiết | 38,5 | 45 |
| Số trang > 40 | 25 | 41 |
| Số trang > 60 | 11 | 9 (đều trần 80) |
| Số trang > 80 | 3 | 0 |
| Trang vượt trần (60 hoặc 80 theo loại trang) | 6 (P02 86/80, A00 76/60, A03 75/60, H03 75/60, H13 83/80, C00 99/80) | 0 |
| Dòng > 20 âm tiết (trừ dòng dẫn tiêu đề mạch) | 17 dòng trên 13 trang | 1 (câu luận đề, 26 token, trần 25 của bìa) |
| Ghi chú diễn giả > 150 âm tiết | 14 | 18 |

Trung vị và số trang > 40 tăng vì nhãn dẫn ("Nhu cầu:", "Đầu vào:", "Kết luận:"…) được thêm, ba trang tổng kết mới có bảng, và các trang tách giữ dữ kiện; không trang nào vượt trần. Ghi chú > 150 âm tiết (mức `nhẹ`) phần lớn là trang tính đúng, chứng minh hoặc lời giải (H05, H06, H08, H10B, I03, R05), trần khuyến nghị 250.

| # | Mã | Trước | Sau | Trần | Dòng | Dòng dài nhất | Âm tiết ghi chú | Quyết định |
|---:|---|---:|---:|---:|---:|---:|---:|---|
| 1 | P00 | 36 | 50 | — | 4 | 26 | 139 | `sửa` |
| 2 | P03 | — | 57 | 60 | 5 | 18 | 164 | `thêm` |
| 3 | P02 | 86 | 47 | 80 | 3 | 17 | 125 | `tách` |
| 4 | P04 | — | 51 | 80 | 8 | 16 | 134 | `thêm` |
| 5 | P05 | — | 60 | 60 | 6 | 12 | 131 | `thêm` |
| 6 | P01 | 34 | 40 | 60 | 3 | 8 | 157 | `sửa` |
| 7 | AT | 41 | 41 | — | 2 | 22 | 82 | `giữ` |
| 8 | A00 | 76 | 56 | 60 | 4 | 18 | 140 | `sửa` |
| 9 | A01 | 26 | 33 | 60 | 2 | 17 | 98 | `sửa` |
| 10 | A02 | 79 | 77 | 80 | 5 | 15 | 115 | `sửa` |
| 11 | A03 | 75 | 57 | 80 | 6 | 13 | 146 | `sửa` |
| 12 | HT | 33 | 33 | — | 2 | 19 | 102 | `sửa` |
| 13 | H00 | 56 | 48 | 60 | 3 | 20 | 135 | `sửa` |
| 14 | H01 | 49 | 40 | 60 | 7 | 20 | 157 | `sửa` |
| 15 | H03 | 75 | 53 | 60 | 4 | 19 | 174 | `sửa` |
| 16 | H03B | 26 | 28 | 60 | 3 | 8 | 150 | `sửa` |
| 17 | H04 | 38 | 43 | 60 | 4 | 14 | 115 | `sửa` |
| 18 | H05 | 8 | 8 | 60 | 1 | 8 | 189 | `sửa` |
| 19 | H06 | 39 | 54 | 60 | 6 | 15 | 172 | `sửa` |
| 20 | H06B | 47 | 34 | 60 | 3 | 17 | 152 | `sửa` |
| 21 | H07 | 37 | 45 | 60 | 4 | 16 | 176 | `sửa` |
| 22 | H09 | 26 | 26 | 60 | 3 | 14 | 115 | `sửa` |
| 23 | H08 | 36 | 53 | 60 | 5 | 16 | 167 | `sửa` |
| 24 | H10 | 46 | 36 | 60 | 5 | 16 | 167 | `sửa` |
| 25 | H10B | 19 | 15 | 60 | 2 | 8 | 196 | `sửa` |
| 26 | H11 | 22 | 36 | 60 | 5 | 14 | 179 | `sửa` |
| 27 | H12 | 71 | 69 | 80 | 4 | 14 | 125 | `sửa` |
| 28 | H13 | 83 | 50 | 80 | 6 | 19 | 137 | `tách` |
| 29 | H14 | — | 58 | 60 | 5 | 15 | 166 | `thêm` |
| 30 | QT | 39 | 39 | — | 2 | 23 | 80 | `giữ` |
| 31 | Q00 | 38 | 45 | 60 | 4 | 20 | 129 | `sửa` |
| 32 | Q02 | 34 | 36 | 60 | 3 | 17 | 119 | `sửa` |
| 33 | Q03 | 76 | 67 | 80 | 7 | 15 | 123 | `sửa` |
| 34 | Q04 | 26 | 44 | 60 | 4 | 17 | 120 | `sửa` |
| 35 | Q05 | 11 | 18 | 60 | 3 | 7 | 92 | `sửa` |
| 36 | Q07 | 41 | 43 | 80 | 6 | 15 | 123 | `sửa` |
| 37 | Q06 | 22 | 22 | 60 | 3 | 13 | 114 | `sửa` |
| 38 | Q08 | 34 | 51 | 60 | 4 | 19 | 141 | `sửa` |
| 39 | Q09 | 44 | 20 | 60 | 6 | 10 | 63 | `tách` |
| 40 | Q11 | — | 53 | 80 | 6 | 16 | 101 | `thêm` |
| 41 | Q10 | 59 | 61 | 80 | 6 | 15 | 138 | `sửa` |
| 42 | IT | 36 | 36 | — | 2 | 21 | 90 | `giữ` |
| 43 | I00 | 54 | 46 | 60 | 4 | 15 | 132 | `sửa` |
| 44 | I01 | 13 | 13 | 60 | 1 | 3 | 147 | `sửa` |
| 45 | I02 | 27 | 31 | 60 | 4 | 13 | 142 | `sửa` |
| 46 | I04 | 32 | 32 | 60 | 2 | 19 | 130 | `tách` |
| 47 | I05 | — | 24 | 60 | 3 | 12 | 83 | `thêm` |
| 48 | I03 | 43 | 55 | 80 | 8 | 15 | 172 | `sửa` |
| 49 | CT | 31 | 44 | — | 2 | 22 | 95 | `sửa` |
| 50 | C03 | — | 80 | 80 | 8 | 17 | 111 | `thêm` |
| 51 | C00 | 99 | 67 | 80 | 6 | 15 | 159 | `sửa` |
| 52 | C04 | — | 65 | 80 | 6 | 16 | 134 | `thêm` |
| 53 | C01 | 53 | 50 | 60 | 4 | 17 | 138 | `sửa` |
| 54 | C02 | 48 | 53 | 60 | 4 | 16 | 89 | `sửa` |
| 55 | C05 | — | 50 | 80 | 4 | 19 | 109 | `thêm` |
| 56 | RT | 40 | 40 | — | 2 | 21 | 84 | `giữ` |
| 57 | R00 | 45 | 47 | 80 | 10 | 11 | 96 | `sửa` |
| 58 | R01 | 34 | 44 | 80 | 7 | 13 | 141 | `sửa` |
| 59 | R02 | 26 | 37 | 80 | 3 | 13 | 115 | `sửa` |
| 60 | R03 | 69 | 72 | 80 | 7 | 19 | 152 | `sửa` |
| 61 | R04 | 37 | 48 | 80 | 4 | 17 | 103 | `sửa` |
| 62 | R05 | 63 | 66 | 80 | 5 | 17 | 168 | `sửa` |
| 63 | R06 | 33 | 38 | 80 | 4 | 11 | 138 | `sửa` |
| 64 | R07 | 33 | 42 | 80 | 5 | 16 | 157 | `sửa` |
| 65 | R08 | 44 | 52 | 80 | 4 | 16 | 141 | `sửa` |

Ngoại lệ dòng ghi trong `storyboard.md`, mục "Sửa toàn diện theo chuẩn 2026-10-14".

**Tự kiểm no-ai-slop (Edit, đối chiếu `eval.md`).** Văn bản mới: câu luận đề (của điều phối viên), P03, P05, mục tiêu (giữ chữ), C03, C00, C04, C05, H14, Q11, I05, các dòng nhãn và ghi chú diễn giả mới. Đạt: không từ cấm, không đối lập nhị phân, không câu mở dọn đường, không bình luận về tầm quan trọng, không câu kết châm ngôn; mỗi câu kết luận là kết luận có điều kiện hoặc con số. Đã sửa khi tự kiểm: ghi chú P00, A03, Q08 lấy "Bài này" làm chủ ngữ; "bài này dùng định nghĩa" (A01), "phần PQ và IVF-PQ của bài" (A00), "bài này không dùng hai tùy chọn" (H11) viết lại; "theo giả định ở phần mở đầu" (I03) thành "theo giả định của ví dụ truy hồi ngữ nghĩa"; ánh xạ câu → mục tiêu (siêu dữ liệu) chuyển khỏi ghi chú C01, C02. Rà "chúng ta", "ta thấy", "Trang này", "Bài này", "phần sau", "Sản phẩm", "Đáp án", "Yêu cầu", "Trạng thái:", "Giả định:", mã nội bộ, thời lượng trong mặt trang và ghi chú: 0 kết quả.

**Kiểm kỹ thuật.** `git diff --check` sạch cho deck và ba tệp planning. HTML cân bằng (`html.parser`: 0 thẻ chưa đóng, 0 thẻ đóng sai); section mở/đóng 72/72; 65 `data-slide-id` duy nhất; `id` chỉ ở sáu trang tiêu đề mạch `mach-2` … `mach-7`, không đổi. Chromium Playwright trên máy chủ cục bộ cổng 8771, `wait_until="load"`, tắt hiệu ứng chuyển trang:

- 1600×900: duyệt cả 65 trang bằng `Reveal.getIndices` + `Reveal.slide(h, v, 99)`; 0 lỗi console, 0 lỗi trang, 0 `.katex-error`, 0 yêu cầu mạng ngoài, không cuộn ngang; không phần tử (trừ `.katex-mathml` ẩn và SVG nội bộ KaTeX) vượt khung `.slides`. Lượt đầu phát hiện Q04 (đáy 915/864) và R07 (894/864) tràn; đã sửa (hình Q04 dùng lớp sẵn có `ann-short`; R07 bỏ dòng Nguồn riêng, ghi ô trong dòng Câu hỏi); lượt sau đáy thấp nhất là P01 852/864 (mạch mở đầu không có chân trang), Q04 830, R07 837, dưới mép chân trang 845. Cỡ chữ thân nhỏ nhất 24 px (bảng đề recitation) trên khung 1280×720 nhân 1,2.
- 390×844: chế độ cuộn; cuộn tới từng trang, 0 phần tử vượt mép phải, `scrollWidth` = `clientWidth` = 390, 0 lỗi console, 0 `.katex-error`.
- Ảnh đã tự xem ở 1600×900: P01, P03, P04, Q04, H14, I03, I05, C03, C00, C04, C05, R07. Ảnh lưu trong scratchpad của phiên, không đưa vào kho.

**Tác động tới ghi chú bài giảng `materials/lec-07/lecture-note.md`.** Không sửa. Ký hiệu, ví dụ, con số và kết luận không đổi; ba mục tiêu giữ nguyên chữ. Điểm để đợt sửa ghi chú xử lý: (a) quy ước 1 TB $=10^{12}$ byte, 1 GB $=10^9$ byte và tọa độ dùng dấu chấm phẩy được ghi chú dùng ngầm, có thể thêm vào bảng ký hiệu; (b) tên mạch 6 mới không có mục tương ứng (ghi chú có mục So sánh và mục Tự kiểm), không bắt buộc đổi; (c) ký hiệu $n_c$ chỉ có trên Q11; (d) ghi chú chưa đánh số kết quả nên deck không dẫn "(Định lý 07.k)". `index.html` không đổi.

| Mức độ | Trang chiếu | Vấn đề | Bằng chứng | Đề xuất sửa | Trạng thái |
|---|---|---|---|---|---|
| trung bình | P00 | Câu luận đề 26 token, trần 25 của bìa | đếm script | Bỏ "(PQ)" (PQ đã có ở tên mạch 4 và Q04) hoặc điều phối viên chấp nhận ngoại lệ | chờ điều phối viên |
| nhẹ | toàn deck | Trung vị 45 trên mức nhắm 40 | bảng mật độ | Để vai sinh viên kèm mật độ đánh giá; không rút ví dụ, chứng minh, vết chạy | mở, chờ rà |
| nhẹ | 18 trang | Ghi chú diễn giả > 150 âm tiết | bảng mật độ | Rút ở lượt sửa sau rà nếu không mất giả thiết hay lời giải | mở |
| nhẹ | R07, P01, R03 | Trang sát chân trang (đáy 837–852/864) | Playwright | Theo dõi khi đổi chữ | đã kiểm, không tràn |

## Lượt sửa sau ba báo cáo rà (2026-10-14)

Căn cứ: ba báo cáo rà deck 07 sau đợt sửa toàn diện (vai toán và thuật toán, vai mạch truyện và liên kết, vai sinh viên; tác tử chỉ đọc do điều phối viên tạo) và quyết định hợp nhất của điều phối viên `fix-d07.md` (mục 1 nghiêm trọng, bắt buộc). Vai sửa: tác tử `fork` kế thừa Opus 5.5, effort `high` (bằng chứng: lời gọi Agent của điều phối viên), là tác tử ghi duy nhất. Phạm vi ghi: deck 07 và ba tệp planning; không sửa CSS, SVG, index, ghi chú bài giảng, deck khác. Không commit. Số trang (65), thứ tự, thời lượng 120 + 60 phút không đổi.

**Đính chính bản trước.** Đoạn "Con số mới. Không có" của mục "Sửa toàn diện theo chuẩn 2026-10-14" bỏ sót câu mới trong ghi chú C04 "với ngân sách bộ nhớ một máy, chỉ IVF-PQ trong bốn cấu trúc vừa". Câu đó sai: PQ quét đủ chiếm 5,12 TB, ít hơn IVF-PQ 5,2 TB, nên mọi ngân sách chứa IVF-PQ cũng chứa PQ; PQ bị loại vì thời gian (≈5,12 giây so với ≈3,6 ms). Câu thay thế trong ghi chú C04: "HNSW và LSH vượt ngân sách bộ nhớ. PQ quét đủ chiếm 5,12 TB, ít hơn IVF-PQ, nên bị loại vì thời gian chứ không vì bộ nhớ."

**Phép tính các con số mới hoặc mới đưa lên mặt trang.** 1 TB $=10^{12}$ byte, 1 GB $=10^9$ byte, 1 MB $=10^6$ byte; tốc độ $10^{12}$ thao tác (lượt tọa độ hoặc lần tra) mỗi giây là giả định của ví dụ P01; một lần tra ngang một lượt tọa độ. Mọi phép tính chạy lại bằng Python.

| Con số | Trang (mặt trang / ghi chú) | Phép tính | Loại |
|---|---|---|---|
| 122,88 TB | P05, C04 (ghi chú), P01 | $10^{10}\cdot3072\cdot4=1{,}2288\cdot10^{14}$ byte | suy ra từ cấu hình BIODS tr.17 |
| ≈30,7 giây | P05; ghi chú P05, P01 | $3{,}072\cdot10^{13}/10^{12}=30{,}72$ s | suy ra, dưới giả định tốc độ |
| 3072 lần | ghi chú P01 (lời giải câu hỏi mới) | $30{,}72/0{,}01=3072$ | suy ra |
| 6 TB, 10 ms | P05, C04; ghi chú P05, C04, CT | — | giả định của học phần, ghi "(giả định)" trên mặt trang; không lấy từ nguồn |
| ≈125,5 TB | C04; ghi chú C04, C00, HT | $(12\,288+265)\cdot10^{10}=1{,}2553\cdot10^{14}$ byte; 265 byte cạnh từ H13 | suy ra |
| ≈12 553 byte mỗi véc-tơ | C00 | $4\cdot3072+265=12\,553$ | suy ra |
| 5,12 TB | C04 | $10^{10}\cdot512=5{,}12\cdot10^{12}$ byte | suy ra (Q07) |
| ≈5,12 giây | C04 | $10^{10}\cdot512=5{,}12\cdot10^{12}$ lần tra; $/10^{12}=5{,}12$ s | suy ra (lời giải Q10) |
| 5,2 TB | I03, C04 | $(512+8)\cdot10^{10}=5{,}2\cdot10^{12}$ byte; 8 byte mã định danh vì $10^{10}>2^{32}$ | suy ra |
| 1,23 GB tâm thô; 3,1 MB bộ mã | ghi chú I03, C04 | $10^5\cdot3072\cdot4=1{,}2288\cdot10^9$; $256\cdot3072\cdot4=3\,145\,728$ | suy ra; tổng IVF-PQ ≈5,2012 TB < 6 TB |
| $3{,}07\cdot10^8$; $5{,}03\cdot10^7$; $3{,}28\cdot10^9$; tổng $3{,}63\cdot10^9$ | I03, C00 | $10^5\cdot3072=307\,200\,000$; $64\cdot256\cdot3072=50\,331\,648$; $64\cdot10^{10}/10^5\cdot512=3{,}2768\cdot10^9$; tổng $3\,634\,331\,648$ | suy ra (thay cột cũ hai chữ số có tổng cột 3,66·10⁹) |
| ≈1410 lần (mặt trang "khoảng 1400") | ghi chú I03 | $5{,}12\cdot10^{12}/3{,}6343\cdot10^9=1408{,}8$ | suy ra |
| ≈3,6 ms | C04 | $3{,}6343\cdot10^9/10^{12}=3{,}63\cdot10^{-3}$ s | suy ra |
| $12\,288+8b$ byte mỗi véc-tơ (LSH) | C00 | véc-tơ gốc $4D$ byte và $b$ mã định danh 8 byte, một trong mỗi bảng băm | công thức, không thay số vì bài không chọn $b$, $r$ |

**Quyết định cho từng phát hiện.** Quyết định: `sửa` | `bác bỏ` | `mở`.

| Vai | Mức độ | Trang chiếu | Vấn đề | Quyết định | Cách xử lý, lý do |
|---|---|---|---|---|---|
| toán | nghiêm trọng | C04 (ghi chú) | "chỉ IVF-PQ trong bốn cấu trúc vừa" sai; PQ 5,12 TB < IVF-PQ 5,2 TB | sửa | ghi chú C04 viết lại với phép tính từng số; PQ bị loại vì thời gian; HNSW, LSH vượt bộ nhớ; thêm điều kiện "nếu một máy có hơn 125,5 TB, HNSW lại thành lựa chọn" |
| toán | trung bình | C04 dòng 6, P05 dòng 6 | "bộ nhớ một máy" không có con số | sửa | ngân sách giả định 6 TB và 10 ms trên P05 dòng 6 và C04 dòng 6, ghi "(giả định)"; ghi chú P05 nêu nguồn gốc giả định |
| toán | nhẹ | I03 | cột Đóng góp hai chữ số cộng ra 3,66·10⁹ | sửa | ba chữ số: 3,07·10⁸; 5,03·10⁷; 3,28·10⁹; tổng ≈3,63·10⁹; C00 cũng ghi 3,63·10⁹ |
| toán | nhẹ | I02 | "Phần dư nhỏ hơn $y$" không điều kiện | sửa | mặt trang "thường nhỏ hơn"; ghi chú: năng lượng (bình phương chuẩn trung bình) của phần dư thường nhỏ hơn, véc-tơ gần gốc tọa độ có thể có phần dư dài hơn |
| toán | nhẹ | I02; ghi chú H00, H03, H13 | chữ Việt trong `\text{}` gây cảnh báo KaTeX | sửa | I02: "với $y\in L_i$" và "mã PQ của $r(y)$" ra ngoài công thức; H00, H13: $N\cdot(s+4g)$ byte kèm lời định nghĩa $s$, $g$; H03: "Ban đầu $C$ và $W$ chỉ chứa điểm vào"; Playwright 0 cảnh báo KaTeX |
| toán | nhẹ | Q11, Q10, I03 | $n_c$ không được dùng lại | sửa | Q10 hàng "Số véc-tơ được chấm, $n_c=N$"; I03 "$n_c\approx nprobe\,N/k_c$ mã"; ghi chú Q11 nêu hai trường hợp. Trùng chữ $c$ với $k_c$: giữ, ghi chú phân biệt (chỉ số $c$ của $n_c$ là "chấm") — mở cho đợt sửa ký hiệu chung |
| toán | nhẹ | C00 | cột Chi phí không ghi "mỗi véc-tơ" | sửa | "byte mỗi véc-tơ" ở cả bốn hàng |
| toán | nhẹ | A00 | "trả $K$ điểm" lệch "tối đa $K$" của H09, I04 | sửa | A00 "trả tối đa $K$ điểm"; ghi chú A01: nếu trả ít hơn $K$ điểm, mẫu số vẫn là $K$ |
| mạch | nghiêm trọng | C04, P05 | điều kiện chọn IVF-PQ không có ở vấn đề trung tâm; ghi chú sai; dòng 3–5 chép cột C00 | sửa | P05 Nhu cầu: 122,88 TB, ≈30,7 giây; dòng 6: 6 TB, 10 ms (giả định). C04 dòng 3–5 nêu điều kiện và con số trả lời (TB, giây, ms), dòng 6 nêu cả hai điều kiện; P01 câu hỏi đổi vì P05 đã nêu 30,7 giây |
| mạch | trung bình | P03, A03, C00 (LSH) | kết nối Bài 06 chưa khớp: thiếu "ứng viên", "xác minh", bảo đảm xác suất; hàng LSH khác mô hình chi phí | sửa | P03 "LSH chỉ xác minh ứng viên cùng thùng với $q$; hàng xóm gần có thể bị bỏ sót (Bài 06)"; ghi chú P03 nêu biến thể truy vấn và $1-(1-p_1^r)^b$; C00 hàng LSH: $d(q,y)\le d_1$ được xác minh với xác suất $\ge1-(1-p_1^r)^b$; chi phí "số ứng viên × $D$; $12\,288+8b$ byte mỗi véc-tơ" |
| mạch | trung bình | P05 dòng 3 ↔ C04 dòng 3 | dòng HNSW của P05 nói cực tiểu cục bộ, C04 trả lời bằng bộ nhớ | sửa | P05 "HNSW: đo ít đỉnh, đúng trên đỉnh đã thấy; giữ véc-tơ gốc."; C04 "HNSW, $M=16$: giữ véc-tơ gốc, khoảng 125,5 TB, vượt 6 TB." |
| mạch | trung bình | A00 ↔ Q10 | đặc tả ANN chỉ nêu "đo một phần kho" | sửa | A00 "đo một phần kho hoặc đo xấp xỉ"; ghi chú nêu hai nguồn sai số tương ứng hai thừa số |
| mạch | trung bình | toàn deck | "được đo" / "được chấm" đổi tên giữa các mạch | sửa | Q11 dòng Mô hình: "chấm một mã là phép đo xấp xỉ qua bảng tra"; trước Q11 dùng "đo" (P05, A03); từ Q11 trở đi "chấm" đã được định nghĩa |
| mạch | trung bình | IT, mạch 5, C00/C04 | bộ nhớ IVF-PQ chưa tính trong mạch 5 | sửa | I03 dòng Mô hình nêu 8 + 512 byte mỗi phần tử, Kết luận có $(512+8)\cdot10^{10}$ byte $=5{,}2$ TB; ghi chú I03 thêm tâm thô và bộ mã; ghi chú IT nêu $(512+8)$ byte mỗi véc-tơ |
| mạch | trung bình | storyboard | "Hành trình khái niệm", bản đồ mạch, hàng CT, mục C01–C02 chưa khớp | sửa | thêm thứ tự hiện hành (có H14, I05, C03–C05), đánh dấu bốn gạch cũ là bản 03/10/2026; bản đồ và hàng CT "Tổng kết và tự kiểm tra", trước C03; C01, C02 thêm dòng "Sửa 2026-10-14" và kết nối mới |
| mạch | nhẹ | P03 dòng 4 | tên đầy đủ HNSW đặt ở trang tiên quyết | bác bỏ | P03 là trang đầu tiên sau bìa; bìa đã dùng "HNSW", nên tên đầy đủ phải xuất hiện ở trang kế tiếp; lý do đã ghi trong storyboard (hàng P03) |
| mạch | nhẹ | P03, A03 (ghi chú) | câu phạm vi soạn bài | sửa | P03 thay bằng biến thể truy vấn và bảo đảm của LSH; A03 thay bằng "chỉ các ứng viên cùng thùng được xác minh, nên LSH giảm thừa số thứ nhất" |
| mạch | nhẹ | C04, CT, P05 (ghi chú) | câu siêu dữ liệu về cách trình bày | sửa | bỏ ở C04 và P05; CT thay bằng câu về hai giả định ngân sách |
| mạch | nhẹ | P00 (ghi chú) | "Cả hai cách" sau ba cấu trúc; "LSH chỉ đo phần tử cùng thùng" | sửa | "Cả ba cấu trúc"; "chỉ xác minh cặp cùng thùng" |
| mạch | nhẹ | HT (ghi chú) | chữ hoa "Đồ"; "khoảng 125 TB" dễ hiểu là véc-tơ gốc | sửa | chữ thường; "vẫn giữ 122,88 TB véc-tơ gốc, toàn chỉ mục khoảng 125,5 TB" |
| mạch | nhẹ | QT (ghi chú) | câu "mã hóa được ví dụ bốn chiều" tối nghĩa | sửa | "ví dụ bốn chiều được mã hóa bằng tay" |
| mạch | nhẹ | I01, I05 | hai câu hỏi cùng kiểm việc bỏ lỡ $y_3$ | sửa | I01 hỏi "Với $nprobe=3$, danh sách nào được mở, danh sách nào không?" (lời giải $L_1$, $L_0$, $L_3$; $L_2$ không mở); giải thích $y_3$ giữ trong ghi chú I01 |
| mạch | nhẹ | Q07 → Q06 | thiếu câu nối sang khoảng cách tính từ mã | sửa | ghi chú Q07 thêm "Kho chỉ còn mã, nên khoảng cách tới $q$ phải tính từ mã và bộ mã con." |
| mạch | nhẹ | Q04 → Q05 | thứ tự định nghĩa/ví dụ khác cặp ADC | bác bỏ | Q05 dùng ký hiệu đoạn $x^{(j)}$, $k^*$ do Q04 định nghĩa; ghi lý do trong storyboard |
| mạch | nhẹ | P03, toàn deck (quill) | một chữ cái nhiều nghĩa ($C$, $L$, $b$, $e$, $s$, $k$) | sửa một phần, mở | ghi chú Q00 phân biệt bộ mã $C$ với tập ứng viên $C$, số tâm $k$ với $K$; đổi $C$ thành $\mathcal C$ chạm nhiều trang và SVG nên để đợt sửa ký hiệu chung |
| mạch | nhẹ | C05 | thiếu trang, năm, dòng MMDS | sửa | HNSW "(2018), mục 3–4, tr.1–8"; PQ "mục II–IV, tr.2–7"; thêm dòng Leskovec, Rajaraman, Ullman, ấn bản 3 (2020), Chương 3 |
| mạch | nhẹ | RT | không có nhãn Thực hành | bác bỏ | trang tiêu đề mạch có khuôn riêng, không có ô nhãn; thêm `slide-badge-row` sẽ lệch khuôn chung của sáu trang tiêu đề mạch; R00–R08 có nhãn. Ghi trong storyboard |
| mạch | nhẹ | toàn deck so với Bài 06 | "véc-tơ" (Bài 07) và "vector" (Bài 06) | mở | ngoài phạm vi lượt này theo quyết định chung; cần thống nhất giữa các bài trong đợt thuật ngữ |
| sinh viên | trung bình | H10 | tiêu đề in hoa biến $x$ thành $X$ | sửa | tiêu đề "Ví dụ: chèn một điểm vào đồ thị ba tầng"; dòng dữ kiện "Điểm $x=2{,}6$, …" |
| sinh viên | trung bình | Q00 | thiếu tọa độ $c_0$, $c_2$ trên mặt trang | sửa | thêm dòng "Tâm: $c_0=(0;\ 0)$, $c_1=(2;\ 0)$, $c_2=(0;\ 2)$." |
| sinh viên | trung bình | Q05 | thiếu bốn tâm con | sửa | thêm dòng "Tâm con: đoạn 1 $(0;\ 2)$, $(2;\ 0)$; đoạn 2 $(0;\ 0)$, $(3;\ 0)$." |
| sinh viên | trung bình | I05 | thiếu tập đúng $N_3(q)$ | sửa | dòng dữ kiện thêm "tập đúng $N_3(q)=\{y_8,y_3,y_7\}$" |
| sinh viên | trung bình | H14, C03 | "đồ thị Delaunay" chưa giải nghĩa trên mặt trang | sửa | H14 (lần đầu): "đồ thị Delaunay chính xác (tham lam luôn tới điểm gần $q$ nhất)"; C03 dùng lại sau H14, trang ở trần 80 nên không thêm chữ |
| sinh viên | trung bình | C04 | ngân sách không có số; ghi chú sai | sửa | như hai phát hiện của vai toán và mạch |
| sinh viên | trung bình | CT | từ khóa 22 âm tiết | sửa | "Giả thiết · Bảo đảm và chi phí · Vấn đề trung tâm · Câu hỏi tự kiểm tra · Tài liệu đọc" (19) |
| sinh viên | trung bình | H12 | hộp câu hỏi 22 âm tiết | sửa | "Giảm độ trễ mà không xây lại chỉ mục: chỉnh tham số nào, theo chiều nào, mất gì?" (17) |
| sinh viên | trung bình | R08 | 9 dòng | sửa | gộp thành "Câu hỏi: vẽ recall@1 theo thời gian trung bình; giải thích xu hướng bằng số mã được chấm." (8 dòng); "năm phép đo" chuyển vào ghi chú |
| sinh viên | nhẹ | P00 | luận đề 26 token | sửa | bỏ "(PQ)" (25); "(PQ)" chuyển sang mục tiêu 2 ở P02 |
| sinh viên | nhẹ | Q04, H10 | mẩu dòng mồ côi | sửa | Q04 bỏ "($m$ chia hết $D$)" khỏi mặt trang (ghi chú đã có điều kiện $m\mid D$); H10 "ở các tầng $0,\ldots,\ell$" |
| sinh viên | nhẹ | I02 | cảnh báo KaTeX chữ Việt | sửa | như phát hiện của vai toán |
| sinh viên | nhẹ | Q00, Q02 ↔ H03–H06 | $C$ và $k$ trùng nghĩa | sửa một phần | câu phân biệt trong ghi chú Q00; đổi ký hiệu để đợt sửa chung |
| sinh viên | nhẹ | H03B | hàng cuối gộp ba lần mở | sửa | dòng yêu cầu "… sau mỗi lần mở (ba lần mở cuối gộp một hàng)"; tách ba hàng sẽ vượt trần 8 dòng |
| sinh viên | nhẹ | H03 (ghi chú) | khẳng định quá mạnh "không kẹt … khi chùm đủ rộng" | sửa | "ít kẹt ở cực tiểu cục bộ hơn tham lam; trên đồ thị ví dụ, $ef=3$ đủ để tới $z$" |
| sinh viên | nhẹ | H11 | nhãn "So với $c1$" | sửa | "$d(\cdot,c1)$ so với $d(\cdot,x)$", đúng thứ tự hai vế trong ô |
| sinh viên | nhẹ | C00 | "$12\,288+{\approx}265$ byte" khó đọc | sửa | "$\approx12\,553$ byte mỗi véc-tơ"; ghi chú nêu $12\,288+265$ |
| sinh viên | nhẹ | I02 | "Phần dư nhỏ hơn $y$" | sửa | như phát hiện của vai toán |
| sinh viên | nhẹ | R01–R08 | tiêu đề in hoa hiện "(A)" trong khi R05 nói "câu (a)" | sửa | R05 "dùng bảng ở trang (a)"; giữ nhãn (a)/(b)/(c) trong tiêu đề |
| sinh viên | nhẹ | R07 | sát chân trang | sửa | bỏ hàng $nprobe/200$ của bảng (ghi chú đã có số mã được chấm); đáy nội dung 807/864 px ở 1600×900 |
| sinh viên | nhẹ | H00, H01, H03, H03B, H06 (SVG) | chú giải SVG khoảng 11 px | bác bỏ | không sửa SVG trong lượt này (phạm vi); đọc được ở 1600×900; để đợt sửa hình |
| sinh viên | nhẹ | H05, I04 (ghi chú) | "Khung để ngỏ …" lấy bố cục làm chủ ngữ | sửa | H05 "Giả mã chưa cho biết $W$ đúng theo nghĩa nào; bất biến SEARCH-LAYER trả lời điều đó."; I04 "Số mã được chấm phụ thuộc kích thước các danh sách mở." |
| sinh viên | nhẹ | ghi chú diễn giả | nhiều ghi chú > 150 âm tiết | mở | các ghi chú được sửa trong lượt này đã rút phần nhắc lại (bản nháp C00 197 → 174, P03 197 → 167; H14 166 → 160, I03 172 → 158); còn 20 ghi chú trên 150, dài nhất H10B 196, H03 188, H05 187 (trang thuật toán và vết), C00 174 (tăng từ 159 vì thêm bảo đảm LSH); đều dưới 250; rút thêm có thể mất giả thiết hoặc lời giải |
| sinh viên | nhẹ | C01 câu 3 | quy ước GB chỉ ở ghi chú | bác bỏ | suy ra được từ "1 TB là $10^{12}$ byte" ở P03; thêm vào dòng Quy ước làm P03 vượt trần 60 |
| sinh viên | nhẹ | storyboard (mật độ) | số dòng thấp hơn hiển thị; câu "không dòng nào vượt 20" sai | sửa | đếm lại cột Dòng cho cả 65 trang bằng quy tắc mới (đoạn, mục, hàng bảng, hộp câu hỏi, đoạn chỉ có công thức); viết lại câu tổng hợp mật độ và mục ngoại lệ dòng |

**Mật độ sau lượt sửa** (`python3 -I m07.py`). Trang trần 60: không trang nào vượt 60 (P05, A00, H14 bằng 60). Trang trần 80: không trang nào vượt 80 (C03 80, C00 77, C04 69, C05 64, I03 64). Dòng dài nhất ≤ 20 âm tiết trên mọi trang nội dung; câu luận đề 25 token; dòng dẫn tiêu đề mạch 21–23 (trần 25); từ khóa CT 19. Âm tiết các trang đổi: P00 50 → 49; P03 57 → 59; P02 47 → 50; P01 40 → 35; A00 56 → 60; H03B 28 → 35; H10 36 → 37; H12 69 → 65; H14 58 → 60; Q00 45 → 46; Q04 44 → 42; Q05 18 → 22; Q11 53 → 55; I01 13 → 15; I02 31 → 37; I05 24 → 26; I03 55 → 64; CT 44 → 41; C00 67 → 77; C04 65 → 69; C05 50 → 64; R07 42 → 33; R08 52 → 42; P05 60 → 60.

**Tự kiểm no-ai-slop (Edit, đối chiếu `eval.md`).** Đạt: không câu siêu dữ liệu ("Các mục được đánh số theo mạch", "Phần tổng kết trả lời từng mục", "Khung để ngỏ"), không lời nói mô phỏng, không câu hỏi tu từ, không cường điệu; câu mới nêu con số, giả thiết hoặc phép tính cụ thể; không gạch ngang dài.

**Kiểm kỹ thuật.** `git diff --check` sạch cho deck và ba tệp planning. HTML cân bằng (`html.parser`: 0 thẻ chưa đóng, 0 thẻ đóng sai); 65 `data-slide-id` duy nhất; 0 `<style>`, 0 thuộc tính `style=`, 0 `fragment`, 0 `.dense`; số dấu `$` chẵn trong mọi đoạn. Playwright Chromium, máy chủ cổng 8771, `wait_until="load"`, tắt chuyển cảnh; bộ lọc console bắt cả `error` và `warning` của KaTeX (đã thử: một lệnh `katex.renderToString('\\text{với}')` sinh hai cảnh báo và bộ lọc bắt được).
- 1600×900: duyệt cả 65 trang; 0 lỗi console, 0 cảnh báo KaTeX, 0 lỗi trang, 0 `.katex-error`, 0 yêu cầu mạng ngoài, không cuộn ngang, không phần tử vượt khung. Trang sát đáy: P01 852/864 px (câu hỏi mới, không tràn), H07 828, R07 807.
- 390×844: 0 phần tử vượt mép phải, `scrollWidth` = `clientWidth` = 390, 0 lỗi, 0 `.katex-error`.
- Ảnh đã tự xem (1600×900): P01, P03, P05, A00, H10, H11, H12, H14, Q00, Q05, Q10, Q11, I01, I02, I03, I05, C00, C03, C04, C05, CT, R07, R08; 390×844: P05, C04, Q00, I03, C00, H14. Ảnh trong scratchpad của phiên.

**Tác động tới ghi chú bài giảng.** Không sửa trong lượt này. Cần đồng bộ ở đợt sửa ghi chú: ngân sách giả định 6 TB, 10 ms và câu trả lời bằng TB, giây; bảo đảm LSH trong bảng so sánh; "phần dư thường nhỏ hơn"; định nghĩa "chấm một mã".

### Sửa nhỏ cuối sau rà lại (2026-10-14)

Căn cứ: báo cáo rà lại chỉ đọc các trang đổi (`recheck-d07.md`) và quyết định của điều phối viên `fix-d07b.md`. Cùng vai sửa (tác tử `fork`, Opus 5.5, effort `high`); không commit.

| Vai | Mức độ | Trang chiếu | Vấn đề | Quyết định | Cách xử lý, lý do |
|---|---|---|---|---|---|
| rà lại | trung bình | C00 | $b=8$ (bit PQ) trùng $b$ (số dải LSH) trên cùng trang | sửa | bỏ $b=8$, ghi "mã PQ 512 byte"; ô IVF-PQ "$k_c$, $nprobe$, mã PQ"; giữ $b$ cho LSH như Bài 06; rút ô PQ và ô Bảo đảm HNSW để giữ 79/80 |
| rà lại | trung bình | P05 | 30,7 giây phụ thuộc giả định $10^{12}$ lượt/giây chưa nêu trên trang | sửa | dòng cuối nêu đủ "$10^{12}$ lượt/giây, 6 TB, dưới 10 ms (giả định)"; dòng 2 rút; 59/60 |
| rà lại | nhẹ | H14 | ngoặc nêu tính chất, không nêu định nghĩa Delaunay | sửa | "(nối điểm có ô Voronoi kề nhau)"; tính chất ở ghi chú |
| rà lại | nhẹ | ghi chú C04, P05 | còn câu tả bố cục | sửa | C04 "Kết luận chọn IVF-PQ có điều kiện."; P05 "Đặc tả gần đúng cho phép chỉ mục thiếu hàng xóm thật…", "Lựa chọn chỉ mục đổi theo…" |
| rà lại | nhẹ | Q09 | "chấm" trên mặt trang trước định nghĩa ở Q11 | bác bỏ | Q09 định nghĩa phép chấm bằng công thức $\sum_jT[j,i_j]$ ngay trên trang; Q11 nêu thêm rằng chấm một mã là phép đo xấp xỉ |
| rà lại | nhẹ | storyboard | câu dẫn "Hành trình khái niệm" nói sai vị trí bản cũ | sửa | "Sáu gạch … thứ tự hiện hành; bốn gạch dưới nhãn "Bản 03/10/2026" giữ để đối chiếu." |

**Kiểm.** `git diff --check` sạch. Mật độ: P05 59/60, C00 79/80, H14 60/60, C04 69/80; mọi dòng ≤ 20 âm tiết. Playwright 1600×900 và 390×844 trên cả 65 trang: 0 lỗi console, 0 cảnh báo KaTeX, 0 `.katex-error`, không tràn khung. Ảnh đã tự xem: C00, P05, H14, C04 (1600×900).

## Rà chủ đề mạch và phong cách MAT1101 (2026-10-16)

Yêu cầu người dùng: mỗi mạch có chủ đề rõ; mọi trang trong mạch phục vụ chủ đề đó; trang không phục vụ hoặc không thấy kết nối thì xóa hoặc sửa; mặt trang theo phong cách `../MAT1101`.

### Tác tử và mô hình

Điều phối viên kiêm kiểm soát chất lượng: phiên chính Claude Opus 5.5 (`claude-opus-5-5`), effort `high`, theo xác nhận của người dùng ngày 2026-10-16 (CLAUDE.md, AGENTS.md §"Điều phối mô hình trong dự án" đã cập nhật cùng ngày). Mọi tác tử con tạo bằng `Agent`, `subagent_type: "general-purpose"`, `model: "opus"`, `effort: "high"` (theo lời gọi công cụ).

| Tác tử | Vai | Ghi tệp | Đầu ra | Quyết định của điều phối viên |
|---|---|---|---|---|
| rà mạch | chủ đề mạch, vai trò từng trang (65 trang), phụ thuộc khi xóa | không | `audit-strands-07.md` (scratchpad) | chấp nhận Phương án A; đã đối chiếu trích dẫn H11, R03, C01/C02 và cấu trúc mở đầu Bài 03, 06 |
| rà phong cách | đặc điểm MAT1101 (Bài 2, 4, 8, 9, 11), mật độ 65 trang, lệch phong cách từng trang | không | `audit-style-07.md` | chấp nhận; đã kiểm năm trích dẫn ("Bài báo HNSW:", "khổng lồ", "Ký hiệu: HNSW là", cột "Giữ cố định khi so sánh", "trang (a)") |
| sửa | sửa deck, storyboard, outline theo đặc tả `spec-revise-07.md`; ba lượt | có (deck, storyboard.md, outline.md) | diff ba tệp | lượt 1, 2, 3: chấp nhận sau khi đọc mặt trang và diff; yêu cầu sửa qua `SendMessage` ở lượt 2 và 3 |
| rà lại độ chính xác | số liệu, vết chạy, giả mã sau lượt 1 | không | `recheck-accuracy-07.md` | chấp nhận; đã kiểm H03 ($C$ theo giả mã H05) và 98% ($12\,288/12\,553=0{,}979$) |
| rà lại mạch | toàn deck sau lượt 1 | không | `recheck-storyline-07.md` | chấp nhận |
| rà lại sinh viên và mật độ | đọc như sinh viên, mật độ 63 trang, Playwright hai cỡ | không | `recheck-student-07.md` | chấp nhận; bác phát hiện chân trang (xem dưới) |
| rà lại lượt 2 và 3 | độ chính xác + mạch trên trang đổi | không | `recheck2-07.md` | chấp nhận; đã kiểm giả mã H09 ($ep$ là đỉnh, lệch H04/H10B) |

### Quyết định cấu trúc

| Mức độ | Trang chiếu | Vấn đề | Quyết định | Xử lý, lý do |
|---|---|---|---|---|
| nghiêm trọng | HT, H00–H14 | mạch HNSW 17 trang, hai câu hỏi trung tâm (tìm trên một đồ thị; cấu trúc nhiều tầng) | sửa | tách thành mạch 2 "Tìm kiếm trên đồ thị lân cận" (H00–H06) và mạch 3 "Đồ thị thế giới nhỏ phân tầng (HNSW)" (trang tiêu đề mới NT; H06B–H13) |
| trung bình | AT, A00–A03 | mạch "Bài toán hàng xóm gần đúng" là phần bài toán của mạch mở đầu (như Bài 03, 06); dòng dẫn hứa "tránh quét" | gộp | bỏ AT; A00–A03 vào mạch 1; P04 mục 1 "Bài toán hàng xóm gần đúng"; bài vẫn 7 mạch |
| trung bình | H11 | chọn lân cận đa dạng: chi tiết tùy chọn, không trang nào dùng, không mục tiêu nào đòi | bỏ | nội dung và `lan-can-da-dang.svg` giữ trong ghi chú bài giảng §5; ghi chú H10B giữ tham chiếu |
| trung bình | C01, C02 | sáu câu tự kiểm, ba câu trùng thao tác trong mạch | gộp | một trang C01, ba câu ($ef$ và bất biến; bộ nhớ HNSW; số mã IVF-PQ); lời giải khớp ghi chú bài giảng §12 |
| trung bình | R03 | nhiệm vụ giải thích không có trong sổ nguồn, không phải số đo | gộp | vào ghi chú R02 (gợi ý, lời giải mẫu, chấm 3 + 7 điểm); R02 14 phút; ghi chú bài giảng §11 giữ câu này như phần mở rộng |
| trung bình | A00 | hai đặc tả trên một trang | tách | A00 (tìm đúng) + A00B "Tìm hàng xóm gần đúng" |
| nhẹ | H13, H14 | chi phí truy vấn chen giữa bộ nhớ và nhu cầu của Q00 | sửa | H14 trước H13; mạch 3 kết ở "khoảng 98% bộ nhớ" mà Q00 nhận vào |

Số trang 65 → 63; thời lượng 120 + 60 phút giữ nguyên (phân lại trong storyboard). Phong cách: các phát hiện của `audit-style-07.md` (Nhu cầu nêu đích, Kết luận một con số, định nghĩa dạng "là", "Câu hỏi:" đầu trang bài tập, P03/P05/A02/H12 về dưới trần không ngoại lệ, "Bài báo HNSW:" thành "Mệnh đề." có giả thiết) đã áp dụng; chi tiết từng trang và âm tiết trước → sau ở storyboard, mục 2026-10-16 và các lượt sửa 2, 3.

### Phát hiện rà lại và xử lý

| Vai | Mức độ | Trang chiếu | Vấn đề | Quyết định | Xử lý |
|---|---|---|---|---|---|
| độ chính xác, sinh viên | trung bình | H03 | $C$ mô tả là "đỉnh đã thấy, chưa mở", lệch giả mã H05 | sửa | "$C$ chứa các đỉnh từng vào $W$ nhưng chưa mở"; lượt 3 trả lại "đã thấy" trong định nghĩa $W$ |
| sinh viên | trung bình | H03B | câu hỏi $ef=2$ cần quy tắc dừng đã bị bỏ khỏi H03 | sửa | "Gợi ý:" quy tắc dừng trong hộp câu hỏi (hai câu); lời giải nêu lần lấy thứ tư |
| độ chính xác, sinh viên | trung bình | H10 | $efConstruction$ chưa định nghĩa; ví dụ chèn trước ý tưởng chèn | sửa | hai dòng đầu: tầng $>\ell$ tìm với $ef=1$; tầng $\le\ell$ tìm với bề rộng chùm $efConstruction$ rồi nối $M$ đỉnh |
| mạch | trung bình | P04, NT | viết tắt HNSW trước khai triển | sửa | tên mạch 3 "Đồ thị thế giới nhỏ phân tầng (HNSW)" |
| mạch | trung bình | H06 → H06B | ranh giới mạch không hiện trên mặt trang | sửa | dòng kế thừa "SEARCH-LAYER đúng trên đỉnh đã thấy; với cạnh ngắn, số bước tăng …" + Nhu cầu |
| mạch | trung bình | storyboard | thiếu mục đầy đủ cho A00B, NT | sửa | đã thêm |
| rà lại 2 | trung bình | H09 | $ep$ là một đỉnh, lệch H04/H10B | sửa | giả mã dùng tập; H10 "$ep=\{p4\}$" |
| rà lại 2 | trung bình | outline, storyboard | tên mạch 3 cũ trong bảng hiện hành | sửa | sửa tại chỗ; mục lịch sử giữ |
| độ chính xác | nhẹ | H14, C03 | "tăng theo $\log N$" | sửa | "trung bình là $O(\log N)$", giả thiết Delaunay chính xác, bậc bị chặn |
| sinh viên | nhẹ | P00–A03 | chân trang ẩn trên mạch mở đầu | bác bỏ | quy tắc CSS dùng chung `section:first-of-type.present~.footer`, cùng hành vi ở Bài 03, 06; không sửa CSS dùng chung |
| sinh viên | nhẹ | P01 | sát đáy khung | bác bỏ | không tràn (kiểm tự động 0 phần tử vượt khung) |
| mạch | nhẹ | P00 | luận đề không nhắc tệp đảo | bác bỏ | IVF-PQ ghép hai cơ chế đã nêu; thêm vào vượt 25 âm tiết |
| mạch | nhẹ | P05 | thiếu dòng cho mạch 1 | bác bỏ | thêm làm trang 63 > 60; đặc tả gần đúng ở A00B |

Các phát hiện nhẹ khác (Q00 "khoảng 98%", Q03 câu kết, C00 "$b$ dải", I02, I03, H00, P03, P00, HT, NT, A00B ghi chú, ký hiệu $p1,\ldots,p11$, I05 tiêu đề "Ví dụ: truy vấn IVF-PQ") đã sửa; danh sách ở storyboard lượt 2, 3.

### Kiểm của điều phối viên

- Đọc mặt trang toàn deck sau lượt 1; đọc diff và ảnh các trang đổi sau lượt 2, 3.
- `git diff --check` sạch. Mật độ (`density07.py`, scratchpad): 63 trang, không trang nào vượt trần; cao nhất trần 60: H08 59, H03 56, H12 56, P05 56; trần 80: C00 79, C03 76, C05 69 (ngoại lệ trang tổng kết ghi ở storyboard), R05 66, Q03 63, P04 60. Dòng dẫn trang tiêu đề mạch 18–23 âm tiết. Ghi chú trên 150 âm tiết (nhẹ, đã ghi ở storyboard): R02 196 (lời giải và chấm), P03 181, H05 175, I03 171, C01 170 (lời giải), I02 168, R05 168.
- Playwright Chromium, server repo ở cổng 8771: cả 63 trang ở 1600×900 và 390×844, 0 lỗi console hoặc trang, 0 `.katex-error`, 0 yêu cầu mạng ngoài, 0 phần tử vượt khung ở 1600×900, không cuộn ngang ở 390×844. Sáu trang tiêu đề mạch có `span.strand-number` khớp chỉ số ngang (`#/2`…`#/7`); phím phải và xuống điều hướng đúng. Ảnh đã tự xem: NT, HT, P04, H03, H03B, H10, A00B, H14 (sau lượt 2); H09, H06B, H10 (sau lượt 3); C00 ở 390×844.
- Ghi chú bài giảng không sửa: không tham chiếu số mạch hay tiêu đề trang bị sai; deck vẫn là bản tóm tắt của ghi chú.

### Rà lại lượt 3 và sửa cuối (2026-10-16)

Tác tử rà lại lượt 2 (cùng tác tử, tiếp tục bằng `SendMessage`) rà các trang của lượt 3: không còn phát hiện chặn bàn giao, nghiêm trọng hay trung bình (`recheck2-07.md`, mục "Rà lượt 3").

| Vai | Mức độ | Trang chiếu | Vấn đề | Quyết định | Xử lý, lý do |
|---|---|---|---|---|---|
| rà lại 3 | nhẹ | H10B (ghi chú) | câu cắt lân cận chỉ đúng với cách chọn đơn giản | sửa | ghi chú nêu Thuật toán 3 giữ $M_{max}(\ell_c)$ đỉnh gần nhất, Thuật toán 4 có thể giữ tập khác; 146 âm tiết; mặt trang không đổi |
| rà lại 3 | nhẹ | H06B | dòng "Nhu cầu:" đứng sau dòng giới hạn | bác bỏ | thứ tự "giới hạn của cách trước → nhu cầu" theo `AGENTS.md` §"Mở một khái niệm hoặc một thuật toán" |
| rà lại 3 | nhẹ | outline.md:207 | còn dòng dẫn NT cũ | bác bỏ | câu ghi lịch sử thay đổi trong mục 2026-10-16, không phải bảng hiện hành |

Điều phối viên đọc lại ghi chú H10B; `git diff --check` sạch. Kiểm Playwright sau lượt 3 (63 trang, hai cỡ): 0 lỗi, 0 `.katex-error`, không tràn, không cuộn ngang.

## Lượt biên tập theo bản đánh giá giảng dạy (2026-10-27)

Yêu cầu người dùng (2026-10-27): biên tập lại các trang theo bản đánh giá giảng dạy 63 trang do người dùng gửi, để mặt trang thể hiện các giải thích và dễ hiểu với sinh viên, giữ văn phong đã thiết lập; làm lần lượt từng mạch, commit và push sau mỗi mạch. Bản đánh giá chép gọn ở scratchpad (`guide-07.md`); không dùng ảnh raster và giọng giảng viên của bản đánh giá.

### Tác tử

Mọi tác tử tạo bằng công cụ `Agent`, `subagent_type: "general-purpose"`, `model: "opus"`, `effort: "high"` (Claude Opus 5.5); điều phối viên chạy Opus 5.5, effort high. Sửa tiếp bằng `SendMessage` cho cùng tác tử.

| Vai | Nhiệm vụ | Ghi tệp | Sản phẩm | Quyết định của điều phối viên |
|---|---|---|---|---|
| lập kế hoạch | đối chiếu 63 trang với bản đánh giá; kiểm lại mọi số; đề xuất sửa/tách/thêm, mật độ, thời lượng | không | `plan-guide-07.md` (scratchpad) | chấp nhận; đã tự chạy lại vết $ef=2$, $ef=3$ để xác nhận lỗi S17 của bản đánh giá |
| biên tập | sửa deck, storyboard, outline theo từng mạch | có | diff | xem từng mạch |
| rà lại độ chính xác | số liệu, công thức, nguồn trên trang đổi | không | `recheck-acc-m<N>.md` | xem từng mạch |
| rà lại mạch, văn phong, sinh viên | kết nối, `no-ai-slop` Detect, mật độ, đồng bộ planning | không | `recheck-story-m<N>.md` | xem từng mạch |

### Quyết định chung

| Mục | Quyết định | Lý do |
|---|---|---|
| Lỗi của bản đánh giá, S17 | bác bỏ ví dụ | với $ef=3$, $C\subseteq W$ ở mọi bước; $C\not\subseteq W$ chỉ xuất hiện khi $ef=2$ sau khi mở $a$ ($C=\{s,b\}$, $W=\{b,a\}$); điều phối viên đã chạy lại |
| S24 | sửa | bước $\lfloor t\rfloor\ge k\iff t\ge k$ cần $k$ nguyên |
| S11, S43, "HNSW" trước H07, $x^{(j)}$ ở P03, "GPU" | không đưa lên mặt trang | số tự đặt khác ví dụ xuyên suốt; chỉ mục đảo từ khóa thuộc Bài 14; thuật ngữ, ký hiệu chưa định nghĩa |
| A03 | lời + $n_c$, không $t_d$ | khớp ghi chú bài giảng §1 |
| H04 | giữ hình $ef=3$, sửa chú thích | hình $ef=2$ lộ lời giải câu hỏi ngay trước đó |
| C00, ký hiệu LSH | thay bằng lời (mạch 6) | $d_1,p_1,r,b$ chưa nhắc lại trên mặt trang |
| Ghi chú bài giảng | đồng bộ sau mạch 7 | lệch có chủ đích tạm thời: ví dụ năm điểm (A00, A00B), A01B, H08B, C01B chưa có trong `lecture-note.md` |

### Mạch 1

Trang đổi: P03, P02, P01, A00, A00B, A01, A01B (mới), A02, A03; ghi chú P04. Deck 63 → 64 trang. Chi tiết và âm tiết trước → sau ở `storyboard.md`, mục "Lượt biên tập theo bản đánh giá giảng dạy (2026-10-27)".

| Vai | Mức độ | Trang chiếu | Vấn đề | Quyết định | Xử lý |
|---|---|---|---|---|---|
| độ chính xác | trung bình | A00B (ghi chú) | phép kéo theo đảo chiều ("khoảng cách xấp xỉ của $y_2$ lớn hơn của $y_1$ thì $y_1$ vào kết quả") | sửa | viết lại đúng chiều; điều phối viên kiểm phản ví dụ $y_3{:}1{,}0$ |
| mạch | trung bình | A00B | "chỉ mục" chưa định nghĩa | sửa | dòng "Chỉ mục (index) là cấu trúc dựng sẵn trên $Y$, quyết định véc-tơ nào được đo và đo thế nào."; Lưu ý chuyển vào ghi chú |
| mạch | trung bình | A01B | kết luận "0,9 không cho biết tỷ lệ truy vấn đúng hoàn toàn" chỉ ở ghi chú | sửa | lên mặt trang; câu hỏi tính cả tỷ lệ đúng hoàn toàn; "không xét thứ tự" lên A01 |
| mạch | trung bình | P03 | dòng Nhắc lại hai lần "bằng" | sửa | công thức theo phân hoạch $G_1,\ldots,G_m$ |
| độ chính xác | nhẹ | A01, P03, A01B, A03 (ghi chú) | tr.8 → mục V-A tr.7; tính độc lập của hàm; $nok$ và $nok/100$; chi phí cố định; "từ vài byte" | sửa | — |
| độ chính xác | nhẹ | P03 | $G_j$ khác ký hiệu đoạn $x^{(j)}$ của PQ | bác bỏ | không mâu thuẫn; thêm câu nối làm ghi chú > 150 âm tiết |
| mạch | nhẹ | A01 | dòng Ví dụ không nói số nào lấy từ hình | bác bỏ | bản có "Hình:" xuống hai dòng ở 1600×900 |
| mạch | nhẹ | P04 (ghi chú), P03, outline | chủ ngữ "Mỗi mạch"; "(Bài 06)" lặp; câu "$n_c$ chỉ dùng ở Q11" | sửa | — |
| mạch | nhẹ | P01 | mép dưới hộp Câu hỏi chạm mũi tên điều khiển dọc ở 1600×900 | tồn đọng | có từ trước lượt này (hộp một dòng, cùng vị trí); sửa cần đổi CSS dùng chung hoặc bỏ nội dung |
| mạch | nhẹ | Q11; P02 | $n_c$ nên là "Nhắc lại:"; mục tiêu dạng giải thích | để sau | mạch 4; mạch 6 |

Kiểm của điều phối viên: đọc diff deck và planning; `check07.py` (Playwright Chromium, cổng 8771): 64 trang, 0 lỗi console/trang, 0 `.katex-error`, 0 yêu cầu mạng ngoài, 0 phần tử vượt khung 1600×900, không cuộn ngang 390×844; mạch 1 cao nhất A00B 59, A01B 58, P03 56 âm tiết (trần 60), A02, A03 6 dòng. Ảnh đã tự xem: A01B, A03, A00B, P01 (1600×900). `git diff --check` sạch. Hai báo cáo rà lượt 2: không còn phát hiện từ mức trung bình trở lên.

### Mạch 2

Trang đổi: H00, H01, H01B (mới, hình mới `cuc-tieu-cuc-bo.svg` sinh bằng chế độ `'local'` của `generate_svg.py`), H03, H03B, H03C (mới), H04, H05 (chú thích trong giả mã), H06. Deck 64 → 66 trang. Chạy lại `generate_svg.py` không đổi 19 SVG cũ (`git diff --stat img/lec-07/` chỉ có `generate_svg.py`).

| Vai | Mức độ | Trang chiếu | Vấn đề | Quyết định | Xử lý |
|---|---|---|---|---|---|
| mạch | trung bình | H03B, H03C | cột $d(c,q)$, $d(f,q)$ có trên bảng nhưng quy tắc mở/dừng chưa có trên mặt trang trước giả mã; "Gợi ý:" trên mặt trang H03C | sửa | dòng "Mở $c$ khi $d(c,q)\le d(f,q)$, với $f$ là đỉnh xa $q$ nhất của $W$; ngược lại dừng." trên H03B (7 dòng, trần bảng vết 8); gợi ý vào ghi chú H03C |
| mạch | nhẹ | H05, H03, H01, H04 | chú thích lệch cột; "đã thấy" trước định nghĩa; $e:9$ không thống nhất; công thức ngắt dòng | sửa | canh cột 40; "(đã đo $d(\cdot,q)$)"; `{:}`; "(một đồ thị thì $\ell_c=0$)" |
| mạch, độ chính xác | nhẹ | ghi chú H01, H06 | câu "4 phép đo" lặp; "thăm mọi đỉnh và cạnh của tầng" | sửa | giữ ở H01B; "đến được từ $ep$ trong tầng" |
| biên tập | — | H06 | câu kế hoạch "$y$ không thuộc $ef$ đỉnh gần nhất" sai khi hòa khoảng cách | sửa | "$W$ vẫn là $ef$ đỉnh gần nhất"; tác tử độ chính xác xác nhận cả trường hợp hòa |

Tác tử độ chính xác tự chạy Thuật toán 2 (hai thứ tự duyệt lân cận) với $ef=3$, $ef=2$, $ef=1$: mọi ô của H03B, H03C khớp; $C\not\subseteq W$ chỉ ở $ef=2$ sau khi mở $a$ (ghi chú H03C); chú thích H04 đúng. Điều phối viên tự kiểm cột so sánh bảy lần mở ($9\le9$, $7\le9$, $5\le8$, $8\le8$, $4\le7$, $2\le5$, $1\le4$).

Kiểm của điều phối viên: đọc diff; `check07.py`: 66 trang, 0 lỗi, 0 `.katex-error`, 0 mạng ngoài, 0 vượt khung 1600×900, không cuộn ngang 390×844; mạch 2 cao nhất H03 58, H04 48 âm tiết; H03B 7 dòng (bảng vết). Ảnh đã tự xem: H01B, H03B, H05, H06 (1600×900). Thời lượng tạm 121 phút cho tới khi mạch 3–5 phân lại (ghi ở storyboard). Hai báo cáo rà lượt 2: không có phát hiện.

### Mạch 3

Trang đổi: H06B (tiêu đề rút thành "Ví dụ: cạnh dài" để không chạm mũi tên điều khiển), H07 (khai triển HNSW), H09, H08 (chứng minh với "$k$ nguyên"), H08B (mới, số điểm mỗi tầng), H10, H10B, H14 (bảng thừa số–cận–giả thiết), H13; ghi chú H12. Deck 66 → 67 trang. Không đổi SVG.

| Vai | Mức độ | Trang chiếu | Vấn đề | Quyết định | Xử lý |
|---|---|---|---|---|---|
| độ chính xác (rà lượt 2) | nghiêm trọng | H14 | cận "số bước mỗi tầng trung bình $\le1/(1-\rho)\approx1{,}07$" sai; lấy theo hằng số $S=1/(1-\exp(-m_L))$ in ở bài báo, mục 4.2.1, tr.7, vốn không nhất quán với chính lập luận của bài báo ($p$ là xác suất đỉnh kế tiếp thuộc tầng trên) | sửa | "trung bình $\le1/\rho=M$": mọi đỉnh trên đường đi trừ điểm xuất phát không thuộc tầng trên, nên $\Pr[\ge s\text{ bước}]\le(1-\rho)^s$; $\rho=1/16$ cho tối đa 16 bước kỳ vọng, không phụ thuộc $N$. Điều phối viên đã đọc đoạn 4.2.1 của bài báo (pdftotext) để xác nhận. Không chép hằng số của bài báo |
| mạch | trung bình | H14 | mô hình ba thừa số không nối thừa số với giả thiết | sửa | bảng `Thừa số | Cận | Giả thiết dùng`; ô Voronoi vào ghi chú; 69 âm tiết, 6 dòng (trang chi phí, trần 80) |
| độ chính xác | nhẹ | H10, H10B, H14 (ghi chú) | điều kiện dừng ở tầng 0 ($p1$ đã lấy ra); bậc tối đa ngầm định 3 khác $M_{max}=M$ của H13; thứ tự lý do–kết luận; số trang | sửa | ghi rõ $M_{max}=3$, $M_{max,0}=4$; "mục 4.2.1, tr.7" |
| mạch | nhẹ | H06B, H13, ghi chú H14 | "khoảng cách tới $q$" mơ hồ; nhãn dòng kỳ vọng; câu không nguồn về số chiều | sửa | "từ điểm vào tới $q$"; "Mỗi điểm, kỳ vọng …"; thay bằng ý của bài báo |
| biên tập | — | H06B | thêm dòng Nhận xét làm tràn khung | sửa | dòng kế thừa gộp vào Nhu cầu; ý "SEARCH-LAYER đúng trên đỉnh đã thấy" ở ghi chú NT, H06B |
| biên tập | — | H08B | $\rho$ trong tiêu đề viết hoa thành "Ρ" | sửa | tiêu đề "Ví dụ: số điểm mỗi tầng của kho mười tỷ véc-tơ" |

Kiểm của điều phối viên: đọc diff; tự kiểm bảng H08B ($10^{10}/256\approx3{,}9\cdot10^7$; $16^{-3}\approx2{,}4\cdot10^{-4}$; $10^{10}/16^8\approx2{,}33$); `check07.py`: 67 trang, 0 lỗi, 0 `.katex-error`, 0 mạng ngoài, 0 vượt khung, không cuộn ngang; mạch 3 cao nhất H13 55, H07 54 (trần 60), H14 69 (trần 80); ghi chú H14 231 âm tiết (lập luận chứng minh). Ảnh đã tự xem: H08, H08B, H14 (1600×900). Thời lượng tạm 119 phút cho tới mạch 4, 5. Rà lượt 2 (mạch) và lượt 3 (độ chính xác): không còn phát hiện.

### Mạch 4

Trang đổi: Q00, Q02, Q03, Q04, Q07, Q06, Q08, Q09, Q11, Q10; QT, Q05 giữ. Không trang mới, không đổi SVG.

| Vai | Mức độ | Trang chiếu | Vấn đề | Quyết định | Xử lý |
|---|---|---|---|---|---|
| độ chính xác | nhẹ | Q06 (ghi chú) | "0,31 và 0,18 chỉ liên hệ qua bất đẳng thức tam giác" nói quá | sửa | khai triển $\|q-\widehat x\|^2=\|q-x\|^2+\|x-\widehat x\|^2+2\langle q-x,x-\widehat x\rangle$, $0{,}31=0{,}07+0{,}18+0{,}06$ (điều phối viên tự tính $\langle\cdot\rangle=0{,}03$); bất đẳng thức tam giác cho căn bậc hai (mục III-B) |
| độ chính xác | nhẹ | Q07 (ghi chú) | "sai số PQ không nhỏ hơn VQ" thiếu lý do | sửa | mọi bộ mã PQ là bộ mã VQ khả thi có $(k^*)^m$ tâm |
| mạch | nhẹ | Q11 | Mô hình không nêu đơn vị đếm; thiếu dòng tổng | sửa | "đếm phép toán trên tọa độ và lần tra ô bảng"; "Tổng: $k^*D+mn_c$ so với $Dn_c$" |
| mạch | nhẹ | Q04, Q02 (và ghi chú) | trang kín khung; "Nhắc lại" chen giữa Đầu vào và Đầu ra; câu ghi chú dạng lời dặn | sửa | Định nghĩa một dòng; Nhắc lại lên trước Đầu vào; "bộ mã đã học không nhất thiết tối ưu toàn cục" |
| mạch | nhẹ | Q07 | "bậc tự do" chưa giải nghĩa trên mặt trang | bác bỏ | dòng giải nghĩa 29 âm tiết, vượt trần 20 âm tiết mỗi dòng; ghi chú giải nghĩa |

Công cụ kiểm: tác tử biên tập phát hiện ở 390×844 Reveal chạy chế độ cuộn, nên ảnh 390 của `check07.py` trước lượt mạch 4 có thể là trang liền trước; kiểm cuộn ngang toàn trang không bị ảnh hưởng. Điều phối viên sửa script chụp theo phần tử `section`; ảnh 390 từ mạch 4 trở đi chụp đúng trang.

Kiểm của điều phối viên: đọc diff; `check07.py`: 67 trang, 0 lỗi, 0 `.katex-error`, 0 mạng ngoài, 0 vượt khung, không cuộn ngang; mạch 4 cao nhất Q04 57, Q07 59, Q08 58 (trần 60 hoặc 80 bảng so sánh), Q11 70, Q03 66, Q10 61 (trang chi phí, trần 80). Ảnh đã tự xem: Q04 (1600, 390), Q11 (1600). Một phiên rà bị gián đoạn do lỗi hạn mức API (429), tiếp tục bằng `SendMessage` cho cùng tác tử. Thời lượng tạm 118 phút cho tới mạch 5. Hai báo cáo rà lượt 2: không có phát hiện.

### Mạch 5

Trang đổi: I00 (ghi chú), I01, I02, I02B (mới, "Ví dụ: truy vấn dư theo đúng danh sách", dùng lại `tep-dao-du.svg`), I04, I05, I03. Deck 67 → 68 trang. Phần giảng về đúng 120 phút (19,5 + 21 + 21 + 27 + 19 + 12,5), 59 trang; thực hành 60 phút.

| Vai | Mức độ | Trang chiếu | Vấn đề | Quyết định | Xử lý |
|---|---|---|---|---|---|
| điều phối viên | trung bình | I01 | hộp Câu hỏi đè mũi tên điều khiển dưới ở 1600×900 (script không báo tràn) | sửa | dòng Nhận xét $y_3$ chuyển sang cột trái dưới hình; đã tự xem ảnh sau sửa |
| độ chính xác, mạch | nhẹ | I02 | "nhỏ hơn" (đúng là "không lớn hơn"); công thức bọc `{…}` làm cụm chữ đứng một mình | sửa | "không lớn hơn"; viết lại câu lý do đẳng thức |
| mạch | nhẹ | I03 | dùng 3,6 ms trước khi suy ra | sửa | dòng "Với $10^{12}$ thao tác mỗi giây: khoảng 3,6 ms; đọc $\approx3{,}3$ GB trong 3,6 ms cần cỡ 0,9 TB/s." trước Kết luận |
| độ chính xác | nhẹ | I03 (ghi chú) | 1409 chỉ đúng với mẫu số $3{,}634\cdot10^9$; "cỡ 1 TB/s" | sửa | mẫu số chưa làm tròn; 0,92 TB/s |
| mạch | nhẹ | I02B (ghi chú) | "thường gặp" không nguồn | sửa | bỏ |
| mạch | nhẹ | C03 | hàng HNSW chưa đồng bộ ba giả thiết của H14 | để sau | mạch 6 |

Kiểm của điều phối viên: đọc diff; `check07.py` toàn deck: 68 trang, 0 lỗi console/trang, 0 `.katex-error`, 0 mạng ngoài, 0 vượt khung 1600×900, không cuộn ngang 390×844; mạch 5 cao nhất I02 54 (trần 60), I03 62 (trang chi phí, trần 80, 8 dòng). Ảnh đã tự xem: I01 (trước và sau sửa), I02B, I03 (1600×900). Hai báo cáo rà lượt 2: không có phát hiện từ mức trung bình trở lên.

### Mạch 6

Trang đổi: C03, C00, C04, C01 (tiêu đề "…, câu 1–2"), C01B (mới, "Câu hỏi tự kiểm tra, câu 3–4"), C05 (ghi chú); mạch 1: P02 (mục tiêu 1 thêm "giải thích hai nguồn thiếu điểm"; ghi chú ánh xạ câu tự kiểm → mục tiêu). Deck 68 → 69 trang; phần giảng 60 trang, 120 phút.

| Vai | Mức độ | Trang chiếu | Vấn đề | Quyết định | Xử lý |
|---|---|---|---|---|---|
| mạch (báo trước từ mạch 5) | nhẹ | C03 | hàng HNSW chưa đồng bộ ba giả thiết của H14 | sửa | "tầng rút độc lập vị trí; Delaunay chính xác; bậc trung bình bị chặn"; cận $\le1/\rho$ ở ghi chú |
| kế hoạch | trung bình (có từ trước) | C00 | $d_1,p_1,r,b$ trên mặt trang chưa được nhắc lại | sửa | ô Bảo đảm LSH bằng lời; chi phí "$12\,288+8b$ byte ($b$ dải)"; ghi chú dẫn về P03 |
| mạch, độ chính xác | nhẹ | C01 (ghi chú), C03, C01B | lời giải $ef=2$ ngầm định thứ tự duyệt; "đoạn rời nhau"; "PQ xếp sai"; hai trang trùng tiêu đề | sửa | nêu cả hai thứ tự (kết quả không đổi); "phân hoạch tọa độ"; "ADC xếp sai thứ tự"; tiêu đề kèm số câu |
| mạch | — | P02 | năng lực giải thích (để sau từ mạch 1) | sửa | đặt ở mục tiêu 1, khớp câu tự kiểm 4; mục tiêu 2 không thêm vì dòng lên 28 âm tiết |
| mạch | — | H14 (mạch 3) | tác tử mạch đính chính đề xuất $1/(1-\rho)$ của chính mình ở mạch 3 | ghi nhận | đã sửa thành $\le1/\rho$ ở commit mạch 3 |

Câu tự kiểm sau lượt này: câu 1 ($ef=2$, $ef=3$) → mục tiêu 2; câu 2 (bộ nhớ HNSW) → mục tiêu 3; câu 3 (số mã IVF-PQ) → mục tiêu 3; câu 4 (chẩn đoán độ thu hồi thấp, mới) → mục tiêu 1 và 3. Câu "Tại sao SEARCH-LAYER … trả sai KNN?" của bản đánh giá không thêm (trùng năng lực câu 1, dạng câu hỏi "Tại sao" không hợp nhãn).

Kiểm của điều phối viên: đọc diff; `check07.py` toàn deck: 69 trang, 0 lỗi, 0 `.katex-error`, 0 mạng ngoài, 0 vượt khung, không cuộn ngang; mạch 6 cao nhất C03 71, C00 65 (bảng tổng kết, trần 80), C04 56 (trần 60). Ảnh đã tự xem: C03, C00, C04 (1600×900). Hai báo cáo rà lượt 2: không có phát hiện.
