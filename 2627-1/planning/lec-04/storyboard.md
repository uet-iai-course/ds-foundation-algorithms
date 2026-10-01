# Storyboard mới Bài 04: PageRank theo chủ đề, liên kết rác và HITS

Ngày soạn: 27/09/2026; cập nhật làm rõ nội dung: 29/09/2026. Các phiếu dưới đây phản ánh bản HTML hiện tại gồm53 trang. Kết quả kiểm định từng phiên được lưu trong review-log.md.

Nguồn nền là sách MMDS Chương 5: §5.3 → §5.4 → §5.5. Các slide MMDS, Stanford và Cambridge chỉ đối chiếu cách minh họa; không quyết định lại mạch sách. Đọc cùng [outline.md](outline.md) để tra mã NG, MT, HT, VD và bản đồ quyết định; xem [review-log.md](review-log.md) cho sai khác nguồn và các lượt rà độc lập.

## Quy ước đọc phiếu

- **Nội dung hiển thị dự kiến** và **Ghi chú học thuật dự kiến** là hai vùng văn bản công khai dự kiến; chỉ chứa nội dung môn học, nhiệm vụ người học và lời giải. Các trường còn lại là metadata nội bộ, không chuyển nguyên lên slide hoặc ghi chú diễn giả.
- Mỗi trang có một bố cục được chọn, nội dung cụ thể và trọng tâm. Bố cục đã triển khai trong HTML; lượt chỉnh29/09 đang chờ kiểm định render độc lập. Khung1280×720, thành phần chung của `lecture-style.css`, không thu nhỏ chữ để chứa thêm nội dung, không dùng `fragment`.
- Công thức hiển thị bằng KaTeX; bảng và giả mã là văn bản/HTML; sơ đồ kỹ thuật sẽ vẽ SVG từ đúng cạnh, có nhãn ngoài màu và mô tả thay thế. HTML dùng các SVG hiện có; lượt chỉnh này không tạo hoặc sửa mã thực hành.
- Mã đầy đủ `lec04-sxx-yy` chỉ nằm ở phiếu và metadata. Tên phần, tiêu đề slide và ghi chú học thuật không chứa mã nội bộ hoặc thời lượng.
- Các VD1–VD4 giữ số, vai trò đại lượng, trạng thái và kiểm lỗi trong outline. Từng phiếu chỉ rõ phần dữ kiện thực sự hiển thị. Tên G4/G5 là nhãn đồ thị minh họa, không là mã quy trình.
- Bộ bài gồm50 slide giảng/120 phút và3 slide recitation/60 phút. Thời gian của câu hỏi đã nằm trong thời lượng slide; lời giải recitation thuộc ghi chú, không đưa lên mặt slide ban đầu.

## Bản đồ phần và kiểm tra

| Phần | Số slide | Thời lượng | Slide kiểm tra riêng |
|---|---:|---:|---|
| S01. Bài toán xếp hạng liên kết | 6 | 12 phút | `lec04-s01-06` |
| S02. PageRank theo chủ đề | 13 | 30 phút | `lec04-s02-12` |
| S03. Cơ chế liên kết rác | 8 | 20 phút | `lec04-s03-08` |
| S04. TrustRank và Spam Mass | 8 | 18 phút | `lec04-s04-07` |
| S05. HITS | 11 | 30 phút | `lec04-s05-11` |
| S06. So sánh các phương pháp xếp hạng | 4 | 10 phút | `lec04-s06-04` |
| S07. Bài tập | 3 | 60 phút | `lec04-s07-03` |

## Phiếu từng trang chiếu

## S01. Bài toán xếp hạng liên kết

Giới thiệu và động lực. PageRank Bài 03 → truy vấn đa nghĩa và giới hạn lưu trữ → ba mục tiêu xếp hạng → kiểm tra chiều truyền điểm. Đầu ra chuyển sang S02 là nhu cầu thay phân phối dịch chuyển. Tình huống “jaguar” được dùng lại ở S02-11, S06-02.

Phân bổ: 6 slide, 12 phút.

### lec04-s01-01 — PageRank theo chủ đề, liên kết rác và HITS

**Vai trò, mục tiêu, đầu vào và sản phẩm:** Mở đầu; MT1–MT5. Đầu vào: PageRank Bài 03. Sản phẩm: xác định vị trí và phạm vi Bài 04.

**Luận điểm trung tâm:** Ba nhu cầu xếp hạng dẫn tới các điểm theo chủ đề, theo tập tin cậy và theo hai vai trò liên kết.

**Nội dung hiển thị dự kiến:**

<!-- public-slide:start -->
Bài 04. PageRank theo chủ đề, liên kết rác và HITS

Giải thuật nền tảng của Khoa học dữ liệu

Học kỳ 1, năm học 2026–2027
<!-- public-slide:end -->

**Bố cục đã chọn:** Tiêu đề ở giữa phía trên, chiếm khoảng 55% chiều cao; tên học phần và học kỳ thành hai dòng dưới. Dùng thành phần trang tiêu đề chung.

**Trọng tâm và thứ tự đọc:** Đọc tên ba cụm nội dung trước, sau đó tên học phần và học kỳ.

**Lý do phù hợp sinh viên năm 2:** Sinh viên nhận diện đây là phần tiếp của xếp hạng liên kết; trang không đưa thêm công thức trước nhu cầu sử dụng.

**Giới hạn bố cục và phân chia nội dung:** Chỉ ba khối chữ đã nêu; mục tiêu cụ thể thuộc trang nội dung kế tiếp.

**Ví dụ, phiếu số và hình thức hóa:** Không có ví dụ số hoặc phát biểu hình thức ở trang tiêu đề.

**Kết nối vào–ra:** Bài 03 đã tạo điểm PageRank toàn cục → bài này thay mục tiêu xếp hạng.

**Nguồn và vị trí:** NG0: bài đề xuất 4, buổi gốc 5; NG1 §5.3–5.5, tr.195–208.

**Thời lượng:** 1 phút.

**Ghi chú học thuật dự kiến:**

<!-- public-notes:start -->
Bài học xét ba yêu cầu trên dữ liệu liên kết: thiên lệch điểm theo chủ đề, giảm tác động của liên kết thao túng và phân biệt hai vai trò cấu trúc. Cơ chế PageRank đã học là đầu vào của hai yêu cầu đầu; HITS xây dựng hai vector điểm trên cùng kiểu dữ liệu đồ thị.
<!-- public-notes:end -->

### lec04-s01-02 — Nội dung và mục tiêu học tập

**Vai trò, mục tiêu, đầu vào và sản phẩm:** Định vị mạch; MT1–MT5. Đầu vào: tên bài. Sản phẩm: nhận diện các năng lực và thứ tự nội dung.

**Luận điểm trung tâm:** Mạch bài theo PageRank theo chủ đề, liên kết rác rồi HITS, kết thúc bằng lựa chọn và bài tập.

**Nội dung hiển thị dự kiến:**

<!-- public-slide:start -->
1. Bài toán xếp hạng liên kết.
2. PageRank theo chủ đề.
3. Cơ chế liên kết rác.
4. TrustRank và Spam Mass.
5. HITS.
6. So sánh các phương pháp xếp hạng.
7. Bài tập.

Mục tiêu: tính PageRank theo chủ đề, TrustRank, Spam Mass và điểm HITS; giải thích tác động của cụm liên kết rác; chọn phương pháp theo đầu ra cần tạo.
<!-- public-slide:end -->

**Bố cục đã chọn:** Bảy mục chia hai cột 55%–45%, lần lượt 1–4 và 5–7; một dòng mục tiêu ở chân trang nội dung nêu đối tượng tính, cơ chế cần giải thích và tiêu chí chọn. Dùng thành phần mục lục chung.

**Trọng tâm và thứ tự đọc:** Đọc cột trái từ trên xuống, tiếp sang cột phải; dòng mục tiêu nối các phần bằng ba thao tác gắn với từng phương pháp.

**Lý do phù hợp sinh viên năm 2:** Thứ tự chủ đề–liên kết rác–HITS theo sách giúp sinh viên nhận biết phần nào dùng lại PageRank, phần nào đổi mô hình điểm.

**Giới hạn bố cục và phân chia nội dung:** Mặt slide giữ tên phần và một dòng năng lực; mã MT và thời lượng chỉ nằm trong hồ sơ này.

**Ví dụ, phiếu số và hình thức hóa:** Không có dữ liệu số; danh mục phần khớp bảy section đã duyệt.

**Kết nối vào–ra:** Phạm vi bài → tình huống truy vấn cần điểm theo chủ đề.

**Nguồn và vị trí:** NG1 §5.3→§5.4→§5.5; NG0 sản phẩm học tập Bài 04.

**Thời lượng:** 1 phút.

**Ghi chú học thuật dự kiến:**

<!-- public-notes:start -->
PageRank theo chủ đề giữ phép lặp của Bài 03 và chỉ đổi nơi đến của bước nhảy ngẫu nhiên: bước nhảy tới các trang đại diện một chủ đề thay vì mọi trang. Mô hình cụm liên kết rác cho thấy một cấu trúc liên kết có thể khuếch đại điểm của trang đích. TrustRank dùng cùng phép lặp, với tập trang tin cậy làm nơi đến của bước nhảy; Spam Mass so sánh TrustRank với PageRank để chọn trang cần rà soát. HITS gán mỗi trang hai điểm, trung tâm và uy tín, thay cho một điểm duy nhất. Phần bài tập áp dụng các phương trình này trên dữ liệu của giáo trình.
<!-- public-notes:end -->

**Quyết định duyệt trang 01/10/2026:** sửa. Giữ tiêu đề và bảy mục; thay dòng mục tiêu trừu tượng bằng động từ gắn với từng phương pháp; ghi chú nêu mạch bốn phương pháp và nối “bước nhảy ngẫu nhiên” của Bài 03.

### lec04-s01-03 — Truy vấn đa nghĩa

**Vai trò, mục tiêu, đầu vào và sản phẩm:** Tình huống sử dụng; MT1. Đầu vào: PageRank toàn cục. Sản phẩm: xác định đầu ra xếp hạng có điều kiện theo chủ đề.

**Luận điểm trung tâm:** Cùng truy vấn có thể cần thứ tự trang khác nhau khi chủ đề thay đổi; PageRank toàn cục chỉ cho một thứ tự, nên cần điểm phụ thuộc chủ đề.

**Nội dung hiển thị dự kiến:**

<!-- public-slide:start -->
Truy vấn: “jaguar”.

- Chủ đề động vật: ưu tiên các trang về loài báo đốm.
- Chủ đề ô tô: ưu tiên các trang về hãng xe Jaguar.

Dữ liệu: trang web và liên kết. Đầu ra: thứ tự trang theo chủ đề đã xác định.

PageRank toàn cục cho cùng một thứ tự trong cả hai ngữ cảnh. Khi biết chủ đề người dùng quan tâm, điểm xếp hạng cần phụ thuộc chủ đề đó.
<!-- public-slide:end -->

**Bố cục đã chọn:** Từ truy vấn ở dải trên; bên dưới là hai nhóm trang ngang nhau với nhãn “Động vật” và “Ô tô”. Dòng đầu vào–đầu ra nằm dưới hai thẻ; giới hạn của PageRank toàn cục đặt trong khối kết luận cuối trang. Không gán điểm minh họa.

**Trọng tâm và thứ tự đọc:** Đọc cùng truy vấn, đối chiếu hai nhóm chủ đề, rồi xác định đại lượng cần thay đổi.

**Lý do phù hợp sinh viên năm 2:** Ví dụ dùng hai nghĩa trong sách, không đòi kiến thức phân loại văn bản; sinh viên phân biệt truy vấn với ngữ cảnh xếp hạng.

**Giới hạn bố cục và phân chia nội dung:** Chỉ hai nghĩa, không thêm sản phẩm lịch sử. Các bước xác định chủ đề không thuộc mặt slide này.

**Ví dụ, phiếu số và hình thức hóa:** Ví dụ định tính NG1 §5.3.1; không tạo số liệu truy vấn hay điểm trang.

**Kết nối vào–ra:** PageRank toàn cục đã có → cần điểm phụ thuộc chủ đề; ghi chú nêu phương án trực tiếp (một vector cho mỗi người dùng) mà trang sau xét chi phí lưu trữ.

**Nguồn và vị trí:** NG1 §5.3.1, tr.195–196/PDF21–22.

**Thời lượng:** 3 phút.

**Ghi chú học thuật dự kiến:**

<!-- public-notes:start -->
Từ “jaguar” có thể chỉ loài vật, hãng ô tô hoặc một số đối tượng khác. MMDS nêu rằng nếu suy ra được người dùng quan tâm tới ô tô, máy tìm kiếm có thể trả các trang phù hợp hơn. Điểm PageRank toàn cục đo độ quan trọng của trang trên toàn đồ thị và không chứa thông tin về chủ đề đó. Trong bài này, chủ đề là đầu vào đã biết; cách suy ra chủ đề từ truy vấn hay lịch sử người dùng nằm ngoài phép tính PageRank theo chủ đề. Phương án trực tiếp để phản ánh sở thích là lưu một vector PageRank riêng cho mỗi người dùng; chi phí lưu trữ của phương án này quyết định cách làm được chọn.
<!-- public-notes:end -->

**Quyết định duyệt trang 01/10/2026:** sửa. Rút tiêu đề còn “Truy vấn đa nghĩa”; đưa giới hạn của PageRank toàn cục thành khối kết luận vì đây là nhu cầu dẫn sang PageRank theo chủ đề; ghi chú nêu căn cứ MMDS §5.3.1, chủ đề là đầu vào và câu nối sang phương án một vector cho mỗi người dùng.

### lec04-s01-04 — Chi phí lưu PageRank riêng

**Vai trò, mục tiêu, đầu vào và sản phẩm:** Giới hạn dữ liệu lớn; MT1, MT5. Đầu vào: nhu cầu theo ngữ cảnh. Sản phẩm: giải thích việc tiền tính số ít vector chủ đề.

**Luận điểm trung tâm:** Phương án trực tiếp, mỗi người dùng một vector PageRank toàn web, không lưu được ở quy mô web; $k$ vector chủ đề và $k$ trọng số cho mỗi người dùng thay thế, đổi lại mất một phần độ chính xác.

**Nội dung hiển thị dự kiến:**

<!-- public-slide:start -->
Phương án trực tiếp: mỗi người dùng có một vector PageRank riêng trên toàn web.

[Hình: mỗi người dùng → vector điểm toàn web; các chủ đề → vector điểm toàn web, mỗi người dùng → trọng số chủ đề.]

Quy mô minh họa trong MMDS: khoảng một tỷ người dùng, mỗi vector có nhiều tỷ thành phần. Phương án theo chủ đề lưu $k$ vector toàn web; mỗi người dùng chỉ cần $k$ trọng số, đổi lại mất một phần độ chính xác.
<!-- public-slide:end -->

**Bố cục đã chọn:** Một dòng nêu phương án trực tiếp ở đầu trang, trước khi nêu giới hạn. Hai hàng so sánh theo cùng chiều ngang: hàng trên “Mỗi người dùng → vector toàn web”; hàng dưới “Các chủ đề → vector toàn web; người dùng → trọng số chủ đề”. Sơ đồ chiếm 70%, câu kết chiếm 30%.

**Trọng tâm và thứ tự đọc:** So sánh đối tượng được nhân bản ở hai hàng; nhãn “toàn web” luôn gắn với vector dài.

**Lý do phù hợp sinh viên năm 2:** Sinh viên đã biết mảng một chiều; sơ đồ phân biệt số vector và độ dài vector trước khi đếm bộ nhớ bằng ký hiệu.

**Giới hạn bố cục và phân chia nội dung:** Dùng quy mô minh họa có sẵn trong NG1: khoảng một tỷ người dùng, mỗi vector nhiều tỷ thành phần; không trình bày như số đo hiện hành. Phép đếm theo số chủ đề nằm ở phần chi phí.

**Ví dụ, phiếu số và hình thức hóa:** Bối cảnh lưu trữ NG1 §5.3.1–2; không có phiếu số riêng.

**Kết nối vào–ra:** Phương án một vector cho mỗi người dùng nêu ở ghi chú trang trước → $k$ vector chủ đề; ghi chú nối sang ba nhu cầu xếp hạng ở trang sau.

**Nguồn và vị trí:** NG1 §5.3.1–5.3.2, tr.195–196/PDF21–22.

**Thời lượng:** 2 phút.

**Ghi chú học thuật dự kiến:**

<!-- public-notes:start -->
Ở phương án trực tiếp, số vector dài cần lưu bằng số người dùng; ở phương án theo chủ đề, số này bằng số chủ đề $k$. Độ dài mỗi vector vẫn là số trang. Phần lưu riêng cho mỗi người dùng giảm từ một vector có nhiều tỷ thành phần xuống $k$ trọng số. Sở thích khi đó chỉ được biểu diễn qua các chủ đề đã chọn, nên một vector riêng tùy ý không còn được tái tạo đúng; MMDS ghi nhận đây là phần độ chính xác bị mất. Xếp hạng theo chủ đề là một trong ba nhu cầu mà điểm dựa trên liên kết phải đáp ứng trong bài.
<!-- public-notes:end -->

**Quyết định duyệt trang 01/10/2026:** sửa. Tiêu đề cũ dùng “xếp hạng cá nhân” trước khi khái niệm được nêu; thêm dòng phương án trực tiếp ở đầu trang rồi mới nêu quy mô và phương án thay thế. Khối kết luận nêu cái giá mất một phần độ chính xác theo MMDS §5.3.1. Dùng “$k$ vector”, chưa đưa ký hiệu trọng số $w_j$.

### lec04-s01-05 — Ba yêu cầu xếp hạng liên kết

**Vai trò, mục tiêu, đầu vào và sản phẩm:** Phân biệt vấn đề; MT1, MT3–MT5. Đầu vào: điểm toàn cục. Sản phẩm: ánh xạ yêu cầu sang loại điểm cần tính.

**Luận điểm trung tâm:** Mỗi yêu cầu xuất phát từ một hạn chế của PageRank toàn cục và cho điểm xếp hạng một ý nghĩa khác.

**Nội dung hiển thị dự kiến:**

<!-- public-slide:start -->
| Hạn chế của PageRank toàn cục | Yêu cầu đối với điểm |
|---|---|
| Cùng truy vấn ở hai ngữ cảnh nhận cùng một thứ tự | Điểm phụ thuộc chủ đề |
| Liên kết có thể được tạo ra để làm tăng điểm một trang | Điểm ít chịu tác động của liên kết thao túng |
| Một điểm duy nhất không tách trang dẫn tới thông tin khỏi trang cung cấp thông tin | Hai điểm cho hai vai trò |

Mỗi yêu cầu cho điểm xếp hạng một ý nghĩa riêng và cần một phép tính riêng.
<!-- public-slide:end -->

**Bố cục đã chọn:** Bảng hai cột chiếm khoảng 75% diện tích; một câu kết ở dưới. Ba hàng giữ cùng độ cao, không thêm công thức.

**Trọng tâm và thứ tự đọc:** Đọc hạn chế ở trái rồi yêu cầu tương ứng ở phải; mỗi hàng là động cơ của một phần sau.

**Lý do phù hợp sinh viên năm 2:** Bảng giúp sinh viên tránh coi mọi thuật toán đều đo một khái niệm chất lượng duy nhất; chưa yêu cầu thuật ngữ sẽ học sau.

**Giới hạn bố cục và phân chia nội dung:** Chỉ ba yêu cầu; tên thuật toán chi tiết và ưu nhược điểm để cuối bài khi đã có cơ chế.

**Ví dụ, phiếu số và hình thức hóa:** Không có số; phân loại theo NG1 §5.3–5.5.

**Kết nối vào–ra:** Giới hạn của một vector toàn cục → ba yêu cầu, ánh xạ sang S02, S03–S04, S05; hai yêu cầu đầu dùng lại phép lặp với $M_0$ nên trang sau ôn phép truyền điểm.

**Nguồn và vị trí:** NG1 §5.3.1, tr.195; §5.4.1, tr.199–200; §5.5.1, tr.204–205.

**Thời lượng:** 2 phút.

**Ghi chú học thuật dự kiến:**

<!-- public-notes:start -->
Hạn chế thứ nhất đã xuất hiện ở truy vấn “jaguar”; PageRank theo chủ đề đổi nơi đến của bước nhảy ngẫu nhiên để điểm phụ thuộc chủ đề. Hạn chế thứ hai nằm ngay trong cơ chế truyền điểm: MMDS gọi một tập trang được lập ra để tăng PageRank của một trang là cụm thao túng liên kết (spam farm). Phần cơ chế liên kết rác tính mức khuếch đại của cụm này; phần TrustRank và Spam Mass dùng đánh giá bên ngoài đồ thị để hạn chế tác động đó. Hạn chế thứ ba là PageRank chỉ có một chiều quan trọng: trang danh sách học phần có giá trị vì dẫn tới các trang học phần, còn trang học phần có giá trị vì chứa nội dung. HITS gán mỗi trang hai điểm cho hai vai trò này. Ba yêu cầu có thể cùng xuất hiện trong một hệ thống; phép tính và ý nghĩa đầu ra của chúng vẫn khác nhau. Hai yêu cầu đầu dùng lại phép lặp PageRank với ma trận $M_0$ của Bài 03; HITS dùng cùng đồ thị nhưng cộng điểm theo cạnh.
<!-- public-notes:end -->

**Quyết định duyệt trang 01/10/2026:** sửa. Hai yêu cầu liên kết rác và hai vai trò trước đây thiếu động cơ, cụm “tập trang tin cậy” xuất hiện trước khái niệm và câu kết tối nghĩa. Bảng mới đặt hạn chế của PageRank toàn cục cạnh yêu cầu, theo MMDS §5.3.1, §5.4.1 (spam farm) và §5.5.1 (một chiều quan trọng); bỏ “tập trang tin cậy”; ghi chú ánh xạ từng hạn chế sang phần tương ứng.

### lec04-s01-06 — Kiểm tra chiều truyền điểm

**Vai trò, mục tiêu, đầu vào và sản phẩm:** Kiểm tra tiên quyết; MT1. Đầu vào: quy tắc chia đều PageRank Bài 03. Sản phẩm: tính đúng đóng góp theo một cạnh.

**Luận điểm trung tâm:** PageRank chia tại trang nguồn và cộng tại trang đích.

**Nội dung hiển thị dự kiến:**

<!-- public-slide:start -->
Trên đồ thị Hình 5.15: A trỏ tới B, C, D; B trỏ tới A, D; C trỏ tới A; D trỏ tới B, C.

Giả sử $r_A=r_B=r_C=r_D=1/4$ và $\beta=4/5$.

**Câu hỏi:** Tính phần điểm theo liên kết mà B chuyển tới A. Xác định phần tử tương ứng trong ma trận $M_0$ với quy ước cột là trang nguồn.
<!-- public-slide:end -->

**Bố cục đã chọn:** G4 ở trái 45%, dữ kiện và hai yêu cầu ở phải 55%; cạnh B→A có nhãn bậc ra của B. Không đặt đáp án trên hình.

**Trọng tâm và thứ tự đọc:** Đọc B có hai cạnh ra, theo cạnh B→A, rồi liên hệ hàng A/cột B.

**Lý do phù hợp sinh viên năm 2:** Phép tính dùng kiến thức cũ và số nhỏ; tách một đóng góp khỏi toàn bộ điểm mới để phát hiện nhầm dòng/cột.

**Giới hạn bố cục và phân chia nội dung:** Giữ toàn bộ tám cạnh nhìn được; chỉ yêu cầu một đóng góp. Không tính vector chủ đề chưa học.

**Ví dụ, phiếu số và hình thức hóa:** VD1: giữ G4, dùng khởi tạo đều của Bài 03; $(M_0)_{AB}$ và đóng góp $\beta r_B/d_B$.

**Kết nối vào–ra:** Chiều truyền PageRank đã xác nhận → thay phân phối dịch chuyển ở S02.

**Nguồn và vị trí:** NG1 Hình 5.15, tr.197; quy tắc PageRank §5.1.2; NG5 ký hiệu đã học.

**Thời lượng:** 3 phút.

**Nhiệm vụ và tiêu chí nội bộ:** Slide kiểm tra riêng của phần.

- Câu hỏi/đề: Tính đóng góp B→A và xác định ô của ma trận như nội dung hiển thị.
- Đáp án/gợi ý: $1/10$; hàng A, cột B bằng $1/2$.
- Tiêu chí đánh giá: Đạt khi xác định đúng bậc ra2, nhân beta một lần và chọn hàng đích/cột nguồn. Lấy bậc ra của A hoặc đảo ô cho thấy nhầm chiều.
- Phân bổ hoạt động: Suy nghĩ1 phút, trả lời1 phút, đối chiếu1 phút; nằm trong3 phút.

**Ghi chú học thuật dự kiến:**

<!-- public-notes:start -->
B có hai liên kết ra nên $(M_0)_{AB}=1/2$. Đóng góp theo liên kết là $(4/5)(1/4)/2=1/10$. Đây chưa phải toàn bộ điểm của A vì còn các đóng góp từ trang khác và phần dịch chuyển. Bậc ra được lấy tại B là nguồn của cạnh, không lấy tại A.
<!-- public-notes:end -->

## S02. PageRank theo chủ đề

Khái niệm, thuật toán và chi phí. Nhu cầu chủ đề → thay nhánh dịch chuyển → G4/VD1 → HT1 → thuật toán, bảo toàn và tính co → kết hợp chủ đề, chi phí → kiểm tra. Bù nút cụt là cầu nối từ Bài 03; chứng minh gọi lại lập luận co, không tạo phần lý thuyết phổ. Kết quả v, r được chuyển sang TrustRank. Mỗi lần đổi trang giữ vị trí và thứ tự A–D.

Phân bổ: 13 slide, 30 phút.

### lec04-s02-01 — Dịch chuyển ưu tiên theo chủ đề

**Vai trò, mục tiêu, đầu vào và sản phẩm:** Trực giác; MT1. Đầu vào: hai nhánh di chuyển PageRank. Sản phẩm: chỉ ra thành phần thay đổi khi ưu tiên chủ đề.

