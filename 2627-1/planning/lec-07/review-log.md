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
