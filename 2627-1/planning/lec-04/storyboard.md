# Storyboard mới Bài 04: PageRank theo chủ đề, liên kết rác và HITS

Ngày soạn: 27/09/2026; cập nhật làm rõ nội dung: 29/09/2026; duyệt từng trang: 01/10/2026. Các phiếu dưới đây phản ánh bản HTML hiện tại gồm 52 trang (49 trang giảng, 3 trang bài tập). Kết quả kiểm định từng phiên được lưu trong review-log.md.

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
| S01. Bài toán xếp hạng liên kết | 6 | 12 phút | `lec04-s01-06` (ôn tiên quyết Bài 03; S01 là phần mở bài, không có trang kiểm đầu ra riêng) |
| S02. PageRank theo chủ đề | 13 | 30 phút | `lec04-s02-12` |
| S03. Cơ chế liên kết rác | 8 | 20 phút | `lec04-s03-08` |
| S04. TrustRank và Spam Mass | 7 | 18 phút | `lec04-s04-07` |
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

Mục tiêu: tính PageRank theo chủ đề, TrustRank, Spam Mass và điểm HITS; giải thích tác động của cụm thao túng liên kết; chọn phương pháp theo đầu ra cần tạo.
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
PageRank theo chủ đề giữ phép lặp của Bài 03 và chỉ đổi nơi đến của bước nhảy ngẫu nhiên: bước nhảy tới các trang đại diện một chủ đề thay vì mọi trang. Mô hình cụm thao túng liên kết cho thấy một cấu trúc liên kết có thể khuếch đại điểm của trang đích. TrustRank dùng cùng phép lặp, với tập trang tin cậy làm nơi đến của bước nhảy; Spam Mass so sánh TrustRank với PageRank để chọn trang cần rà soát. HITS gán mỗi trang hai điểm, trung tâm và uy tín, thay cho một điểm duy nhất. Phần bài tập áp dụng các phương trình này trên dữ liệu của giáo trình.
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
Hạn chế thứ nhất đã xuất hiện ở truy vấn “jaguar”; PageRank theo chủ đề đổi nơi đến của bước nhảy ngẫu nhiên để điểm phụ thuộc chủ đề. Hạn chế thứ hai nằm ngay trong cơ chế truyền điểm: MMDS gọi một tập trang được lập ra để tăng PageRank của một trang là cụm thao túng liên kết (spam farm). Phần cơ chế liên kết rác tính mức khuếch đại của cụm này; phần TrustRank và Spam Mass dùng đánh giá bên ngoài đồ thị để hạn chế tác động đó. Hạn chế thứ ba là PageRank chỉ có một chiều quan trọng: trang danh sách học phần có giá trị vì dẫn tới các trang học phần, còn trang học phần có giá trị vì chứa nội dung. HITS gán mỗi trang hai điểm cho hai vai trò này. Ba yêu cầu có thể cùng xuất hiện trong một hệ thống. Hai yêu cầu đầu dùng lại phép lặp PageRank với ma trận $M_0$ của Bài 03; HITS dùng cùng đồ thị nhưng cộng điểm theo cạnh, không chia theo bậc ra, rồi chuẩn hóa.
<!-- public-notes:end -->

**Quyết định duyệt trang 01/10/2026:** sửa. Hai yêu cầu liên kết rác và hai vai trò trước đây thiếu động cơ, cụm “tập trang tin cậy” xuất hiện trước khái niệm và câu kết tối nghĩa. Bảng mới đặt hạn chế của PageRank toàn cục cạnh yêu cầu, theo MMDS §5.3.1, §5.4.1 (spam farm) và §5.5.1 (một chiều quan trọng); bỏ “tập trang tin cậy”; ghi chú ánh xạ từng hạn chế sang phần tương ứng.

### lec04-s01-06 — Ôn tập phép truyền điểm

**Vai trò, mục tiêu, đầu vào và sản phẩm:** Kiểm tra tiên quyết; MT1. Đầu vào: quy tắc chia đều PageRank Bài 03. Sản phẩm: tính đúng đóng góp theo một cạnh.

**Luận điểm trung tâm:** PageRank chia tại trang nguồn và cộng tại trang đích; đây là nhánh theo liên kết mà PageRank theo chủ đề giữ nguyên.

**Nội dung hiển thị dự kiến:**

<!-- public-slide:start -->
Đồ thị G4 (Hình 5.15): A trỏ tới B, C, D; B trỏ tới A, D; C trỏ tới A; D trỏ tới B, C.

Giả sử $r_A=r_B=r_C=r_D=1/4$ và $\beta=4/5$.

**Câu hỏi:** Tính phần điểm theo liên kết mà B chuyển tới A. Xác định phần tử tương ứng trong ma trận $M_0$ với quy ước cột là trang nguồn.
<!-- public-slide:end -->

**Bố cục đã chọn:** G4 ở trái 45%, dữ kiện và hai yêu cầu ở phải 55%; cạnh B→A có nhãn bậc ra của B. Không đặt đáp án trên hình.

**Trọng tâm và thứ tự đọc:** Đọc B có hai cạnh ra, theo cạnh B→A, rồi liên hệ hàng A/cột B.

**Lý do phù hợp sinh viên năm 2:** Phép tính dùng kiến thức cũ và số nhỏ; tách một đóng góp khỏi toàn bộ điểm mới để phát hiện nhầm dòng/cột.

**Giới hạn bố cục và phân chia nội dung:** Giữ toàn bộ tám cạnh nhìn được; chỉ yêu cầu một đóng góp. Không tính vector chủ đề chưa học.

**Ví dụ, phiếu số và hình thức hóa:** VD1: giữ G4, dùng khởi tạo đều của Bài 03; $(M_0)_{AB}$ và đóng góp $\beta r_B/d_B$.

**Kết nối vào–ra:** Chiều truyền PageRank đã xác nhận → thay phân phối dịch chuyển ở S02. Ghi chú nối “bước nhảy ngẫu nhiên” của Bài 03 với thuật ngữ “dịch chuyển” của Bài 04; nhãn “Đồ thị G4” đặt tên đồ thị dùng lại ở S02, S04, S06.

**Quyết định 01/10/2026:** sửa — tiêu đề “Kiểm tra chiều truyền điểm” thành “Ôn tập phép truyền điểm” vì trang kiểm tiên quyết Bài 03, không kiểm đầu ra S01; thêm nhãn G4; thêm cầu nối thuật ngữ.

**Nguồn và vị trí:** NG1 Hình 5.15, tr.197; quy tắc PageRank §5.1.2; NG5 ký hiệu đã học.

**Thời lượng:** 3 phút.

**Nhiệm vụ và tiêu chí nội bộ:** Slide kiểm tra riêng của phần.

- Câu hỏi/đề: Tính đóng góp B→A và xác định ô của ma trận như nội dung hiển thị.
- Đáp án/gợi ý: $1/10$; hàng A, cột B bằng $1/2$.
- Tiêu chí đánh giá: Đạt khi xác định đúng bậc ra2, nhân beta một lần và chọn hàng đích/cột nguồn. Lấy bậc ra của A hoặc đảo ô cho thấy nhầm chiều.
- Phân bổ hoạt động: Suy nghĩ1 phút, trả lời1 phút, đối chiếu1 phút; nằm trong3 phút.

**Ghi chú học thuật dự kiến:**

<!-- public-notes:start -->
B có hai liên kết ra nên $(M_0)_{AB}=1/2$. Đóng góp theo liên kết là $(4/5)(1/4)/2=1/10$. Bậc ra được lấy tại B là nguồn của cạnh, không lấy tại A. Đây chưa phải toàn bộ điểm của A vì còn các đóng góp từ trang khác và phần bước nhảy ngẫu nhiên.

Phép cập nhật của Bài 03 có hai nhánh: theo liên kết với xác suất $\beta$ và bước nhảy ngẫu nhiên với xác suất $1-\beta$. Bài 04 gọi bước nhảy này là dịch chuyển (teleport). PageRank theo chủ đề giữ nguyên nhánh theo liên kết vừa tính và chỉ đổi nơi đến của bước dịch chuyển.
<!-- public-notes:end -->

## S02. PageRank theo chủ đề

Khái niệm, thuật toán và chi phí. Nhu cầu chủ đề → thay nhánh dịch chuyển → G4/VD1 → HT1 → thuật toán, bảo toàn và tính co → kết hợp chủ đề, chi phí → kiểm tra. Bù nút cụt là cầu nối từ Bài 03; chứng minh gọi lại lập luận co, không tạo phần lý thuyết phổ. Kết quả v, r được chuyển sang TrustRank. Mỗi lần đổi trang giữ vị trí và thứ tự A–D.

Phân bổ: 13 slide, 30 phút.

### lec04-s02-01 — Dịch chuyển vào tập chủ đề

**Vai trò, mục tiêu, đầu vào và sản phẩm:** Trực giác; MT1. Đầu vào: hai nhánh di chuyển PageRank. Sản phẩm: chỉ ra thành phần thay đổi khi ưu tiên chủ đề.

**Luận điểm trung tâm:** Thiên lệch chủ đề được đưa vào nhánh dịch chuyển, không xóa các trang ngoài tập chủ đề.

**Nội dung hiển thị dự kiến:**

<!-- public-slide:start -->
Với xác suất $\beta$: đi theo một liên kết ra, chia đều giữa các liên kết.

Với xác suất $1-\beta$: dịch chuyển tới tập chủ đề $S$; Bài 03 chọn đều trong $n$ trang.

Các trang ngoài $S$ vẫn có thể nhận điểm qua liên kết. Đồ thị liên kết được giữ nguyên.
<!-- public-slide:end -->

**Bố cục đã chọn:** Sơ đồ hai nhánh từ một trang chiếm trái 55%; hai câu giải thích và kết luận ở phải 45%. Nhánh dịch chuyển dùng nét đứt và nhãn để phân biệt cạnh thật.

**Trọng tâm và thứ tự đọc:** Theo nhánh liên kết trước, nhánh dịch chuyển sau; đối chiếu đích được phép ở từng nhánh.

**Lý do phù hợp sinh viên năm 2:** Sinh viên đã biết hai nhánh của PageRank; chỉ thay tập đích của một nhánh để giảm số thành phần mới cùng lúc.

**Giới hạn bố cục và phân chia nội dung:** Không dựng thêm cạnh dịch chuyển thành dữ liệu đồ thị. Nút cụt được đặc tả ở S02-05.

**Ví dụ, phiếu số và hình thức hóa:** HT1 ở mức trực giác; $0<\beta<1$, $S\ne\varnothing$; chưa dùng ma trận mới.

**Kết nối vào–ra:** Nhu cầu chủ đề → một thay đổi trong bước nhảy; G4 cụ thể hóa ở trang sau.

**Quyết định 01/10/2026:** sửa — tiêu đề gọi đúng thay đổi duy nhất (đích của bước dịch chuyển); mặt trang đối chiếu trực tiếp với bước nhảy đều của Bài 03; ghi chú đặt tên “tập dịch chuyển” trước khi trang sau dùng và nêu giả định trực quan của MMDS §5.3.2.

**Nguồn và vị trí:** NG1 §5.3.2, tr.196/PDF22; NG3 trang8 chỉ đối chiếu hình.

**Thời lượng:** 2 phút.

**Ghi chú học thuật dự kiến:**

<!-- public-notes:start -->
So với Bài 03, chỉ nơi đến của bước dịch chuyển thay đổi; nhánh theo liên kết và đồ thị giữ nguyên. Tập $S$ gồm các trang đã được xác định là thuộc chủ đề và còn được gọi là tập dịch chuyển (teleport set). Dịch chuyển đưa phần điểm mới vào các trang này; các bước theo liên kết tiếp tục chuyển điểm tới những trang tới được từ $S$ qua đường đi ngắn. Vì vậy, $S$ không phải tập duy nhất có điểm dương.

MMDS dựa trên giả định trực quan: trang được các trang của một chủ đề trỏ tới thường cũng thuộc chủ đề đó. Đây là giả định ý nghĩa của mô hình, không phải một phép phân loại chắc chắn.
<!-- public-notes:end -->

### lec04-s02-02 — Phân phối dịch chuyển trên G4

**Vai trò, mục tiêu, đầu vào và sản phẩm:** Ví dụ dẫn nhập; MT1. Đầu vào: hai nhánh di chuyển. Sản phẩm: lập vector bước nhảy từ tập S.

**Luận điểm trung tâm:** $v$ quy định phân phối đích khi dịch chuyển; $r^0=v$ chỉ là lựa chọn khởi tạo của ví dụ.

**Nội dung hiển thị dự kiến:**

<!-- public-slide:start -->
[Hình: Đồ thị G4: A tới B, C, D; B tới A, D; C tới A; D tới B, C. B và D có viền đôi và nhãn tập S.]

$\beta=4/5$, $S=\{B,D\}$; thứ tự thành phần A, B, C, D.

$v$ là phân phối chọn trang đích khi thực hiện dịch chuyển:
$$v=(0,1/2,0,1/2)^\mathsf T.$$

Cập nhật trên G4 (không có nút cụt), khởi tạo $r^0=v$:
$$r^{t+1}=\beta M_0r^t+(1-\beta)v.$$

Mỗi vòng thêm $(1-\beta)v$: B, D nhận $1/10$; A, C nhận $0$.
<!-- public-slide:end -->

**Bố cục đã chọn:** Đồ thị G4 ở trái45%; định nghĩa v, vector cụ thể và vai trò khởi tạo ở phải55%. Giữ nhãn B,D và thứ tự A–D.

**Trọng tâm và thứ tự đọc:** Tập S → phân phối v → khởi tạo r0 → phần thêm trong mỗi vòng.

**Lý do phù hợp sinh viên năm 2:** Nhãn chữ tách danh tính đỉnh khỏi giá trị điểm và số vòng; hai vector giúp phân biệt phân phối v với phần điểm thực sự thêm mỗi vòng.

**Giới hạn bố cục và phân chia nội dung:** Giữ một vector hiển thị; ghi phần dịch chuyển bằng lời và giá trị mỗi trang. Giải thích xác suất có điều kiện trong ghi chú.

**Ví dụ, phiếu số và hình thức hóa:** VD1; giữ số nguồn. $v$ không âm, tổng 1; $(1-\beta)v$ có tổng 1/5.

**Kết nối vào–ra:** Tập chủ đề → dữ liệu khởi tạo và điểm thêm; dùng nguyên các giá trị cho vòng 1.

**Quyết định 01/10/2026:** sửa — tiêu đề gọi đúng đối tượng mới (phân phối $v$) và tên đồ thị; viết quy tắc cập nhật trên mặt trang vì s02-03 dùng hai số hạng của nó làm tiêu đề cột; chuyển câu “$v$ cố định, $r^t$ thay đổi” vào ghi chú.

**Nguồn và vị trí:** NG1 VD5.10/Hình 5.15, tr.196–197/PDF22–23.

**Thời lượng:** 2 phút.

**Ghi chú học thuật dự kiến:**

<!-- public-notes:start -->
Tập $S$ có hai phần tử, nên xác suất chọn một trang trong bước dịch chuyển là $1/2$. Xác suất thực hiện nhánh dịch chuyển là $1/5$, vì thế phần điểm thêm vào mỗi trang B, D là $1/10$. $v_i$ là xác suất chọn trang $i$ với điều kiện đã thực hiện nhánh dịch chuyển; $v$ không phải kết quả PageRank. Phép cập nhật giữ nhánh theo liên kết $\beta M_0r^t$ của Bài 03 và thay phần dịch chuyển đều $(1-\beta)u$ bằng $(1-\beta)v$; G4 không có nút cụt nên không cần phần bù. Vector $v$ cố định qua mọi vòng, còn $r^t$ thay đổi. Khởi tạo bằng $v$ là lựa chọn theo ví dụ sách; trạng thái khởi tạo $r^0$ và vector $(1-\beta)v$ được thêm mỗi vòng có vai trò khác nhau.
<!-- public-notes:end -->

### lec04-s02-03 — Vòng lặp thứ nhất trên G4

**Vai trò, mục tiêu, đầu vào và sản phẩm:** Chạy tay; MT1. Đầu vào: G4, v, r0. Sản phẩm: tái tạo từng thành phần r1.

**Luận điểm trung tâm:** Mỗi điểm mới là tổng phần theo liên kết và phần dịch chuyển đúng tập.

**Nội dung hiển thị dự kiến:**

<!-- public-slide:start -->
$r^0=(0,1/2,0,1/2)^\mathsf T$, $\beta=4/5$, $S=\{B,D\}$. G4: A→B, C, D; B→A, D; C→A; D→B, C.

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

**Quyết định 01/10/2026:** sửa — tiêu đề bỏ cụm “PageRank theo chủ đề” trùng tên phần và tránh mơ hồ “chủ đề thứ nhất”; thêm danh sách cạnh G4 để kiểm phép tính tại từng trang khi trang không có hình.

**Nguồn và vị trí:** NG1 VD5.10, tr.197/PDF23; bảng phân rã là diễn giải phép tính nguồn.

**Thời lượng:** 2,5 phút.

**Ghi chú học thuật dự kiến:**

<!-- public-notes:start -->
Từ B, điểm $1/2$ chia cho A, D; từ D, điểm $1/2$ chia cho B, C. Vì vậy mỗi thành phần của $M_0r^0$ bằng $1/4$. Sau khi nhân $4/5$, mỗi trang có $1/5$; B, D nhận thêm $1/10$. Tổng là $1/5+3/10+1/5+3/10=1$. Nếu thay $v$ bằng phân phối đều, bốn điểm mới đều bằng $1/4$, khác phép tính theo tập dịch chuyển đã chọn.
<!-- public-notes:end -->

### lec04-s02-04 — Vòng thứ hai và điểm cố định

**Vai trò, mục tiêu, đầu vào và sản phẩm:** Chạy tay và quan sát; MT1. Đầu vào: r1. Sản phẩm: tính r2 và phân biệt một vòng với giới hạn.

**Luận điểm trung tâm:** Điểm cố định có thể ưu tiên B,D trong khi A,C ngoài tập vẫn nhận điểm dương.

**Nội dung hiển thị dự kiến:**

<!-- public-slide:start -->
Tại A ở vòng 2: $r_A^2=\tfrac45\big(\tfrac12\cdot\tfrac3{10}+\tfrac15\big)=\tfrac7{25}$.

| Trang | $r^1$ | $r^2$ | Điểm cố định $r^*$ |
|---|---:|---:|---:|
| A | $1/5$ | $7/25$ | $9/35$ |
| B | $3/10$ | $41/150$ | $59/210$ |
| C | $1/5$ | $13/75$ | $19/105$ |
| D | $3/10$ | $41/150$ | $59/210$ |

$r^*$ là nghiệm của $r=\beta M_0r+(1-\beta)v$, $\sum_ir_i=1$: phân phối không đổi (Bài 03).

B và D có điểm cố định lớn hơn A; các trang ngoài $S$ vẫn có điểm dương.
<!-- public-slide:end -->

**Bố cục đã chọn:** Phép tính tại A ở trên25%; bảng bốn hàng giữa60%; kết luận dưới15%. Cột điểm cố định có nhãn riêng và đường phân cách, không ám chỉ r2 đã hội tụ.

**Trọng tâm và thứ tự đọc:** Kiểm một cập nhật từ r1 → đối chiếu r2 → đọc giới hạn và thứ hạng.

**Lý do phù hợp sinh viên năm 2:** Tách giới hạn khỏi các vòng hữu hạn giúp sinh viên không coi bảng vài bước là chứng minh hội tụ; B,D hòa có nguyên nhân cấu trúc.

**Giới hạn bố cục và phân chia nội dung:** Không thêm r3 trên mặt slide; giá trị r3 và phép kiểm điểm cố định trong ghi chú.

**Ví dụ, phiếu số và hình thức hóa:** VD1 vòng 1→2 và nghiệm sách; giữ phân số thay số thập phân gần nhau.

**Kết nối vào–ra:** Vết tính cụ thể → nhu cầu một đặc tả có điều kiện dừng và lập luận hội tụ.

**Quyết định 01/10/2026:** sửa — tiêu đề ngắn, gọi hai đối tượng của trang; định nghĩa “điểm cố định” một dòng và nối với “phân phối không đổi” của Bài 03 (G3); ghi chú nêu cách thu nghiệm (giải hệ, thế lại) làm cầu nối sang bài tập s07-01.