**Luận điểm trung tâm:** Thiên lệch chủ đề được đưa vào nhánh dịch chuyển, không xóa các trang ngoài tập chủ đề.

**Nội dung hiển thị dự kiến:**

<!-- public-slide:start -->
Với xác suất $\beta$: đi theo một liên kết ra, chia đều giữa các liên kết.

Với xác suất $1-\beta$: dịch chuyển tới một trang trong tập chủ đề $S$.

Các trang ngoài $S$ vẫn có thể nhận điểm qua liên kết. Đồ thị liên kết được giữ nguyên.
<!-- public-slide:end -->

**Bố cục đã chọn:** Sơ đồ hai nhánh từ một trang chiếm trái 60%; hai câu giải thích và kết luận ở phải40%. Nhánh dịch chuyển dùng nét đứt và nhãn để phân biệt cạnh thật.

**Trọng tâm và thứ tự đọc:** Theo nhánh liên kết trước, nhánh dịch chuyển sau; đối chiếu đích được phép ở từng nhánh.

**Lý do phù hợp sinh viên năm 2:** Sinh viên đã biết hai nhánh của PageRank; chỉ thay tập đích của một nhánh để giảm số thành phần mới cùng lúc.

**Giới hạn bố cục và phân chia nội dung:** Không dựng thêm cạnh dịch chuyển thành dữ liệu đồ thị. Nút cụt được đặc tả ở S02-05.

**Ví dụ, phiếu số và hình thức hóa:** HT1 ở mức trực giác; $0<\beta<1$, $S\ne\varnothing$; chưa dùng ma trận mới.

**Kết nối vào–ra:** Nhu cầu chủ đề → một thay đổi trong bước nhảy; G4 cụ thể hóa ở trang sau.

**Nguồn và vị trí:** NG1 §5.3.2, tr.196/PDF22; NG3 trang8 chỉ đối chiếu hình.

**Thời lượng:** 2 phút.

**Ghi chú học thuật dự kiến:**

<!-- public-notes:start -->
Dịch chuyển đưa phần điểm mới vào các trang đại diện chủ đề. Các bước theo liên kết tiếp tục chuyển điểm tới những trang có thể tới được từ tập này. Vì vậy, tập dịch chuyển không phải tập duy nhất được phép có điểm dương. Quan hệ giữa chủ đề và các trang liên kết là giả định ý nghĩa của mô hình, không phải một phép phân loại chắc chắn.
<!-- public-notes:end -->

### lec04-s02-02 — Tập dịch chuyển trên đồ thị bốn trang

**Vai trò, mục tiêu, đầu vào và sản phẩm:** Ví dụ dẫn nhập; MT1. Đầu vào: hai nhánh di chuyển. Sản phẩm: lập vector bước nhảy từ tập S.

**Luận điểm trung tâm:** $v$ quy định phân phối đích khi dịch chuyển; $r^0=v$ chỉ là lựa chọn khởi tạo của ví dụ.

**Nội dung hiển thị dự kiến:**

<!-- public-slide:start -->
[Hình: Đồ thị G4: A tới B, C, D; B tới A, D; C tới A; D tới B, C. B và D có viền đôi và nhãn tập S.]

$\beta=4/5$, $S=\{B,D\}$; thứ tự thành phần A, B, C, D.

$v$ là phân phối chọn trang đích khi thực hiện dịch chuyển:
$$v=(0,1/2,0,1/2)^\mathsf T.$$

Khởi tạo ví dụ: $r^0=v$. Trong phép lặp, $v$ cố định, còn $r^t$ thay đổi.

Mỗi vòng thêm $(1-\beta)v$: B và D nhận $1/10$, A và C nhận $0$.
<!-- public-slide:end -->

**Bố cục đã chọn:** Đồ thị G4 ở trái45%; định nghĩa v, vector cụ thể và vai trò khởi tạo ở phải55%. Giữ nhãn B,D và thứ tự A–D.

**Trọng tâm và thứ tự đọc:** Tập S → phân phối v → khởi tạo r0 → phần thêm trong mỗi vòng.

**Lý do phù hợp sinh viên năm 2:** Nhãn chữ tách danh tính đỉnh khỏi giá trị điểm và số vòng; hai vector giúp phân biệt phân phối v với phần điểm thực sự thêm mỗi vòng.

**Giới hạn bố cục và phân chia nội dung:** Giữ một vector hiển thị; ghi phần dịch chuyển bằng lời và giá trị mỗi trang. Giải thích xác suất có điều kiện trong ghi chú.

**Ví dụ, phiếu số và hình thức hóa:** VD1; giữ số nguồn. $v$ không âm, tổng 1; $(1-\beta)v$ có tổng 1/5.

**Kết nối vào–ra:** Tập chủ đề → dữ liệu khởi tạo và điểm thêm; dùng nguyên các giá trị cho vòng 1.

**Nguồn và vị trí:** NG1 VD5.10/Hình 5.15, tr.196–197/PDF22–23.

**Thời lượng:** 2 phút.

**Ghi chú học thuật dự kiến:**

<!-- public-notes:start -->
Tập $S$ có hai phần tử, nên xác suất chọn một trang trong bước dịch chuyển là $1/2$. Xác suất thực hiện nhánh dịch chuyển là $1/5$, vì thế phần điểm thêm vào mỗi trang B, D là $1/10$. $v_i$ là xác suất chọn trang $i$ với điều kiện đã thực hiện nhánh dịch chuyển; $v$ không phải kết quả PageRank. Khởi tạo bằng $v$ là lựa chọn theo ví dụ sách; trạng thái khởi tạo $r^0$ và vector $(1-\beta)v$ được thêm mỗi vòng có vai trò khác nhau.
<!-- public-notes:end -->

### lec04-s02-03 — Vòng lặp PageRank theo chủ đề thứ nhất

**Vai trò, mục tiêu, đầu vào và sản phẩm:** Chạy tay; MT1. Đầu vào: G4, v, r0. Sản phẩm: tái tạo từng thành phần r1.

**Luận điểm trung tâm:** Mỗi điểm mới là tổng phần theo liên kết và phần dịch chuyển đúng tập.

**Nội dung hiển thị dự kiến:**

<!-- public-slide:start -->
$r^0=(0,1/2,0,1/2)^\mathsf T$, $\beta=4/5$, $S=\{B,D\}$.

| Trang | Theo liên kết $\beta(M_0r^0)_i$ | Dịch chuyển $(1-\beta)v_i$ | Điểm mới $r_i^1$ |
|---|---:|---:|---:|
| A | $1/5$ | $0$ | $1/5$ |
| B | $1/5$ | $1/10$ | $3/10$ |
| C | $1/5$ | $0$ | $1/5$ |
| D | $1/5$ | $1/10$ | $3/10$ |

Tại A: $(4/5)[(1/2)(1/2)+1\cdot0]=1/5$. Tổng điểm mới bằng 1.
<!-- public-slide:end -->

**Bố cục đã chọn:** Bảng bốn hàng chiếm75% khung giữa; vector cũ ở dải trên, phép tính tại A và tổng điểm ở dải dưới. Không đặt thêm hình nhỏ cạnh bảng.

**Trọng tâm và thứ tự đọc:** Đọc vector cũ → đóng góp qua liên kết → phần dịch chuyển → điểm mới trên cùng hàng.

**Lý do phù hợp sinh viên năm 2:** Một hàng được tính đủ giúp sinh viên tái tạo ba hàng còn lại; các cột tách nguồn điểm để tránh cộng1/10 cho mọi trang.

**Giới hạn bố cục và phân chia nội dung:** Bốn hàng và một phép tính mẫu; giải thích từng cạnh còn lại nằm trong ghi chú. Đáp số vòng 2 chưa xuất hiện.

**Ví dụ, phiếu số và hình thức hóa:** VD1 vòng0→1; HT1 với delta=0. Các cột trước–sau phân biệt trạng thái, không dùng màu làm tín hiệu duy nhất.

**Kết nối vào–ra:** Khởi tạo theo tập S → r1; r1 là đầu vào duy nhất của vòng 2.

**Nguồn và vị trí:** NG1 VD5.10, tr.197/PDF23; bảng phân rã là diễn giải phép tính nguồn.

**Thời lượng:** 2,5 phút.

**Ghi chú học thuật dự kiến:**

<!-- public-notes:start -->
Từ B, điểm $1/2$ chia cho A, D; từ D, điểm $1/2$ chia cho B, C. Vì vậy mỗi thành phần của $M_0r^0$ bằng $1/4$. Sau khi nhân $4/5$, mỗi trang có $1/5$; B, D nhận thêm $1/10$. Tổng là $1/5+3/10+1/5+3/10=1$. Nếu thay $v$ bằng phân phối đều, bốn điểm mới đều bằng $1/4$, khác phép tính theo tập dịch chuyển đã chọn.
<!-- public-notes:end -->

### lec04-s02-04 — Vết lặp và điểm cố định theo chủ đề

**Vai trò, mục tiêu, đầu vào và sản phẩm:** Chạy tay và quan sát; MT1. Đầu vào: r1. Sản phẩm: tính r2 và phân biệt một vòng với giới hạn.

**Luận điểm trung tâm:** Điểm cố định có thể ưu tiên B,D trong khi A,C ngoài tập vẫn nhận điểm dương.

**Nội dung hiển thị dự kiến:**

<!-- public-slide:start -->
Tại A ở vòng 2:
$$r_A^2=\frac45\left(\frac12\frac3{10}+\frac15\right)=\frac7{25}.$$

| Trang | $r^1$ | $r^2$ | Điểm cố định $r^*$ |
|---|---:|---:|---:|
| A | $1/5$ | $7/25$ | $9/35$ |
| B | $3/10$ | $41/150$ | $59/210$ |
| C | $1/5$ | $13/75$ | $19/105$ |
| D | $3/10$ | $41/150$ | $59/210$ |

B và D có điểm cố định lớn hơn A; các trang ngoài $S$ vẫn có điểm dương.
<!-- public-slide:end -->

**Bố cục đã chọn:** Phép tính tại A ở trên25%; bảng bốn hàng giữa60%; kết luận dưới15%. Cột điểm cố định có nhãn riêng và đường phân cách, không ám chỉ r2 đã hội tụ.

**Trọng tâm và thứ tự đọc:** Kiểm một cập nhật từ r1 → đối chiếu r2 → đọc giới hạn và thứ hạng.

**Lý do phù hợp sinh viên năm 2:** Tách giới hạn khỏi các vòng hữu hạn giúp sinh viên không coi bảng vài bước là chứng minh hội tụ; B,D hòa có nguyên nhân cấu trúc.

**Giới hạn bố cục và phân chia nội dung:** Không thêm r3 trên mặt slide; giá trị r3 và phép kiểm điểm cố định trong ghi chú.

**Ví dụ, phiếu số và hình thức hóa:** VD1 vòng 1→2 và nghiệm sách; giữ phân số thay số thập phân gần nhau.

**Kết nối vào–ra:** Vết tính cụ thể → nhu cầu một đặc tả có điều kiện dừng và lập luận hội tụ.

**Nguồn và vị trí:** NG1 VD5.10, tr.197/PDF23.

**Thời lượng:** 2,5 phút.

**Ghi chú học thuật dự kiến:**

<!-- public-notes:start -->
Tại B, $r_B^2=(4/5)[(1/3)(1/5)+(1/2)(3/10)]+1/10=41/150$; tại C không có số hạng $1/10$, nên được $13/75$. Vòng 3 là $(31/125,71/250,23/125,71/250)^\mathsf T$. Nghiệm trong cột cuối thỏa phương trình cố định và có tổng bằng $1$. Việc các vòng đầu tiến gần nghiệm là quan sát; bảo đảm hội tụ đòi hỏi lập luận cho mọi vòng lặp.
<!-- public-notes:end -->

### lec04-s02-05 — Đặc tả PageRank theo phân phối dịch chuyển

**Vai trò, mục tiêu, đầu vào và sản phẩm:** Hình thức hóa; MT1. Đầu vào: vết chạy và bù nút cụt Bài 03. Sản phẩm: xác định miền đầu vào và quy tắc tổng quát.

**Luận điểm trung tâm:** Đổi v và giữ quy ước bù đều tạo đặc tả PageRank theo chủ đề nhất quán với Bài 03.

**Nội dung hiển thị dự kiến:**

<!-- public-slide:start -->
Đầu vào: đồ thị $G=(V,E)$, $n\ge1$; phân phối $v\ge0$, $\sum_i v_i=1$; $0<\beta<1$; ngưỡng $\tau>0$ và số vòng tối đa $K\ge1$.

$$r^{t+1}=\underbrace{\beta M_0r^t}_{\text{theo liên kết}}+\underbrace{\beta\delta^t u}_{\text{bù nút cụt}}+\underbrace{(1-\beta)v}_{\text{dịch chuyển}}.$$

$u_i=1/n$; $\delta^t=\sum_{j:d_j=0}r_j^t$. Cột $j$ của $M_0$ là trang nguồn $j$.

Đầu ra: vector xấp xỉ và trạng thái đạt ngưỡng hoặc hết số vòng. Bù nút cụt vẫn phân phối đều như Bài 03.
<!-- public-slide:end -->

**Bố cục đã chọn:** Đầu vào thành dải trên25%; công thức ba số hạng giữa45%; ký hiệu và đầu ra dưới30%. Dùng một công thức trung tâm, không thêm ma trận số.

**Trọng tâm và thứ tự đọc:** Chốt miền đầu vào → đọc ba nguồn điểm → xác định đầu ra và quy ước bù.

**Lý do phù hợp sinh viên năm 2:** Ba số hạng nối trực tiếp với hai nhánh quen thuộc và trường hợp nút cụt; giữ bù đều tránh thay hai thành phần mô hình cùng lúc.

**Giới hạn bố cục và phân chia nội dung:** Không đưa chứng minh tại trang đặc tả; chi tiết M0 cột0 và tập S đều trong ghi chú.

**Ví dụ, phiếu số và hình thức hóa:** HT1. Ví dụ VD1 có delta=0; v tổng quát bao gồm v đều trên S. Nguồn cầu nối NG5 được công khai.

**Kết nối vào–ra:** Ví dụ không nút cụt → quy tắc cho đồ thị tổng quát → giả mã áp dụng nguyên quy tắc.

**Nguồn và vị trí:** NG1 §5.3.2, tr.196; NG1 §5.1.5; NG5 quy ước bù nút cụt. Phần bù là cầu nối đã duyệt.

**Thời lượng:** 3 phút.

**Ghi chú học thuật dự kiến:**

<!-- public-notes:start -->
Với $d_j>0$, $(M_0)_{ij}=1/d_j$ nếu có cạnh $j\to i$; cột nút cụt bằng $0$. Điểm bị thiếu trong nhánh theo liên kết là $\beta$ lần tổng điểm nút cụt, được bù đều bằng $u$. Phân phối $v$ chỉ điều khiển nhánh dịch chuyển. Khi $S$ không rỗng và chọn đều trên $S$, $v_i=1/|S|$ trên $S$ và bằng $0$ bên ngoài. Đồ thị, $\beta$, $v$ và quy tắc bù được giữ cố định suốt phép lặp.
<!-- public-notes:end -->

### lec04-s02-06 — Thuật toán lặp PageRank theo chủ đề

**Vai trò, mục tiêu, đầu vào và sản phẩm:** Thuật toán; MT1. Đầu vào: HT1 và danh sách kề. Sản phẩm: theo dõi cập nhật đồng thời và điều kiện trả kết quả.

**Luận điểm trung tâm:** Cập nhật dùng một vector cũ chung và trả trạng thái dừng rõ ràng.

**Nội dung hiển thị dự kiến:**

<!-- public-slide:start -->
```text
r ← v
với t = 0, ..., K - 1:
    delta ← tổng r[j] trên các nút cụt
    với mỗi i: new[i] ← beta * delta / n + (1 - beta) * v[i]
    với mỗi j có d[j] > 0:
        với mỗi i thuộc out[j]:
            new[i] ← new[i] + beta * r[j] / d[j]
    Delta ← tổng |new[i] - r[i]|
    r ← new
    nếu Delta ≤ tau: trả về (r, đạt ngưỡng)
trả về (r, hết số vòng)
```

Mọi đóng góp trong một vòng dùng cùng vector điểm cũ.
<!-- public-slide:end -->

**Bố cục đã chọn:** Khối giả mã chiếm85% khung, câu bất biến đọc–ghi ở đáy15%; dùng thành phần mã chung. Hai tên r/new luôn giữ nguyên.

**Trọng tâm và thứ tự đọc:** Đọc khởi tạo → phần bù và dịch chuyển → cạnh → phép đo thay đổi → thay vector và trả trạng thái.

**Lý do phù hợp sinh viên năm 2:** Giả mã tách r và new phù hợp kiến thức mảng/vòng lặp năm2; sinh viên thấy rõ lúc nào dữ liệu mới được phép trở thành dữ liệu cũ.

**Giới hạn bố cục và phân chia nội dung:** Giữ11 dòng điều khiển như trên; giả thiết đầu vào tham chiếu ngay trang trước, không thêm mã framework.

**Ví dụ, phiếu số và hình thức hóa:** HT1; VD1 là phép chạy của cùng thuật toán. K nguyên dương; tau dương. Ký hiệu Latin trong giả mã tương ứng ký hiệu toán đã định nghĩa.

**Kết nối vào–ra:** Phương trình cập nhật → thứ tự thực thi → bất biến cần chứng minh.

**Nguồn và vị trí:** NG1 §5.3.2, tr.196–197; giả mã cụ thể hóa phép lặp nguồn và quy ước NG5.

**Thời lượng:** 3 phút.

**Ghi chú học thuật dự kiến:**

<!-- public-notes:start -->
Vector `new` được khởi tạo bằng phần bù và phần dịch chuyển, không phụ thuộc từng cạnh. Mỗi cạnh $j\to i$ cộng một phần điểm cũ của $j$, nên tổng đóng góp không phụ thuộc thứ tự duyệt cạnh trong số học chính xác. Sau khi hoàn tất tất cả các đỉnh, `Delta` đo chênh lệch theo tổng trị tuyệt đối. Nếu hết $K$ vòng mà chưa đạt $\tau$, vector hiện tại vẫn là đầu ra tính được, nhưng trạng thái không xác nhận tiêu chí dừng đã đạt.
<!-- public-notes:end -->

### lec04-s02-07 — Bảo toàn phân phối điểm

**Vai trò, mục tiêu, đầu vào và sản phẩm:** Lập luận đúng; MT1. Đầu vào: HT1. Sản phẩm: chứng minh điểm không âm và tổng 1 sau mỗi vòng.

**Luận điểm trung tâm:** Ba nguồn điểm bảo toàn tính không âm và tổng 1 qua mọi vòng.

**Nội dung hiển thị dự kiến:**

<!-- public-slide:start -->
Giả sử $r^t\ge0$ và $\sum_i r_i^t=1$.

| Thành phần | Tổng điểm đóng góp |
|---|---:|
| Theo cạnh từ các trang không cụt | $\beta(1-\delta^t)$ |
| Bù nút cụt | $\beta\delta^t$ |
| Dịch chuyển theo $v$ | $1-\beta$ |

$$\sum_i r_i^{t+1}=\beta(1-\delta^t)+\beta\delta^t+(1-\beta)=1.$$

Mọi số hạng đều không âm. Khởi tạo $r^0=v$ thỏa giả thiết.
<!-- public-slide:end -->

**Bố cục đã chọn:** Giả thiết ở trên20%; bảng ba dòng giữa50%; phép cộng và kết luận dưới30%. Ba nhãn trùng với HT1.

**Trọng tâm và thứ tự đọc:** Đọc giả thiết → đếm từng nguồn điểm → cộng tổng → kiểm cơ sở r0.

**Lý do phù hợp sinh viên năm 2:** Phép chứng minh dùng tổng hữu hạn và xác suất cơ bản; bảng giúp truy nguyên từng số hạng thay vì ghi một kết luận bảo toàn không có lý do.

**Giới hạn bố cục và phân chia nội dung:** Chỉ chứng minh bảo toàn; không gọi bảo toàn là hội tụ. Phép kiểm số VD1 ở ghi chú.

**Ví dụ, phiếu số và hình thức hóa:** HT2 phần bất biến; VD1 tổng mỗi vòng bằng 1 là phép kiểm độc lập, không thay chứng minh.

**Kết nối vào–ra:** Thuật toán → bất biến ở mọi vòng; tính co tiếp tục giải thích giới hạn.

**Nguồn và vị trí:** NG1 §5.3.2 cùng mô hình §5.1.5; chứng minh từ quy tắc cập nhật đã duyệt, không trích nguyên sách.

**Thời lượng:** 2,5 phút.

**Ghi chú học thuật dự kiến:**

<!-- public-notes:start -->
Một trang không cụt chia đều điểm cho đúng $d_j$ cạnh ra, nên tổng phần điểm của trang ấy sau khi nhân $\beta$ là $\beta r_j^t$. Cộng trên mọi trang không cụt được $\beta(1-\delta^t)$. Các nút cụt trả lại $\beta\delta^t$ bằng bù đều; phân phối $v$ có tổng bằng $1$ nhận phần $1-\beta$. Mọi hệ số đều không âm và cơ sở $r^0=v$ thỏa giả thiết, hoàn thành lập luận quy nạp. Bất biến chỉ xác nhận mỗi trạng thái là phân phối hợp lệ; chưa xác nhận dãy có giới hạn.
<!-- public-notes:end -->

### lec04-s02-08 — Tính co và sai số dừng

**Vai trò, mục tiêu, đầu vào và sản phẩm:** Hội tụ và điều kiện dừng; MT1. Đầu vào: HT2 và chuẩn1. Sản phẩm: phân biệt Delta với sai số nghiệm, nêu cơ sở duy nhất.

**Luận điểm trung tâm:** Tính co bảo đảm nghiệm duy nhất và chặn sai số tới nghiệm theo chênh lệch hai vòng bằng một hệ số xác định.

**Nội dung hiển thị dự kiến:**

<!-- public-slide:start -->
$\bar M$ là ma trận đã thay mỗi cột nút cụt bằng $u$; mọi phần tử không âm và mỗi cột có tổng bằng $1$.

Với $F(r)=\beta\bar Mr+(1-\beta)v$ và $0<\beta<1$, tính co $\|F(p)-F(q)\|_1\le\beta\|p-q\|_1$ bảo đảm điểm cố định duy nhất $r^*$.

Đặt $\Delta=\|r^{t+1}-r^t\|_1$. Sai số của vector mới thỏa
$$\|r^{t+1}-r^*\|_1\le\beta\Delta+\beta^2\Delta+\cdots=\frac{\beta}{1-\beta}\Delta.$$

Với $\beta=4/5$, cận sai số là $4\Delta$.
<!-- public-slide:end -->

**Bố cục đã chọn:** Giả thiết về ma trận và một dòng nhắc tính co ở dải trên 30%; định nghĩa độ thay đổi và tổng đuôi cấp số nhân ở giữa 50%; ví dụ hệ số 4 ở dải dưới 20%. Cận sai số của vector mới là công thức trung tâm.

**Trọng tâm và thứ tự đọc:** Nhận lại giả thiết ma trận đã bù → nhắc kết quả co của Bài 03 → theo các sai khác trong tổng đuôi → đọc cận sai số của vector mới.

**Lý do phù hợp sinh viên năm 2:** Tính co đã có ở Bài 03; tổng đuôi cấp số nhân làm hiện bước mới nối độ thay đổi với sai số nghiệm. Ví dụ beta bằng 4/5 phân biệt hai đại lượng mà không thêm một phép tính dài.

**Giới hạn bố cục và phân chia nội dung:** Mặt slide tập trung cận dừng trong 3 phút. Vector chỉ báo nút cụt và chứng minh co, tồn tại, duy nhất nằm trong ghi chú; không mở phần lý thuyết điểm cố định hoặc phổ mới.

**Ví dụ, phiếu số và hình thức hóa:** HT2. Chuẩn1 là tổng trị tuyệt đối; v có thể có thành phần0. Phiếu VD1 cung cấp beta, không tạo ngưỡng thực nghiệm.

**Kết nối vào–ra:** Bảo toàn miền phân phối → co và điểm cố định → có thể kết hợp các vector chủ đề cùng mô hình.

**Nguồn và vị trí:** NG1 §5.3.2; NG5 lập luận co kế thừa. Bất đẳng thức và cận đuôi là diễn giải toán học bổ sung đã duyệt.

**Thời lượng:** 2,5 phút.

**Ghi chú học thuật dự kiến:**

<!-- public-notes:start -->
Đặt $z_j=1$ nếu $j$ là nút cụt và $z_j=0$ nếu không. Khi đó $\bar M=M_0+uz^\mathsf T$ không âm và có tổng mỗi cột bằng $1$. Lập luận co kế thừa Bài 03: vector dịch chuyển cố định triệt tiêu trong $F(p)-F(q)$. Bất đẳng thức tam giác và việc đổi thứ tự tổng cho
$$\|F(p)-F(q)\|_1\le\beta\sum_j|p_j-q_j|\sum_i\bar M_{ij}=\beta\|p-q\|_1.$$
Các sai khác liên tiếp giảm theo cấp số nhân. Tổng khoảng cách từ một vòng tới mọi vòng sau hữu hạn và phần đuôi tiến về $0$, nên dãy hội tụ. Tính liên tục của $F$ cho phương trình cố định. Nếu hai điểm cố định cách nhau một khoảng $D$, thì $D\le\beta D$; vì $\beta<1$, suy ra $D=0$.

Với $\Delta=\|r^{t+1}-r^t\|_1$, sai khác kế tiếp không quá $\beta\Delta$. Tổng phần đuôi các sai khác sau vector mới $r^{t+1}$ không quá $\beta\Delta/(1-\beta)$. Để cận sai số không quá $\varepsilon>0$, đủ chọn $\tau\le(1-\beta)\varepsilon/\beta$ và dừng khi $\Delta\le\tau$.
<!-- public-notes:end -->

### lec04-s02-09 — Các vector điểm theo chủ đề

**Vai trò, mục tiêu, đầu vào và sản phẩm:** Định nghĩa và cầu nối; MT1, MT5. Đầu vào: điểm cố định theo v. Sản phẩm: phân biệt nhãn chủ đề j, chỉ số vòng t, đầu vào v^(j), nghiệm r^(j) và trọng số w_j.

