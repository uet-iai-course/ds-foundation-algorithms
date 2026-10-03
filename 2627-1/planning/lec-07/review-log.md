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