**Nguồn và vị trí:** NG1 VD5.10, tr.197/PDF23.

**Thời lượng:** 2,5 phút.

**Ghi chú học thuật dự kiến:**

<!-- public-notes:start -->
Tại B, $r_B^2=(4/5)[(1/3)(1/5)+(1/2)(3/10)]+1/10=41/150$; tại C không có số hạng $1/10$, nên được $13/75$. Vòng 3 là $(31/125,71/250,23/125,71/250)^\mathsf T$. Nghiệm trong cột cuối thu được bằng cách giải hệ bốn phương trình tuyến tính cùng điều kiện tổng bằng $1$; phép thế lại cho thấy nó thỏa phương trình cố định. Cách giải này được dùng lại trong bài tập cuối bài. Việc các vòng đầu tiến gần nghiệm là quan sát; bảo đảm hội tụ đòi hỏi lập luận cho mọi vòng lặp.
<!-- public-notes:end -->

### lec04-s02-05 — Đặc tả PageRank theo chủ đề

**Vai trò, mục tiêu, đầu vào và sản phẩm:** Hình thức hóa; MT1. Đầu vào: vết chạy và bù nút cụt Bài 03. Sản phẩm: xác định miền đầu vào và quy tắc tổng quát.

**Luận điểm trung tâm:** Đổi v và giữ quy ước bù đều tạo đặc tả PageRank theo chủ đề nhất quán với Bài 03.

**Nội dung hiển thị dự kiến:**

<!-- public-slide:start -->
Đầu vào: đồ thị $G=(V,E)$, $n\ge1$; phân phối $v\ge0$, $\sum_i v_i=1$; $0<\beta<1$; ngưỡng $\tau>0$ và số vòng tối đa $K\ge1$.

$$r^{t+1}=\underbrace{\beta M_0r^t}_{\text{theo liên kết}}+\underbrace{\beta\delta^t u}_{\text{bù nút cụt}}+\underbrace{(1-\beta)v}_{\text{dịch chuyển}}.$$

Khi có nút cụt, $\delta^t=\sum_{j:d_j=0}r_j^t$ được bù đều theo $u_i=1/n$ như Bài 03; G4 có $\delta^t=0$.

Đầu ra: vector xấp xỉ và trạng thái đạt ngưỡng hoặc hết số vòng.
<!-- public-slide:end -->

**Bố cục đã chọn:** Đầu vào thành dải trên25%; công thức ba số hạng giữa45%; ký hiệu và đầu ra dưới30%. Dùng một công thức trung tâm, không thêm ma trận số.

**Trọng tâm và thứ tự đọc:** Chốt miền đầu vào → đọc ba nguồn điểm → xác định đầu ra và quy ước bù.

**Lý do phù hợp sinh viên năm 2:** Ba số hạng nối trực tiếp với hai nhánh quen thuộc và trường hợp nút cụt; giữ bù đều tránh thay hai thành phần mô hình cùng lúc.

**Giới hạn bố cục và phân chia nội dung:** Không đưa chứng minh tại trang đặc tả; chi tiết M0 cột0 và tập S đều trong ghi chú.

**Ví dụ, phiếu số và hình thức hóa:** HT1. Ví dụ VD1 có delta=0; v tổng quát bao gồm v đều trên S. Nguồn cầu nối NG5 được công khai.

**Kết nối vào–ra:** Ví dụ không nút cụt → quy tắc cho đồ thị tổng quát → giả mã áp dụng nguyên quy tắc.

**Quyết định 01/10/2026:** sửa — tiêu đề ngắn “Đặc tả PageRank theo chủ đề”; dòng giải thích $\delta^t$, $u$ nêu lý do số hạng bù xuất hiện (đồ thị tổng quát có nút cụt, giữ quy tắc Bài 03) và ghi rõ G4 có $\delta^t=0$, nối với ví dụ vừa chạy. Quy ước cột $M_0$ đã ôn ở s01-06 và có trong ghi chú.

**Nguồn và vị trí:** NG1 §5.3.2, tr.196; NG1 §5.1.5; NG5 quy ước bù nút cụt. Phần bù là cầu nối đã duyệt.

**Thời lượng:** 3 phút.

**Ghi chú học thuật dự kiến:**

<!-- public-notes:start -->
Với $d_j>0$, $(M_0)_{ij}=1/d_j$ nếu có cạnh $j\to i$; cột nút cụt bằng $0$. Điểm bị thiếu trong nhánh theo liên kết là $\beta$ lần tổng điểm nút cụt, được bù đều bằng $u$. Phân phối $v$ chỉ điều khiển nhánh dịch chuyển. Khi $S$ không rỗng và chọn đều trên $S$, $v_i=1/|S|$ trên $S$ và bằng $0$ bên ngoài. Đồ thị, $\beta$, $v$ và quy tắc bù được giữ cố định suốt phép lặp.
<!-- public-notes:end -->

### lec04-s02-06 — Giả mã PageRank theo chủ đề

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

`delta` là $\delta^t$, điểm ở nút cụt; `Delta` là $\|r^{t+1}-r^t\|_1$, dùng để dừng. Mọi đóng góp trong một vòng dùng cùng vector điểm cũ.
<!-- public-slide:end -->

**Bố cục đã chọn:** Khối giả mã chiếm85% khung, câu bất biến đọc–ghi ở đáy15%; dùng thành phần mã chung. Hai tên r/new luôn giữ nguyên.

**Trọng tâm và thứ tự đọc:** Đọc khởi tạo → phần bù và dịch chuyển → cạnh → phép đo thay đổi → thay vector và trả trạng thái.

**Lý do phù hợp sinh viên năm 2:** Giả mã tách r và new phù hợp kiến thức mảng/vòng lặp năm2; sinh viên thấy rõ lúc nào dữ liệu mới được phép trở thành dữ liệu cũ.

**Giới hạn bố cục và phân chia nội dung:** Giữ11 dòng điều khiển như trên; giả thiết đầu vào tham chiếu ngay trang trước, không thêm mã framework.

**Ví dụ, phiếu số và hình thức hóa:** HT1; VD1 là phép chạy của cùng thuật toán. K nguyên dương; tau dương. Ký hiệu Latin trong giả mã tương ứng ký hiệu toán đã định nghĩa.

**Kết nối vào–ra:** Phương trình cập nhật → thứ tự thực thi → bất biến cần chứng minh.

**Quyết định 01/10/2026:** sửa — tiêu đề gọi đúng đối tượng của trang (giả mã); thêm dòng phân biệt `delta` ($\delta^t$) với `Delta` (sai khác dùng để dừng) vì hai tên gần giống nhau.

**Nguồn và vị trí:** NG1 §5.3.2, tr.196–197; giả mã cụ thể hóa phép lặp nguồn và quy ước NG5.

**Thời lượng:** 3 phút.

**Ghi chú học thuật dự kiến:**

<!-- public-notes:start -->
Vector `new` được khởi tạo bằng phần bù và phần dịch chuyển, không phụ thuộc từng cạnh. Mỗi cạnh $j\to i$ cộng một phần điểm cũ của $j$, nên tổng đóng góp không phụ thuộc thứ tự duyệt cạnh trong số học chính xác. Sau khi hoàn tất tất cả các đỉnh, `Delta` đo chênh lệch theo tổng trị tuyệt đối. Nếu hết $K$ vòng mà chưa đạt $\tau$, vector hiện tại vẫn là đầu ra tính được, nhưng trạng thái không xác nhận tiêu chí dừng đã đạt.
<!-- public-notes:end -->

### lec04-s02-07 — Bất biến tổng điểm

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

Lập luận của Bài 03 giữ nguyên; điều kiện mới duy nhất là $v\ge0$, $\sum_iv_i=1$. Khởi tạo $r^0=v$ thỏa giả thiết.
<!-- public-slide:end -->

**Bố cục đã chọn:** Giả thiết ở trên20%; bảng ba dòng giữa50%; phép cộng và kết luận dưới30%. Ba nhãn trùng với HT1.

**Trọng tâm và thứ tự đọc:** Đọc giả thiết → đếm từng nguồn điểm → cộng tổng → kiểm cơ sở r0.

**Lý do phù hợp sinh viên năm 2:** Phép chứng minh dùng tổng hữu hạn và xác suất cơ bản; bảng giúp truy nguyên từng số hạng thay vì ghi một kết luận bảo toàn không có lý do.

**Giới hạn bố cục và phân chia nội dung:** Chỉ chứng minh bảo toàn; không gọi bảo toàn là hội tụ. Phép kiểm số VD1 ở ghi chú.

**Ví dụ, phiếu số và hình thức hóa:** HT2 phần bất biến; VD1 tổng mỗi vòng bằng 1 là phép kiểm độc lập, không thay chứng minh.

**Kết nối vào–ra:** Thuật toán → bất biến ở mọi vòng; tính co tiếp tục giải thích giới hạn.

**Quyết định 01/10/2026:** sửa — tiêu đề gọi đúng kết quả (bất biến tổng điểm); câu chốt chỉ ra điểm mới so với “Bảo toàn tổng điểm” của Bài 03 là điều kiện $v\ge0$, $\sum_iv_i=1$, tránh lặp lại kết quả cũ như một mệnh đề mới.

**Nguồn và vị trí:** NG1 §5.3.2 cùng mô hình §5.1.5; chứng minh từ quy tắc cập nhật đã duyệt, không trích nguyên sách.

**Thời lượng:** 2,5 phút.

**Ghi chú học thuật dự kiến:**

<!-- public-notes:start -->
Một trang không cụt chia đều điểm cho đúng $d_j$ cạnh ra, nên tổng phần điểm của trang ấy sau khi nhân $\beta$ là $\beta r_j^t$. Cộng trên mọi trang không cụt được $\beta(1-\delta^t)$. Các nút cụt trả lại $\beta\delta^t$ bằng bù đều; phân phối $v$ có tổng bằng $1$ nhận phần $1-\beta$. Mọi hệ số đều không âm và cơ sở $r^0=v$ thỏa giả thiết, hoàn thành lập luận quy nạp. Bất biến chỉ xác nhận mỗi trạng thái là phân phối hợp lệ; chưa xác nhận dãy có giới hạn.
<!-- public-notes:end -->

### lec04-s02-08 — Hội tụ và cận sai số khi dừng

**Vai trò, mục tiêu, đầu vào và sản phẩm:** Hội tụ và điều kiện dừng; MT1. Đầu vào: HT2 và chuẩn1. Sản phẩm: phân biệt Delta với sai số nghiệm, nêu cơ sở duy nhất.

**Luận điểm trung tâm:** Tính co bảo đảm nghiệm duy nhất và chặn sai số tới nghiệm theo chênh lệch hai vòng bằng một hệ số xác định.

**Nội dung hiển thị dự kiến:**

<!-- public-slide:start -->
$\bar M$: $M_0$ với mỗi cột nút cụt thay bằng $u$ (ma trận $S$ của Bài 03); $\bar M\ge0$, tổng mỗi cột bằng $1$.

Với $F(r)=\beta\bar Mr+(1-\beta)v$ và $0<\beta<1$: $\|F(p)-F(q)\|_1\le\beta\|p-q\|_1$ (Bài 03). Khoảng cách sau cập nhật không vượt $\beta$ lần khoảng cách trước (tính co), nên có duy nhất một điểm cố định $r^*$.

Đặt $\Delta=\|r^{t+1}-r^t\|_1$; các sai khác sau đó không quá $\beta\Delta,\beta^2\Delta,\ldots$, nên
$$\|r^{t+1}-r^*\|_1\le\beta\Delta+\beta^2\Delta+\cdots=\frac{\beta}{1-\beta}\Delta.$$

Với $\beta=4/5$, cận sai số là $4\Delta$.
<!-- public-slide:end -->

**Bố cục đã chọn:** Giả thiết về ma trận và một dòng nhắc tính co ở dải trên 30%; định nghĩa độ thay đổi và tổng đuôi cấp số nhân ở giữa 50%; ví dụ hệ số 4 ở dải dưới 20%. Cận sai số của vector mới là công thức trung tâm.

**Trọng tâm và thứ tự đọc:** Nhận lại giả thiết ma trận đã bù → nhắc kết quả co của Bài 03 → theo các sai khác trong tổng đuôi → đọc cận sai số của vector mới.

**Lý do phù hợp sinh viên năm 2:** Tính co đã có ở Bài 03; tổng đuôi cấp số nhân làm hiện bước mới nối độ thay đổi với sai số nghiệm. Ví dụ beta bằng 4/5 phân biệt hai đại lượng mà không thêm một phép tính dài.

**Giới hạn bố cục và phân chia nội dung:** Mặt slide tập trung cận dừng trong 3 phút. Vector chỉ báo nút cụt và chứng minh co, tồn tại, duy nhất nằm trong ghi chú; không mở phần lý thuyết điểm cố định hoặc phổ mới.

**Ví dụ, phiếu số và hình thức hóa:** HT2. Chuẩn1 là tổng trị tuyệt đối; v có thể có thành phần0. Phiếu VD1 cung cấp beta, không tạo ngưỡng thực nghiệm.

**Kết nối vào–ra:** Bảo toàn miền phân phối → co và điểm cố định → có thể kết hợp các vector chủ đề cùng mô hình.

**Quyết định 01/10/2026:** sửa — tiêu đề gọi hai kết quả của trang (hội tụ, cận sai số khi dừng) thay cho thuật ngữ chưa giải nghĩa; nêu $\bar M$ là ma trận $S$ của Bài 03 (G2); giải nghĩa “tính co” bằng lời và dẫn nguồn bất đẳng thức từ Bài 03 (G3); thêm bước “các sai khác sau đó không quá $\beta\Delta,\beta^2\Delta,\ldots$” trước chuỗi cấp số nhân.

**Nguồn và vị trí:** NG1 §5.3.2; NG5 lập luận co kế thừa. Bất đẳng thức và cận đuôi là diễn giải toán học bổ sung đã duyệt.

**Thời lượng:** 2,5 phút.

**Ghi chú học thuật dự kiến:**

<!-- public-notes:start -->
Bài 03 ký hiệu ma trận này là $S$; Bài 04 dùng $\bar M$ vì $S$ đã chỉ tập chủ đề. Đặt $z_j=1$ nếu $j$ là nút cụt và $z_j=0$ nếu không. Khi đó $\bar M=M_0+uz^\mathsf T$ không âm và có tổng mỗi cột bằng $1$. Lập luận co kế thừa Bài 03: vector dịch chuyển cố định triệt tiêu trong $F(p)-F(q)$. Bất đẳng thức tam giác và việc đổi thứ tự tổng cho
$$\|F(p)-F(q)\|_1\le\beta\sum_j|p_j-q_j|\sum_i\bar M_{ij}=\beta\|p-q\|_1.$$
Các sai khác liên tiếp giảm theo cấp số nhân. Tổng khoảng cách từ một vòng tới mọi vòng sau hữu hạn và phần đuôi tiến về $0$, nên dãy hội tụ. Tính liên tục của $F$ cho phương trình cố định. Nếu hai điểm cố định cách nhau một khoảng $D$, thì $D\le\beta D$; vì $\beta<1$, suy ra $D=0$.

Với $\Delta=\|r^{t+1}-r^t\|_1$, sai khác kế tiếp không quá $\beta\Delta$. Tổng phần đuôi các sai khác sau vector mới $r^{t+1}$ không quá $\beta\Delta/(1-\beta)$. Để cận sai số không quá $\varepsilon>0$, đủ chọn $\tau\le(1-\beta)\varepsilon/\beta$ và dừng khi $\Delta\le\tau$.
<!-- public-notes:end -->

### lec04-s02-09 — Ký hiệu cho nhiều chủ đề

**Vai trò, mục tiêu, đầu vào và sản phẩm:** Định nghĩa và cầu nối; MT1, MT5. Đầu vào: điểm cố định theo v. Sản phẩm: phân biệt nhãn chủ đề j, chỉ số vòng t, đầu vào v^(j), nghiệm r^(j) và trọng số w_j.

**Luận điểm trung tâm:** Mỗi chủ đề có một phân phối dịch chuyển đầu vào và một vector PageRank hội tụ trên cùng n trang.

**Nội dung hiển thị dự kiến:**

<!-- public-slide:start -->
Có $k$ chủ đề. Từ đây $j=1,\ldots,k$ chỉ chủ đề, $i$ chỉ trang, $t$ chỉ vòng lặp.

| Ký hiệu | Vai trò |
| --- | --- |
| $v^{(j)}\in\mathbb R^n$ | Phân phối dịch chuyển đầu vào của chủ đề $j$ |
| $r^{(j)}\in\mathbb R^n$ | Điểm cố định PageRank của chủ đề $j$ trên $n$ trang |

Mỗi chủ đề dùng cùng $\bar M$ và $\beta$:
$$r^{(j)}=\beta\bar Mr^{(j)}+(1-\beta)v^{(j)}.$$
<!-- public-slide:end -->

**Bố cục đã chọn:** Dòng phân biệt j và t ở trên; bảng ba hàng ở giữa; phương trình cố định ở dưới. Không dùng hình tổng trước khi định nghĩa các vector.

**Trọng tâm và thứ tự đọc:** Chỉ số chủ đề → đầu vào → kết quả → trọng số → phương trình riêng từng chủ đề.

**Lý do phù hợp sinh viên năm 2:** Bảng đối chiếu đầu vào và kết quả ngăn nhầm các vector cùng kích thước; tách j khỏi t trước công thức tổng.

**Giới hạn bố cục và phân chia nội dung:** Phép cộng các phương trình chuyển sang trang kế tiếp. Không thêm ví dụ số.

**Ví dụ, phiếu số và hình thức hóa:** HT3; k chủ đề, n trang, j chỉ số chủ đề; cùng Mbar và beta.

**Kết nối vào–ra:** Nghiệm duy nhất theo v → các nghiệm theo chủ đề → tổng có trọng số.

**Quyết định 01/10/2026:** sửa — tiêu đề “Ký hiệu cho nhiều chủ đề” gọi đúng chức năng của trang; nêu rõ $j$ từ đây chỉ chủ đề vì ở đặc tả và giả mã $j$ chỉ trang nguồn; chuyển $w_j$ sang trang xử lý truy vấn, nơi nhu cầu kết hợp xuất hiện (thứ tự cụm mới: ký hiệu → quy trình tiền tính và truy vấn → tính đúng của phép ghép → chi phí).

**Nguồn và vị trí:** NG1 §5.3.2 tr.196; §5.3.4 tr.199/PDF25.

**Thời lượng:** 1 phút.

**Ghi chú học thuật dự kiến:**

<!-- public-notes:start -->
Chủ đề $j$ được xác định bằng phân phối dịch chuyển $v^{(j)}$. Phép lặp PageRank với đầu vào này cho vector hội tụ $r^{(j)}$; thành phần $r_i^{(j)}$ là điểm của trang $i$ theo chủ đề $j$. Cả hai vector đều có $n$ thành phần, nhưng một vector là đầu vào, một vector là kết quả. Dấu ngoặc trong chỉ số $(j)$ phân biệt nhãn chủ đề với chỉ số vòng $t$ của $r^t$.

Trong đặc tả và giả mã trước, $j$ chỉ trang nguồn; từ đây $j$ chỉ chủ đề và trang được đánh chỉ số $i$. Điều kiện cùng $\bar M$ bao gồm cùng đồ thị và cùng quy tắc bù nút cụt. Cùng $\beta$ giữ hệ số truyền theo liên kết không đổi. Mỗi chủ đề cần một vector như vậy, tính trước khi có truy vấn, thay cho một vector riêng của từng người dùng. Khi có truy vấn, $k$ vector này phải được kết hợp theo mức quan tâm tới từng chủ đề.
<!-- public-notes:end -->

### lec04-s02-11 — Tiền tính và xử lý truy vấn

**Vai trò, mục tiêu, đầu vào và sản phẩm:** Ứng dụng và thu hồi tình huống; MT1, MT5. Đầu vào: k vector và chi phí. Sản phẩm: phân biệt tiền tính với xử lý truy vấn.

**Luận điểm trung tâm:** Vector chủ đề được tiền tính và dùng lại khi người dùng chọn ngữ cảnh truy vấn.

**Nội dung hiển thị dự kiến:**

<!-- public-slide:start -->
**Trước truy vấn**

Chọn các phân phối $v^{(j)}$.