**Luận điểm trung tâm:** Mỗi chủ đề có một phân phối dịch chuyển đầu vào và một vector PageRank hội tụ trên cùng n trang.

**Nội dung hiển thị dự kiến:**

<!-- public-slide:start -->
Có $k$ chủ đề; $j=1,\ldots,k$ là chỉ số chủ đề, $t$ là chỉ số vòng lặp.

| Ký hiệu | Vai trò |
| --- | --- |
| $v^{(j)}\in\mathbb R^n$ | Phân phối dịch chuyển đầu vào của chủ đề $j$ |
| $r^{(j)}\in\mathbb R^n$ | Vector PageRank hội tụ của chủ đề $j$ trên $n$ trang |
| $w_j\ge0$, $\sum_jw_j=1$ | Trọng số chủ đề trong ngữ cảnh truy vấn |

Mỗi chủ đề dùng cùng $\bar M$ và $\beta$:
$$r^{(j)}=\beta\bar Mr^{(j)}+(1-\beta)v^{(j)}.$$
<!-- public-slide:end -->

**Bố cục đã chọn:** Dòng phân biệt j và t ở trên; bảng ba hàng ở giữa; phương trình cố định ở dưới. Không dùng hình tổng trước khi định nghĩa các vector.

**Trọng tâm và thứ tự đọc:** Chỉ số chủ đề → đầu vào → kết quả → trọng số → phương trình riêng từng chủ đề.

**Lý do phù hợp sinh viên năm 2:** Bảng đối chiếu đầu vào và kết quả ngăn nhầm các vector cùng kích thước; tách j khỏi t trước công thức tổng.

**Giới hạn bố cục và phân chia nội dung:** Phép cộng các phương trình chuyển sang trang kế tiếp. Không thêm ví dụ số.

**Ví dụ, phiếu số và hình thức hóa:** HT3; k chủ đề, n trang, j chỉ số chủ đề; cùng Mbar và beta.

**Kết nối vào–ra:** Nghiệm duy nhất theo v → các nghiệm theo chủ đề → tổng có trọng số.

**Nguồn và vị trí:** NG1 §5.3.2 tr.196; §5.3.4 tr.199/PDF25.

**Thời lượng:** 1 phút.

**Ghi chú học thuật dự kiến:**

<!-- public-notes:start -->
Chủ đề $j$ được xác định bằng phân phối dịch chuyển $v^{(j)}$. Phép lặp PageRank với đầu vào này cho vector hội tụ $r^{(j)}$; thành phần $r_i^{(j)}$ là điểm của trang $i$ theo chủ đề $j$. Cả hai vector đều có $n$ thành phần, nhưng một vector là đầu vào, một vector là kết quả. Dấu ngoặc trong chỉ số $(j)$ phân biệt nhãn chủ đề với chỉ số vòng $t$ của $r^t$.

Các trọng số $w_j$ biểu diễn mức quan tâm tới các chủ đề. Chúng không âm và có tổng bằng $1$. Điều kiện cùng $\bar M$ bao gồm cùng đồ thị và cùng quy tắc bù nút cụt. Cùng $\beta$ giữ hệ số truyền theo liên kết không đổi. Các điều kiện này cho phép kết hợp các kết quả theo trọng số.
<!-- public-notes:end -->

### lec04-s02-09a — Kết hợp các vector chủ đề

**Vai trò, mục tiêu, đầu vào và sản phẩm:** Lập luận và ứng dụng; MT1, MT5. Đầu vào: các đại lượng của S02-09 và tính duy nhất. Sản phẩm: chứng minh đẳng thức ghép và nêu đủ điều kiện.

**Luận điểm trung tâm:** Cùng toán tử và beta cho phép ghép các nghiệm PageRank theo trọng số của phân phối dịch chuyển.

**Nội dung hiển thị dự kiến:**

<!-- public-slide:start -->
Giữ cùng $\bar M$, $\beta$; $w_j\ge0$ và $\sum_jw_j=1$.

$$v=\sum_{j=1}^k w_jv^{(j)}\quad\Longrightarrow\quad r^*=\sum_{j=1}^k w_jr^{(j)}.$$

Nhân phương trình của chủ đề $j$ với $w_j$, rồi cộng:

$$\sum_jw_jr^{(j)}=\beta\bar M\sum_jw_jr^{(j)}+(1-\beta)\sum_jw_jv^{(j)}.$$

Tổng có trọng số thỏa phương trình PageRank với $v$. Tính duy nhất xác định đó là nghiệm $r^*$.
<!-- public-slide:end -->

**Bố cục đã chọn:** Giả thiết ở trên; công thức ghép lớn giữa; một dòng cộng phương trình và kết luận duy nhất ở dưới.

**Trọng tâm và thứ tự đọc:** Điều kiện chung → cặp tổng → phương trình của tổng → tính duy nhất.

**Lý do phù hợp sinh viên năm 2:** Phép phân phối ma trận qua tổng dùng đại số tuyến tính đã học; các vector đã được định nghĩa ở trang trước.

**Giới hạn bố cục và phân chia nội dung:** Mặt trang chỉ chứng minh cho nghiệm hội tụ. Sai số tổng ghép các xấp xỉ thuộc ghi chú.

**Ví dụ, phiếu số và hình thức hóa:** HT3; giữ w không âm, tổng1; không đưa tỷ lệ số tự tạo.

**Kết nối vào–ra:** Các nghiệm riêng → nghiệm cho ngữ cảnh ghép → chi phí tiền tính và chi phí truy vấn.

**Nguồn và vị trí:** NG1 §5.3.2 tr.196; §5.3.4 tr.199/PDF25; diễn giải đại số từ phương trình cố định.

**Thời lượng:** 2 phút.

**Ghi chú học thuật dự kiến:**

<!-- public-notes:start -->
Đặt $q=\sum_jw_jr^{(j)}$. Mỗi $r^{(j)}$ thỏa phương trình cố định của chủ đề tương ứng. Nhân với $w_j$ rồi cộng cho $q=\beta\bar Mq+(1-\beta)v$, với $v=\sum_jw_jv^{(j)}$. Vì mọi trọng số không âm và có tổng bằng $1$, cả $q$ và $v$ đều là phân phối xác suất. Tính duy nhất của điểm cố định suy ra $q=r^*$.

Đẳng thức này áp dụng cho các nghiệm hội tụ. Khi lưu các xấp xỉ $\hat r^{(j)}$, tổng ghép cũng là xấp xỉ; sai số thỏa $\|\sum_jw_j\hat r^{(j)}-r^*\|_1\le\sum_jw_j\|\hat r^{(j)}-r^{(j)}\|_1$. Nếu đổi $\beta$ hoặc cách bù nút cụt theo chủ đề, không thể dùng chung toán tử trong phép chứng minh này. Khi các điều kiện được giữ nguyên, xử lý truy vấn chỉ cần ghép các điểm đã tiền tính.
<!-- public-notes:end -->


### lec04-s02-10 — Chi phí tính và lưu các vector chủ đề

**Vai trò, mục tiêu, đầu vào và sản phẩm:** Đánh giá chi phí; MT5. Đầu vào: giả mã HT1 và ghép HT3. Sản phẩm: truy nguyên số hạng thời gian và bộ nhớ.

**Luận điểm trung tâm:** Chi phí mỗi vòng tuyến tính theo đỉnh/cạnh, còn lưu các kết quả tăng theo số chủ đề.

**Nội dung hiển thị dự kiến:**

<!-- public-slide:start -->
Mô hình: phép toán vô hướng chi phí đơn vị; $n$ đỉnh, $\ell$ cạnh, danh sách kề.

| Công việc | Số đối tượng mỗi vòng |
| --- | --- |
| Cộng điểm theo liên kết | $\ell$ cạnh |
| Bù, dịch chuyển, so sánh | Số lượt cố định trên $n$ đỉnh |

Một vector: mỗi vòng $\Theta(n+\ell)$; chạy đủ $K$ vòng cần $\Theta(K(n+\ell))$.

Bộ nhớ đầu vào $\Theta(n+\ell)$; bộ nhớ phụ $\Theta(n)$. Lưu $k$ kết quả $r^{(j)}$ cần $\Theta(kn)$ số. Ghép điểm trên tập ứng viên $C$, $c=|C|$: $\Theta(kc)$ phép nhân–cộng, chưa gồm sắp xếp.
<!-- public-slide:end -->

**Bố cục đã chọn:** Mô hình trên20%, bảng hai hàng giữa35%, hai khối kết quả thời gian/bộ nhớ dưới45%. Không đặt đồ thị hoặc giả mã đầy đủ ở cùng trang.

**Trọng tâm và thứ tự đọc:** Đọc đơn vị → truy hai bước giả mã → cộng → phân biệt chi phí một vector với lưu k kết quả.

**Lý do phù hợp sinh viên năm 2:** Phép đếm theo cạnh phù hợp nền phân tích thuật toán; tách đầu vào/phụ/đầu ra ngăn gộp bộ nhớ sai.

**Giới hạn bố cục và phân chia nội dung:** C là tập ứng viên, c=|C|. Mặt trang nêu lưu trữ và ghép chưa gồm sắp xếp; ghi chú tách tìm ứng viên, chọn trọng số, ghép và sắp xếp.

**Ví dụ, phiếu số và hình thức hóa:** HT3, VD1 có n4/ell8 chỉ đối chiếu vai trò, không coi là dữ liệu hiệu năng.

**Kết nối vào–ra:** Giả mã và ghép vector → giới hạn tài nguyên của tình huống mở đầu → quy trình sử dụng.

**Nguồn và vị trí:** NG1 §5.2.1 tr.191–192; §5.3.2–5.3.4 tr.196–199. Phép đếm từ HT1/HT3.

**Thời lượng:** 2 phút.

**Ghi chú học thuật dự kiến:**

<!-- public-notes:start -->
Mỗi cạnh tạo đúng một đóng góp; các bước khởi tạo vector, cộng bù và đo $\Delta$ duyệt mỗi đỉnh một số lần không phụ thuộc kích thước. Danh sách kề lưu đỉnh và cạnh, còn các vector $r$, $v$ cùng vector điểm mới cần bộ nhớ tuyến tính theo $n$.

Nếu chủ đề $j$ thực chạy $K_j$ vòng, tiền tính độc lập $k$ vector cần $\Theta((\sum_{j=1}^kK_j)(n+\ell))$ phép toán. Giới hạn tối đa $K$ vòng cho mỗi vector cho cận $O(kK(n+\ell))$. Nếu mọi vector đều chạy đủ $K$ vòng thì chi phí là $\Theta(kK(n+\ell))$. Tính tuần tự tiết kiệm trạng thái lặp trong bộ nhớ nhưng vẫn phải thực hiện phép lặp cho từng chủ đề.

Lưu $k$ kết quả $r^{(j)}$ cần $kn$ số. Tại truy vấn, xác định các trọng số $w_j$ và tập ứng viên $C$, $c=|C|$. Với mỗi $i\in C$, tính $r_i^*=\sum_jw_jr_i^{(j)}$ từ điểm đã lưu; không lặp PageRank. Ghép điểm cho $c$ ứng viên cần $k$ đóng góp mỗi ứng viên, tức $\Theta(kc)$ phép nhân–cộng. Chi phí này không bao gồm tìm ứng viên, xác định trọng số chủ đề hoặc sắp xếp kết quả. Không cần tạo toàn bộ vector ghép trên $n$ trang nếu chỉ xếp hạng $C$.
<!-- public-notes:end -->

### lec04-s02-11 — Sử dụng điểm đã lưu khi có truy vấn

**Vai trò, mục tiêu, đầu vào và sản phẩm:** Ứng dụng và thu hồi tình huống; MT1, MT5. Đầu vào: k vector và chi phí. Sản phẩm: phân biệt tiền tính với xử lý truy vấn.

**Luận điểm trung tâm:** Vector chủ đề được tiền tính và dùng lại khi người dùng chọn ngữ cảnh truy vấn.

**Nội dung hiển thị dự kiến:**

<!-- public-slide:start -->
**Trước truy vấn**

Chọn các phân phối $v^{(j)}$.

Tính và lưu các vector $r^{(j)}$ trên toàn bộ $n$ trang.

**Khi có truy vấn**

Xác định $w_j$ theo ngữ cảnh và tập trang ứng viên $C$.

Với từng $i\in C$, tính:

$$r_i^*=\sum_{j=1}^k w_jr_i^{(j)}.$$

Ghép các điểm đã lưu, không lặp lại PageRank. Chỉ cần điểm của các trang trong $C$.

Truy vấn “jaguar” có trọng số chủ đề động vật và ô tô khác nhau theo ngữ cảnh.
<!-- public-slide:end -->

**Bố cục đã chọn:** Hai thẻ bằng nhau: tiền tính bên trái, truy vấn bên phải; công thức theo thành phần i trong C đặt ở thẻ phải. Dòng dưới thu hồi ngữ cảnh jaguar.

**Trọng tâm và thứ tự đọc:** Đọc các vector đã lưu → xác định trọng số và ứng viên → lấy từng điểm và cộng → giới hạn công việc.

**Lý do phù hợp sinh viên năm 2:** Hai hàng phân biệt tính toán dùng lại với thao tác theo ngữ cảnh, nối trực tiếp giới hạn bộ nhớ ở mở đầu.

**Giới hạn bố cục và phân chia nội dung:** Không dùng sơ đồ SVG cũ để tránh lặp chữ; không tạo ví dụ trọng số số học. Sắp xếp và xác định ứng viên nằm ngoài phép ghép.

**Ví dụ, phiếu số và hình thức hóa:** HT3 ở mức sử dụng; ví dụ định tính jaguar của NG1, không có điểm mới.

**Kết nối vào–ra:** Chi phí tiền tính → thao tác trả lời truy vấn → kiểm khả năng phân biệt đồ thị và bước nhảy.

**Nguồn và vị trí:** NG1 §5.3.1–5.3.4 tr.195–199; đặc biệt phép ghép theo tỷ lệ ở §5.3.4 tr.199.

**Thời lượng:** 2 phút.

**Ghi chú học thuật dự kiến:**

<!-- public-notes:start -->
Giai đoạn tiền tính chọn chủ đề và các phân phối dịch chuyển, sau đó chạy PageRank để lưu các vector điểm. Mỗi vector chứa điểm của toàn bộ $n$ trang theo một chủ đề. Tại truy vấn, người dùng có thể chọn chủ đề hoặc cung cấp trọng số quan tâm; cách suy ra chủ đề tự động nằm ngoài phạm vi phép tính này.

Gọi $C$ là tập trang ứng viên đã được xác định, $c=|C|$. Với mỗi trang $i\in C$, lấy $k$ điểm $r_i^{(j)}$ đã lưu, nhân từng điểm với $w_j$ và cộng. Phép ghép cần $\Theta(kc)$ phép nhân–cộng, không cần một phép lặp PageRank mới và không cần dựng vector dài $n$ nếu chỉ dùng các điểm trong $C$. Tìm ứng viên, xác định trọng số và sắp xếp kết quả là các công việc riêng. Ví dụ “jaguar” chỉ minh họa hai ngữ cảnh, không ấn định trọng số số học.
<!-- public-notes:end -->

### lec04-s02-12 — Kiểm tra phép cập nhật theo chủ đề

**Vai trò, mục tiêu, đầu vào và sản phẩm:** Kiểm tra riêng S02; MT1. Đầu vào: HT1 và VD1. Sản phẩm: tính điểm ngoài tập dịch chuyển, giải thích ý nghĩa S.

**Luận điểm trung tâm:** Một trang ngoài tập dịch chuyển vẫn nhận điểm từ các liên kết vào.

**Nội dung hiển thị dự kiến:**

<!-- public-slide:start -->
G4: A→B,C,D; B→A,D; C→A; D→B,C.

$\beta=4/5$, $S=\{B,D\}$, $r^1=(1/5,3/10,1/5,3/10)^\mathsf T$.

**Câu hỏi:**
1. Tính $r_C^2$ và chỉ rõ các trang đóng góp.
2. Xác định tính đúng sai của mệnh đề: “Một trang ngoài $S$ luôn có điểm bằng 0”. Giải thích bằng dữ kiện trên.
<!-- public-slide:end -->

**Bố cục đã chọn:** Đồ thị trái45%; vector cũ, tham số và hai yêu cầu phải55%. Dòng điểm C chưa điền trên mặt slide.

**Trọng tâm và thứ tự đọc:** Theo các cạnh vào C → đọc điểm nguồn trong r1 → quyết định phần dịch chuyển của C.

**Lý do phù hợp sinh viên năm 2:** Yêu cầu tập trung một thành phần nhưng đồng thời đo chiều cạnh, chia bậc ra và ranh giới tập dịch chuyển.

**Giới hạn bố cục và phân chia nội dung:** Hai câu, không yêu cầu giải cả hệ. Đáp án và phép so sánh nằm trong ghi chú.

**Ví dụ, phiếu số và hình thức hóa:** VD1 r1→r2; HT1; mọi dữ kiện nguồn hiện đủ để tính lại.

**Kết nối vào–ra:** Phép cập nhật đã hoàn chỉnh → khả năng đồ thị liên kết bị xây có chủ đích để thay điểm.

**Nguồn và vị trí:** NG1 VD5.10, tr.197; câu hỏi áp dụng trực tiếp đúng dữ kiện ví dụ.

**Thời lượng:** 3 phút.

**Nhiệm vụ và tiêu chí nội bộ:** Slide kiểm tra riêng của phần.

- Câu hỏi/đề: Hai yêu cầu như nội dung hiển thị, trên toàn bộ dữ kiện G4 và r1.
- Đáp án/gợi ý: $r_C^2=13/75$; đóng góp từ A,D. Mệnh đề sai.
- Tiêu chí đánh giá: Đúng hai nguồn, đúng bậc ra3 và2, không cộng1/10 vào C; giải thích S điều khiển dịch chuyển. Chỉ bác mệnh đề không có phép tính chưa đạt đầy đủ.
- Phân bổ hoạt động: Tính và lập luận1,5 phút; trả lời0,5 phút; đối chiếu1 phút; tổng3 phút.

**Ghi chú học thuật dự kiến:**

<!-- public-notes:start -->
C nhận từ A và D. Phần theo liên kết là $(4/5)[(1/3)(1/5)+(1/2)(3/10)]=13/75$; C không nhận trực tiếp phần dịch chuyển. Mệnh đề điểm bằng $0$ là sai: điểm dương tới C qua cạnh. Tập $S$ chỉ xác định nơi nhận phần $1-\beta$; không xóa các cạnh hoặc loại đỉnh ngoài $S$ khỏi không gian trạng thái.
<!-- public-notes:end -->

## S03. Cơ chế liên kết rác

Mô hình và phân tích. Liên kết có thể bị thao túng → ba vùng quyền tác động → điểm một hỗ trợ → ba nguồn điểm đích → giải phương trình và phân biệt xấp xỉ → giới hạn, kiểm tra. Đây là phân tích mô hình cân bằng, không có thuật toán thực thi riêng; giả mã không áp dụng. Đếm trang/cạnh và các giả thiết thay cho một phân tích thời gian không có đối tượng. Đầu ra là nhu cầu bổ sung thông tin tin cậy.

Phân bổ: 8 slide, 20 phút.

### lec04-s03-01 — Liên kết rác và điểm xếp hạng

**Vai trò, mục tiêu, đầu vào và sản phẩm:** Tình huống và vấn đề; MT2. Đầu vào: điểm phụ thuộc cạnh. Sản phẩm: xác định mục tiêu và quyền tác động của người tạo liên kết rác.

**Luận điểm trung tâm:** Liên kết có thể được tạo để tăng điểm trang đích ngoài ý nghĩa chất lượng nội dung.

**Nội dung hiển thị dự kiến:**

<!-- public-slide:start -->
Liên kết rác được tạo để làm tăng điểm xếp hạng không tương xứng với giá trị nội dung.

Phân tích xét PageRank toàn cục với dịch chuyển đều; đối tượng bị thay đổi là các cạnh trong cụm.

Cụm thao túng tập trung PageRank tại một trang đích. Phân tích cấu trúc và các chỉ số trên đồ thị hỗ trợ xác định trang cần rà soát.
<!-- public-slide:end -->

**Bố cục đã chọn:** Định nghĩa trên25%; ba khối “Dữ liệu–Quyền tác động–Mục tiêu” ở giữa55%; câu giới hạn kiểm tra ở dưới20%. Không dùng ảnh trang rác.

**Trọng tâm và thứ tự đọc:** Đọc điều bị thao túng → dữ liệu có thể kiểm soát → đầu ra người thao túng muốn tăng.

**Lý do phù hợp sinh viên năm 2:** Sinh viên nhìn cùng đồ thị dưới giả thiết đầu vào có chủ ý đối kháng, trước khi tiếp nhận phương trình mới.

**Giới hạn bố cục và phân chia nội dung:** Không mô tả thủ thuật thao tác trên hệ thống thực; mô hình đồ thị cụ thể nằm ở trang sau. Không đưa số lượng trang rác không có nguồn.

**Ví dụ, phiếu số và hình thức hóa:** Khái niệm §5.4; không có ví dụ số hoặc giả mã riêng.

**Kết nối vào–ra:** S02 đã thay phân phối dịch chuyển; ở đây trở lại phân phối đều u và xét tác động của việc thay cạnh → kiến trúc cụm xác định các nguồn điểm cần phân tích.

**Nguồn và vị trí:** NG1 mở §5.4 và §5.4.1, tr.199–200/PDF25–26.

**Thời lượng:** 2 phút.

**Ghi chú học thuật dự kiến:**

<!-- public-notes:start -->
Giáo trình xét các kỹ thuật tạo liên kết nhằm làm PageRank đánh giá cao một trang hơn mức đóng góp nội dung. Mô hình tiếp theo tách phần web không thể tác động, phần có thể đặt liên kết và phần sở hữu. Phân tích chỉ mô tả tác động của một cấu trúc xác định; không suy rằng mọi nhóm trang liên kết dày đều là liên kết rác.
<!-- public-notes:end -->

### lec04-s03-02 — Cấu trúc cụm thao túng liên kết

**Vai trò, mục tiêu, đầu vào và sản phẩm:** Mô hình và trực giác; MT2. Đầu vào: quyền tạo/sửa cạnh. Sản phẩm: đọc đúng ba vùng và các giả thiết của Hình 5.16.

**Luận điểm trung tâm:** Ba vùng quyền tác động và cạnh nội bộ xác định mô hình phân tích cụm thao túng.

**Nội dung hiển thị dự kiến:**

<!-- public-slide:start -->
Ba nhóm trang: không tác động được; tác động được; thuộc quyền sở hữu.

Trong nhóm sở hữu, trang đích chỉ trỏ tới $m$ trang hỗ trợ; mỗi trang hỗ trợ chỉ trỏ lại đích.

Mọi liên kết từ ngoài vào cụm đều tới đích; mỗi trang hỗ trợ chỉ nhận cạnh từ đích.

Mô hình phân tích dùng đồ thị không có nút cụt; $m\ge1$, $n\ge m+1$.
<!-- public-slide:end -->

**Bố cục đã chọn:** Sơ đồ ba vùng chiếm trái65%; giả thiết thành ba dòng ngắn phải35%. Đích đặt giữa vùng sở hữu, m hỗ trợ thành cột; dấu chấm lửng có nhãn m trang.

**Trọng tâm và thứ tự đọc:** Đọc ba vùng từ trái sang phải → cạnh ngoài vào đích → cặp chiều đích–hỗ trợ.

**Lý do phù hợp sinh viên năm 2:** Ranh giới vùng tách quyền đặt cạnh với quyền sở hữu trang, cần trước khi gộp mọi đóng góp ngoài vào x.

**Giới hạn bố cục và phân chia nội dung:** Giữ nhãn m thay số trang tự đặt. Giả thiết không nút cụt phải hiện trên mặt slide. Hình chỉ ghi “Đóng góp từ ngoài”; ký hiệu $x$ và cách gộp hệ số được định nghĩa tại S03-04.

**Ví dụ, phiếu số và hình thức hóa:** VD2/Hình 5.16; miền n,m. Các cạnh ngoài vào hỗ trợ bị loại theo mô hình đã chọn.

**Kết nối vào–ra:** Mục tiêu tăng điểm → cấu trúc vòng quay điểm → điểm của một trang hỗ trợ.

**Nguồn và vị trí:** NG1 §5.4.1/Hình 5.16, tr.199–200/PDF25–26; giả thiết không nút cụt làm rõ phạm vi phép tính nguồn.

**Thời lượng:** 2 phút.

**Ghi chú học thuật dự kiến:**

<!-- public-notes:start -->
Trang tác động được không đồng nghĩa trang sở hữu: một người có thể đặt liên kết ở vị trí được phép mà không điều khiển toàn bộ trang. Mô hình dùng PageRank toàn cục với dịch chuyển đều. Các liên kết ngoài đưa điểm tới đích; đích chia điểm cho mọi hỗ trợ, và các hỗ trợ trả điểm về đích. Điều kiện toàn đồ thị không có nút cụt giữ phần dịch chuyển đều bằng $b=(1-\beta)/n$, không phát sinh số hạng bù nút cụt bổ sung.
<!-- public-notes:end -->

### lec04-s03-03 — Điểm của một trang hỗ trợ

**Vai trò, mục tiêu, đầu vào và sản phẩm:** Ví dụ ký hiệu và tính đóng góp; MT2. Đầu vào: Hình 5.16. Sản phẩm: suy ra p từ hai nguồn điểm.

**Luận điểm trung tâm:** Một hỗ trợ nhận phần điểm chia từ đích và phần dịch chuyển đều.

**Nội dung hiển thị dự kiến:**

<!-- public-slide:start -->
Ký hiệu: $y$ là điểm trang đích; $p$ là điểm mỗi trang hỗ trợ; $b=(1-\beta)/n$.

Đích có đúng $m$ liên kết ra; mỗi hỗ trợ chỉ nhận cạnh từ đích.

| Nguồn điểm tại một hỗ trợ | Đóng góp |
|---|---:|
| Điểm theo cạnh từ đích | $\beta y/m$ |
| Dịch chuyển đều | $b$ |

