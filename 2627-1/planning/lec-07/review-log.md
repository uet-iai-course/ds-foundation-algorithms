# Nhật ký rà soát Bài 7

## Quyết định nguồn và biên tập

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