Tính và lưu các vector $r^{(j)}$ trên toàn bộ $n$ trang.

**Khi có truy vấn**

Xác định trọng số $w_j\ge0$, $\sum_jw_j=1$, theo ngữ cảnh và tập trang ứng viên $C$.

Với từng $i\in C$, ghép:

$$q_i=\sum_{j=1}^k w_jr_i^{(j)}.$$

Với “jaguar”: trọng số lớn cho chủ đề động vật hoặc ô tô, tùy ngữ cảnh. Khi có truy vấn chỉ ghép điểm đã lưu, không lặp lại PageRank.
<!-- public-slide:end -->

**Bố cục đã chọn:** Hai thẻ bằng nhau: tiền tính bên trái, truy vấn bên phải; công thức theo thành phần i trong C đặt ở thẻ phải. Dòng dưới thu hồi ngữ cảnh jaguar.

**Trọng tâm và thứ tự đọc:** Đọc các vector đã lưu → xác định trọng số và ứng viên → lấy từng điểm và cộng → giới hạn công việc.

**Lý do phù hợp sinh viên năm 2:** Hai hàng phân biệt tính toán dùng lại với thao tác theo ngữ cảnh, nối trực tiếp giới hạn bộ nhớ ở mở đầu.

**Giới hạn bố cục và phân chia nội dung:** Không dùng sơ đồ SVG cũ để tránh lặp chữ; không tạo ví dụ trọng số số học. Sắp xếp và xác định ứng viên nằm ngoài phép ghép.

**Ví dụ, phiếu số và hình thức hóa:** HT3 ở mức sử dụng; ví dụ định tính jaguar của NG1, không có điểm mới.

**Kết nối vào–ra:** Ký hiệu nhiều chủ đề → quy trình hai giai đoạn, đưa vào $w_j$ và $C$ → nhu cầu chứng minh phép ghép (s02-09a) → đếm chi phí (s02-10).

**Quyết định 01/10/2026:** sửa và chuyển vị trí — đặt ngay sau s02-09, trước s02-09a, theo trình tự bốn bước MMDS §5.3.3; trang tạo nhu cầu kết hợp trước khi chứng minh tính đúng của phép kết hợp. Định nghĩa $w_j$ và $C$ tại đây (G6). Chi phí $\Theta(kc)$ chỉ còn ở s02-10. Tiêu đề “Tiền tính và xử lý truy vấn”.

**Nguồn và vị trí:** NG1 §5.3.1–5.3.4 tr.195–199; đặc biệt phép ghép theo tỷ lệ ở §5.3.4 tr.199.

**Thời lượng:** 2 phút.

**Ghi chú học thuật dự kiến:**

<!-- public-notes:start -->
Quy trình theo MMDS §5.3.3 gồm bốn bước: chọn các chủ đề; chọn tập dịch chuyển cho từng chủ đề và tính vector PageRank tương ứng; xác định chủ đề liên quan tới truy vấn; dùng các vector của chủ đề đó để sắp thứ tự kết quả. Hai bước đầu chạy trước khi có truy vấn, trên toàn bộ $n$ trang. Bước thứ ba có thể dựa vào lựa chọn của người dùng, từ ngữ trong các truy vấn gần đây hoặc thông tin về người dùng; cách suy ra chủ đề nằm ngoài phạm vi phép tính của bài.

Trọng số $w_j$ biểu diễn mức quan tâm của truy vấn hoặc người dùng tới chủ đề $j$; mỗi người dùng chỉ cần lưu $k$ số này. $C$ là tập trang ứng viên đã được xác định cho truy vấn. Với mỗi $i\in C$, phép ghép nhân $k$ điểm đã lưu với các trọng số rồi cộng. Ví dụ “jaguar” chỉ minh họa hai ngữ cảnh, không ấn định trọng số số học. Phép ghép này chỉ hợp lệ nếu tổng có trọng số của các nghiệm chủ đề trùng với nghiệm PageRank khi phân phối dịch chuyển là $\sum_jw_jv^{(j)}$; điều này cần được chứng minh.
<!-- public-notes:end -->

### lec04-s02-09a — Tính tuyến tính theo phân phối dịch chuyển

**Vai trò, mục tiêu, đầu vào và sản phẩm:** Lập luận và ứng dụng; MT1, MT5. Đầu vào: các đại lượng của S02-09 và tính duy nhất. Sản phẩm: chứng minh đẳng thức ghép và nêu đủ điều kiện.

**Luận điểm trung tâm:** Cùng toán tử và beta cho phép ghép các nghiệm PageRank theo trọng số của phân phối dịch chuyển.

**Nội dung hiển thị dự kiến:**

<!-- public-slide:start -->
Giữ cùng $\bar M$, $\beta$; $w_j\ge0$ và $\sum_jw_j=1$.

$$v=\sum_{j=1}^k w_jv^{(j)}\quad\Longrightarrow\quad r^*=\sum_{j=1}^k w_jr^{(j)}.$$

Nhân phương trình của chủ đề $j$ với $w_j$, rồi cộng:

$$\sum_jw_jr^{(j)}=\beta\bar M\sum_jw_jr^{(j)}+(1-\beta)\sum_jw_jv^{(j)}.$$

Tổng có trọng số thỏa phương trình PageRank với $v$. Điểm cố định là duy nhất, nên tổng này bằng $r^*$.

Điểm ghép $q_i$ khi có truy vấn bằng đúng $r_i^*$ với $v=\sum_jw_jv^{(j)}$; mỗi người dùng chỉ cần $k$ trọng số.
<!-- public-slide:end -->

**Bố cục đã chọn:** Giả thiết ở trên; công thức ghép lớn giữa; một dòng cộng phương trình và kết luận duy nhất ở dưới.

**Trọng tâm và thứ tự đọc:** Điều kiện chung → cặp tổng → phương trình của tổng → tính duy nhất.

**Lý do phù hợp sinh viên năm 2:** Phép phân phối ma trận qua tổng dùng đại số tuyến tính đã học; các vector đã được định nghĩa ở trang trước.

**Giới hạn bố cục và phân chia nội dung:** Mặt trang chỉ chứng minh cho nghiệm hội tụ. Sai số tổng ghép các xấp xỉ thuộc ghi chú.

**Ví dụ, phiếu số và hình thức hóa:** HT3; giữ w không âm, tổng1; không đưa tỷ lệ số tự tạo.

**Kết nối vào–ra:** Các nghiệm riêng → nghiệm cho ngữ cảnh ghép → chi phí tiền tính và chi phí truy vấn.

**Quyết định 01/10/2026:** sửa — đứng sau s02-11 nên chứng minh trả lời nhu cầu vừa nêu; tiêu đề gọi tên kết quả (tính tuyến tính theo $v$); thêm khối kết luận thu hồi nhu cầu lưu trữ ở s01-04 (mỗi người dùng chỉ cần $k$ trọng số).

**Nguồn và vị trí:** NG1 §5.3.2 tr.196; §5.3.4 tr.199/PDF25; diễn giải đại số từ phương trình cố định.

**Thời lượng:** 2 phút.

**Ghi chú học thuật dự kiến:**

<!-- public-notes:start -->
Đặt $q=\sum_jw_jr^{(j)}$. Mỗi $r^{(j)}$ thỏa phương trình cố định của chủ đề tương ứng. Nhân với $w_j$ rồi cộng cho $q=\beta\bar Mq+(1-\beta)v$, với $v=\sum_jw_jv^{(j)}$. Vì mọi trọng số không âm và có tổng bằng $1$, cả $q$ và $v$ đều là phân phối xác suất. Tính duy nhất của điểm cố định suy ra $q=r^*$.

Đẳng thức này áp dụng cho các nghiệm hội tụ. Khi lưu các xấp xỉ $\hat r^{(j)}$, tổng ghép cũng là xấp xỉ; sai số thỏa $\|\sum_jw_j\hat r^{(j)}-r^*\|_1\le\sum_jw_j\|\hat r^{(j)}-r^{(j)}\|_1$. Nếu đổi $\beta$ hoặc cách bù nút cụt theo chủ đề, không thể dùng chung toán tử trong phép chứng minh này. Khi các điều kiện được giữ nguyên, xử lý truy vấn chỉ cần ghép các điểm đã tiền tính.
<!-- public-notes:end -->


### lec04-s02-10 — Chi phí tiền tính và truy vấn

**Vai trò, mục tiêu, đầu vào và sản phẩm:** Đánh giá chi phí; MT5. Đầu vào: giả mã HT1 và ghép HT3. Sản phẩm: truy nguyên số hạng thời gian và bộ nhớ.

**Luận điểm trung tâm:** Chi phí mỗi vòng tuyến tính theo đỉnh/cạnh, còn lưu các kết quả tăng theo số chủ đề.

**Nội dung hiển thị dự kiến:**

<!-- public-slide:start -->
Mô hình: phép toán vô hướng chi phí đơn vị; $n$ đỉnh, $\ell$ cạnh, danh sách kề.

| Công việc | Khối lượng mỗi vòng |
| --- | --- |
| Cộng điểm theo liên kết | $\ell$ cạnh |
| Bù, dịch chuyển, so sánh | Số lượt cố định trên $n$ đỉnh |

**Tiền tính.** Mỗi vòng $\Theta(n+\ell)$; $k$ chủ đề, tối đa $K$ vòng: $O(kK(n+\ell))$. Bộ nhớ: đầu vào $\Theta(n+\ell)$, phụ $\Theta(n)$; lưu kết quả $\Theta(kn)$ số.

**Khi có truy vấn.** Mỗi $i\in C$ cần $k$ phép nhân–cộng: tổng $\Theta(kc)$, $c=|C|$. Chưa gồm tìm ứng viên, xác định $w_j$ và sắp xếp.
<!-- public-slide:end -->

**Bố cục đã chọn:** Mô hình trên20%, bảng hai hàng giữa35%, hai khối kết quả thời gian/bộ nhớ dưới45%. Không đặt đồ thị hoặc giả mã đầy đủ ở cùng trang.

**Trọng tâm và thứ tự đọc:** Đọc đơn vị → truy hai bước giả mã → cộng → phân biệt chi phí một vector với lưu k kết quả.

**Lý do phù hợp sinh viên năm 2:** Phép đếm theo cạnh phù hợp nền phân tích thuật toán; tách đầu vào/phụ/đầu ra ngăn gộp bộ nhớ sai.

**Giới hạn bố cục và phân chia nội dung:** C là tập ứng viên, c=|C|. Mặt trang nêu lưu trữ và ghép chưa gồm sắp xếp; ghi chú tách tìm ứng viên, chọn trọng số, ghép và sắp xếp.

**Ví dụ, phiếu số và hình thức hóa:** HT3, VD1 có n4/ell8 chỉ đối chiếu vai trò, không coi là dữ liệu hiệu năng.

**Kết nối vào–ra:** Giả mã và ghép vector → giới hạn tài nguyên của tình huống mở đầu → quy trình sử dụng.

**Quyết định 01/10/2026:** sửa — nay đứng sau s02-11 nên $C$, $w_j$ đã được định nghĩa (G6); tiêu đề gọi hai giai đoạn được đếm; thay đoạn văn bốn số đo bằng hai thẻ “Tiền tính”, “Khi có truy vấn” khớp bố cục s02-11; giữ bảng đếm mỗi vòng để số hạng truy được về giả mã.

**Nguồn và vị trí:** NG1 §5.2.1 tr.191–192; §5.3.2–5.3.4 tr.196–199. Phép đếm từ HT1/HT3.

**Thời lượng:** 2 phút.

**Ghi chú học thuật dự kiến:**

<!-- public-notes:start -->
Mỗi cạnh tạo đúng một đóng góp; các bước khởi tạo vector, cộng bù và đo $\Delta$ duyệt mỗi đỉnh một số lần không phụ thuộc kích thước. Danh sách kề lưu đỉnh và cạnh, còn các vector $r$, $v$ cùng vector điểm mới cần bộ nhớ tuyến tính theo $n$.

Nếu chủ đề $j$ thực chạy $K_j$ vòng, tiền tính độc lập $k$ vector cần $\Theta((\sum_{j=1}^kK_j)(n+\ell))$ phép toán. Giới hạn tối đa $K$ vòng cho mỗi vector cho cận $O(kK(n+\ell))$. Nếu mọi vector đều chạy đủ $K$ vòng thì chi phí là $\Theta(kK(n+\ell))$. Tính tuần tự tiết kiệm trạng thái lặp trong bộ nhớ nhưng vẫn phải thực hiện phép lặp cho từng chủ đề.

Bộ nhớ lưu kết quả tăng tuyến tính theo số chủ đề, độc lập với số người dùng; đây là lợi ích so với một vector riêng cho mỗi người dùng. Khi có truy vấn, phép ghép $q_i$ chỉ đọc $k$ số đã lưu cho mỗi ứng viên, nên không cần dựng vector ghép trên toàn bộ $n$ trang.
<!-- public-notes:end -->

### lec04-s02-12 — Kiểm tra PageRank theo chủ đề

**Vai trò, mục tiêu, đầu vào và sản phẩm:** Kiểm tra riêng S02; MT1. Đầu vào: HT1 và VD1. Sản phẩm: tính điểm ngoài tập dịch chuyển, giải thích ý nghĩa S.

**Luận điểm trung tâm:** Vận dụng phép cập nhật cho một trang ngoài tập dịch chuyển và vận dụng cận sai số khi dừng.

**Nội dung hiển thị dự kiến:**

<!-- public-slide:start -->
G4: A→B,C,D; B→A,D; C→A; D→B,C.

$\beta=4/5$, $S=\{B,D\}$.

$r^1=(1/5,3/10,1/5,3/10)^\mathsf T$

$r^2=(7/25,41/150,13/75,41/150)^\mathsf T$

**Câu hỏi:**
1. Tính $r_C^3$ và chỉ rõ các trang đóng góp.
2. Tính $\Delta=\|r^2-r^1\|_1$ và cận $\beta\Delta/(1-\beta)$ cho sai số của $r^2$.
<!-- public-slide:end -->

**Bố cục đã chọn:** Đồ thị trái45%; vector cũ, tham số và hai yêu cầu phải55%. Đáp án không xuất hiện trên các trang trước.

**Trọng tâm và thứ tự đọc:** Theo các cạnh vào C → đọc điểm nguồn trong $r^2$ → quyết định phần dịch chuyển của C; sau đó tính $\Delta$ và áp dụng cận dừng.

**Lý do phù hợp sinh viên năm 2:** Yêu cầu tập trung một thành phần nhưng đồng thời đo chiều cạnh, chia bậc ra và ranh giới tập dịch chuyển.

**Giới hạn bố cục và phân chia nội dung:** Hai câu, không yêu cầu giải cả hệ. Đáp án và phép so sánh nằm trong ghi chú.

**Ví dụ, phiếu số và hình thức hóa:** VD1 $r^2\to r^3$ (MMDS tr.197); cận dừng s02-08; mọi dữ kiện hiện đủ để tính lại.

**Kết nối vào–ra:** Phép cập nhật đã hoàn chỉnh → khả năng đồ thị liên kết bị xây có chủ đích để thay điểm.

**Quyết định 01/10/2026:** sửa — tiêu đề ngắn “Kiểm tra PageRank theo chủ đề”; ghi chú thêm câu nối ranh giới S02→S03 (điểm do cấu trúc liên kết quyết định nên có thể bị tác động bằng cạnh mới). Sau rà lại: đổi câu hỏi vì đáp án cũ ($r_C^2=13/75$, “trang ngoài $S$ có điểm dương”) đã hiển thị ở s02-01, s02-04; câu mới kiểm vòng 3 và cận sai số khi dừng.

**Nguồn và vị trí:** NG1 VD5.10, tr.197; câu hỏi áp dụng trực tiếp đúng dữ kiện ví dụ.

**Thời lượng:** 3 phút.

**Nhiệm vụ và tiêu chí nội bộ:** Slide kiểm tra riêng của phần.

- Câu hỏi/đề: Hai yêu cầu như nội dung hiển thị, trên toàn bộ dữ kiện G4 và r1.
- Đáp án/gợi ý: $r_C^3=23/125$; đóng góp từ A, D. $\Delta=4/25$, cận $16/25$; sai số thật $8/175$.
- Tiêu chí đánh giá: Đúng hai nguồn, đúng bậc ra 3 và 2, không cộng $1/10$ vào C; tính đúng $\Delta$ theo chuẩn tổng trị tuyệt đối và hệ số $\beta/(1-\beta)=4$.
- Phân bổ hoạt động: Tính và lập luận1,5 phút; trả lời0,5 phút; đối chiếu1 phút; tổng3 phút.

**Ghi chú học thuật dự kiến:**

<!-- public-notes:start -->
C nhận điểm qua các cạnh A→C (A có ba cạnh ra) và D→C (D có hai cạnh ra); C không thuộc $S$ nên không nhận phần dịch chuyển: $r_C^3=(4/5)[(1/3)(7/25)+(1/2)(41/150)]=23/125$, khớp vòng 3 của MMDS. Trang ngoài $S$ vẫn có điểm dương nhờ các cạnh tới nó.

$r^2-r^1=(2/25,-2/75,-2/75,-2/75)^\mathsf T$, nên $\Delta=4/25$. Với $\beta=4/5$, cận sai số là $4\Delta=16/25$. Sai số thật $\|r^2-r^*\|_1=8/175$ nhỏ hơn nhiều: cận bảo đảm sai số không vượt quá nó, không cho giá trị sai số.

Điểm PageRank, kể cả theo chủ đề, do cấu trúc liên kết và phân phối dịch chuyển quyết định; khi $v$ cố định, chỉ còn các cạnh thay đổi được. Người kiểm soát một phần đồ thị có thể thêm cạnh để làm tăng điểm của một trang; cơ chế này được phân tích với PageRank dịch chuyển đều.
<!-- public-notes:end -->

## S03. Cơ chế liên kết rác

Mô hình và phân tích. Liên kết có thể bị thao túng → ba vùng quyền tác động → điểm một hỗ trợ → ba nguồn điểm đích → giải phương trình và phân biệt xấp xỉ → giới hạn, kiểm tra. Đây là phân tích mô hình cân bằng, không có thuật toán thực thi riêng; giả mã không áp dụng. Đếm trang/cạnh và các giả thiết thay cho một phân tích thời gian không có đối tượng. Đầu ra là nhu cầu bổ sung thông tin tin cậy.

Phân bổ: 8 slide, 20 phút.

### lec04-s03-01 — Liên kết rác

**Vai trò, mục tiêu, đầu vào và sản phẩm:** Tình huống và vấn đề; MT2. Đầu vào: điểm phụ thuộc cạnh. Sản phẩm: xác định mục tiêu và quyền tác động của người tạo liên kết rác.

**Luận điểm trung tâm:** Liên kết có thể được tạo để tăng điểm trang đích ngoài ý nghĩa chất lượng nội dung.

**Nội dung hiển thị dự kiến:**

<!-- public-slide:start -->
PageRank cộng điểm theo liên kết vào. Liên kết rác được tạo để làm tăng điểm một trang không tương xứng với giá trị nội dung.

- Dữ liệu: đồ thị liên kết; PageRank dịch chuyển đều.
- Quyền tác động: thêm liên kết ở trang sở hữu hoặc được phép đăng.
- Mục tiêu: tập trung điểm tại trang đích.

Vấn đề: định lượng mức một cấu trúc liên kết đơn giản làm tăng điểm trang đích.
<!-- public-slide:end -->

**Bố cục đã chọn:** Định nghĩa trên25%; ba khối “Dữ liệu–Quyền tác động–Mục tiêu” ở giữa55%; câu giới hạn kiểm tra ở dưới20%. Không dùng ảnh trang rác.

**Trọng tâm và thứ tự đọc:** Đọc điều bị thao túng → dữ liệu có thể kiểm soát → đầu ra người thao túng muốn tăng.

**Lý do phù hợp sinh viên năm 2:** Sinh viên nhìn cùng đồ thị dưới giả thiết đầu vào có chủ ý đối kháng, trước khi tiếp nhận phương trình mới.

**Giới hạn bố cục và phân chia nội dung:** Không mô tả thủ thuật thao tác trên hệ thống thực; mô hình đồ thị cụ thể nằm ở trang sau. Không đưa số lượng trang rác không có nguồn.

**Ví dụ, phiếu số và hình thức hóa:** Khái niệm §5.4; không có ví dụ số hoặc giả mã riêng.