$$p=\frac{\beta y}{m}+b.$$

Mọi trang hỗ trợ có cùng phương trình trong mô hình này.
<!-- public-slide:end -->

**Bố cục đã chọn:** Một cặp đích–hỗ trợ lớn trái40%, bảng hai nguồn điểm và công thức phải60%. Trên cạnh ghi beta y/m; nguồn dịch chuyển dùng mũi tên nét đứt b.

**Trọng tâm và thứ tự đọc:** Theo điểm y rời đích → chia m → cộng b → gọi tổng p.

**Lý do phù hợp sinh viên năm 2:** Một hỗ trợ đại diện làm rõ mẫu số m và giữ quan hệ với phân phối đều; bảng phân biệt n tổng web với m trang hỗ trợ.

**Giới hạn bố cục và phân chia nội dung:** Không đưa phương trình y ở cùng trang. Giả thiết đồ thị không nút cụt và cạnh như S03-02 được nhắc trong ghi chú.

**Ví dụ, phiếu số và hình thức hóa:** VD2; HT4 điểm hỗ trợ. p,y là điểm; n,m là số trang; beta xác suất.

**Kết nối vào–ra:** Kiến trúc cụm → điểm một hỗ trợ → tổng điểm quay về từ m hỗ trợ.

**Nguồn và vị trí:** NG1 §5.4.2, tr.201/PDF27.

**Thời lượng:** 3 phút.

**Ghi chú học thuật dự kiến:**

<!-- public-notes:start -->
Mỗi hỗ trợ nhận cùng phần $\beta y/m$ vì đích chỉ có $m$ cạnh ra. Dịch chuyển đều đưa thêm $b$ cho mỗi trang, kể cả các hỗ trợ. Các hỗ trợ không nhận điểm theo cạnh từ bên ngoài nên không có số hạng thứ ba trong $p$. Nếu thêm cạnh ngoài vào hỗ trợ hoặc thêm cạnh ra từ đích, phương trình này phải đổi; kết quả chỉ áp dụng cho kiến trúc đã nêu.
<!-- public-notes:end -->

### lec04-s03-04 — Ba nguồn điểm tại trang đích

**Vai trò, mục tiêu, đầu vào và sản phẩm:** Gộp đóng góp; MT2. Đầu vào: p. Sản phẩm: lập y từ ngoài, hỗ trợ và dịch chuyển.

**Luận điểm trung tâm:** Điểm đích nhận ba nguồn; x đã là đóng góp theo cạnh nên không nhân beta lần nữa.

**Nội dung hiển thị dự kiến:**

<!-- public-slide:start -->
$x$ là tổng đóng góp theo các cạnh từ ngoài tới đích, đã nhân $\beta$ và chia bậc ra tại nguồn.

[Hình: Ba nhánh x, beta m p và b cùng đi vào đích có điểm y.]

| Nguồn điểm tại đích | Đóng góp |
| --- | --- |
| Liên kết từ ngoài | $x$ |
| $m$ trang hỗ trợ, mỗi trang chỉ trỏ tới đích | $\beta mp$ |
| Dịch chuyển đều tới đích | $b$ |

$$y=x+\beta mp+b.$$

Đóng góp $x$ đã bao gồm hệ số $\beta$.
<!-- public-slide:end -->

**Bố cục đã chọn:** Ba mũi tên có nhãn vào đích chiếm trái45%; bảng và phương trình phải55%. Vị trí đích/hỗ trợ khớp S03-02.

**Trọng tâm và thứ tự đọc:** Đọc định nghĩa x → cộng cùng một loại đóng góp beta p qua m hỗ trợ → cộng b tại đích.

**Lý do phù hợp sinh viên năm 2:** Ba nhánh làm rõ nơi phát sinh từng số hạng; số m xuất hiện do cộng các trang, beta xuất hiện do nhánh đi theo cạnh.

**Giới hạn bố cục và phân chia nội dung:** Mặt slide không thế p; việc thế và giải để trang sau. Chú thích x đã tính beta phải nằm cạnh nhánh ngoài.

**Ví dụ, phiếu số và hình thức hóa:** VD2; HT4 phương trình điểm đích; không có dữ kiện số mới.

**Kết nối vào–ra:** Điểm từng hỗ trợ → dòng quay lại đích → phương trình tự phụ thuộc y.

**Nguồn và vị trí:** NG1 §5.4.2, tr.201/PDF27.

**Thời lượng:** 3 phút.

**Ghi chú học thuật dự kiến:**

<!-- public-notes:start -->
Đối với một trang ngoài $j$ trỏ tới đích, đóng góp là $\beta r_j/d_j$. Đại lượng $x$ là tổng các đóng góp này, nên không nhân thêm $\beta$. Mỗi hỗ trợ chỉ có một cạnh ra, trả $\beta p$; $m$ hỗ trợ trả $\beta mp$. Phương trình đầy đủ còn có $b$ tại đích. Phương trình cân bằng dùng điểm cố định của hệ; ba số hạng không phải ba trạng thái thời gian khác nhau.
<!-- public-notes:end -->

### lec04-s03-05 — Vòng truyền điểm qua các trang hỗ trợ

**Vai trò, mục tiêu, đầu vào và sản phẩm:** Hình thức hóa và giải đại số; MT2. Đầu vào: hai phương trình p,y. Sản phẩm: giải biểu thức chính xác trong mô hình.

**Luận điểm trung tâm:** Hai bước đích → hỗ trợ → đích tạo beta²y; giải phương trình cân bằng cho hệ số1/(1-beta²).

**Nội dung hiển thị dự kiến:**

<!-- public-slide:start -->
Phần điểm bắt nguồn từ đích đi qua hai bước theo liên kết:

$$y\ \xrightarrow{\text{đích → hỗ trợ}}\ \frac{\beta y}{m}\text{ mỗi trang}\ \xrightarrow{\text{hỗ trợ → đích}}\ \beta m\frac{\beta y}{m}=\beta^2y.$$

Với $p=\beta y/m+b$ và $y=x+\beta mp+b$:

$$y=x+\beta^2y+\beta mb+b,$$
$$y=\frac{x+\beta mb+b}{1-\beta^2},\qquad b=\frac{1-\beta}{n}.$$

Hai bước tạo $\beta^2$; số hỗ trợ $m$ triệt tiêu trong phần điểm quay lại từ đích.
<!-- public-slide:end -->

**Bố cục đã chọn:** Luồng hai mũi tên bằng KaTeX ở trên; phương trình thay p và nghiệm phía dưới. Nhãn mũi tên nêu nguồn–đích, không thay bằng màu.

**Trọng tâm và thứ tự đọc:** Điểm đích → phần mỗi hỗ trợ nhận → tổng phần quay lại → phương trình cân bằng.

**Lý do phù hợp sinh viên năm 2:** Ba bước đại số không bỏ thao tác tạo beta bình phương; sinh viên thấy vòng đích–hỗ trợ gồm hai lần nhân beta.

**Giới hạn bố cục và phân chia nội dung:** Giữ hai dòng đại số sau luồng; diễn giải từng số hạng và x là đóng góp cân bằng thuộc ghi chú.

**Ví dụ, phiếu số và hình thức hóa:** HT4; VD2. Beta bình phương biểu diễn hai bước theo cạnh; không phải một tham số mới.

**Kết nối vào–ra:** Ba nguồn điểm → hệ số tuần hoàn → xấp xỉ trong phân tích nguồn.

**Nguồn và vị trí:** NG1 §5.4.2, tr.201; phần giữ b tại đích là diễn giải đầy đủ trước phép lược trong sách.

**Thời lượng:** 3 phút.

**Ghi chú học thuật dự kiến:**

<!-- public-notes:start -->
Trang đích chia phần theo liên kết $\beta y$ đều cho $m$ hỗ trợ, nên mỗi hỗ trợ nhận $\beta y/m$. Mỗi hỗ trợ chỉ có một cạnh quay lại đích; phần điểm này qua bước theo liên kết thứ hai được nhân thêm $\beta$. Tổng trên $m$ hỗ trợ là $m\beta(\beta y/m)=\beta^2y$. Đây là thành phần bắt nguồn từ đích, tách khỏi phần $b$ mà mỗi hỗ trợ nhận trực tiếp từ dịch chuyển.

Thay $p=\beta y/m+b$ vào phương trình của đích cho $y=x+\beta^2y+\beta mb+b$. Chuyển $\beta^2y$ sang trái rồi chia cho $1-\beta^2>0$ thu được nghiệm. Hạng $\beta mb$ là phần dịch chuyển nhận tại các hỗ trợ rồi truyền về đích; hạng $b$ là dịch chuyển trực tiếp tới đích. Mô hình giả định toàn đồ thị không có nút cụt và giữ đúng kiến trúc đã nêu. Đại lượng $x$ là đóng góp ngoài ở trạng thái cân bằng, chịu ràng buộc tổng điểm toàn đồ thị.
<!-- public-notes:end -->

### lec04-s03-06 — Hệ số khuếch đại trong mô hình giản lược

**Vai trò, mục tiêu, đầu vào và sản phẩm:** Xấp xỉ và diễn giải số; MT2. Đầu vào: công thức đầy đủ. Sản phẩm: phân biệt giá trị sau nhân với phần trăm tăng.

**Luận điểm trung tâm:** Hệ số khuếch đại và mức tăng phần trăm là hai đại lượng khác nhau.

**Nội dung hiển thị dự kiến:**

<!-- public-slide:start -->
Bỏ riêng phần dịch chuyển trực tiếp $b$ tới trang đích như phép phân tích của sách:

$$y\approx\frac{x}{1-\beta^2}+\frac{\beta}{1+\beta}\frac mn.$$

Với $\beta=0.85=17/20$:

| Thành phần | Hệ số |
| --- | --- |
| Đóng góp từ ngoài $x$ | $400/111\approx3.6036$ |
| Tỷ lệ trang hỗ trợ $m/n$ | $17/37\approx0.45946$ |

Hệ số $400/111$ chỉ nhân với $x$. Hạng từ hỗ trợ là $(17/37)(m/n)$; hạng đã bỏ là $1/[n(1+\beta)]$.
<!-- public-slide:end -->

**Bố cục đã chọn:** Phép xấp xỉ ở trên40%; bảng hai hệ số giữa40%; câu giải nghĩa dưới20%. Nhãn “bỏ riêng b tới đích” đặt trước công thức.

**Trọng tâm và thứ tự đọc:** Xác định hạng bị bỏ → đọc hai hệ số → diễn giải “lần” và “phần tăng”.

**Lý do phù hợp sinh viên năm 2:** Giữ số nguồn và phân số chính xác giúp kiểm phép tính; tách tỷ lệ m/n khỏi điểm x tránh cộng hai đại lượng khác nghĩa không có nhãn.

**Giới hạn bố cục và phân chia nội dung:** Mặt trang phân biệt hệ số của x với hạng theo m/n và hạng bị bỏ. Phần tăng260,36% chỉ thuộc ghi chú, không diễn giải là tăng toàn bộ y.

**Ví dụ, phiếu số và hình thức hóa:** VD2; HT4 xấp xỉ. Bảng số giữ beta 17/20 theo VD5.11, khác beta 4/5 của G4 và có nhãn rõ.

**Kết nối vào–ra:** Phương trình đầy đủ → ý nghĩa khuếch đại → giới hạn suy luận và chi phí cấu trúc.

**Nguồn và vị trí:** NG1 VD5.11, tr.201/PDF27; sửa diễn đạt phần trăm để phân biệt hệ số với mức tăng.

**Thời lượng:** 3 phút.

**Ghi chú học thuật dự kiến:**

<!-- public-notes:start -->
Hạng chính xác bị bỏ trong biểu thức $y$ là $b/(1-\beta^2)=1/[n(1+\beta)]$. Phần dịch chuyển vào $m$ hỗ trợ vẫn được giữ vì tổng của chúng tạo hạng $m/n$. Với $\beta=17/20$, hệ số của $x$ là $400/111$; trừ $1$ rồi nhân $100$ cho phần tăng khoảng $260{,}36\%$. Đây là hệ số của một mô hình đại số, không phải số đo hiệu quả trên hệ tìm kiếm hiện hành.
<!-- public-notes:end -->

### lec04-s03-07 — Giới hạn của phân tích cấu trúc liên kết

**Vai trò, mục tiêu, đầu vào và sản phẩm:** Ứng dụng và giới hạn; MT2, MT3. Đầu vào: hệ số khuếch đại. Sản phẩm: nêu điều kiện áp dụng và nhu cầu đánh giá tin cậy.

**Luận điểm trung tâm:** Công thức gắn với đúng cấu trúc; hình dạng liên kết không tự chứng nhận nội dung rác.

**Nội dung hiển thị dự kiến:**

<!-- public-slide:start -->
Cụm mô hình cần $m$ trang hỗ trợ và $2m$ cạnh nội bộ; các cạnh từ ngoài được xét riêng.

Công thức áp dụng khi giữ đúng kiến trúc, quy tắc dịch chuyển và định nghĩa $x$.

Một cấu trúc liên kết dày chưa đủ xác định nội dung rác. Đánh giá dựa trên tập trang tin cậy bổ sung thông tin ngoài cấu trúc.
<!-- public-slide:end -->

**Bố cục đã chọn:** Hàng biểu tượng đích↔m hỗ trợ phía trên45% có nhãn2m cạnh; hai câu điều kiện và giới hạn phía dưới55%.

**Trọng tâm và thứ tự đọc:** Đếm hai chiều cạnh → đọc phạm vi công thức → nhận giới hạn của chỉ kiểm cấu trúc.

**Lý do phù hợp sinh viên năm 2:** Phép đếm trực tiếp từ hình nối phân tích với tài nguyên cần tạo; giới hạn không để sinh viên biến mẫu đồ thị thành quy tắc phân loại chắc chắn.

**Giới hạn bố cục và phân chia nội dung:** Không xây thuật toán phát hiện cụm ngoài nguồn. Không ước lượng thời gian rà toàn web từ2m cạnh.

**Ví dụ, phiếu số và hình thức hóa:** HT4; đếm2m là suy luận từ Hình 5.16. Không có thuật toán thực thi riêng; chu trình chi phí áp dụng ở mức cấu trúc.

**Kết nối vào–ra:** Mức khuếch đại → giới hạn phát hiện bằng hình dạng → kiểm tra dòng điểm, sau đó TrustRank.

**Nguồn và vị trí:** NG1 Hình 5.16, tr.200; §5.4.3, tr.202.

**Thời lượng:** 1 phút.

**Ghi chú học thuật dự kiến:**

<!-- public-notes:start -->
Trang đích có $m$ cạnh ra và mỗi trang trong $m$ hỗ trợ có một cạnh quay lại, tạo $2m$ cạnh nội bộ. Sách phân biệt phát hiện cấu trúc với thay cách đánh giá điểm. Một cụm có nhiều liên kết qua lại có thể xuất hiện vì chức năng hợp lệ, nên hình dạng cần được đặt trong ngữ cảnh dữ liệu. Tập tin cậy cung cấp thông tin bổ sung cho việc đánh giá.
<!-- public-notes:end -->

### lec04-s03-08 — Kiểm tra nguồn điểm tại đích

**Vai trò, mục tiêu, đầu vào và sản phẩm:** Kiểm tra riêng S03; MT2. Đầu vào: HT4. Sản phẩm: phát hiện đếm sai beta và phân biệt công thức đủ/xấp xỉ.

**Luận điểm trung tâm:** Phương trình đầy đủ và xấp xỉ chỉ khác ở hạng được lược có chỉ rõ.

**Nội dung hiển thị dự kiến:**

<!-- public-slide:start -->
Trong mô hình không nút cụt, đích chỉ trỏ $m$ hỗ trợ; mỗi hỗ trợ chỉ trỏ lại đích và chỉ nhận cạnh từ đích. Đặt $b=(1-\beta)/n$, $p=\beta y/m+b$; $x$ đã gồm $\beta$.

**Câu hỏi:**
1. Sửa phương trình $y=\beta x+\beta mp$ để có phương trình đầy đủ.
2. Xác định hạng của $y$ bị bỏ khi dùng công thức xấp xỉ trong sách.
<!-- public-slide:end -->

**Bố cục đã chọn:** Giả thiết ngắn và hai công thức đã biết ở trên45%; hai yêu cầu ở khung kiểm tra dưới55%. Không cho sẵn phương trình sửa.

**Trọng tâm và thứ tự đọc:** Kiểm ý nghĩa x → tìm điểm thiếu → giải tác động của hạng bị lược lên y.

**Lý do phù hợp sinh viên năm 2:** Một lỗi nhân thừa và một hạng thiếu buộc sinh viên truy nguồn thay vì chỉ nhớ công thức cuối.

**Giới hạn bố cục và phân chia nội dung:** Chỉ hai yêu cầu trên mô hình đã học; bài đổi liên kết được dành cho recitation.

**Ví dụ, phiếu số và hình thức hóa:** VD2/HT4; câu hỏi dùng phương trình nguồn và một phép sai để kiểm cơ chế.

**Kết nối vào–ra:** Kiểm dòng điểm trong mô hình thao túng → lựa chọn tập trang đáng tin ở S04.

**Nguồn và vị trí:** NG1 §5.4.2, tr.201; kiểm tra áp dụng trên cùng ký hiệu và giả thiết.

**Thời lượng:** 3 phút.

**Nhiệm vụ và tiêu chí nội bộ:** Slide kiểm tra riêng của phần.

- Câu hỏi/đề: Sửa phương trình và xác định hạng bị lược như nội dung hiển thị.
- Đáp án/gợi ý: $y=x+\beta mp+b$; hạng bỏ khỏi y là $b/(1-\beta^2)=1/[n(1+\beta)]$.
- Tiêu chí đánh giá: Đúng định nghĩa x; giữ b tại đích trong bản đầy đủ; phân biệt b trước giải với hạng đóng góp vào nghiệm. Không lược b ở mọi hỗ trợ.
- Phân bổ hoạt động: Suy nghĩ1,5 phút, trả lời0,5 phút, đối chiếu1 phút; tổng3 phút.

**Ghi chú học thuật dự kiến:**

<!-- public-notes:start -->
Phương trình đầy đủ là $y=x+\beta mp+b$. Đại lượng $x$ đã qua hệ số $\beta$ nên không nhân lần nữa. Thế $p$ rồi giải cho $y$ cho hạng bị lược bằng $b/(1-\beta^2)=1/[n(1+\beta)]$. Phần $\beta mb$ vẫn được giữ vì đó là tổng phần dịch chuyển nhận bởi $m$ hỗ trợ sau khi truyền về đích.
<!-- public-notes:end -->

## S04. TrustRank và Spam Mass

Thuật toán và diễn giải. Tập tin cậy → tái dùng HT1 → cùng G4/VD1 → đối chiếu r/rho cùng beta → chỉ số tương đối → chi phí và giới hạn → kiểm tra. Giả mã, bảo toàn và hội tụ kế thừa S02, không lặp lại toàn bộ. Đầu ra gồm chỉ số có dấu và giới hạn suy luận; HITS tiếp tục bằng một nhu cầu điểm khác.

Phân bổ: 8 slide, 18 phút.

### lec04-s04-01 — Tập trang tin cậy và TrustRank

**Vai trò, mục tiêu, đầu vào và sản phẩm:** Vấn đề và trực giác; MT3. Đầu vào: giới hạn phát hiện cấu trúc và PageRank theo chủ đề. Sản phẩm: xác định thông tin ngoài đồ thị cần cho TrustRank.

**Luận điểm trung tâm:** TrustRank cần tập tin cậy từ đánh giá bên ngoài và giả định về hướng liên kết.

**Nội dung hiển thị dự kiến:**

<!-- public-slide:start -->
[Hình: Tập T có viền đôi được đánh giá bên ngoài; cạnh thật đi từ T tới các trang khác.]

Tập hạt giống $T$ gồm các trang được đánh giá đáng tin bằng thông tin ngoài phép lặp TrustRank.

TrustRank dịch chuyển tới $T$. Tập này biểu diễn độ tin cậy; tập chủ đề biểu diễn lĩnh vực nội dung.

Giả định: trang tin cậy ít trỏ tới trang rác. Độ phủ của $T$ ảnh hưởng điểm của các trang ngoài tập.
<!-- public-slide:end -->

**Bố cục đã chọn:** Một nhóm T có viền đôi và các cạnh ra tới phần còn lại chiếm trái55%; giả định và giới hạn phải45%. Nhãn “đánh giá bên ngoài” gắn với T.

**Trọng tâm và thứ tự đọc:** Xác định nguồn thông tin chọn T → theo chiều liên kết → đọc giới hạn của điểm thấp.

**Lý do phù hợp sinh viên năm 2:** Dùng lại trực giác tập dịch chuyển thay vì giới thiệu phép lặp mới; tách tin cậy được kiểm ngoài mô hình với điểm lan truyền.

**Giới hạn bố cục và phân chia nội dung:** Mặt trang có nguồn đánh giá T, khác biệt ý nghĩa với tập chủ đề, giả định ít trỏ rác và độ phủ; ghi chú nêu tính không tuyệt đối.

**Ví dụ, phiếu số và hình thức hóa:** HT5; tập T không rỗng. Không có số mới, sơ đồ chỉ khái niệm.

**Kết nối vào–ra:** Liên kết có thể bị thao túng → chọn nơi đưa điểm mới → đặc tả TrustRank.

**Nguồn và vị trí:** NG1 §5.4.3–5.4.4, tr.202–203/PDF28–29.

**Thời lượng:** 2 phút.

**Ghi chú học thuật dự kiến:**

<!-- public-notes:start -->
Các hạt giống được đánh giá nội dung từ bên ngoài trước khi chạy thuật toán. TrustRank không tự lựa chọn và chứng nhận chúng từ điểm đầu ra. Các trang ngoài $T$ vẫn có thể nhận điểm qua liên kết. TrustRank giữ cơ chế PageRank theo chủ đề, nhưng ý nghĩa tập dịch chuyển là tin cậy thay cho lĩnh vực nội dung. Giả định về hướng liên kết không có tính tuyệt đối, nhất là khi trang cho phép người khác tạo liên kết. Chất lượng và phạm vi bao phủ của $T$ ảnh hưởng cách diễn giải điểm; vector kết quả không chứng nhận nội dung của từng trang.
<!-- public-notes:end -->

### lec04-s04-02 — Các đại lượng trong phép lặp TrustRank

**Vai trò, mục tiêu, đầu vào và sản phẩm:** Định nghĩa ký hiệu; MT3. Đầu vào: tập T, PageRank có nút cụt. Sản phẩm: đọc đúng n,rho,t,M0,dj,delta,u,vT,beta.

**Luận điểm trung tâm:** TrustRank tái dùng các đối tượng PageRank với vector điểm rho và phân phối dịch chuyển vT.

**Nội dung hiển thị dự kiến:**

<!-- public-slide:start -->
Đồ thị có $n$ trang; $T\ne\varnothing$ là tập hạt giống tin cậy.

| Ký hiệu | Ý nghĩa |
| --- | --- |
| $\rho^t\in\mathbb R^n$; $\rho_i^t$ | Vector TrustRank ở vòng $t$; điểm của trang $i$ |
| $d_j$; $M_0$ | Bậc ra của trang $j$; ma trận liên kết với cột $j$ là nguồn |
| $\delta_\rho^t=\sum_{j:d_j=0}\rho_j^t$ | Tổng điểm tại các nút cụt ở vòng $t$ |
| $u_i=1/n$; $v_T$ | Phân phối đều trên toàn bộ trang; phân phối đều trên $T$ |
| $0<\beta<1$ | Xác suất thực hiện bước theo liên kết |

$(M_0)_{ij}=1/d_j$ nếu $j\to i$ và $d_j>0$; bằng $0$ trong các trường hợp khác, gồm cột nút cụt.
<!-- public-slide:end -->

**Bố cục đã chọn:** Dòng đầu xác định n,T; bảng năm hàng ánh xạ ký hiệu–vai trò; dòng cuối định nghĩa phần tử ma trận liên kết và cột nút cụt.

**Trọng tâm và thứ tự đọc:** Vector điểm → cấu trúc liên kết → điểm nút cụt → hai phân phối → beta.

**Lý do phù hợp sinh viên năm 2:** Bảng gắn mỗi ký hiệu với đối tượng trước khi đọc công thức ba số hạng; tránh nhầm t với T.

**Giới hạn bố cục và phân chia nội dung:** Mặt trang định nghĩa phần tử M0; giá trị từng thành phần vT và phương trình cập nhật nằm ở S04-02a. Ghi chú phân biệt tổng điểm nút cụt với lượng bù sau nhân beta.

**Ví dụ, phiếu số và hình thức hóa:** HT5 kế thừa HT1; rho có n thành phần, delta là tổng vô hướng.

**Kết nối vào–ra:** Hạt giống ngoài thuật toán → ký hiệu → công thức ba thành phần.

**Nguồn và vị trí:** NG1 §5.4.4, tr.202–203; quy tắc bù và dừng là đặc tả thống nhất với HT1.

**Thời lượng:** 2 phút.

**Ghi chú học thuật dự kiến:**

<!-- public-notes:start -->
Vector $\rho^t$ chứa $n$ điểm không âm, tổng bằng $1$, ở vòng lặp $t$. Thành phần $\rho_i^t$ thuộc trang $i$; khi hội tụ, ký hiệu $\rho_i$ chỉ thành phần tương ứng của vector giới hạn. Với $d_j>0$, $(M_0)_{ij}=1/d_j$ nếu có cạnh $j\to i$, bằng $0$ nếu không có cạnh. Cột của nút cụt bằng $0$.

Tổng điểm tại nút cụt là $\delta_\rho^t$; lượng điểm phải bù trong nhánh theo liên kết là $\beta\delta_\rho^t$. Phân phối $u$ đều trên toàn bộ $n$ trang dùng để phân phối lượng điểm bù này. Phân phối $v_T$ có thành phần $1/|T|$ với trang trong $T$ và bằng $0$ ngoài $T$, dùng cho nhánh dịch chuyển. Hai phân phối có vai trò khác nhau dù đều có tổng bằng $1$. Tham số $\beta$ được giữ như trong phép tính PageRank nền để so sánh.
<!-- public-notes:end -->