**Kết nối vào–ra:** S02 đã thay phân phối dịch chuyển; ở đây trở lại phân phối đều u và xét tác động của việc thay cạnh → kiến trúc cụm xác định các nguồn điểm cần phân tích.

**Quyết định 01/10/2026:** sửa — tiêu đề ngắn “Liên kết rác”; câu mở nêu cơ chế làm liên kết rác có tác dụng (PageRank cộng điểm theo liên kết vào), nối với câu cuối S02; thẻ quyền tác động không dùng “cụm” trước khi định nghĩa; khối kết luận chung chung được thay bằng vấn đề định lượng mà S03 giải. Khối nội dung công khai được đồng bộ lại với HTML (bản trước còn lệch bố cục thẻ).

**Nguồn và vị trí:** NG1 mở §5.4 và §5.4.1, tr.199–200/PDF25–26.

**Thời lượng:** 2 phút.

**Ghi chú học thuật dự kiến:**

<!-- public-notes:start -->
Giáo trình xét các kỹ thuật tạo liên kết nhằm làm PageRank đánh giá cao một trang hơn mức đóng góp nội dung. Mô hình tiếp theo tách phần web không thể tác động, phần có thể đặt liên kết và phần sở hữu. Phân tích chỉ mô tả tác động của một cấu trúc xác định; không suy rằng mọi nhóm trang liên kết dày đều là liên kết rác.
<!-- public-notes:end -->

### lec04-s03-02 — Cụm thao túng liên kết

**Vai trò, mục tiêu, đầu vào và sản phẩm:** Mô hình và trực giác; MT2. Đầu vào: quyền tạo/sửa cạnh. Sản phẩm: đọc đúng ba vùng và các giả thiết của Hình 5.16.

**Luận điểm trung tâm:** Ba vùng quyền tác động và cạnh nội bộ xác định mô hình phân tích cụm thao túng.

**Nội dung hiển thị dự kiến:**

<!-- public-slide:start -->
Đích trỏ tới $m$ trang hỗ trợ; mỗi hỗ trợ chỉ trỏ lại đích.

Liên kết từ ngoài cụm chỉ vào đích.

Giả thiết: đồ thị không có nút cụt; $m\ge1$, $n\ge m+1$.
<!-- public-slide:end -->

**Bố cục đã chọn:** Sơ đồ ba vùng chiếm trái65%; giả thiết thành ba dòng ngắn phải35%. Đích đặt giữa vùng sở hữu, m hỗ trợ thành cột; dấu chấm lửng có nhãn m trang.

**Trọng tâm và thứ tự đọc:** Đọc ba vùng từ trái sang phải → cạnh ngoài vào đích → cặp chiều đích–hỗ trợ.

**Lý do phù hợp sinh viên năm 2:** Ranh giới vùng tách quyền đặt cạnh với quyền sở hữu trang, cần trước khi gộp mọi đóng góp ngoài vào x.

**Giới hạn bố cục và phân chia nội dung:** Giữ nhãn m thay số trang tự đặt. Giả thiết không nút cụt phải hiện trên mặt slide. Hình chỉ ghi “Đóng góp từ ngoài”; ký hiệu $x$ và cách gộp hệ số được định nghĩa tại S03-04.

**Ví dụ, phiếu số và hình thức hóa:** VD2/Hình 5.16; miền n,m. Các cạnh ngoài vào hỗ trợ bị loại theo mô hình đã chọn.

**Kết nối vào–ra:** Mục tiêu tăng điểm → cấu trúc vòng quay điểm → điểm của một trang hỗ trợ.

**Quyết định 01/10/2026:** sửa — tiêu đề ngắn “Cụm thao túng liên kết”; bỏ cụm “nhóm sở hữu” chưa định nghĩa; ba vùng do hình thể hiện, ghi chú giải thích theo MMDS §5.4.1; tách mô tả cạnh thành hai dòng ngắn, bỏ ý lặp “hỗ trợ chỉ nhận cạnh từ đích”; sửa SVG để nhãn “đóng góp từ ngoài vào đích” không đè tiêu đề vùng giữa (SVG dùng chung với ghi chú tự học).

**Nguồn và vị trí:** NG1 §5.4.1/Hình 5.16, tr.199–200/PDF25–26; giả thiết không nút cụt làm rõ phạm vi phép tính nguồn.

**Thời lượng:** 2 phút.

**Ghi chú học thuật dự kiến:**

<!-- public-notes:start -->
Hình chia web thành ba vùng theo MMDS §5.4.1: phần lớn web không thể tác động; vùng có thể tác động gồm các trang cho phép người khác đăng nội dung, như bình luận; vùng sở hữu do người tạo cụm điều khiển. Trang tác động được không đồng nghĩa trang sở hữu: một người có thể đặt liên kết ở vị trí được phép mà không điều khiển toàn bộ trang. Mô hình dùng PageRank toàn cục với dịch chuyển đều. Các liên kết ngoài đưa điểm tới đích; đích chia điểm cho mọi hỗ trợ, và các hỗ trợ trả điểm về đích. Điều kiện toàn đồ thị không có nút cụt giữ phần dịch chuyển đều bằng $b=(1-\beta)/n$, không phát sinh số hạng bù nút cụt bổ sung.
<!-- public-notes:end -->

### lec04-s03-03 — Điểm của một trang hỗ trợ

**Vai trò, mục tiêu, đầu vào và sản phẩm:** Ví dụ ký hiệu và tính đóng góp; MT2. Đầu vào: Hình 5.16. Sản phẩm: suy ra p từ hai nguồn điểm.

**Luận điểm trung tâm:** Một hỗ trợ nhận phần điểm chia từ đích và phần dịch chuyển đều.

**Nội dung hiển thị dự kiến:**

<!-- public-slide:start -->
Ký hiệu: $y$, $p$ là điểm cố định của đích và của mỗi trang hỗ trợ; $b=(1-\beta)/n$.

Đích có đúng $m$ liên kết ra; mỗi hỗ trợ chỉ nhận cạnh từ đích.

| Nguồn điểm tại một hỗ trợ | Đóng góp |
|---|---:|
| Điểm theo cạnh từ đích | $\beta y/m$ |
| Dịch chuyển đều | $b$ |

$$p=\frac{\beta y}{m}+b.$$
<!-- public-slide:end -->

**Bố cục đã chọn:** Một cặp đích–hỗ trợ lớn trái40%, bảng hai nguồn điểm và công thức phải60%. Trên cạnh ghi beta y/m; nguồn dịch chuyển dùng mũi tên nét đứt b.

**Trọng tâm và thứ tự đọc:** Theo điểm y rời đích → chia m → cộng b → gọi tổng p.

**Lý do phù hợp sinh viên năm 2:** Một hỗ trợ đại diện làm rõ mẫu số m và giữ quan hệ với phân phối đều; bảng phân biệt n tổng web với m trang hỗ trợ.

**Giới hạn bố cục và phân chia nội dung:** Không đưa phương trình y ở cùng trang. Giả thiết đồ thị không nút cụt và cạnh như S03-02 được nhắc trong ghi chú.

**Ví dụ, phiếu số và hình thức hóa:** VD2; HT4 điểm hỗ trợ. p,y là điểm; n,m là số trang; beta xác suất.

**Kết nối vào–ra:** Kiến trúc cụm → điểm một hỗ trợ → tổng điểm quay về từ m hỗ trợ.

**Quyết định 01/10/2026:** sửa — giữ tiêu đề; dòng ký hiệu nêu $y$, $p$ là điểm cố định (phương trình cân bằng, không phải một vòng lặp); bỏ câu thừa “Mọi trang hỗ trợ có cùng phương trình”, ý này đã có trong ghi chú.

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
<!-- public-slide:end -->

**Bố cục đã chọn:** Ba mũi tên có nhãn vào đích chiếm trái45%; bảng và phương trình phải55%. Vị trí đích/hỗ trợ khớp S03-02.

**Trọng tâm và thứ tự đọc:** Đọc định nghĩa x → cộng cùng một loại đóng góp beta p qua m hỗ trợ → cộng b tại đích.

**Lý do phù hợp sinh viên năm 2:** Ba nhánh làm rõ nơi phát sinh từng số hạng; số m xuất hiện do cộng các trang, beta xuất hiện do nhánh đi theo cạnh.

**Giới hạn bố cục và phân chia nội dung:** Mặt slide không thế p; việc thế và giải để trang sau. Chú thích x đã tính beta phải nằm cạnh nhánh ngoài.

**Ví dụ, phiếu số và hình thức hóa:** VD2; HT4 phương trình điểm đích; không có dữ kiện số mới.

**Kết nối vào–ra:** Điểm từng hỗ trợ → dòng quay lại đích → phương trình tự phụ thuộc y.

**Quyết định 01/10/2026:** sửa nhẹ — giữ tiêu đề và bảng; bỏ câu cuối lặp định nghĩa $x$ ở dòng mở đầu.

**Nguồn và vị trí:** NG1 §5.4.2, tr.201/PDF27.

**Thời lượng:** 3 phút.

**Ghi chú học thuật dự kiến:**

<!-- public-notes:start -->
Đối với một trang ngoài $j$ trỏ tới đích, đóng góp là $\beta r_j/d_j$. Đại lượng $x$ là tổng các đóng góp này, nên không nhân thêm $\beta$. Mỗi hỗ trợ chỉ có một cạnh ra, trả $\beta p$; $m$ hỗ trợ trả $\beta mp$. Phương trình dùng điểm cố định của hệ; ba số hạng không phải ba trạng thái thời gian khác nhau.
<!-- public-notes:end -->

### lec04-s03-05 — Điểm cố định của trang đích

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

**Quyết định 01/10/2026:** sửa tiêu đề — trang dùng vòng truyền $\beta^2$ làm trực giác để giải ra $y$; tiêu đề gọi kết quả (điểm cố định của đích, cùng thuật ngữ với s03-03) thay vì chỉ cơ chế. Nội dung giữ nguyên.

**Nguồn và vị trí:** NG1 §5.4.2, tr.201; phần giữ b tại đích là diễn giải đầy đủ trước phép lược trong sách.

**Thời lượng:** 3 phút.

**Ghi chú học thuật dự kiến:**

<!-- public-notes:start -->
Trang đích chia phần theo liên kết $\beta y$ đều cho $m$ hỗ trợ, nên mỗi hỗ trợ nhận $\beta y/m$. Mỗi hỗ trợ chỉ có một cạnh quay lại đích; phần điểm này qua bước theo liên kết thứ hai được nhân thêm $\beta$. Tổng trên $m$ hỗ trợ là $m\beta(\beta y/m)=\beta^2y$. Đây là thành phần bắt nguồn từ đích, tách khỏi phần $b$ mà mỗi hỗ trợ nhận trực tiếp từ dịch chuyển.

Thay $p=\beta y/m+b$ vào phương trình của đích cho $y=x+\beta^2y+\beta mb+b$. Chuyển $\beta^2y$ sang trái rồi chia cho $1-\beta^2>0$ thu được nghiệm. Hạng $\beta mb$ là phần dịch chuyển nhận tại các hỗ trợ rồi truyền về đích; hạng $b$ là dịch chuyển trực tiếp tới đích. Mô hình giả định toàn đồ thị không có nút cụt và giữ đúng kiến trúc đã nêu. Đại lượng $x$ là đóng góp ngoài ở trạng thái cân bằng, chịu ràng buộc tổng điểm toàn đồ thị.
<!-- public-notes:end -->

### lec04-s03-06 — Hệ số khuếch đại của cụm

**Vai trò, mục tiêu, đầu vào và sản phẩm:** Xấp xỉ và diễn giải số; MT2. Đầu vào: công thức đầy đủ. Sản phẩm: phân biệt giá trị sau nhân với phần trăm tăng.

**Luận điểm trung tâm:** Hệ số khuếch đại và mức tăng phần trăm là hai đại lượng khác nhau.

**Nội dung hiển thị dự kiến:**

<!-- public-slide:start -->
Bỏ hạng nhỏ do dịch chuyển trực tiếp $b$ tới đích (MMDS §5.4.2):

$$y\approx\frac{x}{1-\beta^2}+\frac{\beta}{1+\beta}\frac mn.$$

Với $\beta=0{,}85=17/20$:

| Thành phần | Hệ số |
| --- | --- |
| Đóng góp từ ngoài $x$ | $400/111\approx3{,}6036$ |
| Tỷ lệ trang hỗ trợ $m/n$ | $17/37\approx0{,}45946$ |

Cụm nhân đóng góp từ ngoài khoảng $3{,}6$ lần và nhận thêm khoảng $0{,}46\,m/n$, với $m/n$ là tỷ lệ trang web thuộc cụm.
<!-- public-slide:end -->

**Bố cục đã chọn:** Phép xấp xỉ ở trên40%; bảng hai hệ số giữa40%; câu giải nghĩa dưới20%. Nhãn “bỏ riêng b tới đích” đặt trước công thức.

**Trọng tâm và thứ tự đọc:** Xác định hạng bị bỏ → đọc hai hệ số → diễn giải “lần” và “phần tăng”.

**Lý do phù hợp sinh viên năm 2:** Giữ số nguồn và phân số chính xác giúp kiểm phép tính; tách tỷ lệ m/n khỏi điểm x tránh cộng hai đại lượng khác nghĩa không có nhãn.

**Giới hạn bố cục và phân chia nội dung:** Mặt trang phân biệt hệ số của x với hạng theo m/n và hạng bị bỏ. Phần tăng260,36% chỉ thuộc ghi chú, không diễn giải là tăng toàn bộ y.

**Ví dụ, phiếu số và hình thức hóa:** VD2; HT4 xấp xỉ. Bảng số giữ beta 17/20 theo VD5.11, khác beta 4/5 của G4 và có nhãn rõ.

**Kết nối vào–ra:** Phương trình đầy đủ → ý nghĩa khuếch đại → giới hạn suy luận và chi phí cấu trúc.

**Quyết định 01/10/2026:** sửa — tiêu đề ngắn “Hệ số khuếch đại của cụm”; dẫn nguồn cụ thể thay cho “như phép phân tích của sách”; dùng dấu phẩy thập phân (G11); thay dòng cuối dồn hai ý bằng khối kết luận diễn giải hai hệ số theo Ví dụ 5.11; chi tiết hạng bị bỏ và cách đọc “360%” chuyển vào ghi chú.

**Nguồn và vị trí:** NG1 VD5.11, tr.201/PDF27; sửa diễn đạt phần trăm để phân biệt hệ số với mức tăng.

**Thời lượng:** 3 phút.

**Ghi chú học thuật dự kiến:**

<!-- public-notes:start -->
Hạng chính xác bị bỏ trong biểu thức $y$ là $b/(1-\beta^2)=1/[n(1+\beta)]$. Phần dịch chuyển vào $m$ hỗ trợ vẫn được giữ vì tổng của chúng tạo hạng $m/n$. Với $\beta=17/20$, hệ số của $x$ là $400/111$; trừ $1$ rồi nhân $100$ cho phần tăng khoảng $260{,}36\%$; MMDS diễn đạt cùng hệ số này là khuếch đại đóng góp ngoài “360%”. Hệ số $400/111$ chỉ nhân với $x$; hạng từ hỗ trợ là $(17/37)(m/n)$. Đây là hệ số của một mô hình đại số, không phải số đo hiệu quả trên hệ tìm kiếm hiện hành.
<!-- public-notes:end -->

### lec04-s03-07 — Hai hướng chống liên kết rác

**Vai trò, mục tiêu, đầu vào và sản phẩm:** Giới hạn và cầu nối; MT2, MT3. Đầu vào: mô hình cụm và hệ số khuếch đại. Sản phẩm: phân biệt hai hướng chống liên kết rác và nêu nhu cầu dùng tập trang tin cậy.

**Luận điểm trung tâm:** Phát hiện cấu trúc bị né bằng biến thể; đổi cách tính điểm dựa trên tập trang tin cậy không cần định vị cụm.

**Nội dung hiển thị dự kiến:**

<!-- public-slide:start -->
**Phát hiện cấu trúc.** Tìm các cấu trúc như cụm vừa phân tích và loại các trang khỏi chỉ mục. Giới hạn: người tạo rác chuyển sang biến thể khác có cùng tác dụng; số biến thể gần như không giới hạn.

**Đổi cách tính điểm.** Sửa định nghĩa PageRank để tự hạ điểm trang rác, không cần định vị cụm. Dùng thêm tập trang đã được đánh giá đáng tin.

Hướng thứ hai dẫn tới hai công thức: TrustRank và Spam Mass.
<!-- public-slide:end -->

**Bố cục đã chọn:** Hai thẻ ngang nhau “Phát hiện cấu trúc” và “Đổi cách tính điểm”; khối kết luận nối sang TrustRank, Spam Mass. Bỏ hình $2m$ cạnh nội bộ.

**Trọng tâm và thứ tự đọc:** Đọc hướng phát hiện cấu trúc và giới hạn của nó → hướng đổi cách tính điểm → nhu cầu thông tin bên ngoài đồ thị.

**Lý do phù hợp sinh viên năm 2:** Hai hướng đặt cạnh nhau cho thấy vì sao cần một công thức mới thay cho việc tìm mẫu đồ thị; không đòi kiến thức hệ thống tìm kiếm.

**Giới hạn bố cục và phân chia nội dung:** Không xây thuật toán phát hiện cụm ngoài nguồn; không thêm nhận định ngoài MMDS §5.4.3.

**Ví dụ, phiếu số và hình thức hóa:** Dùng lại cụm Hình 5.16 làm ví dụ của hướng thứ nhất; không có phép tính mới.

**Kết nối vào–ra:** Mức khuếch đại của cụm → hai hướng chống liên kết rác → hướng đổi cách tính điểm mở S04 (TrustRank, Spam Mass).

**Quyết định 01/10/2026:** viết lại — theo MMDS §5.4.3, trang trình bày hai hướng chống liên kết rác; hướng thứ hai tạo nhu cầu cho TrustRank và Spam Mass (cầu nối S03→S04, G8). Bỏ hình và câu “$2m$ cạnh nội bộ” vì không phục vụ luận điểm; câu “công thức áp dụng khi giữ đúng kiến trúc” đã nằm ở s03-03. SVG `hai-nhom-canh-noi-bo.svg` không còn được deck dùng.

**Nguồn và vị trí:** NG1 Hình 5.16, tr.200; §5.4.3, tr.202.

**Thời lượng:** 1 phút.

**Ghi chú học thuật dự kiến:**

<!-- public-notes:start -->
MMDS §5.4.3 nêu hai hướng. Hướng thứ nhất tìm các cấu trúc trong đó một trang trỏ tới rất nhiều trang và các trang này trỏ ngược lại, rồi loại chúng khỏi chỉ mục. Người tạo rác khi đó chuyển sang cấu trúc khác có cùng tác dụng thu điểm cho trang đích; số biến thể của Hình 5.16 gần như không giới hạn.

Hướng thứ hai thay định nghĩa điểm để trang rác tự bị hạ điểm. Công thức phải dùng thông tin không do người tạo rác kiểm soát: một tập trang đã được đánh giá đáng tin. Kết quả của phân tích cụm vẫn được dùng: nó cho thấy vì sao không thể chỉ dựa vào điểm PageRank toàn cục.
<!-- public-notes:end -->

### lec04-s03-08 — Kiểm tra cụm thao túng liên kết

**Vai trò, mục tiêu, đầu vào và sản phẩm:** Kiểm tra riêng S03; MT2. Đầu vào: HT4. Sản phẩm: vận dụng công thức khuếch đại với tham số mới và sửa mô hình khi cấu trúc cụm thay đổi.

**Luận điểm trung tâm:** Hệ số khuếch đại phụ thuộc $\beta$; phương trình điểm phụ thuộc đúng cấu trúc cạnh của cụm.

**Nội dung hiển thị dự kiến:**

<!-- public-slide:start -->
Mô hình cụm Hình 5.16, đồ thị không có nút cụt.

**Câu hỏi:**
1. Với $\beta=0{,}9$, tính hệ số của $x$ và hệ số của $m/n$ trong công thức xấp xỉ của $y$; so với $\beta=0{,}85$.
2. Mỗi trang hỗ trợ nhận thêm cạnh từ ngoài cụm. Xác định phương trình nào trong hai phương trình của $p$, $y$ phải đổi và số hạng được thêm.
<!-- public-slide:end -->

**Bố cục đã chọn:** Giả thiết ngắn và hai công thức đã biết ở trên45%; hai yêu cầu ở khung kiểm tra dưới55%. Không cho sẵn phương trình sửa.

**Trọng tâm và thứ tự đọc:** Kiểm ý nghĩa x → tìm điểm thiếu → giải tác động của hạng bị lược lên y.

**Lý do phù hợp sinh viên năm 2:** Một lỗi nhân thừa và một hạng thiếu buộc sinh viên truy nguồn thay vì chỉ nhớ công thức cuối.

**Giới hạn bố cục và phân chia nội dung:** Chỉ hai yêu cầu trên mô hình đã học; bài đổi liên kết được dành cho recitation.

**Ví dụ, phiếu số và hình thức hóa:** VD2/HT4; câu hỏi dùng phương trình nguồn và một phép sai để kiểm cơ chế.

**Kết nối vào–ra:** Kiểm dòng điểm trong mô hình thao túng → lựa chọn tập trang đáng tin ở S04.

**Quyết định 01/10/2026:** sửa — tiêu đề gọi đúng đối tượng kiểm tra của phần; rút dòng dữ kiện lặp toàn bộ giả thiết s03-02…s03-04 thành dẫn chiếu Hình 5.16 và các ký hiệu cần dùng. Sau rà lại: hai câu cũ có đáp án hiển thị ở s03-04, s03-06; thay bằng câu vận dụng công thức với $\beta=0{,}9$ và câu sửa mô hình khi hỗ trợ nhận cạnh ngoài.

**Nguồn và vị trí:** NG1 §5.4.2, tr.201; kiểm tra áp dụng trên cùng ký hiệu và giả thiết.

**Thời lượng:** 3 phút.

**Nhiệm vụ và tiêu chí nội bộ:** Slide kiểm tra riêng của phần.

- Câu hỏi/đề: Hai yêu cầu như nội dung hiển thị.
- Đáp án/gợi ý: $100/19\approx5{,}26$ và $9/19\approx0{,}47$ (so với $3{,}60$ và $0{,}46$); phương trình của $p$ thêm $x'$, phương trình của $y$ giữ dạng.
- Tiêu chí đánh giá: Thay đúng $\beta$ vào hai hệ số; giải thích chiều thay đổi theo $\beta$; đặt $x'$ vào phương trình hỗ trợ, không nhân $\beta$ lần nữa.
- Phân bổ hoạt động: Suy nghĩ1,5 phút, trả lời0,5 phút, đối chiếu1 phút; tổng3 phút.

**Ghi chú học thuật dự kiến:**

<!-- public-notes:start -->
Câu 1: hệ số của $x$ là $1/(1-\beta^2)=100/19\approx5{,}26$; hệ số của $m/n$ là $\beta/(1+\beta)=9/19\approx0{,}47$. Với $\beta=0{,}85$ hai hệ số là $3{,}60$ và $0{,}46$. Khi $\beta$ tăng, phần điểm mất ở mỗi bước theo liên kết giảm, nên vòng đích → hỗ trợ → đích giữ lại nhiều điểm hơn và đóng góp từ ngoài được nhân mạnh hơn.

Câu 2: phương trình của mỗi hỗ trợ có thêm số hạng $x'$ là đóng góp từ ngoài vào hỗ trợ đó, đã nhân $\beta$ và chia bậc ra tại nguồn: $p=\beta y/m+x'+b$. Phương trình $y=x+\beta mp+b$ giữ dạng, nhưng $p$ lớn hơn nên $y$ tăng qua số hạng $\beta mp$. Lỗi thường gặp là nhân $\beta$ thêm một lần vào $x'$ hoặc quên rằng phần thêm tại hỗ trợ cũng quay về đích.
<!-- public-notes:end -->

## S04. TrustRank và Spam Mass

Thuật toán và diễn giải. Tập tin cậy → tái dùng HT1 → cùng G4/VD1 → đối chiếu r/rho cùng beta → chỉ số tương đối → chi phí và giới hạn → kiểm tra. Giả mã, bảo toàn và hội tụ kế thừa S02, không lặp lại toàn bộ. Đầu ra gồm chỉ số có dấu và giới hạn suy luận; HITS tiếp tục bằng một nhu cầu điểm khác.

Phân bổ: 7 slide, 18 phút (từ 01/10/2026, s04-02 gộp vào s04-02a).

### lec04-s04-01 — TrustRank

**Vai trò, mục tiêu, đầu vào và sản phẩm:** Vấn đề và trực giác; MT3. Đầu vào: giới hạn phát hiện cấu trúc và PageRank theo chủ đề. Sản phẩm: xác định thông tin ngoài đồ thị cần cho TrustRank.

**Luận điểm trung tâm:** TrustRank cần tập tin cậy từ đánh giá bên ngoài và giả định về hướng liên kết.

**Nội dung hiển thị dự kiến:**

<!-- public-slide:start -->
[Hình: Tập T có viền đôi được đánh giá bên ngoài; cạnh thật đi từ T tới các trang khác.]

TrustRank: PageRank theo chủ đề, tập dịch chuyển $T$ là các trang tin cậy (tập hạt giống, seed set).

Cơ sở: trang rác dễ đặt liên kết tới trang tin cậy, nhưng trang tin cậy hiếm khi trỏ tới trang rác.

Chọn $T$ ngoài thuật toán: người xem xét các trang PageRank cao, hoặc lấy miền có kiểm soát (.edu, .gov).
<!-- public-slide:end -->

**Bố cục đã chọn:** Một nhóm T có viền đôi và các cạnh ra tới phần còn lại chiếm trái55%; giả định và giới hạn phải45%. Nhãn “đánh giá bên ngoài” gắn với T.

**Trọng tâm và thứ tự đọc:** Xác định nguồn thông tin chọn T → theo chiều liên kết → đọc giới hạn của điểm thấp.

**Lý do phù hợp sinh viên năm 2:** Dùng lại trực giác tập dịch chuyển thay vì giới thiệu phép lặp mới; tách tin cậy được kiểm ngoài mô hình với điểm lan truyền.

**Giới hạn bố cục và phân chia nội dung:** Mặt trang có nguồn đánh giá T, khác biệt ý nghĩa với tập chủ đề, giả định ít trỏ rác và độ phủ; ghi chú nêu tính không tuyệt đối.

**Ví dụ, phiếu số và hình thức hóa:** HT5; tập T không rỗng. Không có số mới, sơ đồ chỉ khái niệm.

**Kết nối vào–ra:** Liên kết có thể bị thao túng → chọn nơi đưa điểm mới → đặc tả TrustRank.

**Quyết định 01/10/2026:** sửa — tiêu đề “TrustRank”; câu chính đặt đầu: TrustRank là PageRank theo chủ đề với tập dịch chuyển tin cậy (MMDS §5.4.4); nêu đủ lý do về hướng liên kết; thêm hai cách chọn $T$ của nguồn (trang PageRank cao; miền có kiểm soát) để “thông tin ngoài phép lặp” có nội dung cụ thể; đặt tên “tập hạt giống (seed set)” lần đầu; đổi tỷ lệ cột thành hình 45%, chữ 55% để mỗi dòng không quá hai dòng.

**Nguồn và vị trí:** NG1 §5.4.3–5.4.4, tr.202–203/PDF28–29.

**Thời lượng:** 2 phút.

**Ghi chú học thuật dự kiến:**

<!-- public-notes:start -->
TrustRank hiện thực hướng thứ hai chống liên kết rác: đổi cách tính điểm bằng thông tin mà người tạo rác không kiểm soát, thay vì tìm từng cụm. Các hạt giống được đánh giá từ bên ngoài trước khi chạy thuật toán; TrustRank không tự chọn hay chứng nhận chúng từ điểm đầu ra. Cách chọn theo các trang PageRank cao dựa trên nhận định của MMDS: liên kết rác có thể đưa một trang từ cuối lên giữa bảng xếp hạng nhưng gần như không đưa được lên đầu. Cách chọn theo miền dựa trên việc người tạo rác khó đưa trang vào các miền có kiểm soát; độ phủ cần được bảo đảm, vì chỉ chọn .edu thì $T$ gần như chỉ gồm trang của Mỹ và phải thêm các miền tương tự của nước khác. Các trang ngoài $T$ vẫn có thể nhận điểm qua liên kết. TrustRank giữ cơ chế PageRank theo chủ đề, nhưng ý nghĩa tập dịch chuyển là tin cậy thay cho lĩnh vực nội dung. Giả định về hướng liên kết không có tính tuyệt đối: trang cho phép người khác đăng liên kết, như trang báo có mục bình luận, không được coi là tin cậy dù nội dung chính đáng tin. Chất lượng và phạm vi bao phủ của $T$ ảnh hưởng cách diễn giải điểm; vector kết quả không chứng nhận nội dung của từng trang.
<!-- public-notes:end -->

### lec04-s04-02a — Phép lặp TrustRank

**Vai trò, mục tiêu, đầu vào và sản phẩm:** Hình thức hóa và tái dùng thuật toán; MT3. Đầu vào: bảng ký hiệu S04-02. Sản phẩm: phân biệt ba số hạng và điều kiện dừng.

**Luận điểm trung tâm:** Theo liên kết, bù nút cụt và dịch chuyển tới T có ba vai trò riêng trong phép cập nhật.

**Nội dung hiển thị dự kiến:**

<!-- public-slide:start -->
Dùng lại thuật toán PageRank theo chủ đề với $r\mapsto\rho$, $v\mapsto v_T$; các thành phần khác giữ nguyên.

$T\ne\varnothing$; $(v_T)_i=1/|T|$ nếu $i\in T$, bằng $0$ ngoài $T$; khởi tạo $\rho^0=v_T$.

$\rho_i^t$: điểm TrustRank của trang $i$ ở vòng $t$; $\delta_\rho^t=\sum_{j:d_j=0}\rho_j^t$; $u$ đều trên $n$ trang.

$$\rho^{t+1}=\underbrace{\beta M_0\rho^t}_{\text{theo liên kết}}+\underbrace{\beta\delta_\rho^t u}_{\text{bù nút cụt}}+\underbrace{(1-\beta)v_T}_{\text{dịch chuyển}}.$$
<!-- public-slide:end -->

**Bố cục đã chọn:** Phân phối vT và khởi tạo ở trên; công thức có ba nhãn ở giữa; bảng ba hàng xác định nơi nhận điểm ở dưới.

**Trọng tâm và thứ tự đọc:** Khởi tạo → từng số hạng theo trái–phải → nơi nhận điểm → thuật toán kế thừa.

**Lý do phù hợp sinh viên năm 2:** Nhãn dưới số hạng nối ký hiệu ở trang trước với thao tác; bảng làm rõ bù đều toàn đồ thị khác dịch chuyển vào T.

**Giới hạn bố cục và phân chia nội dung:** Không chép lại giả mã; bảo toàn, co và trạng thái dừng được giải thích trong ghi chú.

**Ví dụ, phiếu số và hình thức hóa:** HT5 dùng HT1–HT2; bù nút cụt vẫn là u, không đổi sang vT.

**Kết nối vào–ra:** Các đối tượng → cập nhật rho → nghiệm cụ thể trên G4.

**Quyết định 01/10/2026:** gộp — s04-02 (bảng năm ký hiệu, bốn ký hiệu đã có ở S02) được gộp vào trang này. Luận điểm “TrustRank dùng lại thuật toán PageRank theo chủ đề với $v\mapsto v_T$” đặt lên đầu; bỏ bảng “nơi nhận điểm” lặp S02; định nghĩa $\rho$, $\delta_\rho$, $v_T$ giữ trên mặt trang, còn vai trò từng thành phần và lập luận hội tụ nằm trong ghi chú.

**Nguồn và vị trí:** NG1 §5.4.4 tr.202–203; quy tắc bù và dừng thống nhất với HT1.

**Thời lượng:** 4 phút (gộp thời lượng của s04-02).

**Ghi chú học thuật dự kiến:**

<!-- public-notes:start -->
Thành phần $\beta M_0\rho^t$ truyền điểm từ các trang không cụt theo cạnh thật; $\beta\delta_\rho^t u$ bù phần điểm ở các nút cụt lên toàn bộ $n$ trang; $(1-\beta)v_T$ đưa điểm dịch chuyển vào các hạt giống. Hai phân phối $u$ và $v_T$ đều có tổng bằng $1$ nhưng có vai trò khác nhau. Tổng ba thành phần bằng $\beta(1-\delta_\rho^t)+\beta\delta_\rho^t+(1-\beta)=1$.

Vì $v_T\ge0$ và có tổng bằng $1$, bất biến tổng điểm và lập luận co của PageRank theo chủ đề áp dụng nguyên vẹn: với $0<\beta<1$, phép lặp có điểm cố định duy nhất $\rho$, và thuật toán trả vector xấp xỉ cùng trạng thái đạt ngưỡng hoặc hết $K$ vòng. Tham số $\beta$ được giữ như trong phép tính PageRank nền để hai vector so sánh được.
<!-- public-notes:end -->


### lec04-s04-03 — TrustRank trên G4

**Vai trò, mục tiêu, đầu vào và sản phẩm:** Ví dụ tái sử dụng; MT3. Đầu vào: VD1 và T={B,D}. Sản phẩm: liên hệ cùng phép tính với ý nghĩa tin cậy.

**Luận điểm trung tâm:** B,D là hạt giống giả thiết đầu vào; cùng phân phối dịch chuyển cho cùng nghiệm số với ví dụ chủ đề.

**Nội dung hiển thị dự kiến:**

<!-- public-slide:start -->
[Hình: Đồ thị G4: A tới B, C, D; B tới A, D; C tới A; D tới B, C. B và D có viền đôi và nhãn tập tin cậy T.]

$\beta=4/5$. Giả sử B, D đã được đánh giá đáng tin: $T=\{B,D\}$, $v_T=(0,1/2,0,1/2)^\mathsf T$.

| Trang | TrustRank $\rho_i$ |
| --- | --- |
| A | $9/35$ |
| B | $59/210$ |
| C | $19/105$ |
| D | $59/210$ |

Cùng $v$ nên cùng nghiệm với ví dụ theo chủ đề; chỉ ý nghĩa của tập đổi sang độ tin cậy.
<!-- public-slide:end -->

**Bố cục đã chọn:** G4 trái50%, bảng bốn hàng phải50%; B,D có nhãn T và viền đôi, vị trí đỉnh giữ theo VD1.

**Trọng tâm và thứ tự đọc:** Đọc T trên đồ thị → đối chiếu vT → nhận diện nghiệm đã có.

**Lý do phù hợp sinh viên năm 2:** Tái dùng dữ kiện tiết kiệm phép tính lặp nhưng vẫn giữ quan hệ giữa seed và vector; sinh viên thấy thuật toán không đổi.

**Giới hạn bố cục và phân chia nội dung:** Không lặp toàn bộ vết vòng 1/2; tham số và nghiệm phải có trên mặt slide để đọc độc lập.

**Ví dụ, phiếu số và hình thức hóa:** VD3 dùng nghiệm VD1; tổng rho=1. B,D hòa được giữ, không sửa số.

**Kết nối vào–ra:** TrustRank là phép lặp quen thuộc → cần so sánh với PageRank toàn cục cùng tham số.

**Quyết định 01/10/2026:** sửa — tiêu đề dùng tên đồ thị đã đặt (G4); khối kết luận bỏ vế lặp dòng dữ kiện và nêu điểm sư phạm: cùng phép tính, khác ý nghĩa của tập dịch chuyển.

**Nguồn và vị trí:** NG1 §5.4.4, tr.202–203; Ví dụ 5.10, tr.196–197, cung cấp G4 và tập dịch chuyển. Giữ đồ thị/tập của sách.

**Thời lượng:** 1 phút.

**Ghi chú học thuật dự kiến:**

<!-- public-notes:start -->
B, D đã được coi là tin cậy từ đầu, nên phép dịch chuyển ưu tiên chúng. A, C không thuộc tập hạt giống nhưng vẫn nhận điểm qua các liên kết thật. Để đánh giá phần thay đổi so với điểm toàn cục, cần tính một vector PageRank nền theo cùng $\beta$ và cùng chuẩn hóa.
<!-- public-notes:end -->

### lec04-s04-04 — Hiệu giữa PageRank và TrustRank

**Vai trò, mục tiêu, đầu vào và sản phẩm:** Chuẩn bị chỉ số; MT3. Đầu vào: rho. Sản phẩm: đối chiếu hai vector trên cùng mô hình.

**Luận điểm trung tâm:** Hiệu của hai vector cùng mô hình mô tả thay đổi điểm; dấu hiệu không xác định thay đổi thứ hạng hoặc nhãn rác.

**Nội dung hiển thị dự kiến:**

<!-- public-slide:start -->
Ý tưởng: đo phần PageRank của trang không đến từ tập tin cậy.

Cùng G4, $\beta=4/5$: $r$ dùng dịch chuyển đều $u$; $\rho$ dùng $v_T$.

| Trang | PageRank $r_i$ | TrustRank $\rho_i$ | Hiệu $r_i-\rho_i$ |
| --- | --- | --- | --- |
| A | $9/28$ | $9/35$ | $9/140$ |
| B | $19/84$ | $59/210$ | $-23/420$ |
| C | $19/84$ | $19/105$ | $19/420$ |
| D | $19/84$ | $59/210$ | $-23/420$ |

A, C giảm điểm khi chuyển sang TrustRank ($r_i-\rho_i>0$); B, D tăng điểm ($r_i-\rho_i<0$).
<!-- public-slide:end -->

**Bố cục đã chọn:** Bảng bốn trang giữ các giá trị chính xác; đoạn dưới diễn giải ba dấu theo chiều PageRank → TrustRank và giới hạn kết luận về thứ hạng, nhãn rác. Bỏ bảng dấu riêng để dành khoảng cho nguồn và chân trang, giữ thang chữ chung.

**Trọng tâm và thứ tự đọc:** So sánh cùng mô hình → đọc r và rho → hiệu → hướng giảm/tăng/không đổi.

**Lý do phù hợp sinh viên năm 2:** So sánh cùng beta loại nguyên nhân gây nhiễu; phân số giữ chính xác để chuẩn bị phép chia tương đối.

**Giới hạn bố cục và phân chia nội dung:** Mặt trang giữ diễn giải cả ba dấu và giới hạn kết luận; ghi chú giải thích tổng hiệu bằng 0 và khác biệt với bảng nguồn.

**Ví dụ, phiếu số và hình thức hóa:** VD3: bảng tính lại đồng nhất beta; đây không phải số chép từ Hình 5.17. Hiệu B,D âm hợp lệ.

**Kết nối vào–ra:** Hai vector cùng mô hình → hiệu điểm → chuẩn hóa hiệu theo r_i.

**Quyết định 01/10/2026:** sửa — tiêu đề gọi đúng đại lượng mới (hiệu); dòng mở nêu ý tưởng MMDS §5.4.5 (phần PageRank không đến từ tập tin cậy) để cột hiệu có nhu cầu; câu chốt đọc thẳng kết quả trên G4; câu “hiệu không xác định thứ hạng hoặc nhãn rác” chuyển vào ghi chú.

**Nguồn và vị trí:** NG1 §5.4.5/VD5.12, tr.203; bảng dẫn xuất trên G4 với beta 4/5, khác bảng nguyên nguồn.

**Thời lượng:** 3 phút.

**Ghi chú học thuật dự kiến:**

<!-- public-notes:start -->
PageRank đều thỏa $r=(4/5)M_0r+(1/5)u$ và có nghiệm $(9/28,19/84,19/84,19/84)^\mathsf T$. Vector $\rho$ đã được tính với tập tin cậy B, D. Hình 5.17 của sách dùng PageRank không dịch chuyển lấy từ Ví dụ 5.2, trong khi TrustRank dùng $\beta=4/5$; bảng này tính lại PageRank nền cùng $\beta=4/5$ để tách tác động của phân phối dịch chuyển. Tổng các hiệu bằng $0$ vì hai vector đều có tổng bằng $1$. Giá trị tuyệt đối của hiệu chưa xét quy mô điểm nền của từng trang.
<!-- public-notes:end -->

### lec04-s04-05 — Chỉ số Spam Mass