### lec04-s04-02a — Ba thành phần cập nhật TrustRank

**Vai trò, mục tiêu, đầu vào và sản phẩm:** Hình thức hóa và tái dùng thuật toán; MT3. Đầu vào: bảng ký hiệu S04-02. Sản phẩm: phân biệt ba số hạng và điều kiện dừng.

**Luận điểm trung tâm:** Theo liên kết, bù nút cụt và dịch chuyển tới T có ba vai trò riêng trong phép cập nhật.

**Nội dung hiển thị dự kiến:**

<!-- public-slide:start -->
$(v_T)_i=1/|T|$ nếu $i\in T$, bằng $0$ ngoài $T$; khởi tạo $\rho^0=v_T$.

$$\rho^{t+1}=\underbrace{\beta M_0\rho^t}_{\text{theo liên kết}}+\underbrace{\beta\delta_\rho^t u}_{\text{bù nút cụt}}+\underbrace{(1-\beta)v_T}_{\text{dịch chuyển}}.$$

| Thành phần | Nơi nhận điểm |
| --- | --- |
| Theo liên kết | Các trang đích của cạnh thật |
| Bù nút cụt | Toàn bộ $n$ trang, chia đều |
| Dịch chuyển | Các trang trong $T$, chia đều |

Dùng thuật toán PageRank theo chủ đề với $r\mapsto\rho$, $v\mapsto v_T$; giữ quy tắc bù và điều kiện dừng.
<!-- public-slide:end -->

**Bố cục đã chọn:** Phân phối vT và khởi tạo ở trên; công thức có ba nhãn ở giữa; bảng ba hàng xác định nơi nhận điểm ở dưới.

**Trọng tâm và thứ tự đọc:** Khởi tạo → từng số hạng theo trái–phải → nơi nhận điểm → thuật toán kế thừa.

**Lý do phù hợp sinh viên năm 2:** Nhãn dưới số hạng nối ký hiệu ở trang trước với thao tác; bảng làm rõ bù đều toàn đồ thị khác dịch chuyển vào T.

**Giới hạn bố cục và phân chia nội dung:** Không chép lại giả mã; bảo toàn, co và trạng thái dừng được giải thích trong ghi chú.

**Ví dụ, phiếu số và hình thức hóa:** HT5 dùng HT1–HT2; bù nút cụt vẫn là u, không đổi sang vT.

**Kết nối vào–ra:** Các đối tượng → cập nhật rho → nghiệm cụ thể trên G4.

**Nguồn và vị trí:** NG1 §5.4.4 tr.202–203; quy tắc bù và dừng thống nhất với HT1.

**Thời lượng:** 2 phút.

**Ghi chú học thuật dự kiến:**

<!-- public-notes:start -->
Thành phần $\beta M_0\rho^t$ truyền điểm từ các trang không cụt theo cạnh. Thành phần $\beta\delta_\rho^t u$ bù phần điểm ở các nút cụt lên toàn bộ trang. Thành phần $(1-\beta)v_T$ đưa điểm dịch chuyển vào các hạt giống tin cậy. Tổng ba thành phần bằng $\beta(1-\delta_\rho^t)+\beta\delta_\rho^t+(1-\beta)=1$.

Đây là phép lặp PageRank theo chủ đề với tập tin cậy làm tập dịch chuyển. Ma trận bù $\bar M$ vẫn không âm và có tổng mỗi cột bằng $1$; với $0<\beta<1$, lập luận co cho điểm cố định duy nhất $\rho$. Thuật toán trả vector xấp xỉ cùng trạng thái đạt ngưỡng hoặc hết $K$ vòng. Đánh giá hạt giống thuộc đầu vào bên ngoài; phương trình không chứng nhận độ tin cậy tuyệt đối của từng trang.
<!-- public-notes:end -->


### lec04-s04-03 — TrustRank trên đồ thị bốn trang

**Vai trò, mục tiêu, đầu vào và sản phẩm:** Ví dụ tái sử dụng; MT3. Đầu vào: VD1 và T={B,D}. Sản phẩm: liên hệ cùng phép tính với ý nghĩa tin cậy.

**Luận điểm trung tâm:** B,D là hạt giống giả thiết đầu vào; cùng phân phối dịch chuyển cho cùng nghiệm số với ví dụ chủ đề.

**Nội dung hiển thị dự kiến:**

<!-- public-slide:start -->
[Hình: Đồ thị G4: A tới B, C, D; B tới A, D; C tới A; D tới B, C. B và D có viền đôi và nhãn tập tin cậy T.]

G4 giữ nguyên tám cạnh; $\beta=4/5$. Giả sử B và D đã được đánh giá đáng tin: $T=\{B,D\}$.

$$v_T=(0,1/2,0,1/2)^\mathsf T.$$

| Trang | TrustRank $\rho_i$ |
| --- | --- |
| A | $9/35$ |
| B | $59/210$ |
| C | $19/105$ |
| D | $59/210$ |

Nghiệm trùng với ví dụ chủ đề vì cùng phân phối dịch chuyển. B và D là hạt giống giả thiết từ đầu vào.
<!-- public-slide:end -->

**Bố cục đã chọn:** G4 trái50%, bảng bốn hàng phải50%; B,D có nhãn T và viền đôi, vị trí đỉnh giữ theo VD1.

**Trọng tâm và thứ tự đọc:** Đọc T trên đồ thị → đối chiếu vT → nhận diện nghiệm đã có.

**Lý do phù hợp sinh viên năm 2:** Tái dùng dữ kiện tiết kiệm phép tính lặp nhưng vẫn giữ quan hệ giữa seed và vector; sinh viên thấy thuật toán không đổi.

**Giới hạn bố cục và phân chia nội dung:** Không lặp toàn bộ vết vòng 1/2; tham số và nghiệm phải có trên mặt slide để đọc độc lập.

**Ví dụ, phiếu số và hình thức hóa:** VD3 dùng nghiệm VD1; tổng rho=1. B,D hòa được giữ, không sửa số.

**Kết nối vào–ra:** TrustRank là phép lặp quen thuộc → cần so sánh với PageRank toàn cục cùng tham số.

**Nguồn và vị trí:** NG1 §5.4.4, tr.202–203; Ví dụ 5.10, tr.196–197, cung cấp G4 và tập dịch chuyển. Giữ đồ thị/tập của sách.

**Thời lượng:** 1 phút.

**Ghi chú học thuật dự kiến:**

<!-- public-notes:start -->
B, D đã được coi là tin cậy từ đầu, nên phép dịch chuyển ưu tiên chúng. A, C không thuộc tập hạt giống nhưng vẫn nhận điểm qua các liên kết thật. Giá trị của hai trang này không xác nhận hoặc bác bỏ riêng lẻ tính tin cậy của nội dung. Để đánh giá phần thay đổi so với điểm toàn cục, cần tính một vector PageRank nền theo cùng $\beta$ và cùng chuẩn hóa.
<!-- public-notes:end -->

### lec04-s04-04 — So sánh PageRank và TrustRank

**Vai trò, mục tiêu, đầu vào và sản phẩm:** Chuẩn bị chỉ số; MT3. Đầu vào: rho. Sản phẩm: đối chiếu hai vector trên cùng mô hình.

**Luận điểm trung tâm:** Hiệu của hai vector cùng mô hình mô tả thay đổi điểm; dấu hiệu không xác định thay đổi thứ hạng hoặc nhãn rác.

**Nội dung hiển thị dự kiến:**

<!-- public-slide:start -->
Cùng G4, $\beta=4/5$ và tổng điểm bằng 1. PageRank dùng $u$; TrustRank dùng $v_T$, $T=\{B,D\}$.

| Trang | PageRank $r_i$ | TrustRank $\rho_i$ | Hiệu $r_i-\rho_i$ |
| --- | --- | --- | --- |
| A | $9/28$ | $9/35$ | $9/140$ |
| B | $19/84$ | $59/210$ | $-23/420$ |
| C | $19/84$ | $19/105$ | $19/420$ |
| D | $19/84$ | $59/210$ | $-23/420$ |

Khi chuyển PageRank → TrustRank, hiệu dương ứng với điểm giảm; hiệu âm ứng với điểm tăng; hiệu bằng $0$ ứng với điểm không đổi.

Hiệu điểm không xác định thay đổi thứ hạng hoặc nhãn rác.
<!-- public-slide:end -->

**Bố cục đã chọn:** Bảng bốn trang giữ các giá trị chính xác; đoạn dưới diễn giải ba dấu theo chiều PageRank → TrustRank và giới hạn kết luận về thứ hạng, nhãn rác. Bỏ bảng dấu riêng để dành khoảng cho nguồn và chân trang, giữ thang chữ chung.

**Trọng tâm và thứ tự đọc:** So sánh cùng mô hình → đọc r và rho → hiệu → hướng giảm/tăng/không đổi.

**Lý do phù hợp sinh viên năm 2:** So sánh cùng beta loại nguyên nhân gây nhiễu; phân số giữ chính xác để chuẩn bị phép chia tương đối.

**Giới hạn bố cục và phân chia nội dung:** Mặt trang giữ diễn giải cả ba dấu và giới hạn kết luận; ghi chú giải thích tổng hiệu bằng 0 và khác biệt với bảng nguồn.

**Ví dụ, phiếu số và hình thức hóa:** VD3: bảng tính lại đồng nhất beta; đây không phải số chép từ Hình 5.17. Hiệu B,D âm hợp lệ.

**Kết nối vào–ra:** Hai vector cùng mô hình → hiệu điểm → chuẩn hóa hiệu theo r_i.

**Nguồn và vị trí:** NG1 §5.4.5/VD5.12, tr.203; bảng dẫn xuất trên G4 với beta 4/5, khác bảng nguyên nguồn.

**Thời lượng:** 3 phút.

**Ghi chú học thuật dự kiến:**

<!-- public-notes:start -->
PageRank đều thỏa $r=(4/5)M_0r+(1/5)u$ và có nghiệm $(9/28,19/84,19/84,19/84)^\mathsf T$. Vector $\rho$ đã được tính với tập tin cậy B, D. Hình 5.17 của sách dùng PageRank không dịch chuyển lấy từ Ví dụ 5.2, trong khi TrustRank dùng $\beta=0.8$; bảng này tính lại PageRank nền cùng $\beta=0.8$ để tách tác động của phân phối dịch chuyển. Hiệu $r_i-\rho_i>0$ nghĩa là $\rho_i<r_i$, nên điểm giảm khi chuyển từ PageRank sang TrustRank. Hiệu âm nghĩa là điểm tăng; hiệu bằng $0$ nghĩa là điểm không đổi. Dấu của hiệu mô tả thay đổi điểm, không xác định thay đổi thứ hạng hoặc nhãn rác. Tổng các hiệu bằng $0$ vì hai vector đều có tổng bằng $1$. Giá trị tuyệt đối của hiệu chưa xét quy mô điểm nền của từng trang.
<!-- public-notes:end -->

### lec04-s04-05 — Định nghĩa và giá trị Spam Mass

**Vai trò, mục tiêu, đầu vào và sản phẩm:** Hình thức hóa và chạy phép chia; MT3. Đầu vào: r,rho. Sản phẩm: tính chỉ số tương đối, giữ giá trị âm.

**Luận điểm trung tâm:** Spam Mass là mức giảm tương đối so với PageRank nền; A,C cùng giảm20% dù hiệu tuyệt đối khác nhau.

**Nội dung hiển thị dự kiến:**

<!-- public-slide:start -->
Với $r_i>0$, chỉ số Spam Mass là
$$s_i=\frac{r_i-\rho_i}{r_i}=1-\frac{\rho_i}{r_i}.$$

| Trang | Phép tính | $s_i$ |
| --- | --- | --- |
| A | $(9/140)/(9/28)$ | $1/5$ |
| B | $(-23/420)/(19/84)$ | $-23/95$ |
| C | $(19/420)/(19/84)$ | $1/5$ |
| D | $(-23/420)/(19/84)$ | $-23/95$ |

A và C có $s_i=1/5$: TrustRank giảm $20\%$ so với PageRank nền của từng trang. Chỉ số không phải xác suất trang rác.
<!-- public-slide:end -->

**Bố cục đã chọn:** Định nghĩa ở trên30%; bảng giữa55%; giới hạn dưới15%. Cột phép tính giữ tử và mẫu có ngoặc rõ.

**Trọng tâm và thứ tự đọc:** Đọc điều kiện r_i>0 → hiệu chia điểm nền → đối chiếu kết quả dương/âm.

**Lý do phù hợp sinh viên năm 2:** Bảng cùng hàng với trang trước giúp sinh viên thấy một hiệu tuyệt đối được chuyển thành thay đổi tương đối; giá trị âm không bị coi là lỗi tính.

**Giới hạn bố cục và phân chia nội dung:** Giữ bảng giá trị và diễn giải20%; không thêm ngưỡng phân loại hoặc xác suất rác.

**Ví dụ, phiếu số và hình thức hóa:** HT5/VD3. $s_i\le1$ vì rho_i không âm; không áp cận dưới0. Rho_i>r_i cho chỉ số âm.

**Kết nối vào–ra:** Hiệu hai vector → Spam Mass → giới hạn diễn giải và chi phí.

**Nguồn và vị trí:** NG1 §5.4.5, tr.203/PDF29; bảng số mới cùng beta theo VD3.

**Thời lượng:** 3 phút.

**Ghi chú học thuật dự kiến:**

<!-- public-notes:start -->
Tại A, $(9/140)/(9/28)=1/5$; tại C cũng có $s_C=1/5$. Cả hai có $\rho_i=(4/5)r_i$, tức giảm $20\%$ so với điểm nền riêng. Mức giảm tuyệt đối khác nhau: $9/140$ tại A và $19/420$ tại C. Tại B, $(-23/420)/(19/84)=-23/95$. Chỉ số âm có nghĩa TrustRank vượt PageRank nền ở trang đó; đó là quan hệ giữa hai phép xếp hạng, không phải xác suất âm. Giá trị gần $1$ tương ứng $\rho_i$ nhỏ so với $r_i$ và gợi ý cần rà soát dưới giả định của mô hình. Cùng một chỉ số dương không đủ chứng minh các trang A, C là rác.
<!-- public-notes:end -->

### lec04-s04-06 — Độ phủ hạt giống và chi phí đánh giá

**Vai trò, mục tiêu, đầu vào và sản phẩm:** Giới hạn và chi phí; MT3, MT5. Đầu vào: HT5. Sản phẩm: phân biệt chi phí phép lặp với chọn hạt giống.

**Luận điểm trung tâm:** Chỉ số Spam Mass lớn được dùng để ưu tiên rà soát; chỉ số phụ thuộc tập hạt giống và không tự xác định nhãn rác.

**Nội dung hiển thị dự kiến:**

<!-- public-slide:start -->
Tập tin cậy cần cân đối công sức đánh giá và độ phủ của các trang hợp lệ.

| Bước | Phạm vi chi phí |
| --- | --- |
| PageRank và TrustRank | Hai phép lặp thưa; mỗi vòng $\Theta(n+\ell)$ |
| Tính Spam Mass | $\Theta(n)$ phép tính theo đỉnh |
| Đánh giá hạt giống | Công việc ngoài mô hình phép toán đồ thị |

Các trang có chỉ số $s_i$ lớn được ưu tiên rà soát. Chỉ số phụ thuộc $T$ và không tự xác định nhãn rác.
<!-- public-slide:end -->

**Bố cục đã chọn:** Một câu về hạt giống phía trên20%; bảng ba dòng giữa60%; câu giới hạn phía dưới20%.

**Trọng tâm và thứ tự đọc:** Đọc đánh đổi hạt giống → phân biệt ba công việc → giới hạn kết luận.

**Lý do phù hợp sinh viên năm 2:** Bảng không gộp đánh giá con người với phép toán máy; sinh viên so sánh đúng phạm vi chi phí thay vì suy nhanh hơn tuyệt đối.

**Giới hạn bố cục và phân chia nội dung:** Không đưa chi phí giờ công hoặc ngưỡng không có nguồn. Không tạo thuật toán chọn hạt giống mới.

**Ví dụ, phiếu số và hình thức hóa:** HT5; nếu hai phép lặp lần lượt K_r,K_rho vòng thì thời gian tính là Theta((K_r+K_rho)(n+ell)+n).

**Kết nối vào–ra:** Chỉ số đã có → nguồn sai lệch và tài nguyên → kiểm diễn giải.

**Nguồn và vị trí:** NG1 §5.4.4–5, tr.202–203; phép đếm theo HT1. NG3 trang42 đối chiếu đánh đổi hạt giống.

**Thời lượng:** 2 phút.

**Ghi chú học thuật dự kiến:**

<!-- public-notes:start -->
Sau khi có $r$ và $\rho$, chỉ số $s_i$ đo phần điểm giảm tương đối khi chuyển sang ưu tiên hạt giống tin cậy. Giá trị dương lớn có thể được dùng để ưu tiên trang cần rà soát; chỉ số không tự xác định nhãn rác. Đổi tập $T$ có thể đổi $\rho$ và thứ tự ưu tiên. Tập nhỏ giảm số trang phải đánh giá nhưng có thể bỏ sót các vùng nội dung. Điểm tin cậy thấp có thể phản ánh khoảng cách liên kết hoặc thiếu hạt giống phù hợp, không chỉ liên kết rác. Hai phép lặp có thể cần số vòng khác nhau; chỉ bậc chi phí mỗi vòng giống nhau. Sau khi có $r$ và $\rho$, mỗi trang cần một phép trừ và một phép chia nếu $r_i>0$. Chi phí đánh giá hạt giống không được suy ra từ số cạnh hoặc số vòng.
<!-- public-notes:end -->

### lec04-s04-07 — Kiểm tra cách diễn giải Spam Mass

**Vai trò, mục tiêu, đầu vào và sản phẩm:** Kiểm tra riêng S04; MT3. Đầu vào: VD3 và định nghĩa s. Sản phẩm: tính giá trị âm, giới hạn kết luận.

**Luận điểm trung tâm:** Dấu và độ lớn Spam Mass phải được đọc dưới giả định mô hình, không thành nhãn chắc chắn.

**Nội dung hiển thị dự kiến:**

<!-- public-slide:start -->
Với G4 và $\beta=4/5$, trang B có $r_B=19/84$, $\rho_B=59/210$. Trang A có $s_A=1/5$.

**Câu hỏi:**
1. Tính $s_B$ và giải thích dấu của kết quả.
2. Từ $s_A=1/5$, có thể kết luận chắc chắn A là trang rác hay không? Nêu căn cứ.
<!-- public-slide:end -->

**Bố cục đã chọn:** Hai dòng dữ kiện ở trên30%; hai nhiệm vụ chiếm70% còn lại trong khung kiểm tra. Không kèm bảng đáp án trước đó.

**Trọng tâm và thứ tự đọc:** Đọc cặp r/rho của B → tính hiệu có dấu → áp giới hạn diễn giải cho A.

**Lý do phù hợp sinh viên năm 2:** Một tính toán và một nhận định kiểm cả cơ chế lẫn phạm vi suy luận, ngăn đồng nhất s với xác suất.

**Giới hạn bố cục và phân chia nội dung:** Không hỏi xác suất hoặc ngưỡng chưa được định nghĩa; đáp án trong ghi chú.

**Ví dụ, phiếu số và hình thức hóa:** VD3/HT5; giữ nguyên phân số đã kiểm.

**Kết nối vào–ra:** Điểm tin cậy và chỉ báo thao túng → mô hình hai vai trò cấu trúc HITS.

**Nguồn và vị trí:** NG1 §5.4.5, tr.203; dữ kiện VD3 tính lại đồng nhất beta.

**Thời lượng:** 3 phút.

**Nhiệm vụ và tiêu chí nội bộ:** Slide kiểm tra riêng của phần.

- Câu hỏi/đề: Tính s_B, giải thích dấu và đánh giá kết luận chắc chắn về A.
- Đáp án/gợi ý: $s_B=-23/95$; rho_B>r_B. Không thể kết luận chắc chắn A là rác chỉ từ s_A.
- Tiêu chí đánh giá: Giữ dấu âm; phân biệt chỉ số với xác suất; nêu ít nhất một phụ thuộc vào tập tin cậy/độ phủ/giả định liên kết.
- Phân bổ hoạt động: Tính1 phút, giải thích1 phút, đối chiếu1 phút; tổng3 phút.

**Ghi chú học thuật dự kiến:**

<!-- public-notes:start -->
$s_B=-23/95$ vì $\rho_B>r_B$. Giá trị âm cho thấy điểm của B tăng khi ưu tiên tập tin cậy. Chỉ số $1/5$ tại A không chứng minh A là rác; nó mô tả chênh lệch tương đối giữa hai mô hình điểm, phụ thuộc $T$ và giả định liên kết. HITS đánh giá một quan hệ cấu trúc khác: một trang cung cấp nội dung hay dẫn tới các trang cung cấp nội dung.
<!-- public-notes:end -->

## S05. HITS

Thuật toán và ví dụ. Danh sách/nội dung học phần → hai vai trò → G5/VD4 chạy hai vòng → L, phép chuẩn hóa → giả mã, quan hệ điểm ổn định → chi phí thưa → kiểm tra. Ví dụ có trước ma trận, nhưng mỗi phép cộng đã có quy tắc cạnh vào/ra. Đầu ra hai vector hỗ trợ lựa chọn phương pháp ở S06. Điều kiện phổ giải nghĩa trong ghi chú, không thành nhiệm vụ đánh giá mới.

Phân bổ: 11 slide, 30 phút.

### lec04-s05-01 — Hai vai trò trong mạng học phần

**Vai trò, mục tiêu, đầu vào và sản phẩm:** Tình huống sử dụng HITS; MT4. Đầu vào: đồ thị liên kết. Sản phẩm: phân biệt nội dung và đường dẫn tới nội dung.

**Luận điểm trung tâm:** Mỗi trang có hai điểm; danh mục minh họa trung tâm, trang nội dung minh họa uy tín theo liên kết.

**Nội dung hiển thị dự kiến:**

<!-- public-slide:start -->
Đầu vào là đồ thị các trang và liên kết đã chọn. Trang danh sách học phần dẫn tới các trang của từng học phần.

[Hình: Trang danh mục học phần giữ vai trò trung tâm và trỏ tới các trang học phần giữ vai trò uy tín.]
Thuật toán tìm kiếm theo chủ đề dựa trên siêu liên kết (HITS) gán mỗi trang hai điểm: trung tâm (hub) $h_i$ và uy tín (authority) $a_i$.

Trang danh mục minh họa vai trò trung tâm; trang cung cấp nội dung minh họa vai trò uy tín. Uy tín HITS biểu thị quan hệ liên kết, khác độ tin cậy của TrustRank.
<!-- public-slide:end -->

**Bố cục đã chọn:** Đầu vào đồ thị ở trên; sơ đồ trang danh mục trỏ tới các trang học phần ở giữa; phần dưới định nghĩa hai điểm $h_i,a_i$, gắn với hai vai trò và phân biệt uy tín HITS với độ tin cậy TrustRank. Không đưa ký hiệu tích ma trận vào trang mở phần.

**Trọng tâm và thứ tự đọc:** Nhận đồ thị đầu vào → đối chiếu trang danh mục với trang nội dung → nhận diện hai vai trò và hai điểm → phân biệt uy tín theo liên kết với độ tin cậy.

**Lý do phù hợp sinh viên năm 2:** Ví dụ học phần của sách gần với kinh nghiệm sinh viên, không đòi kiến thức hệ tìm kiếm; hai nhu cầu tạo lý do cho hai vector.

**Giới hạn bố cục và phân chia nội dung:** Mặt trang định nghĩa hai vai trò và khác biệt với TrustRank; chi phí đồ thị lớn chuyển sang ghi chú và S05-10.

**Ví dụ, phiếu số và hình thức hóa:** NG1 VD5.13, định tính; hai điểm $h_i,a_i$ được giới thiệu ngay trên trang này. Trang sau diễn giải quan hệ cập nhật giữa hai điểm trên G5.

**Kết nối vào–ra:** S04 phân biệt chỉ số tin cậy với vai trò cấu trúc → đầu vào đồ thị và nhu cầu hai vector HITS → chạy tay trên G5 trước khi xây phép lặp thưa; S05-10 thu hồi giới hạn tính toán.

**Nguồn và vị trí:** NG1 §5.5–5.5.2, tr.204–208/PDF30–34; Ví dụ 5.13 tr.205; phạm vi đồ thị tr.204, phép nhân thưa tr.206 và tính lặp trên web lớn tr.208.

**Thời lượng:** 2 phút.

**Ghi chú học thuật dự kiến:**

<!-- public-notes:start -->
Đồ thị trang và liên kết được coi là đầu vào đã chọn. Trang danh sách không thay thế nội dung chi tiết của một học phần, còn một trang học phần không thay thế danh sách toàn bộ học phần. Hai vai trò được đánh giá từ cấu trúc liên kết. Uy tín trong HITS không đồng nghĩa với điểm tin cậy của TrustRank; nó biểu diễn vai trò nhận liên kết từ các trang trung tâm có điểm cao. Trên đồ thị lớn, phép lặp tính hai vector cần khai thác các cạnh hiện có thay vì lưu ma trận đặc; ví dụ nhỏ cho phép kiểm từng phép cập nhật.
<!-- public-notes:end -->

### lec04-s05-02 — Điểm trung tâm và điểm uy tín

**Vai trò, mục tiêu, đầu vào và sản phẩm:** Trực giác và dữ kiện chạy tay; MT4. Đầu vào: hai vai trò. Sản phẩm: đọc quy tắc cộng theo hai chiều trên G5.

**Luận điểm trung tâm:** Trung tâm và uy tín hỗ trợ lẫn nhau; mỗi trang có cả hai điểm.

**Nội dung hiển thị dự kiến:**

<!-- public-slide:start -->
[Hình: Đồ thị G5: A tới B, C, D; B tới A, D; C tới E; D tới B, C; E không có cạnh ra.]
Đồ thị G5

Mỗi trang $i$ có điểm trung tâm $h_i$ và điểm uy tín $a_i$.

Hai điểm hỗ trợ lẫn nhau: trang nhận liên kết từ các trung tâm có điểm cao sẽ có uy tín cao; trang trỏ tới các trang uy tín cao sẽ có điểm trung tâm cao.