**Vai trò, mục tiêu, đầu vào và sản phẩm:** Hình thức hóa và chạy phép chia; MT3. Đầu vào: r,rho. Sản phẩm: tính chỉ số tương đối, giữ giá trị âm.

**Luận điểm trung tâm:** Spam Mass là mức giảm tương đối so với PageRank nền; A,C cùng giảm20% dù hiệu tuyệt đối khác nhau.

**Nội dung hiển thị dự kiến:**

<!-- public-slide:start -->
Với $r_i>0$, Spam Mass là tỷ lệ của $r_i$ không được tập tin cậy giải thích:
$$s_i=\frac{r_i-\rho_i}{r_i}=1-\frac{\rho_i}{r_i}.$$

| Trang | Phép tính | $s_i$ |
| --- | --- | --- |
| A | $(9/140)/(9/28)$ | $1/5$ |
| B | $(-23/420)/(19/84)$ | $-23/95$ |
| C | $(19/420)/(19/84)$ | $1/5$ |
| D | $(-23/420)/(19/84)$ | $-23/95$ |

$s_i<0$ khi $\rho_i>r_i$. Cách đọc (MMDS §5.4.5): âm hoặc dương nhỏ thì có lẽ không phải rác; gần $1$ thì có lẽ là rác.
<!-- public-slide:end -->

**Bố cục đã chọn:** Định nghĩa ở trên30%; bảng giữa55%; giới hạn dưới15%. Cột phép tính giữ tử và mẫu có ngoặc rõ.

**Trọng tâm và thứ tự đọc:** Đọc điều kiện r_i>0 → hiệu chia điểm nền → đối chiếu kết quả dương/âm.

**Lý do phù hợp sinh viên năm 2:** Bảng cùng hàng với trang trước giúp sinh viên thấy một hiệu tuyệt đối được chuyển thành thay đổi tương đối; giá trị âm không bị coi là lỗi tính.

**Giới hạn bố cục và phân chia nội dung:** Giữ bảng giá trị và diễn giải20%; không thêm ngưỡng phân loại hoặc xác suất rác.

**Ví dụ, phiếu số và hình thức hóa:** HT5/VD3. $s_i\le1$ vì rho_i không âm; không áp cận dưới0. Rho_i>r_i cho chỉ số âm.

**Kết nối vào–ra:** Hiệu hai vector → Spam Mass → giới hạn diễn giải và chi phí.

**Quyết định 01/10/2026:** sửa — tiêu đề “Chỉ số Spam Mass”; câu định nghĩa nêu ý tưởng trước công thức (G7); câu chốt đưa cách đọc của MMDS §5.4.5 lên mặt trang (âm hoặc nhỏ: có lẽ không rác; gần 1: có lẽ rác); “không phải xác suất” và đối chiếu với Ví dụ 5.12 chuyển vào ghi chú.

**Nguồn và vị trí:** NG1 §5.4.5, tr.203/PDF29; bảng số mới cùng beta theo VD3.

**Thời lượng:** 3 phút.

**Ghi chú học thuật dự kiến:**

<!-- public-notes:start -->
Tại A, $(9/140)/(9/28)=1/5$; tại C cũng có $s_C=1/5$. Cả hai có $\rho_i=(4/5)r_i$, tức giảm $20\%$ so với điểm nền riêng. Mức giảm tuyệt đối khác nhau: $9/140$ tại A và $19/420$ tại C. Tại B, $(-23/420)/(19/84)=-23/95$. Chỉ số âm có nghĩa TrustRank vượt PageRank nền ở trang đó; đó là quan hệ giữa hai phép xếp hạng, không phải xác suất âm. Giá trị gần $1$ tương ứng $\rho_i$ nhỏ so với $r_i$ và gợi ý cần rà soát dưới giả định của mô hình. Cùng một chỉ số dương không đủ chứng minh các trang A, C là rác; chỉ số cũng không phải xác suất trang rác. MMDS Ví dụ 5.12 tính với PageRank không dịch chuyển nên được $s_A\approx0{,}229$; ở đây PageRank nền dùng cùng $\beta=4/5$ nên $s_A=1/5$, kết luận định tính không đổi.
<!-- public-notes:end -->

### lec04-s04-06 — Chi phí tính Spam Mass

**Vai trò, mục tiêu, đầu vào và sản phẩm:** Giới hạn và chi phí; MT3, MT5. Đầu vào: HT5. Sản phẩm: phân biệt chi phí phép lặp với chọn hạt giống.

**Luận điểm trung tâm:** Chỉ số Spam Mass lớn được dùng để ưu tiên rà soát; chỉ số phụ thuộc tập hạt giống và không tự xác định nhãn rác.

**Nội dung hiển thị dự kiến:**

<!-- public-slide:start -->
| Bước | Phạm vi chi phí |
| --- | --- |
| PageRank và TrustRank | Hai phép lặp thưa; mỗi vòng $\Theta(n+\ell)$ |
| Tính Spam Mass | $\Theta(n)$ phép tính theo đỉnh |
| Đánh giá hạt giống | Công việc ngoài mô hình phép toán đồ thị |

Trang có $s_i$ gần $1$ được ưu tiên rà soát hoặc hạ điểm, không cần định vị cụm thao túng.
<!-- public-slide:end -->

**Bố cục đã chọn:** Một câu về hạt giống phía trên20%; bảng ba dòng giữa60%; câu giới hạn phía dưới20%.

**Trọng tâm và thứ tự đọc:** Đọc đánh đổi hạt giống → phân biệt ba công việc → giới hạn kết luận.

**Lý do phù hợp sinh viên năm 2:** Bảng không gộp đánh giá con người với phép toán máy; sinh viên so sánh đúng phạm vi chi phí thay vì suy nhanh hơn tuyệt đối.

**Giới hạn bố cục và phân chia nội dung:** Không đưa chi phí giờ công hoặc ngưỡng không có nguồn. Không tạo thuật toán chọn hạt giống mới.

**Ví dụ, phiếu số và hình thức hóa:** HT5; nếu hai phép lặp lần lượt K_r,K_rho vòng thì thời gian tính là Theta((K_r+K_rho)(n+ell)+n).

**Kết nối vào–ra:** Chỉ số đã có → nguồn sai lệch và tài nguyên → kiểm diễn giải.

**Quyết định 01/10/2026:** sửa — tiêu đề “Chi phí và độ phủ tập tin cậy”; dòng mở thay câu chung chung bằng ví dụ độ phủ của MMDS §5.4.4 (.edu chủ yếu là trang Mỹ); câu chốt nêu cách dùng chỉ số theo MMDS §5.4.5 (hạ điểm trang có $s_i$ gần 1 mà không cần định vị cụm), nối lại hướng thứ hai ở s03-07; bỏ câu lặp “phụ thuộc $T$, không tự xác định nhãn rác” và câu lặp trong ghi chú. Sau rà lại: tiêu đề đổi thành “Chi phí tính Spam Mass”, dòng độ phủ chuyển vào ghi chú s04-01 để trang giữ một luận điểm.

**Nguồn và vị trí:** NG1 §5.4.4–5, tr.202–203; phép đếm theo HT1. NG3 trang42 đối chiếu đánh đổi hạt giống.

**Thời lượng:** 2 phút.

**Ghi chú học thuật dự kiến:**

<!-- public-notes:start -->
Sau khi có $r$ và $\rho$, chỉ số $s_i$ đo phần điểm giảm tương đối khi chuyển sang ưu tiên hạt giống tin cậy. Đổi tập $T$ có thể đổi $\rho$ và thứ tự ưu tiên. Tập nhỏ giảm số trang phải đánh giá nhưng có thể bỏ sót các vùng nội dung. Hai phép lặp có thể cần số vòng khác nhau; chỉ bậc chi phí mỗi vòng giống nhau. Chi phí đánh giá hạt giống không được suy ra từ số cạnh hoặc số vòng.
<!-- public-notes:end -->

### lec04-s04-07 — Kiểm tra Spam Mass

**Vai trò, mục tiêu, đầu vào và sản phẩm:** Kiểm tra riêng S04; MT3. Đầu vào: VD3 và định nghĩa s. Sản phẩm: tính giá trị âm, giới hạn kết luận.

**Luận điểm trung tâm:** Dấu và độ lớn Spam Mass phải được đọc dưới giả định mô hình, không thành nhãn chắc chắn.

**Nội dung hiển thị dự kiến:**

<!-- public-slide:start -->
MMDS Ví dụ 5.12 trên G4: $r_C=2/9$ (PageRank của Ví dụ 5.2); TrustRank với $T=\{B,D\}$: $\rho_C=38/210$.

**Câu hỏi:**
1. Tính $s_C$ và chỉ ra đại lượng làm kết quả khác $s_C=1/5$ ở trang Chỉ số Spam Mass.
2. Từ $s_A=1/5$, xác định có thể kết luận chắc chắn A là trang rác không và nêu căn cứ.
<!-- public-slide:end -->

**Bố cục đã chọn:** Hai dòng dữ kiện ở trên30%; hai nhiệm vụ chiếm70% còn lại trong khung kiểm tra. Không kèm bảng đáp án trước đó.

**Trọng tâm và thứ tự đọc:** Đọc cặp r/rho của B → tính hiệu có dấu → áp giới hạn diễn giải cho A.

**Lý do phù hợp sinh viên năm 2:** Một tính toán và một nhận định kiểm cả cơ chế lẫn phạm vi suy luận, ngăn đồng nhất s với xác suất.

**Giới hạn bố cục và phân chia nội dung:** Không hỏi xác suất hoặc ngưỡng chưa được định nghĩa; đáp án trong ghi chú.

**Ví dụ, phiếu số và hình thức hóa:** VD3/HT5; giữ nguyên phân số đã kiểm.

**Kết nối vào–ra:** Điểm tin cậy và chỉ báo thao túng → mô hình hai vai trò cấu trúc HITS.

**Quyết định 01/10/2026:** sửa — tiêu đề “Kiểm tra Spam Mass”; câu 1 cũ có đáp án ($s_B=-23/95$) hiển thị ở s04-05, đổi sang tính $s_C$ từ dữ kiện MMDS Ví dụ 5.12 (đáp án $13/70$ đối chiếu được với Hình 5.17) và giải thích chênh lệch với $1/5$; câu 2 viết dạng yêu cầu.

**Nguồn và vị trí:** NG1 §5.4.5, tr.203; dữ kiện VD3 tính lại đồng nhất beta.

**Thời lượng:** 3 phút.

**Nhiệm vụ và tiêu chí nội bộ:** Slide kiểm tra riêng của phần.

- Câu hỏi/đề: Tính $s_C$ theo dữ kiện MMDS Ví dụ 5.12, chỉ ra đại lượng khác so với phép tính cùng $\beta$; đánh giá kết luận chắc chắn về A.
- Đáp án/gợi ý: $s_C=13/70\approx0{,}186$; khác vì PageRank nền khác (không dịch chuyển so với cùng $\beta=4/5$). $s_A=1/5$ gần 0 hơn 1: theo MMDS có lẽ không phải rác; không thể kết luận chắc chắn.
- Tiêu chí đánh giá: Tính đúng tỷ lệ; nêu đúng đại lượng khác nhau là vector PageRank nền; áp dụng cách đọc của MMDS và phân biệt chỉ số với xác suất.
- Phân bổ hoạt động: Tính1 phút, giải thích1 phút, đối chiếu1 phút; tổng3 phút.

**Ghi chú học thuật dự kiến:**

<!-- public-notes:start -->
$s_C=(2/9-38/210)/(2/9)=13/70\approx0{,}186$, khớp Hình 5.17 của MMDS. Kết quả khác $1/5$ vì PageRank nền khác: Ví dụ 5.2 của sách là PageRank không dịch chuyển, còn trang Chỉ số Spam Mass dùng PageRank nền cùng $\beta=4/5$. Spam Mass chỉ có nghĩa khi ghi rõ cách tính $r$ và $\rho$. Chỉ số $1/5$ tại A gần $0$ hơn $1$ nên theo cách đọc của MMDS, A có lẽ không phải rác. Dù giá trị lớn hay nhỏ, chỉ số chỉ mô tả chênh lệch tương đối giữa hai mô hình điểm, phụ thuộc $T$ và giả định liên kết; nó không chứng minh hay bác bỏ chắc chắn nhãn rác. HITS đánh giá một quan hệ cấu trúc khác: một trang cung cấp nội dung hay dẫn tới các trang cung cấp nội dung.
<!-- public-notes:end -->

## S05. HITS

Thuật toán và ví dụ. Danh sách/nội dung học phần → hai vai trò → G5/VD4 chạy hai vòng → L, phép chuẩn hóa → giả mã, quan hệ điểm ổn định → chi phí thưa → kiểm tra. Ví dụ có trước ma trận, nhưng mỗi phép cộng đã có quy tắc cạnh vào/ra. Đầu ra hai vector hỗ trợ lựa chọn phương pháp ở S06. Điều kiện phổ giải nghĩa trong ghi chú, không thành nhiệm vụ đánh giá mới.

Phân bổ: 11 slide, 30 phút.

### lec04-s05-01 — Trang trung tâm và trang uy tín

**Vai trò, mục tiêu, đầu vào và sản phẩm:** Tình huống sử dụng HITS; MT4. Đầu vào: đồ thị liên kết. Sản phẩm: phân biệt nội dung và đường dẫn tới nội dung.

**Luận điểm trung tâm:** Mỗi trang có hai điểm; danh mục minh họa trung tâm, trang nội dung minh họa uy tín theo liên kết.

**Nội dung hiển thị dự kiến:**

<!-- public-slide:start -->
PageRank và TrustRank gán mỗi trang một mức quan trọng. Ví dụ MMDS §5.5.1: trang danh sách học phần của một khoa có giá trị vì dẫn tới các trang học phần.

[Hình: Trang danh mục học phần giữ vai trò trung tâm và trỏ tới các trang học phần giữ vai trò uy tín.]
Thuật toán tìm kiếm theo chủ đề dựa trên siêu liên kết (HITS) gán mỗi trang hai điểm: trung tâm (hub) $h_i$ và uy tín (authority) $a_i$.

Trang uy tín cung cấp thông tin về một chủ đề; trang trung tâm chỉ ra nơi tìm thông tin đó.
<!-- public-slide:end -->

**Bố cục đã chọn:** Đầu vào đồ thị ở trên; sơ đồ trang danh mục trỏ tới các trang học phần ở giữa; phần dưới định nghĩa hai điểm $h_i,a_i$, gắn với hai vai trò và phân biệt uy tín HITS với độ tin cậy TrustRank. Không đưa ký hiệu tích ma trận vào trang mở phần.

**Trọng tâm và thứ tự đọc:** Nhận đồ thị đầu vào → đối chiếu trang danh mục với trang nội dung → nhận diện hai vai trò và hai điểm → phân biệt uy tín theo liên kết với độ tin cậy.

**Lý do phù hợp sinh viên năm 2:** Ví dụ học phần của sách gần với kinh nghiệm sinh viên, không đòi kiến thức hệ tìm kiếm; hai nhu cầu tạo lý do cho hai vector.

**Giới hạn bố cục và phân chia nội dung:** Mặt trang định nghĩa hai vai trò và khác biệt với TrustRank; chi phí đồ thị lớn chuyển sang ghi chú và S05-10.

**Ví dụ, phiếu số và hình thức hóa:** NG1 VD5.13, định tính; hai điểm $h_i,a_i$ được giới thiệu ngay trên trang này. Trang sau diễn giải quan hệ cập nhật giữa hai điểm trên G5.

**Kết nối vào–ra:** S04 phân biệt chỉ số tin cậy với vai trò cấu trúc → đầu vào đồ thị và nhu cầu hai vector HITS → chạy tay trên G5 trước khi xây phép lặp thưa; S05-10 thu hồi giới hạn tính toán.

**Quyết định 01/10/2026:** sửa — tiêu đề gọi hai vai trò thay cho cụm “mạng học phần”; câu mở nêu giới hạn tạo nhu cầu (PageRank, TrustRank cho một mức quan trọng) và nối từ S04 (G9); định nghĩa hai vai trò theo MMDS §5.5.1; câu “uy tín HITS khác độ tin cậy TrustRank” chuyển vào ghi chú và s06-01.

**Nguồn và vị trí:** NG1 §5.5–5.5.2, tr.204–208/PDF30–34; Ví dụ 5.13 tr.205; phạm vi đồ thị tr.204, phép nhân thưa tr.206 và tính lặp trên web lớn tr.208.

**Thời lượng:** 2 phút.

**Ghi chú học thuật dự kiến:**

<!-- public-notes:start -->
Đồ thị trang và liên kết được coi là đầu vào đã chọn; hai vai trò được đánh giá từ cấu trúc liên kết. Một mức quan trọng duy nhất không phân biệt được hai vai trò này: trang danh sách không thay thế nội dung một học phần, còn trang học phần không thay thế danh sách. Uy tín trong HITS không đồng nghĩa với điểm tin cậy của TrustRank; nó biểu diễn vai trò nhận liên kết từ các trang trung tâm có điểm cao. Trên đồ thị lớn, phép lặp tính hai vector cần khai thác các cạnh hiện có thay vì lưu ma trận đặc.
<!-- public-notes:end -->

### lec04-s05-02 — Định nghĩa tương hỗ của hai điểm

**Vai trò, mục tiêu, đầu vào và sản phẩm:** Trực giác và dữ kiện chạy tay; MT4. Đầu vào: hai vai trò. Sản phẩm: đọc quy tắc cộng theo hai chiều trên G5.

**Luận điểm trung tâm:** Trung tâm và uy tín hỗ trợ lẫn nhau; mỗi trang có cả hai điểm.

**Nội dung hiển thị dự kiến:**

<!-- public-slide:start -->
[Hình: Đồ thị G5: A tới B, C, D; B tới A, D; C tới E; D tới B, C; E không có cạnh ra.]
Đồ thị G5

Uy tín cộng trung tâm của các trang trỏ tới; trung tâm cộng uy tín của các trang được trỏ tới:

$$\tilde a_j=\sum_{i\to j}h_i,\qquad \tilde h_i=\sum_{i\to j}a_j.$$

Chỉ cộng thì giá trị thường tăng không giới hạn; sau mỗi bước chia cho thành phần lớn nhất.

E là nút cụt nhưng không cần dịch chuyển. Khởi tạo $h^0=(1,1,1,1,1)^\mathsf T$ theo thứ tự A,…,E.
<!-- public-slide:end -->

**Bố cục đã chọn:** G5 trái55%, hai quy tắc và khởi tạo phải45%. E đặt dưới C; cạnh C→E thay cạnh C→A của ví dụ G4 và có nhãn rõ.

**Trọng tâm và thứ tự đọc:** Đọc đồ thị mới → theo các cạnh vào khi tính a → theo cạnh ra khi tính h.

**Lý do phù hợp sinh viên năm 2:** Nêu đầy đủ cạnh mới ngăn dùng nhầm ma trận G4; hai điểm được gắn cùng mỗi trang, tránh hiểu hub/authority là hai nhóm rời nhau.

**Giới hạn bố cục và phân chia nội dung:** Không chia bậc ra và không thêm bước nhảy. Hai phép cộng được chạy trước khi viết dạng ma trận.

**Ví dụ, phiếu số và hình thức hóa:** VD4/HT6 trực giác; n5,ell8; h0 không phải phân phối xác suất.

**Kết nối vào–ra:** Vai trò danh mục/nội dung → quan hệ hai điểm → phép cộng uy tín từ h ở vòng đầu.

**Quyết định 01/10/2026:** sửa — tiêu đề “Định nghĩa tương hỗ của hai điểm” (không trùng s05-01); thay câu chữ “hỗ trợ lẫn nhau” bằng hai công thức cộng và quy tắc chuẩn hóa kèm lý do của MMDS §5.5.2 trước khi chạy tay (G5); nêu E là nút cụt nhưng không cần dịch chuyển (MMDS Ví dụ 5.14).

**Nguồn và vị trí:** NG1 §5.5.2, Ví dụ 5.14, Hình 5.18, tr.205–206/PDF31–32.

**Thời lượng:** 2 phút.

**Ghi chú học thuật dự kiến:**