Khởi tạo $h^0=(1,1,1,1,1)^\mathsf T$ theo thứ tự A,B,C,D,E.
<!-- public-slide:end -->

**Bố cục đã chọn:** G5 trái55%, hai quy tắc và khởi tạo phải45%. E đặt dưới C; cạnh C→E thay cạnh C→A của ví dụ G4 và có nhãn rõ.

**Trọng tâm và thứ tự đọc:** Đọc đồ thị mới → theo các cạnh vào khi tính a → theo cạnh ra khi tính h.

**Lý do phù hợp sinh viên năm 2:** Nêu đầy đủ cạnh mới ngăn dùng nhầm ma trận G4; hai điểm được gắn cùng mỗi trang, tránh hiểu hub/authority là hai nhóm rời nhau.

**Giới hạn bố cục và phân chia nội dung:** Không chia bậc ra và không thêm bước nhảy. Hai phép cộng được chạy trước khi viết dạng ma trận.

**Ví dụ, phiếu số và hình thức hóa:** VD4/HT6 trực giác; n5,ell8; h0 không phải phân phối xác suất.

**Kết nối vào–ra:** Vai trò danh mục/nội dung → quan hệ hai điểm → phép cộng uy tín từ h ở vòng đầu.

**Nguồn và vị trí:** NG1 §5.5.2, Ví dụ 5.14, Hình 5.18, tr.205–206/PDF31–32.

**Thời lượng:** 2 phút.

**Ghi chú học thuật dự kiến:**

<!-- public-notes:start -->
G5 có năm trang và tám cạnh, khác G4 ở việc C trỏ E thay vì A. Uy tín cộng điểm của các nguồn liên kết, còn trung tâm cộng điểm của các đích liên kết. Mỗi trang đều có cả hai điểm; hub và authority là hai vai trò, không phải hai tập trang loại trừ nhau. Phép cập nhật luân phiên hiện thực hóa quan hệ hỗ trợ lẫn nhau: $h$ quyết định $a$, rồi $a$ mới quyết định $h$ mới. Khởi tạo toàn $1$ là quy ước thuật toán sách; tổng ban đầu bằng $5$ và không mang ý nghĩa xác suất.
<!-- public-notes:end -->

### lec04-s05-03 — Lượt cập nhật uy tín thứ nhất

**Vai trò, mục tiêu, đầu vào và sản phẩm:** Chạy tay; MT4. Đầu vào: G5,h0. Sản phẩm: cộng đúng cạnh vào và chuẩn hóa max.

**Luận điểm trung tâm:** Uy tín thu điểm trung tâm từ các cạnh vào rồi chuẩn hóa toàn vector.

**Nội dung hiển thị dự kiến:**

<!-- public-slide:start -->
$h^0=(1,1,1,1,1)^\mathsf T$; G5 giữ nguyên.

| Trang | Nguồn liên kết vào | Uy tín thô $\tilde a_i$ | $a_i^1=\tilde a_i/2$ |
|---|---|---:|---:|
| A | B | $1$ | $1/2$ |
| B | A,D | $2$ | $1$ |
| C | A,D | $2$ | $1$ |
| D | A,B | $2$ | $1$ |
| E | C | $1$ | $1/2$ |

Giá trị thô lớn nhất bằng 2; chia toàn vector cho 2.
<!-- public-slide:end -->

**Bố cục đã chọn:** Bảng năm hàng chiếm80%; khởi tạo phía trên10%, dòng chuẩn hóa dưới10%. Các hàng theo A–E như đồ thị.

**Trọng tâm và thứ tự đọc:** Từ nguồn liên kết vào → tổng h0 → chia cùng mẫu2 trên mọi hàng.

**Lý do phù hợp sinh viên năm 2:** Cột nguồn chỉ rõ phép cộng tạo mỗi điểm; cột thô/chuẩn hóa tránh nhầm việc chia max với chia bậc ra.

**Giới hạn bố cục và phân chia nội dung:** Không đưa h mới trên trang này; E có điểm uy tín dương dù không có cạnh ra phải giữ trong bảng.

**Ví dụ, phiếu số và hình thức hóa:** VD4 lượt a1; phép cộng $\tilde a_i=\sum_{j\to i}h_j^0$. Chuẩn max thao tác trực tiếp trước định nghĩa tổng quát.

**Kết nối vào–ra:** Khởi tạo h → a1 → dùng ngay a1 cho cập nhật trung tâm.

**Nguồn và vị trí:** NG1 VD5.15/Hình 5.20, tr.207/PDF33.

**Thời lượng:** 3 phút.

**Ghi chú học thuật dự kiến:**

<!-- public-notes:start -->
B nhận từ A, D nên điểm thô bằng $1+1=2$; D nhận từ A, B cũng bằng $2$. E chỉ nhận từ C, điểm thô bằng $1$. Chia từng thành phần cho giá trị lớn nhất là $2$ thu được $a^1=(1/2,1,1,1,1/2)^\mathsf T$. HITS cộng điểm trung tâm theo từng cạnh vào, không lấy trung bình và không chia số cạnh ra của nguồn. E không có cạnh ra vẫn có thể có uy tín vì có cạnh vào.
<!-- public-notes:end -->

### lec04-s05-04 — Lượt cập nhật trung tâm thứ nhất

**Vai trò, mục tiêu, đầu vào và sản phẩm:** Chạy tay; MT4. Đầu vào: a1 mới. Sản phẩm: cộng đúng uy tín mới theo cạnh ra.

**Luận điểm trung tâm:** Trung tâm cộng uy tín mới của các đích rồi chuẩn hóa toàn vector.

**Nội dung hiển thị dự kiến:**

<!-- public-slide:start -->
Dùng $a^1=(1/2,1,1,1,1/2)^\mathsf T$.

| Trang | Tổng uy tín theo cạnh ra | Trung tâm thô $\tilde h_i$ | $h_i^1=\tilde h_i/3$ |
|---|---|---:|---:|
| A | $1+1+1$ | $3$ | $1$ |
| B | $1/2+1$ | $3/2$ | $1/2$ |
| C | $1/2$ | $1/2$ | $1/6$ |
| D | $1+1$ | $2$ | $2/3$ |
| E | $0$ | $0$ | $0$ |

Giá trị thô lớn nhất bằng 3. Bước trung tâm sử dụng uy tín vừa cập nhật.
<!-- public-slide:end -->

**Bố cục đã chọn:** Giữ bảng năm hàng chiếm80% và vị trí như S05-03; vector a1 phía trên; câu về thứ tự cập nhật phía dưới.

**Trọng tâm và thứ tự đọc:** Đọc a1 → cộng uy tín ở đích cạnh ra → chia toàn vector cho3.

**Lý do phù hợp sinh viên năm 2:** Bảng giữ khung nhưng đổi ý nghĩa nguồn tổng, giúp đối chiếu cạnh vào/cạnh ra; nhãn a1 mới ngăn dùng a0.

**Giới hạn bố cục và phân chia nội dung:** Chỉ vòng 1, không thêm công thức ma trận. Tại E hiển thị0 để tránh phép chia bậc ra0 không có trong HITS.

**Ví dụ, phiếu số và hình thức hóa:** VD4 lượt h1; $\tilde h_i=\sum_{i\to j}a_j^1$. Max 3 khác max 2 ở lượt uy tín.

**Kết nối vào–ra:** a1 → h1 → lặp lại cùng hai quy tắc với điểm đã cải thiện.

**Nguồn và vị trí:** NG1 VD5.15/Hình 5.20, tr.207/PDF33.

**Thời lượng:** 3 phút.

**Ghi chú học thuật dự kiến:**

<!-- public-notes:start -->
A trỏ B, C, D, ba trang có uy tín bằng $1$ nên tổng bằng $3$. B trỏ A, D và nhận $1/2+1=3/2$. C chỉ trỏ E nên nhận $1/2$; E không có cạnh ra nên tổng rỗng bằng $0$. Chia từng thành phần của vector trung tâm thô cho $3$ thu được $h^1=(1,1/2,1/6,2/3,0)^\mathsf T$. Nếu dùng $a^0$ toàn $1$, trung tâm thô sẽ bằng $(3,2,1,2,0)^\mathsf T$, khác thuật toán luân phiên đã chọn.
<!-- public-notes:end -->

### lec04-s05-05 — Vòng lặp HITS thứ hai

**Vai trò, mục tiêu, đầu vào và sản phẩm:** Chạy tay và nhận diện trạng thái; MT4. Đầu vào: h1. Sản phẩm: tái tạo một cập nhật ở vòng 2 và đọc hai vector mới.

**Luận điểm trung tâm:** Hai lượt cập nhật luân phiên dùng kết quả vừa tạo ở lượt trước.

**Nội dung hiển thị dự kiến:**

<!-- public-slide:start -->
$h^1=(1,1/2,1/6,2/3,0)^\mathsf T$.

| Trang | $\tilde a$ | $a^2$ | $h^2$ |
|---|---:|---:|---:|
| A | $1/2$ | $3/10$ | $1$ |
| B | $5/3$ | $1$ | $12/29$ |
| C | $5/3$ | $1$ | $1/29$ |
| D | $3/2$ | $9/10$ | $20/29$ |
| E | $1/6$ | $1/10$ | $0$ |

Tại A: $\tilde h_A=a_B^2+a_C^2+a_D^2=29/10$; đây là giá trị lớn nhất của vector trung tâm thô. Hai vector thay đổi qua mỗi vòng.
<!-- public-slide:end -->

**Bố cục đã chọn:** Vector h1 phía trên15%; bảng năm hàng giữa65%; phép tính tại A dưới20%. Hàng/nhãn nhất quán hai trang trước.

**Trọng tâm và thứ tự đọc:** Từ h1 tính a thô → chuẩn a2 theo max 5/3 → theo một tổng h thô → đọc h2.

**Lý do phù hợp sinh viên năm 2:** Một bước đầy đủ ở vòng đầu cho phép rút gọn vòng 2 mà vẫn truy kết quả; cột thô duy trì phân biệt trước/sau chuẩn hóa.

**Giới hạn bố cục và phân chia nội dung:** Không đặt cả năm vector của sách trên một trang; vector trung tâm thô đầy đủ được ghi trong ghi chú.

**Ví dụ, phiếu số và hình thức hóa:** VD4 vòng 2. Max uy tín5/3; max trung tâm29/10. Phân số giữ chính xác.

**Kết nối vào–ra:** Hai vòng cụ thể → quy tắc ma trận tổng quát và định nghĩa chuẩn hóa.

**Nguồn và vị trí:** NG1 VD5.15/Hình 5.20, tr.207/PDF33.

**Thời lượng:** 3 phút.

**Ghi chú học thuật dự kiến:**

<!-- public-notes:start -->
Uy tín thô tại B bằng $h_A^1+h_D^1=1+2/3=5/3$, là giá trị lớn nhất. Tại D, điểm thô bằng $1+1/2=3/2$; chia cho $5/3$ được $9/10$. Trung tâm thô tính từ $a^2$ là $(29/10,6/5,1/10,2,0)^\mathsf T$. Chia từng thành phần cho $29/10$ thu được $h^2$ trong bảng. Hai lần chuẩn hóa dùng hai mẫu khác nhau. Các giá trị nhỏ dần ở vai trò trung tâm của C và uy tín của E là quan sát của ví dụ, chưa phải chứng minh cho mọi đồ thị.
<!-- public-notes:end -->

### lec04-s05-06 — Ma trận liên kết của HITS

**Vai trò, mục tiêu, đầu vào và sản phẩm:** Hình thức hóa; MT4. Đầu vào: tổng theo hai chiều trên G5. Sản phẩm: lập L và nối với M0 của PageRank.

**Luận điểm trung tâm:** L có hàng nguồn và trọng số cạnh1; nó khác ma trận PageRank chia theo bậc ra.

**Nội dung hiển thị dự kiến:**

<!-- public-slide:start -->
$L_{ij}=1$ khi $i\to j$, bằng 0 nếu không; hàng là trang nguồn.

$$L=\begin{pmatrix}0&1&1&1&0\\1&0&0&1&0\\0&0&0&0&1\\0&1&1&0&0\\0&0&0&0&0\end{pmatrix},\qquad
\tilde a=L^\mathsf Th,\quad\tilde h=La.$$

| Biểu diễn | Vị trí của cạnh $i\to j$ | Giá trị |
|---|---|---|
| HITS: $L$ | Hàng $i$, cột $j$ | $1$ |
| PageRank: $M_0$ | Hàng $j$, cột $i$ | $1/d_i$ |

HITS cộng điểm qua cạnh; không chia bậc ra.
<!-- public-slide:end -->

**Bố cục đã chọn:** Ma trận có nhãn hàng/cột A–E bên trái55%; hai phép nhân và bảng đối chiếu ngắn bên phải45%. Hàng A và cột nguồn PageRank được giải thích bằng nhãn chữ.

**Trọng tâm và thứ tự đọc:** Xác định hàng nguồn của L → đọc chuyển vị khi tính a → đối chiếu với M0.

**Lý do phù hợp sinh viên năm 2:** Cùng cạnh có vị trí đảo và trọng số khác ở hai mô hình; bảng giúp sinh viên không dùng lại ma trận xác suất cho HITS.

**Giới hạn bố cục và phân chia nội dung:** Chỉ ma trận G5; không đưa LLT lên trang này. Bảng hai hàng đủ đối chiếu, không thêm lịch sử ký hiệu nguồn.

**Ví dụ, phiếu số và hình thức hóa:** HT6; VD4 L5×5. h,a đều vector cột5×1; hai tích cùng trả vector5×1.

**Kết nối vào–ra:** Phép cộng vết chạy → nhân ma trận đúng kiểu → chuẩn hóa và thuật toán tổng quát.

**Nguồn và vị trí:** NG1 §5.5.2/Hình 5.19, tr.205–206/PDF31–32.

**Thời lượng:** 3 phút.

**Ghi chú học thuật dự kiến:**

<!-- public-notes:start -->
Phần tử $(L^\mathsf T)_{ji}=L_{ij}$ biểu diễn cạnh $i\to j$; khi nhân với $h_i$, đóng góp được cộng vào $a_j$. Tích $La$ cộng uy tín của các đích ở mỗi hàng nguồn. So với PageRank, $L^\mathsf T$ có giá trị $1$ tại cạnh, còn $M_0$ dùng $1/d_i$ tại cột nguồn $i$. Dùng $M_0$ cho uy tín vòng đầu cho $(1/2,5/6,5/6,5/6,1)^\mathsf T$, khác vector thô $(1,2,2,2,1)^\mathsf T$ của HITS.
<!-- public-notes:end -->

### lec04-s05-07 — Chuẩn hóa điểm HITS

**Vai trò, mục tiêu, đầu vào và sản phẩm:** Cầu nối và điều kiện biên; MT4. Đầu vào: hai vector thô. Sản phẩm: giải thích chuẩn max và phạm vi định nghĩa.

**Luận điểm trung tâm:** Chuẩn max giữ tỷ lệ và thứ hạng, nhưng không đặt tổng điểm bằng 1.

**Nội dung hiển thị dự kiến:**

<!-- public-slide:start -->
Với vector không âm $q$ có $\max_iq_i>0$:
$$N(q)=\frac{q}{\max_iq_i}.$$

Chuẩn hóa giữ tỷ lệ và thứ hạng các thành phần; giá trị lớn nhất trở thành 1.

Ví dụ: $N\big((1,2,2,2,1)^\mathsf T\big)=(1/2,1,1,1,1/2)^\mathsf T$; tổng kết quả bằng 4.

Điểm HITS không là phân phối xác suất. Với đồ thị không cạnh, vector thô bằng 0 nên phép chuẩn hóa không xác định.
<!-- public-slide:end -->

**Bố cục đã chọn:** Định nghĩa chuẩn hóa phía trên35%; cặp vector thô/chuẩn hóa giữa40%; ý nghĩa tổng và biên dưới25%.

**Trọng tâm và thứ tự đọc:** Đọc điều kiện max dương → thao tác chia cùng số → kiểm tỷ lệ và tổng.

**Lý do phù hợp sinh viên năm 2:** Ví dụ tổng 4 chống nhầm điểm HITS phải tổng 1; điều kiện max dương gắn phép chia với ca biên cụ thể.

**Giới hạn bố cục và phân chia nội dung:** Chỉ chuẩn max đã chọn; các chuẩn khác không cần lên slide. Đồ thị ít nhất một cạnh là giả thiết của giả mã kế tiếp.

**Ví dụ, phiếu số và hình thức hóa:** HT6/VD4 a1; giá trị 0,1 và hòa có ý nghĩa, giữ nguyên.

**Kết nối vào–ra:** Hai phép nhân → phép N xác định → thuật toán lặp đủ điều kiện vào/ra.

**Nguồn và vị trí:** NG1 §5.5.2, tr.205–207; ca không cạnh suy trực tiếp từ phép chuẩn hóa.

**Thời lượng:** 2 phút.

**Ghi chú học thuật dự kiến:**

<!-- public-notes:start -->
Chia tất cả thành phần cho cùng một số dương giữ mọi tỷ lệ $q_i/q_j$ khi mẫu khác $0$, đồng thời giữ thứ tự lớn nhỏ. Do đó chuẩn hóa kiểm soát độ lớn số mà không thay ý nghĩa thứ hạng trong từng vector. Sách dùng giá trị lớn nhất; chuẩn tổng bằng $1$ hoặc chuẩn Euclid tạo giá trị khác nên không thể trộn các vết số. Với đồ thị không cạnh, cả hai tích bằng $0$ và quy ước chuẩn hóa bằng giá trị lớn nhất không xác định.
<!-- public-notes:end -->

### lec04-s05-08 — Thuật toán HITS với cập nhật luân phiên

**Vai trò, mục tiêu, đầu vào và sản phẩm:** Đặc tả và thuật toán; MT4. Đầu vào: L và N. Sản phẩm: đọc đúng trạng thái cũ/mới, ngưỡng và ca biên.

**Luận điểm trung tâm:** HITS trả hai vector, dùng uy tín mới khi cập nhật trung tâm và kiểm cả hai thay đổi.

**Nội dung hiển thị dự kiến:**

<!-- public-slide:start -->
Đầu vào: đồ thị có ít nhất một cạnh; $\tau>0$, số vòng tối đa $K\ge1$.

```text
h ← vector toàn 1; a ← vector toàn 1
với t = 0, ..., K - 1:
    a_new ← N(L chuyển vị * h)
    h_new ← N(L * a_new)
    Delta_a ← max |a_new[i] - a[i]|
    Delta_h ← max |h_new[i] - h[i]|
    a ← a_new; h ← h_new
    nếu max(Delta_a, Delta_h) ≤ tau:
        trả về (h, a, đạt ngưỡng)
trả về (h, a, hết số vòng)
```

Đầu ra gồm hai vector và trạng thái dừng; đồ thị không cạnh trả trạng thái không xác định khi chuẩn hóa bằng giá trị lớn nhất.
<!-- public-slide:end -->

**Bố cục đã chọn:** Dòng đầu vào trên15%; giả mã giữa70%; đầu ra và biên dưới15%. Dùng khối mã chung, a_new được nhắc rõ tại dòng tính h_new.

**Trọng tâm và thứ tự đọc:** Đọc điều kiện → khởi tạo → a mới từ h cũ → h mới từ a mới → kiểm cả hai vector.

**Lý do phù hợp sinh viên năm 2:** Sinh viên đã biết vòng lặp/mảng; tên cũ/mới làm hiện phụ thuộc tuần tự khác với hai cập nhật dùng chung trạng thái cũ.

**Giới hạn bố cục và phân chia nội dung:** Giữ10 dòng giả mã; chi tiết thực hiện nhân bằng cạnh thuộc S05-10. Không đưa framework hay chương trình mới.

**Ví dụ, phiếu số và hình thức hóa:** HT6, chuẩn vô cùng=max trị tuyệt đối. Khởi tạo a0=h0=1; hai ngưỡng dùng cùng tau.

**Kết nối vào–ra:** Vết chạy và ma trận → quy trình có đầu ra/điều kiện dừng → lập luận đúng và giới hạn.

**Nguồn và vị trí:** NG1 §5.5.2, tr.206–207; giả mã cụ thể hóa thứ tự sách, điều kiện dừng và biên được nêu tường minh.

**Thời lượng:** 4 phút.

**Ghi chú học thuật dự kiến:**

<!-- public-notes:start -->
HITS cập nhật uy tín trước, rồi tính trung tâm từ uy tín vừa cập nhật. Chuẩn hóa sau từng phép nhân tạo đúng vết chạy của Ví dụ 5.15. Với ít nhất một cạnh và khởi tạo dương, mỗi trang có cạnh ra đóng góp dương cho ít nhất một đích, rồi nhận lại một giá trị dương qua cạnh ấy. Lập luận này tiếp tục ở mọi vòng, nên các vector thô không bằng $0$ và phép chuẩn hóa hợp lệ. Mỗi vòng giữ $h$, $a$ không âm và có giá trị lớn nhất bằng $1$. Điều kiện dừng kiểm tra thay đổi của cả hai vector; hết $K$ vòng không đồng nghĩa đã đạt ngưỡng hoặc có chứng nhận sai số tới giới hạn.
<!-- public-notes:end -->

### lec04-s05-09 — Điểm ổn định và giới hạn của HITS

**Vai trò, mục tiêu, đầu vào và sản phẩm:** Lập luận đúng và phạm vi bảo đảm; MT4. Đầu vào: HT6. Sản phẩm: giải thích quan hệ hai bước, tránh duy nhất vô điều kiện.

**Luận điểm trung tâm:** Quan hệ vector riêng giải thích điểm ổn định nhưng không tự bảo đảm duy nhất trên mọi đồ thị.

**Nội dung hiển thị dự kiến:**

<!-- public-slide:start -->
Mỗi cạnh $i\to j$ đóng góp $h_i$ vào uy tín của $j$, rồi đóng góp uy tín mới $a_j$ vào trung tâm của $i$.

Ở điểm ổn định:
$$a\propto L^\mathsf Th,\qquad h\propto La,$$
$$h\propto LL^\mathsf Th,\qquad a\propto L^\mathsf TLa.$$

Chuẩn hóa giữ tỷ lệ trong mỗi vector. Sự tồn tại một hướng giới hạn duy nhất cần điều kiện bổ sung; không suy từ việc tính đúng vài vòng.
<!-- public-slide:end -->

**Bố cục đã chọn:** Sơ đồ một cạnh và hai chiều đóng góp trái35%; chuỗi hai dòng tỷ lệ phải65%; giới hạn kết luận nằm đáy. Hệ số chuẩn hóa được giải thích trong ghi chú.

**Trọng tâm và thứ tự đọc:** Theo đóng góp cạnh → ghép hai quan hệ → đọc điều kiện giới hạn của mệnh đề.

**Lý do phù hợp sinh viên năm 2:** Sinh viên đã biết phép nhân ma trận; quan hệ ghép nối cơ chế với đại số mà không yêu cầu kiểm tra kiến thức phổ chưa chuẩn bị.

**Giới hạn bố cục và phân chia nội dung:** Không đặt định lý phổ hoặc đa thức trên mặt slide. Điều kiện đủ và nghiệm G5 nằm trong ghi chú học thuật; không hỏi thi thuật ngữ phổ ở đây.

**Ví dụ, phiếu số và hình thức hóa:** HT6; tỷ lệ biểu diễn cùng hướng sau nhân số dương. Không xem LLT là cấu trúc cần tạo để thực thi.

**Kết nối vào–ra:** Giả mã đúng phép cộng → quan hệ điểm ổn định → cách thực thi thưa và chi phí.

**Nguồn và vị trí:** NG1 §5.5.2, tr.206–208; NG3 trang56–58 chỉ đối chiếu, sửa khẳng định duy nhất quá mạnh.

**Thời lượng:** 3 phút.

**Ghi chú học thuật dự kiến:**

<!-- public-notes:start -->
Ở điểm cố định, $h=\lambda La$ và $a=\mu L^\mathsf Th$, với $\lambda,\mu>0$ là các hệ số chuẩn hóa. Thế một quan hệ vào quan hệ kia cho $h=\lambda\mu LL^\mathsf Th$ và tương tự cho $a$.

Một điều kiện đủ để phép lặp có hướng giới hạn duy nhất là trị riêng lớn nhất của ma trận đối xứng nửa xác định dương $LL^\mathsf T$ chỉ có một hướng riêng độc lập, và khởi tạo có thành phần khác $0$ theo hướng ấy. Trong phân tích theo các hướng riêng, phần gắn với trị riêng nhỏ hơn tăng chậm hơn, nên tỷ lệ của nó giảm sau chuẩn hóa. Nếu trị riêng lớn nhất có nhiều hướng độc lập, hướng giới hạn có thể phụ thuộc khởi tạo. Đây là phác thảo điều kiện đủ, không phải chứng minh phổ tổng quát.

Trên G5, giới hạn theo thứ tự A, B, C, D, E là $h\approx(1,0.3583,0,0.7165,0)^\mathsf T$ và $a\approx(0.2087,1,1,0.7913,0)^\mathsf T$.
<!-- public-notes:end -->

### lec04-s05-10 — Chi phí HITS trên đồ thị thưa

**Vai trò, mục tiêu, đầu vào và sản phẩm:** Đánh giá chi phí; MT5. Đầu vào: hai phép cập nhật. Sản phẩm: đếm hai lượt cạnh và lý giải không lập tích ma trận.

**Luận điểm trung tâm:** Hai phép nhân thưa được thực thi bằng hai lượt cạnh, không cần tạo tích ma trận.

**Nội dung hiển thị dự kiến:**

<!-- public-slide:start -->
Mô hình: danh sách cạnh, $n$ đỉnh, $\ell$ cạnh; phép toán vô hướng chi phí đơn vị.

| Công việc mỗi vòng | Phép đếm |
|---|---:|
| Cộng $h$ tại nguồn vào $a$ tại đích | $\ell$ cạnh |
| Cộng $a$ mới tại đích vào $h$ tại nguồn | $\ell$ cạnh |
| Chuẩn hóa, so sánh các vector | Số lượt cố định trên $n$ đỉnh |

Thời gian $\Theta(n+\ell)$ mỗi vòng; bộ nhớ phụ $\Theta(n)$, đầu vào $\Theta(n+\ell)$.

Hai lượt cạnh đáp ứng nhu cầu tính hai vector trên đồ thị lớn. Không tạo $LL^\mathsf T$ hoặc $L^\mathsf TL$ để chạy vì chúng có thể đặc hơn $L$.
<!-- public-slide:end -->

**Bố cục đã chọn:** Mô hình trên15%; bảng ba hàng giữa60%; kết quả và lưu ý tích ma trận dưới25%.

**Trọng tâm và thứ tự đọc:** Gắn mỗi phép nhân với một lượt cạnh → cộng phần đỉnh → tách bộ nhớ phụ/đầu vào.

**Lý do phù hợp sinh viên năm 2:** Cùng mô hình chi phí PageRank giúp so sánh trực tiếp; hai lượt cạnh được đếm trước khi rút gọn bậc tiệm cận.

**Giới hạn bố cục và phân chia nội dung:** Không suy cùng bậc là cùng thời gian thực hay cùng số vòng. K vòng và nguy cơ đặc hóa giải thích trong ghi chú.

**Ví dụ, phiếu số và hình thức hóa:** HT6; VD4 n5,ell8 chỉ là kiểm số đối tượng, không số đo hiệu năng. K vòng Theta(K(n+ell)).

**Kết nối vào–ra:** Quan hệ điểm ổn định → thực thi bằng hai lượt cạnh, thu hồi giới hạn đồ thị lớn ở S05-01 → kiểm một vòng HITS và lựa chọn phương pháp theo cùng mô hình chi phí.

**Nguồn và vị trí:** NG1 §5.5.2, tr.206; phép đếm trực tiếp theo giả mã đã đặc tả.

**Thời lượng:** 2 phút.

**Ghi chú học thuật dự kiến:**

<!-- public-notes:start -->
Mỗi cạnh $i\to j$ được dùng một lần để cộng $h_i$ vào $a_j$, sau đó một lần để cộng $a_j$ mới vào $h_i$. Hai lượt này cần $2\ell$ phép cộng trọng số, còn chuẩn hóa và kiểm thay đổi cần số lượt cố định theo $n$. Hệ số $2$ biến mất trong bậc tiệm cận nhưng vẫn mô tả lượng công việc khác PageRank. Tích $LL^\mathsf T$ có thể nối nhiều cặp trang cùng chung đích, nên số phần tử khác $0$ có thể tăng. Hai phép nhân luân phiên khai thác cạnh trực tiếp, tránh lưu tích ấy khi tính hai vector trên đồ thị lớn.
<!-- public-notes:end -->

### lec04-s05-11 — Kiểm tra một vòng HITS

**Vai trò, mục tiêu, đầu vào và sản phẩm:** Kiểm tra riêng S05; MT4. Đầu vào: G5,a1. Sản phẩm: tính h_B và bác cách chia bậc ra.

**Luận điểm trung tâm:** Tổng HITS không chia bậc ra; chuẩn hóa dùng một số chung cho toàn vector.

**Nội dung hiển thị dự kiến:**

<!-- public-slide:start -->
G5: A→B,C,D; B→A,D; C→E; D→B,C; E không có cạnh ra.

$a^1=(1/2,1,1,1,1/2)^\mathsf T$; trung tâm thô lớn nhất bằng 3.

**Câu hỏi:**
1. Tính trung tâm thô và điểm chuẩn hóa của B.
2. Giải thích vì sao không chia thêm cho hai liên kết ra của B.
3. Xác định điểm trung tâm của E sau vòng này.
<!-- public-slide:end -->

**Bố cục đã chọn:** G5 trái45%; vector, max và ba yêu cầu phải55%. Cạnh B→A,D được phân biệt bằng nét đậm và nhãn, không lộ tổng.

**Trọng tâm và thứ tự đọc:** Theo hai cạnh ra của B → đọc a1 tại đích → chuẩn hóa chung; sau đó xét tổng rỗng tại E.

**Lý do phù hợp sinh viên năm 2:** B có hai đích uy tín khác nhau nên lỗi đổi phép tổng thành trung bình tạo đáp số khác; E kiểm cách xử lý nút không cạnh ra.

**Giới hạn bố cục và phân chia nội dung:** Ba nhiệm vụ ngắn cùng một vòng, không hỏi phổ. Giữ toàn bộ dữ kiện để không phụ thuộc trí nhớ bảng trước.

**Ví dụ, phiếu số và hình thức hóa:** VD4/HT6; không dùng M0 hoặc bước nhảy trong HITS.

**Kết nối vào–ra:** Cơ chế HITS đã kiểm → đối chiếu ba mục tiêu xếp hạng ở S06.

**Nguồn và vị trí:** NG1 VD5.15, tr.207; câu hỏi áp dụng trực tiếp.

**Thời lượng:** 3 phút.

**Nhiệm vụ và tiêu chí nội bộ:** Slide kiểm tra riêng của phần.

- Câu hỏi/đề: Ba yêu cầu như nội dung hiển thị trên G5 và a1.
- Đáp án/gợi ý: B: thô $3/2$, chuẩn $1/2$; không chia bậc ra vì định nghĩa HITS là tổng. E: $h_E^1=0$.
- Tiêu chí đánh giá: Dùng a mới, cộng hai uy tín, chỉ chia max toàn vector; phân biệt điểm trung tâm0 với điểm uy tín.
- Phân bổ hoạt động: Tính1 phút, giải thích1 phút, đối chiếu1 phút; tổng3 phút.

**Ghi chú học thuật dự kiến:**

<!-- public-notes:start -->
Trung tâm thô của B là $a_A^1+a_D^1=1/2+1=3/2$. Chia giá trị này cho giá trị lớn nhất của vector thô là $3$ thu được $h_B^1=1/2$. HITS định nghĩa trung tâm bằng tổng uy tín các đích, nên chia bậc ra là thay đổi mô hình. E không có đích liên kết, tổng rỗng bằng $0$ và điểm trung tâm vẫn bằng $0$ sau chuẩn hóa. Không suy từ $h_E=0$ rằng mọi điểm uy tín của nút cụt đều bằng $0$.
<!-- public-notes:end -->

## S06. So sánh các phương pháp xếp hạng

Tổng hợp và kết luận. Đầu ra các cụm → đối chiếu cùng tiêu chí → giải quyết lại ba tình huống của sách → năm nhiệm vụ tự kiểm. Hai nhiệm vụ ở S06-03, ba nhiệm vụ ở S06-04; S06-04 là slide kiểm tra riêng. Không đưa khái niệm trọng tâm mới.

Phân bổ: 4 slide, 10 phút.

### lec04-s06-01 — Đối chiếu ý nghĩa các điểm xếp hạng

**Vai trò, mục tiêu, đầu vào và sản phẩm:** Tổng hợp; MT5. Đầu vào: HT1,HT5,HT6. Sản phẩm: phân biệt đầu ra và thông tin thêm của mỗi phương pháp.

**Luận điểm trung tâm:** Các phương pháp khác nhau ở ý nghĩa đầu ra và thông tin điều khiển.

**Nội dung hiển thị dự kiến:**

<!-- public-slide:start -->
| Phương pháp | Đầu ra | Thông tin quyết định |
|---|---|---|
| PageRank theo chủ đề | Một phân phối điểm theo ngữ cảnh | Phân phối dịch chuyển $v$ |
| TrustRank | Một phân phối điểm từ tập tin cậy | Hạt giống được đánh giá bên ngoài |
| Spam Mass | Chênh lệch tương đối giữa $r$ và $\rho$ | Hai vector cùng mô hình, $r_i>0$ |
| HITS | Hai vector trung tâm và uy tín | Tổng theo cạnh vào và cạnh ra |

Điểm uy tín HITS và điểm tin cậy TrustRank có ý nghĩa khác nhau.
<!-- public-slide:end -->

**Bố cục đã chọn:** Bảng ba cột chiếm85%; câu phân biệt thuật ngữ ở đáy15%. Mọi hàng so cùng ba tiêu chí, không gán màu tốt/xấu.

**Trọng tâm và thứ tự đọc:** Đọc đầu ra của từng phương pháp → thông tin điều khiển → phân biệt hai từ uy tín/tin cậy.

**Lý do phù hợp sinh viên năm 2:** Bảng thống nhất tiêu chí sau khi học cơ chế giúp sinh viên chọn theo nhu cầu, không xếp thuật toán thành mức nâng cấp chung.

**Giới hạn bố cục và phân chia nội dung:** Không thêm thuộc tính hiệu năng chưa phân tích. Chi phí và tình huống thu hồi ở trang sau.

**Ví dụ, phiếu số và hình thức hóa:** HT1,HT5,HT6; không có ví dụ số mới.

**Kết nối vào–ra:** Ba cụm kiến thức → bảng đầu ra → quyết định trên tình huống mở bài.

**Nguồn và vị trí:** NG1 §5.3.2,§5.4.4–5,§5.5.1–2, tr.196–207.

**Thời lượng:** 2 phút.

**Ghi chú học thuật dự kiến:**

<!-- public-notes:start -->
PageRank theo chủ đề và TrustRank dùng cùng họ phương trình nhưng nhận hai loại thông tin ưu tiên khác nhau. Spam Mass cần cặp điểm để tính chỉ số chênh lệch, không phải phép lặp riêng. HITS đổi từ một phân phối sang hai vai trò cấu trúc. Uy tín HITS có thể cao do quan hệ với các trung tâm có điểm cao, không thay thế đánh giá nội dung của hạt giống TrustRank.
<!-- public-notes:end -->

### lec04-s06-02 — Lựa chọn phương pháp theo yêu cầu dữ liệu

**Vai trò, mục tiêu, đầu vào và sản phẩm:** Thu hồi tình huống; MT5. Đầu vào: bảng so sánh. Sản phẩm: chọn phương pháp kèm điều kiện và giới hạn tài nguyên.

**Luận điểm trung tâm:** Lựa chọn phương pháp phụ thuộc yêu cầu và giả thiết, không chỉ bậc chi phí.

**Nội dung hiển thị dự kiến:**

<!-- public-slide:start -->
| Yêu cầu đã xét | Phương pháp và điều kiện |
|---|---|
| “jaguar” theo động vật hoặc ô tô | PageRank theo chủ đề, khi đã có chủ đề hoặc trọng số |
| Đánh giá ảnh hưởng liên kết thao túng | TrustRank và Spam Mass, khi có tập tin cậy phù hợp |
| Danh sách và nội dung học phần | HITS, khi cần cả điểm trung tâm và uy tín |

Các phép lặp đều khai thác đồ thị thưa. Cùng bậc chi phí mỗi vòng không bảo đảm cùng số vòng hoặc cùng thời gian thực.
<!-- public-slide:end -->

**Bố cục đã chọn:** Bảng hai cột ba hàng giữa80%; câu chi phí dưới20%. Tên tình huống trùng mở đầu và nguồn sách.

**Trọng tâm và thứ tự đọc:** Xác định yêu cầu → chọn đầu ra → kiểm điều kiện đầu vào → đọc giới hạn chi phí.

**Lý do phù hợp sinh viên năm 2:** Ba tình huống quen được dùng lại, không thêm lĩnh vực ứng dụng phải học; điều kiện kèm lựa chọn ngăn học thuộc tên thuật toán.

**Giới hạn bố cục và phân chia nội dung:** Không bổ sung thuật toán mới hoặc kết luận thực nghiệm. Thời gian hoàn thành hệ tìm kiếm nằm ngoài mô hình.

**Ví dụ, phiếu số và hình thức hóa:** HT3,HT5,HT6; ví dụ định tính đã dùng. Không có phiếu số mới.

**Kết nối vào–ra:** Đối chiếu các phương pháp → áp vào vấn đề đầu bài → tự kiểm khả năng tính và giải thích.

**Nguồn và vị trí:** NG1 §5.3.1,§5.4.3–5,VD5.13; phép đếm đã xây ở S02 và S05.

**Thời lượng:** 2 phút.

**Ghi chú học thuật dự kiến:**

<!-- public-notes:start -->
Nhu cầu theo chủ đề còn phụ thuộc độ phù hợp của tập dịch chuyển hoặc trọng số. TrustRank cần hạt giống đáng tin và đủ độ phủ; Spam Mass không tự tạo nhãn đúng chắc chắn. HITS cần đầu ra hai vai trò nên không thay thế trực tiếp chỉ số tin cậy. Chi phí tuyến tính theo $n+\ell$ mỗi vòng chỉ là một tiêu chí; số vòng, độ chính xác dừng và chi phí chuẩn bị thông tin bên ngoài vẫn khác nhau.
<!-- public-notes:end -->

### lec04-s06-03 — Tự kiểm về mô hình và chi phí

**Vai trò, mục tiêu, đầu vào và sản phẩm:** Tự kiểm tổng hợp1–2; MT1,MT5. Đầu vào: phân phối dịch chuyển và phép đếm. Sản phẩm: phân biệt thay mô hình/biểu diễn và hiểu phạm vi chi phí.

**Luận điểm trung tâm:** Thay phân phối dịch chuyển không thay đồ thị; cùng chi phí tiệm cận không đồng nhất thời gian thực.

**Nội dung hiển thị dự kiến:**

<!-- public-slide:start -->
**Câu hỏi:**
1. Trên cùng G4, giữ $\beta=4/5$ và đổi tập dịch chuyển từ {B,D} sang {A}. Xác định đại lượng phải đổi và đại lượng được giữ nguyên trong $r'=\beta M_0r+(1-\beta)v$.
2. PageRank theo chủ đề và HITS đều có chi phí mỗi vòng $\Theta(n+\ell)$. Đánh giá kết luận: “Hai thuật toán luôn có cùng thời gian chạy”. Nêu những đại lượng còn thiếu.
<!-- public-slide:end -->

**Bố cục đã chọn:** Hai khung nhiệm vụ xếp dọc, mỗi khung khoảng50%; công thức ở trong khung1. Không đặt bảng đáp án bên cạnh.

**Trọng tâm và thứ tự đọc:** Nhiệm vụ1 xét mô hình điểm; nhiệm vụ2 xét phạm vi phép đếm; không ghép hai câu vào một lập luận dài.

**Lý do phù hợp sinh viên năm 2:** Hai thao tác khác nhau nhưng dùng đầu vào đã học; câu2 kiểm khả năng bảo toàn giả thiết khi chuyển từ tiệm cận sang hiệu năng.

**Giới hạn bố cục và phân chia nội dung:** Đây là hai trong năm nhiệm vụ tự kiểm S06; quiz riêng của phần là trang kế tiếp. Mỗi câu có lời giải trong ghi chú.

**Ví dụ, phiếu số và hình thức hóa:** VD1/HT1 và HT3/HT6; không cần tính lại nghiệm S={A}.

**Kết nối vào–ra:** Lựa chọn phương pháp → tự kiểm mô hình/chi phí → kiểm tra tổng hợp các giới hạn.

**Nguồn và vị trí:** NG1 §5.3.2,§5.5.2; nhiệm vụ suy trực tiếp từ đặc tả và phép đếm đã dạy.

**Thời lượng:** 3 phút.

**Nhiệm vụ và tiêu chí nội bộ:** Nhiệm vụ tự kiểm; slide kiểm tra riêng của phần được chỉ định trong bản đồ.

- Câu hỏi/đề: Hai nhiệm vụ tự kiểm như nội dung hiển thị.
- Đáp án/gợi ý: Câu1 đổi v và khởi tạo theo v, giữ M0/beta. Câu2 kết luận không được bảo đảm, còn thiếu số vòng/hằng số/điều kiện thực thi.
- Tiêu chí đánh giá: Nêu đúng thành phần thay đổi, không sửa cạnh; phân biệt một vòng với toàn thuật toán và tiệm cận với số đo.
- Phân bổ hoạt động: Suy nghĩ1 phút, trao đổi lời giải1 phút, đối chiếu1 phút; tổng3 phút.

**Ghi chú học thuật dự kiến:**

<!-- public-notes:start -->
Ở câu 1, đồ thị và $M_0$ giữ nguyên, $\beta=4/5$; $v$ đổi từ $(0,1/2,0,1/2)^\mathsf T$ sang $(1,0,0,0)^\mathsf T$. Nếu khởi tạo theo $v$ thì $r^0$ cũng đổi. G4 không có nút cụt nên không có số hạng bù. Ở câu 2, hai thuật toán có thể khác số vòng, hệ số công việc, tiêu chí dừng và cách thực thi; chuẩn bị tập chủ đề hoặc tập tin cậy cũng không nằm trong chi phí một vòng. Cùng bậc tiệm cận không suy ra cùng thời gian chạy.
<!-- public-notes:end -->

### lec04-s06-04 — Kiểm tra tổng hợp các phương pháp

**Vai trò, mục tiêu, đầu vào và sản phẩm:** Kiểm tra riêng S06; tự kiểm3–5; MT2–MT5. Đầu vào: ba mô hình. Sản phẩm: chọn và diễn giải điểm dưới đúng giả thiết.

**Luận điểm trung tâm:** Các định nghĩa về đóng góp, chỉ số và vai trò phải được giữ khi áp dụng phương pháp.

**Nội dung hiển thị dự kiến:**

<!-- public-slide:start -->
**Câu hỏi:**
3. Trong cụm thao túng, $x$ đã là đóng góp từ ngoài sau nhân $\beta$. Giải thích vì sao phương trình điểm đích chứa $x$ thay vì $\beta$ $x$.
4. Trang B có $r_B=19/84$, $\rho_B=59/210$. Xác định dấu Spam Mass; đánh giá việc thay mọi giá trị âm bằng 0.
5. Mạng học phần cần nhận diện cả trang danh sách và trang nội dung. Chọn phương pháp đã học; nêu ý nghĩa của hai đầu ra.
<!-- public-slide:end -->

**Bố cục đã chọn:** Ba nhiệm vụ thành ba hàng đủ rộng, khoảng1/3 mỗi hàng; dữ kiện số chỉ ở câu4. Không có hình phụ.

**Trọng tâm và thứ tự đọc:** Theo từng câu: định nghĩa đóng góp → dấu chỉ số → lựa chọn đầu ra hai vai trò.

**Lý do phù hợp sinh viên năm 2:** Mỗi nhiệm vụ đo một ranh giới thường nhầm; ba câu bao phủ các mục tiêu còn lại mà không giới thiệu dữ kiện mới.

**Giới hạn bố cục và phân chia nội dung:** Năm nhiệm vụ tự kiểm được phân bố giữa hai trang cuối S06, không dồn thành bảng chữ nhỏ. Đáp án chỉ trong ghi chú.

**Ví dụ, phiếu số và hình thức hóa:** VD2,VD3,VD4/HT4–HT6. Không hỏi điều kiện phổ chưa được kiểm tra ở tuyến chính.

**Kết nối vào–ra:** Tổng hợp ba mục tiêu → ba bài nguồn tính và chứng minh trong recitation.

**Nguồn và vị trí:** NG1 §5.4.2,§5.4.5,VD5.13; câu hỏi áp dụng dữ kiện đã học.

**Thời lượng:** 3 phút.

**Nhiệm vụ và tiêu chí nội bộ:** Slide kiểm tra riêng của phần.

- Câu hỏi/đề: Ba nhiệm vụ3–5 như nội dung hiển thị.
- Đáp án/gợi ý: x không nhân beta lần nữa; Spam Mass B âm và không cắt về 0 theo định nghĩa; chọn HITS với hai vai trò trung tâm/uy tín.
- Tiêu chí đánh giá: Một tiêu chí cho mỗi câu: truy nguồn x; bảo toàn dấu và nghĩa chỉ số; chọn HITS đồng thời mô tả đúng hai đầu ra.
- Phân bổ hoạt động: Suy nghĩ1 phút, trả lời1 phút, đối chiếu1 phút; tổng3 phút.

**Ghi chú học thuật dự kiến:**

<!-- public-notes:start -->
Câu 3: mỗi đóng góp từ nguồn ngoài $j$ đã là $\beta r_j/d_j$, nên nhân thêm $\beta$ làm giảm đóng góp lần nữa. Câu 4: $\rho_B>r_B$ nên $s_B<0$, cụ thể $s_B=-23/95$; thay bằng $0$ là đổi định nghĩa và mất thông tin hướng thay đổi. Câu 5: HITS cho điểm trung tâm của trang dẫn tới nguồn và điểm uy tín của trang được các trung tâm trỏ tới; mỗi trang có cả hai điểm. Các câu trả lời phải gắn với đặc tả, không chỉ nêu tên.
<!-- public-notes:end -->

## S07. Bài tập

Recitation sau phần giảng, thành section dọc riêng. Ba bài nguồn, mỗi bài20 phút gồm giải và đối chiếu lời giải. Bài 5.3.1 giữ cả(a,b); Bài 5.4.1 giữ(a,c), lược(b) có lý do bù nút cụt; Bài 5.5.2 giữ khuyên Hình 5.9. S07-03 đồng thời là kiểm tra riêng của phần, thời gian chỉ tính một lần.

Phân bổ: 3 slide, 60 phút.

### lec04-s07-01 — Bài tập PageRank theo chủ đề

**Vai trò, mục tiêu, đầu vào và sản phẩm:** Recitation BT1; MT1. Đầu vào: HT1 và G4. Sản phẩm: hai vector điểm và phép kiểm nghiệm.

**Luận điểm trung tâm:** Hai tập dịch chuyển được giải bằng cùng ma trận với hai vector v khác nhau.

**Nội dung hiển thị dự kiến:**

<!-- public-slide:start -->
**Bài 5.3.1(a, b), MMDS §5.3.5, trang 199.**

G4/Hình 5.15: A→B,C,D; B→A,D; C→A; D→B,C. Dùng $\beta=0.8$ kế thừa Ví dụ 5.10.

**Câu hỏi:** Tính PageRank theo chủ đề khi tập dịch chuyển là (a) chỉ A; (b) A và C.

Sản phẩm: hai phân phối dịch chuyển, hai vector điểm theo thứ tự A,B,C,D, hệ phương trình và phép kiểm tổng 1/điểm cố định.
<!-- public-slide:end -->

**Bố cục đã chọn:** G4 có đầy đủ tám cạnh trái45%; nguồn, hai yêu cầu và sản phẩm phải55%. Tham số beta nằm cạnh tên đồ thị. Lời giải không xuất hiện trên mặt slide.

**Trọng tâm và thứ tự đọc:** Đọc nguồn dữ kiện → dựng v cho từng trường hợp → giải cùng phương trình → kiểm nghiệm.

**Lý do phù hợp sinh viên năm 2:** Dùng lại G4 giảm thời gian học dữ liệu mới; hai tập dịch chuyển khác nhau cho phép kiểm việc chỉ đổi v mà giữ M0.

**Giới hạn bố cục và phân chia nội dung:** Không đổi số/cạnh hoặc yêu cầu nguồn. Các bước giảm hệ và đáp án ở ghi chú; slide chỉ đủ đề và sản phẩm.

**Ví dụ, phiếu số và hình thức hóa:** BT1; VD1. $r=(4/5)M_0r+(1/5)v$. Hình 5.15 có n4,ell8; không có nút cụt.

**Kết nối vào–ra:** Lý thuyết theo chủ đề → bài giải độc lập → phân tích đổi cấu trúc liên kết ở BT2.

**Nguồn và vị trí:** NG1 Bài 5.3.1(a,b), tr.199/PDF25; Hình 5.15 tr.197/PDF23; beta kế thừa VD5.10 tr.196–197.

**Thời lượng:** 20 phút.

**Nhiệm vụ và tiêu chí nội bộ:** Bài tập nguồn; không phải slide kiểm tra riêng của phần.

- Câu hỏi/đề: Giữ nguyên hai ý(a,b) của bài nguồn như nội dung hiển thị.
- Đáp án/gợi ý: (a) $(3/7,4/21,4/21,4/21)^\mathsf T$; (b) $(27/70,6/35,19/70,6/35)^\mathsf T$.
- Tiêu chí đánh giá: Phân phối v đúng2 điểm; hệ đúng chiều2 điểm; hai nghiệm4 điểm; kiểm tổng và phương trình2 điểm. Chấp nhận phép lặp đủ chính xác khi có tiêu chí dừng và kiểm phần dư.
- Phân bổ hoạt động: Thiết lập3 phút, tính12 phút, đối chiếu5 phút; tổng20 phút.

**Ghi chú học thuật dự kiến:**

<!-- public-notes:start -->
Đặt các thành phần nghiệm là $r_A,r_B,r_C,r_D$.

(a) $v=(1,0,0,0)^\mathsf T$. Hệ:
$$r_A=\frac25r_B+\frac45r_C+\frac15,\quad r_B=\frac4{15}r_A+\frac25r_D,$$
$$r_C=\frac4{15}r_A+\frac25r_D,\quad r_D=\frac4{15}r_A+\frac25r_B.$$
Hai phương trình tại B, D cho $r_B-r_D=(2/5)(r_D-r_B)$, nên $r_B=r_D$; hai phương trình tại B, C cho $r_B=r_C$. Đặt giá trị chung là $q$; khi đó $q=4r_A/9$. Điều kiện tổng bằng $1$ cho $r_A=3/7$ và $q=4/21$.

(b) $v=(1/2,0,1/2,0)^\mathsf T$. So với (a), phần dịch chuyển tại A đổi từ $1/5$ thành $1/10$, tại C đổi từ $0$ thành $1/10$; tại B, D vẫn bằng $0$. Do đó $r_B=r_D=q$, $r_C=q+1/10$ và $q=4r_A/9$. Điều kiện $r_A+3q+1/10=1$ cho
$$r=(27/70,6/35,19/70,6/35)^\mathsf T.$$

Hai nghiệm đều có tổng bằng $1$. Phép thế vào cả bốn phương trình kiểm thêm điều kiện điểm cố định; tổng bằng $1$ riêng lẻ chưa đủ xác nhận nghiệm.
<!-- public-notes:end -->

### lec04-s07-02 — Bài tập cấu trúc liên kết hỗ trợ

**Vai trò, mục tiêu, đầu vào và sản phẩm:** Recitation BT2; MT2. Đầu vào: HT4. Sản phẩm: hai mô hình cân bằng và biểu thức y theo tham số.