<!-- public-notes:start -->
G5 có năm trang và tám cạnh, khác G4 ở việc C trỏ E thay vì A. Uy tín cộng điểm của các nguồn liên kết, còn trung tâm cộng điểm của các đích liên kết. Mỗi trang đều có cả hai điểm; hub và authority là hai vai trò, không phải hai tập trang loại trừ nhau. Phép cập nhật luân phiên hiện thực hóa quan hệ hỗ trợ lẫn nhau: $h$ quyết định $a$, rồi $a$ mới quyết định $h$ mới. Khởi tạo toàn $1$ là quy ước thuật toán sách; tổng ban đầu bằng $5$ và không mang ý nghĩa xác suất. Theo MMDS Ví dụ 5.14, nút cụt và bẫy liên kết không ngăn phép lặp HITS hội tụ tới một cặp vector có nghĩa, nên không cần dịch chuyển hay sửa đồ thị. Sách cũng nêu phương án chuẩn hóa để tổng bằng $1$; bài dùng chuẩn hóa theo thành phần lớn nhất như các ví dụ của sách.
<!-- public-notes:end -->

### lec04-s05-03 — Bước uy tín thứ nhất

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

Uy tín thô của mỗi trang là tổng $h^0$ của các trang trỏ tới; chuẩn hóa: chia cho giá trị lớn nhất, bằng $2$.
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

### lec04-s05-04 — Bước trung tâm thứ nhất

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

Bước trung tâm dùng uy tín vừa cập nhật $a^1$; chuẩn hóa: chia cho giá trị lớn nhất, bằng $3$.
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

### lec04-s05-05 — Vòng thứ hai trên G5

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

Tại A: $\tilde h_A=a_B^2+a_C^2+a_D^2=29/10$, trung tâm thô lớn nhất. Trung tâm của C và uy tín của E giảm dần; hai vector chưa ổn định.
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
Phép chia trong các vết trên là chuẩn hóa theo thành phần lớn nhất. Với vector không âm $q$ có $\max_iq_i>0$:
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

**Quyết định 01/10/2026:** sửa nhẹ — giữ vị trí vì quy tắc chuẩn hóa đã nêu ở s05-02; trang này hình thức hóa $N(q)$, tính chất và trường hợp biên. Câu mở nối với các phép chia đã dùng trong vết chạy.

**Nguồn và vị trí:** NG1 §5.5.2, tr.205–207; ca không cạnh suy trực tiếp từ phép chuẩn hóa.

**Thời lượng:** 2 phút.

**Ghi chú học thuật dự kiến:**

<!-- public-notes:start -->
Chia tất cả thành phần cho cùng một số dương giữ mọi tỷ lệ $q_i/q_j$ khi mẫu khác $0$, đồng thời giữ thứ tự lớn nhỏ. Do đó chuẩn hóa kiểm soát độ lớn số mà không thay ý nghĩa thứ hạng trong từng vector. Sách dùng giá trị lớn nhất; chuẩn tổng bằng $1$ hoặc chuẩn Euclid tạo giá trị khác nên không thể trộn các vết số.
<!-- public-notes:end -->

### lec04-s05-08 — Thuật toán HITS

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

Đầu ra gồm hai vector và trạng thái dừng. Đồ thị không cạnh nằm ngoài điều kiện trước vì $N(0)$ không xác định.
<!-- public-slide:end -->

**Bố cục đã chọn:** Dòng đầu vào trên15%; giả mã giữa70%; đầu ra và biên dưới15%. Dùng khối mã chung, a_new được nhắc rõ tại dòng tính h_new.

**Trọng tâm và thứ tự đọc:** Đọc điều kiện → khởi tạo → a mới từ h cũ → h mới từ a mới → kiểm cả hai vector.

**Lý do phù hợp sinh viên năm 2:** Sinh viên đã biết vòng lặp/mảng; tên cũ/mới làm hiện phụ thuộc tuần tự khác với hai cập nhật dùng chung trạng thái cũ.

**Giới hạn bố cục và phân chia nội dung:** Giữ10 dòng giả mã; chi tiết thực hiện nhân bằng cạnh thuộc S05-10. Không đưa framework hay chương trình mới.

**Ví dụ, phiếu số và hình thức hóa:** HT6, chuẩn vô cùng=max trị tuyệt đối. Khởi tạo a0=h0=1; hai ngưỡng dùng cùng tau.

**Kết nối vào–ra:** Vết chạy và ma trận → quy trình có đầu ra/điều kiện dừng → lập luận đúng và giới hạn.

**Quyết định 01/10/2026:** sửa — tiêu đề ngắn “Thuật toán HITS” (cập nhật luân phiên đã thể hiện trong giả mã); ghi chú giải thích vì sao khởi tạo cả `a` dù vết chạy chỉ cần $h^0$.

**Nguồn và vị trí:** NG1 §5.5.2, tr.206–207; giả mã cụ thể hóa thứ tự sách, điều kiện dừng và biên được nêu tường minh.

**Thời lượng:** 4 phút.

**Ghi chú học thuật dự kiến:**

<!-- public-notes:start -->
HITS cập nhật uy tín trước, rồi tính trung tâm từ uy tín vừa cập nhật. Vector `a` khởi tạo toàn $1$ chỉ dùng để đo thay đổi ở vòng đầu; giá trị của nó không đi vào phép tính $a^1$. Chuẩn hóa sau từng phép nhân tạo đúng vết chạy của Ví dụ 5.15. Với ít nhất một cạnh và khởi tạo dương, mỗi trang có cạnh ra đóng góp dương cho ít nhất một đích, rồi nhận lại một giá trị dương qua cạnh ấy. Lập luận này tiếp tục ở mọi vòng, nên các vector thô không bằng $0$ và phép chuẩn hóa hợp lệ. Mỗi vòng giữ $h$, $a$ không âm và có giá trị lớn nhất bằng $1$. Điều kiện dừng kiểm tra thay đổi của cả hai vector; hết $K$ vòng không đồng nghĩa đã đạt ngưỡng hoặc có chứng nhận sai số tới giới hạn.
<!-- public-notes:end -->

### lec04-s05-09 — Điểm ổn định của HITS

**Vai trò, mục tiêu, đầu vào và sản phẩm:** Lập luận đúng và phạm vi bảo đảm; MT4. Đầu vào: HT6. Sản phẩm: giải thích quan hệ hai bước, tránh duy nhất vô điều kiện.

**Luận điểm trung tâm:** Quan hệ vector riêng giải thích điểm ổn định nhưng không tự bảo đảm duy nhất trên mọi đồ thị.

**Nội dung hiển thị dự kiến:**

<!-- public-slide:start -->
Ở điểm ổn định, chuẩn hóa chỉ đổi độ lớn ($\propto$: tỷ lệ với, hệ số dương):
$$a\propto L^\mathsf Th,\qquad h\propto La.$$

Thế quan hệ này vào quan hệ kia:
$$h\propto LL^\mathsf Th,\qquad a\propto L^\mathsf TLa.$$

$h$ là vector riêng của $LL^\mathsf T$, $a$ là vector riêng của $L^\mathsf TL$. Giới hạn duy nhất khi trị riêng lớn nhất chỉ có một hướng riêng và khởi tạo có thành phần theo hướng ấy.
<!-- public-slide:end -->

**Bố cục đã chọn:** Sơ đồ một cạnh và hai chiều đóng góp trái35%; chuỗi hai dòng tỷ lệ phải65%; giới hạn kết luận nằm đáy. Hệ số chuẩn hóa được giải thích trong ghi chú.

**Trọng tâm và thứ tự đọc:** Theo đóng góp cạnh → ghép hai quan hệ → đọc điều kiện giới hạn của mệnh đề.

**Lý do phù hợp sinh viên năm 2:** Sinh viên đã biết phép nhân ma trận; quan hệ ghép nối cơ chế với đại số mà không yêu cầu kiểm tra kiến thức phổ chưa chuẩn bị.

**Giới hạn bố cục và phân chia nội dung:** Không đặt định lý phổ hoặc đa thức trên mặt slide. Điều kiện đủ và nghiệm G5 nằm trong ghi chú học thuật; không hỏi thi thuật ngữ phổ ở đây.

**Ví dụ, phiếu số và hình thức hóa:** HT6; tỷ lệ biểu diễn cùng hướng sau nhân số dương. Không xem LLT là cấu trúc cần tạo để thực thi.

**Kết nối vào–ra:** Giả mã đúng phép cộng → quan hệ điểm ổn định → cách thực thi thưa và chi phí.

**Quyết định 01/10/2026:** viết lại — tiêu đề “Điểm ổn định của HITS”; bỏ câu mở và hình đóng góp theo cạnh (cơ chế đã có ở s05-02, s05-06; `dong-gop-hits.svg` không còn được deck dùng); định nghĩa $\propto$; gọi tên vector riêng (đại số tuyến tính là tiên quyết) và nêu điều kiện giới hạn duy nhất trên mặt trang; dấu phẩy thập phân trong ghi chú.

**Nguồn và vị trí:** NG1 §5.5.2, tr.206–208; NG3 trang56–58 chỉ đối chiếu, sửa khẳng định duy nhất quá mạnh.

**Thời lượng:** 3 phút.

**Ghi chú học thuật dự kiến:**

<!-- public-notes:start -->
Ở điểm cố định, $h=\lambda La$ và $a=\mu L^\mathsf Th$, với $\lambda,\mu>0$ là các hệ số chuẩn hóa. Thế một quan hệ vào quan hệ kia cho $h=\lambda\mu LL^\mathsf Th$ và tương tự cho $a$.

Một điều kiện đủ để phép lặp có hướng giới hạn duy nhất là trị riêng lớn nhất của ma trận đối xứng nửa xác định dương $LL^\mathsf T$ chỉ có một hướng riêng độc lập, và khởi tạo có thành phần khác $0$ theo hướng ấy. Trong phân tích theo các hướng riêng, phần gắn với trị riêng nhỏ hơn tăng chậm hơn, nên tỷ lệ của nó giảm sau chuẩn hóa. Nếu trị riêng lớn nhất có nhiều hướng độc lập, hướng giới hạn có thể phụ thuộc khởi tạo. Đây là phác thảo điều kiện đủ, không phải chứng minh phổ tổng quát.

Trên G5, giới hạn theo thứ tự A, B, C, D, E là $h\approx(1;\,0{,}3583;\,0;\,0{,}7165;\,0)^\mathsf T$ và $a\approx(0{,}2087;\,1;\,1;\,0{,}7913;\,0)^\mathsf T$.
<!-- public-notes:end -->

### lec04-s05-10 — Chi phí HITS

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

Không dựng $LL^\mathsf T$ hoặc $L^\mathsf TL$ để chạy vì chúng có thể đặc hơn $L$.
<!-- public-slide:end -->

**Bố cục đã chọn:** Mô hình trên15%; bảng ba hàng giữa60%; kết quả và lưu ý tích ma trận dưới25%.

**Trọng tâm và thứ tự đọc:** Gắn mỗi phép nhân với một lượt cạnh → cộng phần đỉnh → tách bộ nhớ phụ/đầu vào.

**Lý do phù hợp sinh viên năm 2:** Cùng mô hình chi phí PageRank giúp so sánh trực tiếp; hai lượt cạnh được đếm trước khi rút gọn bậc tiệm cận.

**Giới hạn bố cục và phân chia nội dung:** Không suy cùng bậc là cùng thời gian thực hay cùng số vòng. K vòng và nguy cơ đặc hóa giải thích trong ghi chú.

**Ví dụ, phiếu số và hình thức hóa:** HT6; VD4 n5,ell8 chỉ là kiểm số đối tượng, không số đo hiệu năng. K vòng Theta(K(n+ell)).

**Kết nối vào–ra:** Quan hệ điểm ổn định → thực thi bằng hai lượt cạnh, thu hồi giới hạn đồ thị lớn ở S05-01 → kiểm một vòng HITS và lựa chọn phương pháp theo cùng mô hình chi phí.

**Quyết định 01/10/2026:** sửa — tiêu đề ngắn “Chi phí HITS” (mô hình danh sách cạnh đã ghi trên mặt trang); bỏ vế rỗng nghĩa “hai lượt cạnh đáp ứng nhu cầu…”.

**Nguồn và vị trí:** NG1 §5.5.2, tr.206; phép đếm trực tiếp theo giả mã đã đặc tả.

**Thời lượng:** 2 phút.

**Ghi chú học thuật dự kiến:**

<!-- public-notes:start -->
Mỗi cạnh $i\to j$ được dùng một lần để cộng $h_i$ vào $a_j$, sau đó một lần để cộng $a_j$ mới vào $h_i$. Hai lượt này cần $2\ell$ phép cộng trọng số, còn chuẩn hóa và kiểm thay đổi cần số lượt cố định theo $n$. Hệ số $2$ biến mất trong bậc tiệm cận nhưng vẫn mô tả lượng công việc khác PageRank. Tích $LL^\mathsf T$ có thể nối nhiều cặp trang cùng chung đích, nên số phần tử khác $0$ có thể tăng. Hai phép nhân luân phiên khai thác cạnh trực tiếp, tránh lưu tích ấy khi tính hai vector trên đồ thị lớn.
<!-- public-notes:end -->

### lec04-s05-11 — Kiểm tra HITS

**Vai trò, mục tiêu, đầu vào và sản phẩm:** Kiểm tra riêng S05; MT4. Đầu vào: G5, $h^2$. Sản phẩm: tính một bước uy tín mới, so với cách chia bậc ra, giải thích uy tín của nút cụt.

**Luận điểm trung tâm:** Tổng HITS không chia bậc ra; chuẩn hóa dùng một số chung cho toàn vector.

**Nội dung hiển thị dự kiến:**

<!-- public-slide:start -->
[Hình: Đồ thị G5.]

Từ vòng thứ hai: $h^2=(1,\,12/29,\,1/29,\,20/29,\,0)^\mathsf T$.

**Câu hỏi:**
1. Tính uy tín thô $\tilde a_D$ và điểm chuẩn hóa $a_D^3$.
2. Nếu mỗi nguồn chia $h_i$ cho số liên kết ra của nó, tính lại $\tilde a_D$ và nêu định nghĩa nào bị thay.
3. Tính $a_E^3$; giải thích vì sao E có uy tín dương dù không có cạnh ra.
<!-- public-slide:end -->

**Bố cục đã chọn:** G5 trái 45%, không tô cạnh; vector $h^2$ và ba yêu cầu phải 55%.

**Trọng tâm và thứ tự đọc:** Theo các cạnh vào D → cộng $h^2$ của nguồn → chuẩn hóa chung theo max (B, C); so với phép chia bậc ra; xét E chỉ có cạnh vào.

**Lý do phù hợp sinh viên năm 2:** Phép tính dùng lại đúng quy tắc vừa học trên dữ kiện mới; so sánh hai cách truyền điểm làm rõ khác biệt HITS–PageRank bằng số cụ thể.

**Giới hạn bố cục và phân chia nội dung:** Ba nhiệm vụ ngắn cùng một vòng, không hỏi phổ. Giữ toàn bộ dữ kiện để không phụ thuộc trí nhớ bảng trước.

**Ví dụ, phiếu số và hình thức hóa:** VD4/HT6; không dùng M0 hoặc bước nhảy trong HITS.

**Kết nối vào–ra:** Cơ chế HITS đã kiểm → đối chiếu ba mục tiêu xếp hạng ở S06.

**Quyết định 01/10/2026:** sửa — ba câu cũ hỏi giá trị đã hiện trong bảng s05-04 ($h_B^1$, $h_E^1$); câu mới tính bước uy tín của vòng 3 từ $h^2$ (đáp án không có trên trang nào), giữ câu “không chia bậc ra” và thêm câu uy tín của nút cụt. Dùng hình G5 không tô nét đứt (nét đứt dành cho bước không phải cạnh dữ liệu); `hinh-5-18-kiem-tra.svg` không còn được tham chiếu. Tiêu đề “Kiểm tra HITS”. Sau rà lại: câu 2 cũ có đáp án ở câu chốt s05-06, đổi thành tính lại $\tilde a_D$ theo cách chia bậc ra ($47/87$).

**Nguồn và vị trí:** NG1 VD5.15, tr.207; câu hỏi áp dụng trực tiếp.

**Thời lượng:** 3 phút.

**Nhiệm vụ và tiêu chí nội bộ:** Slide kiểm tra riêng của phần.

- Câu hỏi/đề: Ba yêu cầu như nội dung hiển thị trên G5 và $h^2$.
- Đáp án/gợi ý: $\tilde a_D=41/29$, $a_D^3=41/49$; chia bậc ra cho $47/87$, thay định nghĩa HITS; $a_E^3=1/49$.
- Tiêu chí đánh giá: Cộng đúng hai trung tâm của nguồn, chia cho max của cả vector (B, C), phân biệt uy tín (cạnh vào) với trung tâm (cạnh ra).
- Phân bổ hoạt động: Tính1 phút, giải thích1 phút, đối chiếu1 phút; tổng3 phút.

**Ghi chú học thuật dự kiến:**

<!-- public-notes:start -->
D nhận cạnh từ A và B: $\tilde a_D=h_A^2+h_B^2=1+12/29=41/29$. Uy tín thô lớn nhất thuộc B và C, cùng bằng $h_A^2+h_D^2=49/29$, nên $a_D^3=41/49$. Vector đầy đủ là $a^3=(12/49,\,1,\,1,\,41/49,\,1/49)^\mathsf T$.

Nếu chia theo bậc ra, $\tilde a_D=h_A^2/3+h_B^2/2=1/3+6/29=47/87$, khác $41/29$. Phép chia này thay định nghĩa của HITS (uy tín là tổng điểm trung tâm của các trang trỏ tới) bằng cách truyền điểm kiểu PageRank. E chỉ nhận cạnh từ C nên $\tilde a_E=h_C^2=1/29$ và $a_E^3=1/49$: uy tín phụ thuộc cạnh vào, còn việc thiếu cạnh ra chỉ làm điểm trung tâm của E bằng $0$. Giá trị này tiếp tục giảm vì $h_C$ giảm qua các vòng.
<!-- public-notes:end -->

## S06. So sánh các phương pháp xếp hạng

Tổng hợp và kết luận. Đầu ra các cụm → đối chiếu cùng tiêu chí → giải quyết lại ba tình huống của sách → năm nhiệm vụ tự kiểm. Hai nhiệm vụ ở S06-03, ba nhiệm vụ ở S06-04; S06-04 là slide kiểm tra riêng. Không đưa khái niệm trọng tâm mới.

Phân bổ: 4 slide, 10 phút.

### lec04-s06-01 — Ý nghĩa của các điểm xếp hạng

**Vai trò, mục tiêu, đầu vào và sản phẩm:** Tổng hợp; MT5. Đầu vào: HT1,HT5,HT6. Sản phẩm: phân biệt đầu ra và thông tin thêm của mỗi phương pháp.

**Luận điểm trung tâm:** Các phương pháp khác nhau ở ý nghĩa đầu ra và thông tin điều khiển.

**Nội dung hiển thị dự kiến:**

<!-- public-slide:start -->
| Phương pháp | Đầu ra | Thông tin bổ sung cần có |
|---|---|---|
| PageRank theo chủ đề | Một phân phối điểm theo ngữ cảnh | Phân phối dịch chuyển $v$ |
| TrustRank | Một phân phối điểm từ tập tin cậy | Hạt giống được đánh giá bên ngoài |
| Spam Mass | Chênh lệch tương đối giữa $r$ và $\rho$ | Hai vector cùng mô hình, $r_i>0$ |
| HITS | Hai vector trung tâm và uy tín | Không cần; chỉ dùng cấu trúc liên kết |

Điểm uy tín HITS và điểm tin cậy TrustRank có ý nghĩa khác nhau.
<!-- public-slide:end -->

**Bố cục đã chọn:** Bảng ba cột chiếm85%; câu phân biệt thuật ngữ ở đáy15%. Mọi hàng so cùng ba tiêu chí, không gán màu tốt/xấu.

**Trọng tâm và thứ tự đọc:** Đọc đầu ra của từng phương pháp → thông tin điều khiển → phân biệt hai từ uy tín/tin cậy.

**Lý do phù hợp sinh viên năm 2:** Bảng thống nhất tiêu chí sau khi học cơ chế giúp sinh viên chọn theo nhu cầu, không xếp thuật toán thành mức nâng cấp chung.

**Giới hạn bố cục và phân chia nội dung:** Không thêm thuộc tính hiệu năng chưa phân tích. Chi phí và tình huống thu hồi ở trang sau.

**Ví dụ, phiếu số và hình thức hóa:** HT1,HT5,HT6; không có ví dụ số mới.