**Luận điểm trung tâm:** Thay liên kết của hỗ trợ đổi dòng quay lại đích và hệ số khuếch đại.

**Nội dung hiển thị dự kiến:**

<!-- public-slide:start -->
**Bài 5.4.1(a, c), MMDS §5.4.6, trang 203–204.**

Giữ mô hình Hình 5.16 trên đồ thị không nút cụt: đích vẫn chỉ trỏ tới $m$ hỗ trợ; các hỗ trợ không nhận liên kết từ ngoài cụm; mọi cạnh ngoài vào cụm tới đích. $x$ đã gồm $\beta$; $b=(1-\beta)/n$.

**Câu hỏi:** Lặp lại phân tích khi mỗi trang hỗ trợ (a) chỉ trỏ tới chính nó thay vì đích; (c) trỏ tới cả chính nó và đích.

Sản phẩm: phương trình điểm hỗ trợ $p$ và điểm đích $y$; biểu thức của $y$ theo $x,m,n,\beta$; chỉ rõ công thức chính xác hay xấp xỉ.
<!-- public-slide:end -->

**Bố cục đã chọn:** Dải giả thiết trên35%; hai sơ đồ cấu trúc(a),(c) đặt ngang ở dưới trái40% tổng khung; đề và sản phẩm ở dưới phải60%. Đích→hỗ trợ giữ nguyên; khuyên/cạnh quay lại có nhãn.

**Trọng tâm và thứ tự đọc:** Đọc các điều kiện không đổi → đối chiếu đúng cạnh thay ở(a)/(c) → lập p và y.

**Lý do phù hợp sinh viên năm 2:** Hình cạnh thay đổi giúp sinh viên suy mẫu số 1 hoặc2 theo từng trường hợp; vẫn dùng biến nguồn để không phát sinh bài toán mới.

**Giới hạn bố cục và phân chia nội dung:** Trên mặt slide không đặt lời giải hay số beta mới. Ý(b) lược có lý do trong metadata, không biến thành đề khác.

**Ví dụ, phiếu số và hình thức hóa:** BT2/VD2/HT4; n≥m+1,m≥1,0<beta<1; cả hai cấu trúc giữ không nút cụt.

**Kết nối vào–ra:** BT1 đổi bước nhảy → BT2 đổi cạnh và quy tắc chia → BT3 tính hai vai trò trên chuỗi nguồn.

**Nguồn và vị trí:** NG1 Bài 5.4.1(a,c), tr.203–204/PDF29–30; Hình 5.16 và §5.4.2 tr.200–201. Lược ý(b) để không mở thêm bù nút cụt trong bài20 phút.

**Thời lượng:** 20 phút.

**Nhiệm vụ và tiêu chí nội bộ:** Bài tập nguồn; không phải slide kiểm tra riêng của phần.

- Câu hỏi/đề: Hai ý(a,c) của bài nguồn như nội dung hiển thị.
- Đáp án/gợi ý: (a) $y=x+b\approx x$. (c) $y=[(2-\beta)(x+b)+\beta mb]/[(1-\beta)(2+\beta)]$; xấp xỉ như ghi chú.
- Tiêu chí đánh giá: Đúng cạnh và phương trình(a)2 điểm; chia đôi và hai phương trình(c)3 điểm; giải y3 điểm; giữ nghĩa x, b và dấu xấp xỉ2 điểm.
- Phân bổ hoạt động: Lập mô hình4 phút, biến đổi11 phút, đối chiếu5 phút; tổng20 phút.

**Ghi chú học thuật dự kiến:**

<!-- public-notes:start -->
Trong cả hai ý, $x$ chỉ gồm các đóng góp ngoài vào đích, đã nhân $\beta$ và chia bậc ra; không có cạnh ngoài vào hỗ trợ.

(a) Hỗ trợ giữ toàn phần theo liên kết tại chính nó:
$$p=\frac{\beta y}{m}+\beta p+b,\qquad y=x+b.$$
Vì không còn cạnh hỗ trợ→đích, dòng quay lại bằng 0. Do đó $p=(\beta y/m+b)/(1-\beta)$; theo phép lược bước nhảy trực tiếp tới đích của sách, $y\approx x$.

(c) Hỗ trợ có hai cạnh ra nên mỗi cạnh nhận một nửa:
$$p=\frac{\beta y}{m}+\frac\beta2p+b,\qquad
 y=x+\frac{\beta m}{2}p+b.$$
Từ phương trình $p$, $(2-\beta)p=2\beta y/m+2b$. Thế vào $y$:
$$(2-\beta)y=(2-\beta)(x+b)+\beta^2y+\beta mb.$$
Vì $2-\beta-\beta^2=(1-\beta)(2+\beta)>0$,
$$y=\frac{(2-\beta)(x+b)+\beta mb}{(1-\beta)(2+\beta)}.$$
Bỏ riêng phần dịch chuyển trực tiếp tới đích:
$$y\approx\frac{2-\beta}{(1-\beta)(2+\beta)}x+\frac{\beta}{2+\beta}\frac mn.$$
Không bỏ phần $b$ nhận tại hỗ trợ, vì tổng $m$ phần ấy tạo hạng $m/n$. Hai cách chính xác/xấp xỉ đều hợp lệ nếu giả thiết và dấu quan hệ nhất quán.
<!-- public-notes:end -->

### lec04-s07-03 — Bài tập HITS trên chuỗi có khuyên

**Vai trò, mục tiêu, đầu vào và sản phẩm:** Recitation BT3 và kiểm tra riêng S07; MT4. Đầu vào: HT6. Sản phẩm: vector theo n, chứng minh giới hạn và xử lý biên.

**Luận điểm trung tâm:** Khuyên tại đỉnh 1 quyết định thành phần chi phối và hai vector giới hạn của chuỗi.

**Nội dung hiển thị dự kiến:**

<!-- public-slide:start -->
**Bài 5.5.2, MMDS §5.5.3, trang 208; Hình 5.9, trang 189.**

Đồ thị có $n$ đỉnh, cạnh $1\to1$ và $i\to i+1$ với $1\le i<n$; $n\ge1$.

Khởi tạo $h^0=a^0=\mathbf1$; sau mỗi phép nhân, chuẩn hóa phần tử lớn nhất bằng 1.

**Câu hỏi:** Tính các vector trung tâm và uy tín theo $n$.

Sản phẩm: hai vector giới hạn, lập luận từ phép lặp hoặc ma trận, và các trường hợp biên $n=1$, $n=2$.
<!-- public-slide:end -->

**Bố cục đã chọn:** Chuỗi ngang với khuyên tại1 chiếm dải trên40%; dữ kiện và yêu cầu dưới60%. Dấu chấm lửng chỉ các đỉnh giữa; nhãn cạnh1→1 riêng ngoài khuyên.

**Trọng tâm và thứ tự đọc:** Kiểm khuyên nguồn → xác định hàng 1/hàng giữa/hàng cuối → suy công thức lặp và giới hạn.

**Lý do phù hợp sinh viên năm 2:** Hình làm khuyên nổi bằng đường nét và nhãn, không chỉ màu; lời giải theo nhóm chỉ số phù hợp quy nạp, tránh nhân ma trận kích thước n bằng tay.

**Giới hạn bố cục và phân chia nội dung:** Không thay chuỗi thành dạng không khuyên. Đáp án, ma trận đường chéo và công thức theo vòng nằm trong ghi chú.

**Ví dụ, phiếu số và hình thức hóa:** BT3/HT6; dữ kiện giữ Hình 5.9. Không thêm tham số beta, không xử lý nút cuối bằng bước nhảy.

**Kết nối vào–ra:** Ba mô hình đã học → nghiệm và chứng minh trên bài nguồn → hoàn tất sản phẩm recitation.

**Nguồn và vị trí:** NG1 Bài 5.5.2, tr.208/PDF34; Hình 5.9 tr.189/PDF15 đã kiểm trực tiếp khuyên tại1.

**Thời lượng:** 20 phút.

**Nhiệm vụ và tiêu chí nội bộ:** Slide kiểm tra riêng của phần.

- Câu hỏi/đề: Tính hai vector giới hạn của chuỗi có khuyên theo đúng đề nguồn.
- Đáp án/gợi ý: $n\ge2$: $h^*=(1,0,\ldots,0)^\mathsf T$, $a^*=(1,1,0,\ldots,0)^\mathsf T$; $n=1$: h=a=(1).
- Tiêu chí đánh giá: Giữ khuyên và lập L/LLT đúng2 điểm; vết vòng đầu và công thức quy nạp3 điểm; hai giới hạn3 điểm; xử lý n1/n2 và chuẩn max 2 điểm.
- Phân bổ hoạt động: Lập ma trận4 phút, suy luận11 phút, đối chiếu5 phút; tổng20 phút.

**Ghi chú học thuật dự kiến:**

<!-- public-notes:start -->
Với $n\ge2$, hàng 1 của $L$ có hai số $1$ tại cột 1, 2; mỗi hàng $2\le i<n$ có một số $1$ tại cột $i+1$; hàng cuối bằng $0$. Các hàng khác nhau có tập vị trí cột khác $0$ rời nhau, nên
$$LL^\mathsf T=\operatorname{diag}(2,\underbrace{1,\ldots,1}_{n-2},0).$$
Khởi tạo $h^0$ toàn $1$ cho $a^1$ toàn $1$. Vector trung tâm thô đầu là $(2,1,\ldots,1,0)^\mathsf T$; chuẩn hóa bằng giá trị lớn nhất cho $h^1=(1,1/2,\ldots,1/2,0)^\mathsf T$.

Quy nạp: nếu $h^t=(1,2^{-t},\ldots,2^{-t},0)^\mathsf T$, thì $a^{t+1}$ có hai thành phần đầu bằng $1$ và phần còn lại bằng $2^{-t}$, vì có hai cạnh từ đỉnh 1 tới đỉnh 1 và đỉnh 2. Trung tâm thô kế tiếp là $(2,2^{-t},\ldots,2^{-t},0)^\mathsf T$; chia từng thành phần cho $2$ thu được công thức ở vòng $t+1$. Vì vậy, với $t\ge1$:
$$h^t=(1,\underbrace{2^{-t},\ldots,2^{-t}}_{n-2},0)^\mathsf T,$$
$$a^t=(1,1,\underbrace{2^{-(t-1)},\ldots,2^{-(t-1)}}_{n-2})^\mathsf T.$$
Lấy giới hạn cho $h^*=(1,0,\ldots,0)^\mathsf T$ và $a^*=(1,1,0,\ldots,0)^\mathsf T$.

Khi $n=2$, phần giữa rỗng; hai vector đạt giới hạn ngay sau vòng 1. Khi $n=1$, vẫn còn khuyên $1\to1$, $L=[1]$ và $h=a=(1)$; không có phép chia cho $0$. Khuyên khiến hàng 1 có chuẩn lớn hơn các hàng giữa, nên bỏ khuyên sẽ thay bài toán và nghiệm.
<!-- public-notes:end -->

## Tự kiểm của tác tử soạn trước vòng rà độc lập và giới hạn

- Đã đối chiếu53 phiếu với số trang từng phần6/13/8/8/11/4/3; phần giảng50 trang/120 phút, recitation3 trang/60 phút. Mã duy nhất; hai trang bổ sung có hậu tố a để giữ các mã cũ; bảy slide kiểm tra riêng đã chỉ định.
- Mỗi phiếu có đầu vào/sản phẩm, luận điểm, nội dung hiển thị, bố cục chọn, thứ tự đọc, lý do năm2, giới hạn, nguồn, thời lượng và ghi chú học thuật. Các câu hỏi có dữ kiện, đáp án, tiêu chí và thời gian nằm trong thời lượng trang.
- Mạch theo sách §5.3→§5.4→§5.5. G4 được giữ xuyên PageRank–TrustRank–Spam Mass; G5 được khai báo khác G4 trước HITS; chuỗi bài5.5.2 giữ khuyên. Chỉ có các bổ sung toán học/cầu nối đã duyệt trong outline.
- Áp dụng `no-ai-slop` chế độ Edit và tự kiểm `eval.md`: loại tiêu đề tu từ, lời kể tiến trình, lời chỉ dẫn tác giả và khẳng định quá mạnh khỏi hai vùng công khai. Giữ yêu cầu Tính/Xác định/Giải thích đúng chức năng kiểm tra. Văn phong học thuật ưu tiên hơn giọng nói hay câu rời; không có điểm phát hiện AI.
- Áp dụng `quill` để rà đồ thị tiên quyết và tính liên tục ký hiệu: M0 cột nguồn, L hàng nguồn; beta là xác suất theo cạnh; rho là TrustRank; h/a chuẩn max; b khác delta của nút cụt. Không khởi tạo dự án sách.
- Đây là kiểm nội bộ của bản soạn để bàn giao các lượt đọc độc lập; chưa thay thế báo cáo toán học, sư phạm, nguồn và văn phong độc lập. HTML đã cập nhật; tác tử soạn chưa kiểm render, tràn khung, bàn phím hoặc bản in của lượt chỉnh29/09. Các kết quả ấy không được suy từ độ đầy đủ của phiếu.

## Ánh xạ triển khai ngày 28/09/2026

53 phiếu phía trên là đặc tả hiện hành, gồm hai trang tách mới. HTML giữ các mã cũ và bổ sung hậu tố a; các vùng văn bản được dựng bằng bảng, công thức, khối mã, danh sách nhiệm vụ và sơ đồ theo chức năng của từng phiếu. Tài sản do generator sinh; không có ảnh raster hoặc tài sản từ mạng trong thành phần cốt lõi.

### Ánh xạ ghi chú tự học

Các mã dưới đây chỉ là metadata. Mỗi chủ đề giữ thứ tự vai trò → định nghĩa → ví dụ → trực quan → mệnh đề/thuật toán/chứng minh khi áp dụng → vận dụng và kiểm tra. Nguồn đều là sách MMDS và những suy luận đã được duyệt trong bản đồ chủ đề của outline.

| note-topic-id | Vị trí; vai trò và nguồn | Kiến thức đầu vào → sản phẩm học tập | Kết nối vào–ra và thành phần áp dụng | Slide liên quan |
|---|---|---|---|---|
| `lec04-note-01` | §1; cầu nối; §5.3.1 và Bài 03 | PageRank → phân biệt nhu cầu và chiều cạnh | Bài 03 → phân phối dịch chuyển; định nghĩa/đồ thị/kiểm tra; thuật toán và định lý mới không áp dụng | S01-01–06 |
| `lec04-note-02` | §2.1–2.2; cốt lõi; §5.3.2, VD5.10 | Phân phối, ma trận → cập nhật và nghiệm trên G4 | Nhu cầu → dữ kiện cho thuật toán; định nghĩa trước ví dụ, hình và bảng vết chạy, giải hệ điểm cố định | S02-01–05 |
| `lec04-note-03` | §2.3–2.4; cầu nối/bổ sung; §5.1.5, §5.3.2 | Phép cập nhật → thuật toán, bất biến, cận sai số | Ví dụ → bảo đảm cho mọi vòng; giả mã, chứng minh đầy đủ về bảo toàn/co, biên toàn nút cụt | S02-05–08 |
| `lec04-note-04` | §2.5; cốt lõi/bổ sung; §5.3.2–3 và phép đếm | Điểm cố định → ghép điểm và đánh giá chi phí | Tính duy nhất → tổ hợp có trọng số → truy vấn; chứng minh tuyến tính và chi phí; không có thuật toán mới độc lập | S02-09–12 |
| `lec04-note-05` | §3; cốt lõi; §5.4.1–2, Hình5.16, VD5.11 | Luồng PageRank → phương trình hỗ trợ/đích và xấp xỉ | Đổi về dịch chuyển đều → tác động cạnh → nhu cầu tin cậy; định nghĩa, hình, dẫn xuất đầy đủ, hệ số nguồn và kiểm tra; giả mã không áp dụng cho mô hình cân bằng | S03-01–08 |
| `lec04-note-06` | §4.1–4.2; cốt lõi; §5.4.3–4 | Chủ đề và mô hình thao túng → phép lặp TrustRank | Tập hạt giống → cùng nghiệm G4 → so điểm nền; đặc tả, hình, ví dụ, tái sử dụng thuật toán và chứng minh §2 | S04-01–04 |
| `lec04-note-07` | §4.3–4.4; cốt lõi/bổ sung; §5.4.5 | Hai vector cùng mô hình → chỉ số và giới hạn | Hiệu tuyệt đối → hiệu tương đối → phân biệt với uy tín HITS; bảng tính, giá trị âm, độ phủ, chi phí và kiểm tra; không đặt định lý phân loại chắc chắn | S04-04–07 |
| `lec04-note-08` | §5.1–5.3; cốt lõi/cầu nối; §5.5.1–2 | Tổng theo cạnh → hai vai trò và hai vòng HITS | Ý nghĩa đầu ra → ma trận/chuẩn hóa → vết số; định nghĩa đặt trước ví dụ theo chu trình ghi chú | S05-01–07 |
| `lec04-note-09` | §5.4–5.6; cốt lõi/bổ sung; §5.5.2 | Vết chạy → thuật toán, bất biến và chi phí | Uy tín mới → trung tâm → dừng → quan hệ ổn định; giả mã, lập luận phép chia hợp lệ, phác thảo phổ có điều kiện, hai lượt cạnh và kiểm tra | S05-08–11 |
| `lec04-note-10` | §6; tổng hợp; §5.3–5.5 | Các đầu ra đã định nghĩa → lựa chọn theo yêu cầu | Ba tình huống mở → lựa chọn → bài tập; bảng so sánh và năm nhiệm vụ; không tạo thuật toán/định lý mới | S06-01–04 |
| `lec04-note-11` | §7.1; bài nguồn 5.3.1(a,b), tr.199 | G4 và phương trình → hai nghiệm chính xác | Đổi bước nhảy → kiểm hệ và tổng; đề, gợi ý, lời giải gập; 20 phút | S07-01 |
| `lec04-note-12` | §7.2; bài nguồn 5.4.1(a,c), tr.203–204 | Phương trình cụm → phân tích hai biến thể | Giữ giả thiết nền → đổi cạnh → nghiệm chính xác/xấp xỉ; hai hình, gợi ý và lời giải gập; 20 phút | S07-02 |
| `lec04-note-13` | §7.3; bài nguồn 5.5.2, tr.208, Hình5.9 tr.189 | HITS → hai giới hạn theo $n$ | Khuyên → ma trận → quy nạp và biên; đề/hình/gợi ý/lời giải gập; 20 phút | S07-03 |

### Điều chỉnh bố cục khi dựng

- S01-04 và S02-11: hai hàng luồng được dựng thành SVG; câu văn trùng nhãn trong hình được gộp thành chú thích, không đổi luận điểm hoặc thêm dữ kiện.
- S01-06, S02-02, S02-12, S04-03 và S07-01: danh sách tám cạnh được thể hiện đầy đủ bằng G4; không đặt lại một đoạn liệt kê cạnh cạnh hình. S05-02/11 tương tự với G5; S05-02 có nhãn công khai G5 trước trang gọi lại tên này.
- S03-07: dùng `hai-nhom-canh-noi-bo.svg` để thể hiện hai nhóm $m$ cạnh. Bản dựng thử dùng hình một hỗ trợ chưa cho thấy chiều quay lại; đã thay trước bàn giao rà độc lập.
- S05-06: ma trận có nhãn hàng/cột A–E; các phép nhân và bảng đối chiếu được tách khỏi ma trận đúng tỷ lệ 55%–45%.
- S06-04: ba câu 3–5 dùng một khung nhiệm vụ và danh sách ba hàng. Ba khung riêng làm nguồn chạm chân trang ở bản render đầu; gộp khung giữ nguyên câu hỏi và thứ tự.
- S07-02: chữ trong hai SVG biến thể được tăng bằng generator; giá trị nhỏ nhất trong SVG là 30px, không thu nhỏ chữ HTML. Dữ kiện và hai cấu trúc giữ nguyên.
- S07-03: nguồn được giữ ở đầu trang và trong ghi chú; bỏ lần lặp ở chân trang. Hình chuỗi dùng lớp `.l04-chain-diagram` cao 160px để dành vùng cho dữ kiện và sản phẩm. CSS chỉ thêm quy tắc bố cục dưới `.reveal.lecture-pagerank-advanced`; không sửa thang chữ.
- Các câu hỏi nhiều ý được dựng bằng `ol/li` trong cùng khung; không đổi số câu. Mã giả giữ ngôn ngữ plaintext và `data-trim`; hai thuật toán không bị rút bớt bước.

Bản hiện hành gồm50 trang giảng/120 phút và ba bài/60 phút. Ba ghi chú bài tập có thời lượng 20 phút; mặt slide không có thời lượng. Chi tiết nguồn và lời giải nằm trong từng ghi chú diễn giả; ghi chú tự học được soạn thành mạch riêng thay vì sao chép các trang chiếu.

### Ánh xạ SVG thực tế

| Slide | Tài sản SVG trong `img/lec-04/` |
|---|---|
| `lec04-s01-04` | `luu-vector-theo-chu-de.svg` |
| `lec04-s01-06` | `hinh-5-1-kiem-tra.svg` |
| `lec04-s02-01` | `hai-nhanh-di-chuyen.svg` |
| `lec04-s02-02` | `hinh-5-15.svg` |
| Không dùng trong bản slide29/09 | `tong-vector-chu-de.svg` được giữ làm tài sản hiện có |
| Không dùng trong bản slide29/09 | `tien-tinh-va-truy-van.svg` được giữ làm tài sản hiện có |
| `lec04-s02-12` | `hinh-5-1-trung-tinh.svg` |
| `lec04-s03-02` | `hinh-5-16-cum-thao-tung.svg` |
| `lec04-s03-03` | `diem-mot-ho-tro.svg` |
| `lec04-s03-04` | `luong-hang-trong-cum.svg` |
| `lec04-s03-07` | `hai-nhom-canh-noi-bo.svg` |
| `lec04-s04-01` | `tap-tin-cay.svg` |
| `lec04-s04-03` | `hinh-5-15-tin-cay.svg` |
| `lec04-s05-01` | `cap-vai-tro-hits.svg` |
| `lec04-s05-02` | `hinh-5-18.svg` |
| `lec04-s05-09` | `dong-gop-hits.svg` |
| `lec04-s05-11` | `hinh-5-18-kiem-tra.svg` |
| `lec04-s07-01` | `hinh-5-1-trung-tinh.svg` |
| `lec04-s07-02` | `ho-tro-tu-khuyen.svg`, `ho-tro-khuyen-va-dich.svg` |
| `lec04-s07-03` | `chuoi-co-khuyen.svg` |

Các trang không liệt kê dùng bảng HTML, KaTeX, danh sách hoặc giả mã như phiếu đã duyệt. Toàn bộ 20 SVG có vai trò ảnh, tiêu đề và mô tả trong tệp; mỗi nơi nhúng có văn bản thay thế riêng.

## Đồng bộ sau phản biện bản triển khai ngày 28/09/2026

| Vị trí | Nội dung chỉnh và lý do | Kết nối được giữ |
|---|---|---|
| S01-04, notes; `lec04-note-01`, §1 | Thay câu mô tả chiều dài chung bằng quy mô minh họa MMDS: khoảng một tỷ người dùng, mỗi vector nhiều tỷ thành phần (§5.3.1, tr.195–196). Giữ sơ đồ, câu về vector chủ đề và trọng số; không thêm ước lượng byte hoặc thời gian. | Ngữ cảnh cá nhân → giới hạn lưu trữ → dùng lại vector chủ đề → chi phí S02-10. |
| S02-01 | `desc` của `hai-nhanh-di-chuyen.svg` nêu đích của một cạnh ra từ trang hiện tại; không đặt điều kiện có cạnh ra cho trang đích. | Trực giác hai nhánh → G4 → mô hình có nút cụt. |
| S03-02; `lec04-note-05`, §3.1 | Hình kiến trúc dùng “Đóng góp từ ngoài”; bỏ $x$ cả trong nhãn và mô tả thay thế. Mã sinh hình đã đồng bộ. | Kiến trúc/giả thiết → điểm hỗ trợ S03-03 → định nghĩa $x$ và phương trình ở S03-04. |
| S04-02/03 | Nguồn HTML và notes dùng §5.4.4, tr.202–203; S04-03 giữ Ví dụ 5.10, tr.196–197 cho G4. Phiếu nguồn đã đồng bộ. | Tập tin cậy → tái sử dụng phép lặp → so hai vector cùng mô hình. |
| S05-02/06 | S05-02 dùng §5.5.2, Ví dụ 5.14, Hình 5.18, tr.205–206; S05-06 dùng §5.5.2, Hình 5.19, tr.206. Giữ §5.5.1 tại S05-01. | Trực giác hai vai trò → G5 → vết chạy → ma trận. |
| S05-05/07/08; §5.4 ghi chú | Sửa cách dùng “max” trong câu văn/trạng thái trả về thành “giá trị lớn nhất”; giữ toán tử `max` và công thức. | Hai mẫu số của vòng lặp → miền xác định của chuẩn hóa → giả mã. |

Số trang, thứ tự, mã, thời lượng và sản phẩm học tập không thay đổi. Các quyết định trên đã được điều phối viên duyệt sau khi đọc đủ năm báo cáo triển khai; không dùng kết quả rà dàn bài cũ thay cho rà học liệu. Editor kiểm đồng bộ nội dung và cấu trúc; render cuối, hồi quy viewer, kiểm toán học/mạch sau sửa và công bố thuộc bước kiểm định tiếp theo của điều phối viên.

## Phân bổ lại sau khi tách ký hiệu và phép suy luận ngày29/09/2026

S02 có13 trang: thời lượng lần lượt2;2;2,5;2,5;3;3;2,5;2,5;1;2;2;2;3 phút (S02-09a nằm sau S02-09), tổng30 phút. S04 có8 trang:2;2;2;1;3;3;2;3 phút (S04-02a nằm sau S04-02), tổng18 phút. Các phần khác và60 phút bài tập giữ nguyên. Tách định nghĩa vector chủ đề khỏi chứng minh tổng, tách bảng ký hiệu TrustRank khỏi phép cập nhật để giảm số đối tượng mới trên cùng trang. Không thêm chủ đề, ví dụ số hoặc bài tập.