**Kết nối vào–ra:** Ba cụm kiến thức → bảng đầu ra → quyết định trên tình huống mở bài.

**Quyết định 01/10/2026:** sửa nhẹ — tiêu đề “Ý nghĩa của các điểm xếp hạng”; đổi tên cột “Thông tin quyết định” (mơ hồ) thành “Thông tin bổ sung cần có”.

**Nguồn và vị trí:** NG1 §5.3.2,§5.4.4–5,§5.5.1–2, tr.196–207.

**Thời lượng:** 2 phút.

**Ghi chú học thuật dự kiến:**

<!-- public-notes:start -->
PageRank theo chủ đề và TrustRank dùng cùng họ phương trình nhưng nhận hai loại thông tin ưu tiên khác nhau. Spam Mass cần cặp điểm để tính chỉ số chênh lệch, không phải phép lặp riêng. HITS đổi từ một phân phối sang hai vai trò cấu trúc.
<!-- public-notes:end -->

### lec04-s06-02 — Chọn phương pháp xếp hạng

**Vai trò, mục tiêu, đầu vào và sản phẩm:** Thu hồi tình huống; MT5. Đầu vào: bảng so sánh. Sản phẩm: chọn phương pháp kèm điều kiện và giới hạn tài nguyên.

**Luận điểm trung tâm:** Lựa chọn phương pháp phụ thuộc yêu cầu và giả thiết, không chỉ bậc chi phí.

**Nội dung hiển thị dự kiến:**

<!-- public-slide:start -->
| Yêu cầu đã xét | Phương pháp và điều kiện |
|---|---|
| “jaguar” theo động vật hoặc ô tô | PageRank theo chủ đề, khi đã có chủ đề hoặc trọng số |
| Đánh giá ảnh hưởng liên kết thao túng | TrustRank và Spam Mass, khi có tập tin cậy phù hợp |
| Danh sách và nội dung học phần | HITS, khi cần cả điểm trung tâm và uy tín |

Các phép lặp đều khai thác đồ thị thưa, mỗi vòng tuyến tính theo $n+\ell$.
<!-- public-slide:end -->

**Bố cục đã chọn:** Bảng hai cột ba hàng giữa80%; câu chi phí dưới20%. Tên tình huống trùng mở đầu và nguồn sách.

**Trọng tâm và thứ tự đọc:** Xác định yêu cầu → chọn đầu ra → kiểm điều kiện đầu vào → đọc giới hạn chi phí.

**Lý do phù hợp sinh viên năm 2:** Ba tình huống quen được dùng lại, không thêm lĩnh vực ứng dụng phải học; điều kiện kèm lựa chọn ngăn học thuộc tên thuật toán.

**Giới hạn bố cục và phân chia nội dung:** Không bổ sung thuật toán mới hoặc kết luận thực nghiệm. Thời gian hoàn thành hệ tìm kiếm nằm ngoài mô hình.

**Ví dụ, phiếu số và hình thức hóa:** HT3,HT5,HT6; ví dụ định tính đã dùng. Không có phiếu số mới.

**Kết nối vào–ra:** Đối chiếu các phương pháp → áp vào vấn đề đầu bài → tự kiểm khả năng tính và giải thích.

**Quyết định 01/10/2026:** sửa tiêu đề — “yêu cầu dữ liệu” không khớp nội dung (yêu cầu về đầu ra); tiêu đề mới ngắn và gọi đúng thao tác của trang. Nội dung giữ: bảng thu hồi ba tình huống mở bài.

**Nguồn và vị trí:** NG1 §5.3.1,§5.4.3–5,VD5.13; phép đếm đã xây ở S02 và S05.

**Thời lượng:** 2 phút.

**Ghi chú học thuật dự kiến:**

<!-- public-notes:start -->
Nhu cầu theo chủ đề còn phụ thuộc độ phù hợp của tập dịch chuyển hoặc trọng số. TrustRank cần hạt giống đáng tin và đủ độ phủ; Spam Mass không tự tạo nhãn đúng chắc chắn. HITS cần đầu ra hai vai trò nên không thay thế trực tiếp chỉ số tin cậy. Chi phí tuyến tính theo $n+\ell$ mỗi vòng chỉ là một tiêu chí; số vòng, độ chính xác dừng và chi phí chuẩn bị thông tin bên ngoài vẫn khác nhau.
<!-- public-notes:end -->

### lec04-s06-03 — Câu hỏi về mô hình và chi phí

**Vai trò, mục tiêu, đầu vào và sản phẩm:** Tự kiểm tổng hợp1–2; MT1,MT5. Đầu vào: phân phối dịch chuyển và phép đếm. Sản phẩm: phân biệt thay mô hình/biểu diễn và hiểu phạm vi chi phí.

**Luận điểm trung tâm:** Thay phân phối dịch chuyển không thay đồ thị; cùng chi phí tiệm cận không đồng nhất thời gian thực.

**Nội dung hiển thị dự kiến:**

<!-- public-slide:start -->
**Câu hỏi:**
1. Trên cùng G4, giữ $\beta=4/5$ và đổi tập dịch chuyển từ {B,D} sang {C}. Xác định đại lượng phải đổi và đại lượng được giữ nguyên trong $r'=\beta M_0r+(1-\beta)v$.
2. PageRank theo chủ đề và HITS đều có chi phí mỗi vòng $\Theta(n+\ell)$. Đánh giá kết luận: “Hai thuật toán luôn có cùng thời gian chạy”. Nêu những đại lượng còn thiếu.
<!-- public-slide:end -->

**Bố cục đã chọn:** Hai khung nhiệm vụ xếp dọc, mỗi khung khoảng50%; công thức ở trong khung1. Không đặt bảng đáp án bên cạnh.

**Trọng tâm và thứ tự đọc:** Nhiệm vụ1 xét mô hình điểm; nhiệm vụ2 xét phạm vi phép đếm; không ghép hai câu vào một lập luận dài.

**Lý do phù hợp sinh viên năm 2:** Hai thao tác khác nhau nhưng dùng đầu vào đã học; câu2 kiểm khả năng bảo toàn giả thiết khi chuyển từ tiệm cận sang hiệu năng.

**Giới hạn bố cục và phân chia nội dung:** Đây là hai trong năm nhiệm vụ tự kiểm S06; quiz riêng của phần là trang kế tiếp. Mỗi câu có lời giải trong ghi chú.

**Ví dụ, phiếu số và hình thức hóa:** VD1/HT1 và HT3/HT6; không cần tính lại nghiệm S={A}.

**Kết nối vào–ra:** Lựa chọn phương pháp → tự kiểm mô hình/chi phí → kiểm tra tổng hợp các giới hạn.

**Quyết định 01/10/2026:** sửa — tiêu đề “Câu hỏi về mô hình và chi phí” thay nhãn quy trình “Tự kiểm”; câu 1 đổi tập dịch chuyển sang {C} để không trùng dữ kiện Bài tập 5.3.1(a) (tập {A}) ở s07-01.

**Nguồn và vị trí:** NG1 §5.3.2,§5.5.2; nhiệm vụ suy trực tiếp từ đặc tả và phép đếm đã dạy.

**Thời lượng:** 3 phút.

**Nhiệm vụ và tiêu chí nội bộ:** Nhiệm vụ tự kiểm; slide kiểm tra riêng của phần được chỉ định trong bản đồ.

- Câu hỏi/đề: Hai câu hỏi như nội dung hiển thị.
- Đáp án/gợi ý: Câu1 đổi v và khởi tạo theo v, giữ M0/beta. Câu2 kết luận không được bảo đảm, còn thiếu số vòng/hằng số/điều kiện thực thi.
- Tiêu chí đánh giá: Nêu đúng thành phần thay đổi, không sửa cạnh; phân biệt một vòng với toàn thuật toán và tiệm cận với số đo.
- Phân bổ hoạt động: Suy nghĩ1 phút, trao đổi lời giải1 phút, đối chiếu1 phút; tổng3 phút.

**Ghi chú học thuật dự kiến:**

<!-- public-notes:start -->
Ở câu 1, đồ thị và $M_0$ giữ nguyên, $\beta=4/5$; $v$ đổi từ $(0,1/2,0,1/2)^\mathsf T$ sang $(0,0,1,0)^\mathsf T$. Nếu khởi tạo theo $v$ thì $r^0$ cũng đổi. G4 không có nút cụt nên không có số hạng bù. Ở câu 2, hai thuật toán có thể khác số vòng, hệ số công việc, tiêu chí dừng và cách thực thi; chuẩn bị tập chủ đề hoặc tập tin cậy cũng không nằm trong chi phí một vòng. Cùng bậc tiệm cận không suy ra cùng thời gian chạy.
<!-- public-notes:end -->

### lec04-s06-04 — Câu hỏi so sánh các phương pháp

**Vai trò, mục tiêu, đầu vào và sản phẩm:** Kiểm tra riêng S06; câu 3–5; MT2–MT5. Đầu vào: ba mô hình. Sản phẩm: chọn và diễn giải điểm dưới đúng giả thiết.

**Luận điểm trung tâm:** Kết hợp hai phần đã học (cụm thao túng với TrustRank; định nghĩa Spam Mass với cách đọc) và chọn phương pháp theo đầu ra.

**Nội dung hiển thị dự kiến:**

<!-- public-slide:start -->
**Câu hỏi:**
3. Tính TrustRank cho cụm Hình 5.16 (đồ thị không có nút cụt) khi không trang nào của cụm thuộc $T$. Viết lại phương trình của $p$ và $y$; chỉ ra số hạng của công thức PageRank bị mất.
4. Một hệ thống thay mọi giá trị Spam Mass âm bằng $0$. Đánh giá thay đổi này theo định nghĩa và cách đọc của chỉ số.
5. Trên G4, tính $a^1$ từ $h^0=(1,1,1,1)^\mathsf T$ và so với PageRank nền $(9/28,19/84,19/84,19/84)^\mathsf T$; giải thích khác biệt.
<!-- public-slide:end -->

**Bố cục đã chọn:** Ba nhiệm vụ thành ba hàng đủ rộng, khoảng1/3 mỗi hàng; dữ kiện số chỉ ở câu4. Không có hình phụ.

**Trọng tâm và thứ tự đọc:** Theo từng câu: định nghĩa đóng góp → dấu chỉ số → lựa chọn đầu ra hai vai trò.

**Lý do phù hợp sinh viên năm 2:** Mỗi nhiệm vụ đo một ranh giới thường nhầm; ba câu bao phủ các mục tiêu còn lại mà không giới thiệu dữ kiện mới.

**Giới hạn bố cục và phân chia nội dung:** Năm nhiệm vụ tự kiểm được phân bố giữa hai trang cuối S06, không dồn thành bảng chữ nhỏ. Đáp án chỉ trong ghi chú.

**Ví dụ, phiếu số và hình thức hóa:** VD2,VD3,VD4/HT4–HT6. Không hỏi điều kiện phổ chưa được kiểm tra ở tuyến chính.

**Kết nối vào–ra:** Tổng hợp ba mục tiêu → ba bài nguồn tính và chứng minh trong recitation.

**Quyết định 01/10/2026:** sửa — tiêu đề “Câu hỏi so sánh các phương pháp”; câu 3 cũ lặp s03-08 và câu 4 cũ lặp số liệu s04-05 (G10), nay câu 3 kết hợp cụm thao túng với TrustRank (đặt $b=0$ trong phương trình S03), câu 4 đánh giá việc cắt giá trị âm theo cách đọc của MMDS; câu 5 bỏ cụm “mạng học phần”. Sau rà lại: câu 5 cũ có đáp án ở bảng s06-02, đổi sang so sánh HITS với PageRank trên G4; câu 3 thêm giả thiết không có nút cụt. Sửa khoảng trắng thừa “$\beta$ $x$”.

**Nguồn và vị trí:** NG1 §5.4.2,§5.4.5,VD5.13; câu hỏi áp dụng dữ kiện đã học.

**Thời lượng:** 3 phút.

**Nhiệm vụ và tiêu chí nội bộ:** Slide kiểm tra riêng của phần.

- Câu hỏi/đề: Ba câu 3–5 như nội dung hiển thị.
- Đáp án/gợi ý: $p=\beta y/m$, $y=x_\rho/(1-\beta^2)$, mất số hạng $\frac{\beta}{1+\beta}\frac mn$; cắt giá trị âm về 0 đổi định nghĩa, mất thông tin trang được tập tin cậy hỗ trợ nhưng không đổi thứ tự rà soát trang gần 1; $a^1=(1,1,1,1)^\mathsf T$ vì mọi trang có hai cạnh vào; PageRank ưu tiên A do chia theo bậc ra.
- Tiêu chí đánh giá: Đặt $b=0$ tại mọi trang của cụm và giải lại; nêu đúng ý nghĩa giá trị âm và cách đọc; tính đúng $a^1$ và nêu vai trò của việc chia theo bậc ra.
- Phân bổ hoạt động: Suy nghĩ1 phút, trả lời1 phút, đối chiếu1 phút; tổng3 phút.

**Ghi chú học thuật dự kiến:**

<!-- public-notes:start -->
Câu 3: dịch chuyển chỉ vào $T$ nên mọi trang của cụm có phần dịch chuyển bằng $0$, tức $b$ được thay bằng $0$ tại đích và tại mỗi hỗ trợ: $p=\beta y/m$, $y=x_\rho+\beta mp$, với $x_\rho$ là đóng góp TrustRank từ ngoài. Do đó $y=x_\rho/(1-\beta^2)$: cụm chỉ khuếch đại phần điểm đã tới từ liên kết ngoài, còn số hạng $\frac{\beta}{1+\beta}\frac mn$ do dịch chuyển vào các hỗ trợ bị mất. Nếu các trang ngoài trỏ vào đích ít nhận TrustRank, $\rho$ của đích nhỏ so với $r$ và Spam Mass của đích gần $1$.

Câu 4: giá trị âm cho biết TrustRank lớn hơn PageRank nền, tức trang được tập tin cậy hỗ trợ. Thay bằng $0$ là đổi định nghĩa và mất thông tin này; theo cách đọc của MMDS, mọi giá trị âm hay dương nhỏ đều thuộc nhóm có lẽ không phải rác, nên thứ tự ưu tiên rà soát các trang có giá trị gần $1$ không đổi. Câu 5: mỗi trang của G4 có đúng hai cạnh vào, nên uy tín thô đều bằng $2$ và $a^1=(1,1,1,1)^\mathsf T$. PageRank xếp A cao nhất vì C có một cạnh ra duy nhất và chuyển toàn bộ điểm cho A, còn A chia điểm cho ba trang; HITS cộng điểm theo cạnh, không chia theo bậc ra, nên không phân biệt điều này ở bước đầu. Hai phương pháp đo hai khái niệm khác nhau trên cùng đồ thị.
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

$\beta=0{,}8$, kế thừa Ví dụ 5.10; tám cạnh của G4 giữ nguyên.

**Câu hỏi:** Tính PageRank theo chủ đề khi tập dịch chuyển là (a) chỉ A; (b) A và C.

Sản phẩm: hai phân phối dịch chuyển, hệ phương trình, hai vector điểm theo thứ tự A, B, C, D; kiểm tra tổng bằng 1 và nghiệm thỏa phương trình cố định.
<!-- public-slide:end -->

**Bố cục đã chọn:** G4 có đầy đủ tám cạnh trái45%; nguồn, hai yêu cầu và sản phẩm phải55%. Tham số beta nằm cạnh tên đồ thị. Lời giải không xuất hiện trên mặt slide.

**Trọng tâm và thứ tự đọc:** Đọc nguồn dữ kiện → dựng v cho từng trường hợp → giải cùng phương trình → kiểm nghiệm.

**Lý do phù hợp sinh viên năm 2:** Dùng lại G4 giảm thời gian học dữ liệu mới; hai tập dịch chuyển khác nhau cho phép kiểm việc chỉ đổi v mà giữ M0.

**Giới hạn bố cục và phân chia nội dung:** Không đổi số/cạnh hoặc yêu cầu nguồn. Các bước giảm hệ và đáp án ở ghi chú; slide chỉ đủ đề và sản phẩm.

**Ví dụ, phiếu số và hình thức hóa:** BT1; VD1. $r=(4/5)M_0r+(1/5)v$. Hình 5.15 có n4,ell8; không có nút cụt.

**Kết nối vào–ra:** Lý thuyết theo chủ đề → bài giải độc lập → phân tích đổi cấu trúc liên kết ở BT2.

**Quyết định 01/10/2026:** sửa nhẹ — giữ tiêu đề và bài nguồn; dòng sản phẩm thay cụm “tổng 1/điểm cố định” (dấu gạch chéo mơ hồ) bằng hai phép kiểm tách rời.

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

### lec04-s07-02 — Bài tập biến thể cụm thao túng

**Vai trò, mục tiêu, đầu vào và sản phẩm:** Recitation BT2; MT2. Đầu vào: HT4. Sản phẩm: hai mô hình cân bằng và biểu thức y theo tham số.

**Luận điểm trung tâm:** Thay liên kết của hỗ trợ đổi dòng quay lại đích và hệ số khuếch đại.

**Nội dung hiển thị dự kiến:**

<!-- public-slide:start -->
**Bài 5.4.1(a, c), MMDS §5.4.6, trang 203–204.**

Giữ mô hình Hình 5.16, trừ cạnh ra của các hỗ trợ; $x$ đã gồm $\beta$; $b=(1-\beta)/n$.

**Câu hỏi:** Lặp lại phân tích khi mỗi trang hỗ trợ (a) chỉ trỏ tới chính nó thay vì đích; (c) trỏ tới cả chính nó và đích.

Sản phẩm: phương trình điểm hỗ trợ $p$ và điểm đích $y$; biểu thức của $y$ theo $x,m,n,\beta$; chỉ rõ công thức chính xác hay xấp xỉ.
<!-- public-slide:end -->

**Bố cục đã chọn:** Dải giả thiết trên35%; hai sơ đồ cấu trúc(a),(c) đặt ngang ở dưới trái40% tổng khung; đề và sản phẩm ở dưới phải60%. Đích→hỗ trợ giữ nguyên; khuyên/cạnh quay lại có nhãn.

**Trọng tâm và thứ tự đọc:** Đọc các điều kiện không đổi → đối chiếu đúng cạnh thay ở(a)/(c) → lập p và y.

**Lý do phù hợp sinh viên năm 2:** Hình cạnh thay đổi giúp sinh viên suy mẫu số 1 hoặc2 theo từng trường hợp; vẫn dùng biến nguồn để không phát sinh bài toán mới.

**Giới hạn bố cục và phân chia nội dung:** Trên mặt slide không đặt lời giải hay số beta mới. Ý(b) lược có lý do trong metadata, không biến thành đề khác.

**Ví dụ, phiếu số và hình thức hóa:** BT2/VD2/HT4; n≥m+1,m≥1,0<beta<1; cả hai cấu trúc giữ không nút cụt.

**Kết nối vào–ra:** BT1 đổi bước nhảy → BT2 đổi cạnh và quy tắc chia → BT3 tính hai vai trò trên chuỗi nguồn.

**Quyết định 01/10/2026:** sửa nhẹ — tiêu đề dùng thuật ngữ “cụm thao túng” thống nhất với S03; dòng giả thiết lặp toàn bộ mô hình được rút còn phần khác biệt (cạnh ra của hỗ trợ). Bài nguồn, dữ kiện và lời giải giữ nguyên.

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

**Nhiệm vụ và tiêu chí nội bộ:** Bài tập nguồn; không phải slide kiểm tra riêng của phần.

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
| `lec04-s03-07` | Không dùng hình từ 01/10/2026; `hai-nhom-canh-noi-bo.svg` giữ trong kho, không được tham chiếu |
| `lec04-s04-01` | `tap-tin-cay.svg` |
| `lec04-s04-03` | `hinh-5-15-tin-cay.svg` |
| `lec04-s05-01` | `cap-vai-tro-hits.svg` |
| `lec04-s05-02` | `hinh-5-18.svg` |
| `lec04-s05-09` | Không dùng hình từ 01/10/2026; `dong-gop-hits.svg` giữ trong kho, không được tham chiếu |
| `lec04-s05-11` | `hinh-5-18.svg` (từ 01/10/2026; `hinh-5-18-kiem-tra.svg` không còn được tham chiếu) |
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
