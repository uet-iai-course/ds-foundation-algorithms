# Quy trình chuyển trang chiếu Giải thuật nền tảng của Khoa học dữ liệu sang RevealJS

## Phạm vi

Tệp này áp dụng cho mọi yêu cầu chọn một bộ trang chiếu hoặc tài liệu trong `sources/` và chuyển sang RevealJS cho học phần **Giải thuật nền tảng của Khoa học dữ liệu**, học kỳ 1 năm học 2026–2027.

`sources/source.md` là bản đồ nguồn cấp học phần. Tệp này chứa bản trích xuất đề cương, thứ tự bài học đề xuất, ánh xạ từ buổi gốc, chuẩn đầu ra, kiến thức tiên quyết, học liệu và các điểm cần xác minh. Mọi yêu cầu làm một bài phải đọc `sources/source.md` trước khi chọn và phân tích tài liệu chi tiết. Mặc định dùng thứ tự đề xuất trong tệp này; chỉ dùng thứ tự gốc khi người dùng yêu cầu rõ.

`sources/reference-slides/README.md` là bảng ánh xạ slide tham khảo cho 15 buổi đề xuất. Sau khi xác định bài từ `sources/source.md`, phải đọc dòng tương ứng trong bảng này và các tệp cục bộ được chỉ định. Trạng thái “đủ có điều kiện” là một khoảng trống nguồn phải xử lý trước khi hoàn tất deck, không phải giấy phép tự bổ sung mệnh đề.

Mỗi yêu cầu phải tạo hoặc cập nhật:

- `2627-1/lecture-NN-<ten-bai>.html`;
- các hình SVG trong `2627-1/img/lec-NN/`;
- ba tệp quy trình trong `2627-1/planning/lec-NN/`;
- mục tương ứng trong `2627-1/index.html`.

`NN` lấy theo số bài trong bảng **Thứ tự đề xuất** của `sources/source.md` và luôn có hai chữ số. Ví dụ, bài 1 dùng `lecture-01-<ten-bai>.html`. Tên bài, phạm vi và học liệu phải đối chiếu với mục tương ứng trong `sources/source.md`. Nếu người dùng yêu cầu theo thứ tự gốc, ghi rõ ngoại lệ trong storyboard và nhật ký rà soát.

Điều phối viên phải dùng nhiều tác tử theo quy trình dưới đây. Không giao toàn bộ việc lập kế hoạch, phân tích, soạn, rà soát và chỉnh sửa cho một tác tử.

## Đối tượng và thời lượng

- Đối tượng mặc định là sinh viên đại học đã học lập trình, toán rời rạc, đại số tuyến tính và xác suất cơ bản.
- Buổi học gồm ba tiết, mỗi tiết 50 phút, tổng cộng 150 phút.
- Phần trình chiếu chính được thiết kế cho 120 phút. 30 phút còn lại dành cho chữa bài tập và trình diễn mã.
- Chỉ chuyển hoặc chuẩn bị mã trình diễn khi nguồn có nội dung tương ứng. Không tự tạo sổ tay mã hoặc chương trình ngoài phạm vi nguồn nếu người dùng không yêu cầu.

## Ngôn ngữ và biên tập

- Viết thuần Việt. Chỉ giữ tiếng Anh cho tên riêng, tên phần mềm, ký hiệu chuẩn, tên thuật toán hoặc thuật ngữ chưa có cách dịch ổn định.
- Khi dùng viết tắt lần đầu, viết đầy đủ bằng tiếng Việt rồi đặt dạng viết tắt trong ngoặc.
- Viết ngắn, trực tiếp và học thuật. Dùng câu ngắn, động từ rõ và thuật ngữ nhất quán.
- Không dùng câu hỏi tu từ, câu cảm thán, lời ca tụng, khẩu hiệu hoặc cách diễn đạt quảng bá.
- Không thêm nhận định, số liệu, nguồn hoặc ví dụ không có căn cứ.
- Trong mọi tệp Markdown, chỉ dùng `$...$` cho công thức nội dòng và `$$...$$` cho công thức khối.
- Dùng `$no-ai-slop` để biên tập nội dung hiển thị và ghi chú diễn giả. Giữ ý của nguồn; cắt lời dẫn rỗng, câu tổng kết lặp, diễn đạt phô trương và nhịp câu máy móc. Tự kiểm bản cuối theo `no-ai-slop/eval.md`.
- Dùng `$quill` để rà dàn ý, thứ tự khái niệm, thuật ngữ, ký hiệu và tính liên tục giữa các phần. Không khởi tạo `quill.json`; công việc này không phải dự án sách.

## Thứ tự ưu tiên

Khi có xung đột, tuân theo thứ tự sau:

1. Chỉ dẫn cụ thể của người dùng cho bài đang làm.
2. `sources/source.md` về số bài, tên bài, thứ tự, phạm vi, chuẩn đầu ra, kiến thức tiên quyết và học liệu cần dùng.
3. Bộ trang chiếu hoặc tài liệu chi tiết được chọn trong `sources/` về nội dung, ví dụ, chứng minh, thuật toán, hình và mã của bài.
4. Tài liệu bổ sung và tài sản liên quan do người dùng cung cấp.
5. `2627-1/lecture-template.html` và `2627-1/lecture-style.css` về giao diện và nền kỹ thuật.
6. Các quy ước trong tệp này.

Giữ mạch cấp học phần theo `sources/source.md`; giữ mạch và ý chính trong từng bài theo tài liệu chi tiết. Chỉ gộp, tách, thêm, lược hoặc sắp xếp cục bộ khi cần sửa lỗi, giảm quá tải, khôi phục tiên quyết, hoàn thiện mạch học tập hoặc bảo đảm khả năng đọc. Mọi sai khác phải có lý do trong storyboard và nhật ký rà soát.

## Tiếp nhận và kiểm kê

Sau khi người dùng chọn bài học hoặc tệp nguồn, điều phối viên phải:

- đọc `sources/source.md`, xác định bài theo thứ tự đề xuất và trích mục tiêu, tiên quyết, phạm vi, học liệu, ánh xạ buổi gốc cùng các điểm cần xác minh;
- đọc dòng tương ứng trong `sources/reference-slides/README.md`, kiểm tra trạng thái đầy đủ và mở toàn bộ slide cục bộ được ánh xạ cho bài;
- từ mục học liệu của bài, xác định tài liệu chi tiết cần dùng, đọc các tệp tương ứng và kiểm tra tài liệu liên quan trong `sources/`;
- bỏ qua `.DS_Store`, tệp có tiền tố `._` và tệp tạm có tiền tố `~$`;
- xác định số bài, tên bài, mục tiêu, kiến thức tiên quyết và phạm vi từ `sources/source.md`; xác định số trang, phần hoặc chương nguồn và các tài sản từ tài liệu chi tiết;
- đọc `2627-1/lecture-template.html`, `2627-1/lecture-style.css` và `2627-1/index.html` trước khi lập kế hoạch;
- kiểm kê định nghĩa, định lý, bổ đề, chứng minh, thuật toán, cấu trúc dữ liệu, ví dụ, bài tập, hình, bảng, công thức và đoạn mã phải chuyển;
- xác định phần nào của nguồn là nội dung, bố cục, ghi chú, tài liệu tham khảo hoặc tài sản trực quan;
- chỉ hỏi người dùng về thông tin không thể suy ra từ kho và có thể làm thay đổi đáng kể kết quả.

Nếu người dùng đã nêu số bài hoặc tên bài, dùng `sources/source.md` để xác định các nguồn cần kiểm tra; không yêu cầu lại tên tệp khi ánh xạ đã rõ. Nếu tài liệu được chỉ định trong `sources/source.md` chưa có trong kho, dừng sau bước kiểm kê và yêu cầu người dùng bổ sung hoặc chọn tài liệu thay thế. Nếu người dùng chưa chọn cả bài lẫn tệp nguồn, dừng sau bước kiểm kê danh mục và yêu cầu số bài, tên bài hoặc tên tệp. Không tự chọn bài thay người dùng và không tự bổ sung nội dung thay cho tài liệu còn thiếu.

## Tổ chức tệp

Mỗi bài dùng cấu trúc sau:

```text
2627-1/
├── lecture-NN-<ten-bai>.html
├── img/
│   └── lec-NN/
│       └── *.svg
└── planning/
    └── lec-NN/
        ├── outline.md
        ├── storyboard.md
        └── review-log.md
```

- `outline.md` chứa mục tiêu, dàn ý, ánh xạ nguồn và bảng thuật ngữ hoặc ký hiệu cần thiết.
- `storyboard.md` chứa bản đồ hành trình khái niệm và một mục cho từng trang chiếu.
- `review-log.md` chứa các báo cáo rà soát, quyết định chỉnh sửa, sai khác so với nguồn và ngoại lệ đã được duyệt.
- Tệp HTML nằm trực tiếp trong `2627-1/`. Không đặt tệp HTML trong thư mục `planning/` hoặc `img/`.
- Mọi đường dẫn trong HTML phải tương đối và hợp lệ khi máy chủ được mở tại thư mục gốc của kho.

## Mẫu RevealJS bắt buộc

- Dùng `2627-1/lecture-template.html` làm nền. Chỉ kế thừa cấu trúc, giao diện và cấu hình kỹ thuật; không sao chép chủ đề, nội dung hoặc siêu dữ liệu của bài khác.
- Dùng `2627-1/lecture-style.css`, màu, phông chữ, khoảng cách, thẻ, lưới và chân trang hiện có. Không tạo hệ giao diện mới.
- Tham khảo cách tổ chức bố cục trong kho `uet-iai-course/machine-learning`, ưu tiên `SLIDE_STYLE_GUIDE.md` và các tệp `2526-2/lecture-*.html`. Áp dụng nguyên tắc một luận điểm trung tâm, hình hoặc công thức đủ lớn, chú thích nêu kết luận và nhịp mở phần–trực giác–cơ chế–ví dụ–kiểm tra. Không sao chép nội dung, tài sản hoặc CSS từ kho tham khảo.
- Giữ `lang="vi"`, khung `1280 × 720`, `controlsLayout: "edges"`, `slideNumber: true`, `hashOneBasedIndex: true` và `hash: true`.
- Dùng các thư viện cục bộ trong `2627-1/`: RevealJS, `RevealMath.KaTeX`, `RevealNotes` và `RevealHighlight`.
- Dùng `<section>` ngoài cho từng phần và `<section>` trong cho từng trang chiếu.
- Mỗi trang có `data-slide-id` duy nhất. Mã này chỉ xuất hiện trong HTML, outline, storyboard và nhật ký; không hiển thị trên mặt trang chiếu hoặc trong ghi chú diễn giả.
- Đặt chân trang ở cuối `.slides` và cập nhật đúng tên học phần, học kỳ và số bài.
- Không phụ thuộc mạng cho các thành phần cốt lõi.
- Chỉ dùng tài sản cốt lõi đã có trong `2627-1/` hoặc tài sản SVG được tạo cho bài đang làm. Không tải phông chữ, thư viện hoặc hình từ mạng.

## Chuyển và vẽ lại hình

- Mọi sơ đồ, đồ thị, cây, mạng, hình hình học và hình kỹ thuật phải được vẽ lại thành SVG. Không trích ảnh raster từ PDF hoặc PPTX rồi nhúng vào trang chiếu.
- Lưu SVG chính tại `2627-1/img/lec-NN/`. SVG nhỏ, chỉ dùng một lần, có thể đặt nội dòng trong HTML khi cách này giúp bố cục hoặc khả năng tiếp cận rõ hơn.
- Giữ đúng quan hệ, tỷ lệ có ý nghĩa, nhãn, chiều mũi tên, chú giải, trọng số và dữ liệu của hình nguồn. Không làm hình đẹp hơn bằng cách thay đổi nội dung.
- Đồ thị phải có tên trục, đơn vị, chú giải và nguồn khi các thành phần này có trong nguồn hoặc cần để hiểu hình.
- Mỗi SVG phải có `role="img"` và mô tả thay thế cụ thể. Không dùng màu làm tín hiệu duy nhất.
- Công thức, bảng, giả mã và mã nguồn phải được dựng bằng KaTeX, HTML hoặc khối mã; không chuyển chúng thành ảnh.
- Không dùng ảnh sinh bởi AI để thay cho dữ liệu, kết quả thực nghiệm hoặc hình mô tả bằng chứng.
- Ảnh chụp, logo hoặc ảnh chụp màn hình chỉ được giữ ở dạng điểm ảnh khi không thể tái tạo trung thực bằng SVG và người dùng đã duyệt ngoại lệ. Ghi ngoại lệ, lý do và đường dẫn trong `review-log.md`.
- Nếu ngoại lệ chưa được duyệt, dừng phần bị ảnh hưởng và hỏi người dùng. Không âm thầm giữ ảnh raster hoặc bỏ nội dung.

## Cấu trúc học tập

Mỗi khái niệm hoặc thuật toán trọng tâm đi theo chu trình:

**tình huống sử dụng dữ liệu lớn → vấn đề → trực giác → ví dụ chạy tay → hình thức hóa → thuật toán và lập luận đúng → ứng dụng và chi phí → kiểm tra**

- **Tình huống sử dụng dữ liệu lớn:** mở đầu bằng một trường hợp cụ thể cần thuật toán. Nêu loại dữ liệu, đầu ra hoặc quyết định cần tạo, giới hạn về bộ nhớ, I/O, băng thông, thời gian hoặc số lượt quét, và lý do cách trực tiếp không phù hợp. Dùng quy mô định lượng khi nguồn cung cấp; không bịa số liệu. Không dùng tình huống chỉ để trang trí hoặc không được dùng lại trong phần lập luận.
- **Vấn đề:** nêu đầu vào, đầu ra, giới hạn hoặc nhu cầu tính toán. Không dùng câu hỏi tu từ.
- **Trực giác:** nêu cấu trúc dữ liệu, phép biến đổi hoặc lựa chọn cục bộ chuẩn bị cho ký hiệu.
- **Ví dụ chạy tay:** dùng một trường hợp đủ nhỏ để theo dõi trạng thái, biến trung gian và kết quả.
- **Hình thức hóa:** nêu miền, kiểu, kích thước, điều kiện trước, điều kiện sau và ký hiệu.
- **Thuật toán và lập luận đúng:** nêu giả mã, bất biến hoặc luận điểm chính của chứng minh, điều kiện dừng và kết luận.
- **Ứng dụng và chi phí:** áp dụng trực tiếp kết quả vừa xây dựng; phân tích thời gian, bộ nhớ và giới hạn thực hành.
- **Kiểm tra:** yêu cầu người học tính, mô phỏng, giải thích, chứng minh, so sánh hoặc sửa thuật toán.

Không bắt buộc tám bước là tám trang riêng. Có thể gộp khi trang vẫn có một luận điểm trung tâm. Với khái niệm phụ, có thể dùng chu trình rút gọn nếu storyboard ghi rõ lý do. Không đảo thứ tự hoặc bỏ ngầm một bước đối với khái niệm trọng tâm.

Storyboard phải chỉ ra cho từng cụm:

- mã trang thực hiện từng bước;
- kiến thức đầu vào và sản phẩm học tập;
- dữ liệu, giới hạn quy mô và đầu ra của tình huống mở bài; cách tình huống này được dùng lại trong ví dụ, đặc tả, phân tích chi phí hoặc kiểm tra;
- dữ kiện, trạng thái trung gian hoặc ký hiệu được truyền từ ví dụ sang giả mã và chứng minh;
- bước được gộp hoặc ghi `không áp dụng`, kèm lý do;
- câu nối giữa các bước;
- thời lượng dự kiến của cụm và tổng thời lượng 120 phút.

## Tiêu chuẩn nội dung giải thuật

- Nêu rõ bài toán, miền đầu vào, kiểu dữ liệu, kích thước, chỉ số và quy ước trước khi dùng.
- Phân biệt đặc tả bài toán, biểu diễn dữ liệu, thuật toán, cài đặt và kết quả thực nghiệm.
- Mỗi thuật toán phải có đầu vào, đầu ra, điều kiện trước, điều kiện sau, giả mã hoặc sơ đồ, điều kiện dừng và trường hợp biên.
- Mọi chứng minh tính đúng phải nêu mệnh đề cần chứng minh và các giả thiết. Dùng bất biến vòng lặp, quy nạp, trao đổi, phản chứng hoặc quy nạp cấu trúc khi phù hợp; không thay chứng minh bằng trực giác.
- Với thuật toán đệ quy hoặc chia để trị, kiểm tra trường hợp cơ sở, tiến triển về trường hợp cơ sở, hệ thức truy hồi và điều kiện áp dụng định lý dùng để giải hệ thức.
- Với thuật toán tham lam, nêu lựa chọn tham lam, tính khả thi, tính lựa chọn tham lam và cấu trúc con tối ưu khi nguồn yêu cầu bảo đảm tối ưu.
- Với quy hoạch động, nêu trạng thái, miền chỉ số, ý nghĩa bảng, điều kiện cơ sở, thứ tự tính, công thức chuyển, cách khôi phục nghiệm và chi phí bộ nhớ.
- Với đồ thị, nêu có hướng hay vô hướng, có trọng số hay không, quy ước đỉnh và cạnh, biểu diễn, khả năng có cạnh âm, đa cạnh hoặc khuyên khi chúng ảnh hưởng đến kết quả.
- Với thuật toán ngẫu nhiên, nêu nguồn ngẫu nhiên, đại lượng kỳ vọng hoặc xác suất bảo đảm và điều kiện độc lập khi cần.
- Phân biệt độ phức tạp trường hợp xấu, trung bình, kỳ vọng và khấu hao. Ghi rõ tham số kích thước và mô hình chi phí.
- Không tuyên bố tối ưu, đúng, ổn định số, xấp xỉ hoặc đạt cận dưới nếu thiếu giả thiết quyết định kết luận.
- Tự chạy lại ví dụ, kiểm tra chỉ số, giá trị trung gian, kết quả, độ phức tạp và trường hợp biên quan trọng.
- Giữ nguồn truy nguyên được theo số trang hoặc số trang chiếu của bản nguồn. Chỉ bổ sung nguồn ngoài khi cần sửa hoặc kiểm chứng một mệnh đề và phải ghi nguồn cụ thể.

## Tiêu chuẩn trang chiếu và ghi chú

- Mỗi trang chiếu có một luận điểm trung tâm. Tách chứng minh, giả mã, bảng vết chạy hoặc công thức truy hồi quá dài thay vì thu nhỏ chữ.
- Tiêu đề ngắn và gọi đúng khái niệm. Không đặt tiêu đề dưới dạng “Tại sao...?”, “Vì sao...?” hoặc câu kể tiến trình.
- Văn bản thân bài nên từ `0.75em` trở lên. Chỉ dùng dưới `0.65em` cho chú thích ngắn đã được tác tử góc nhìn sinh viên xác nhận là đọc được.
- Mỗi gạch đầu dòng không quá hai dòng ở khung 16:9. Chuyển diễn giải dài sang ghi chú diễn giả.
- Công thức, giả mã và hình trung tâm phải đủ lớn, có khoảng trắng và không bị cắt.
- Mọi lời mời tương tác trên mặt trang chiếu dùng nhãn **“Câu hỏi:”**.
- Không hiển thị mã nội bộ, nhãn quy trình, phân tuyến hoặc thời lượng trên mặt trang chiếu hay trong ghi chú diễn giả.
- Mỗi trang nội dung có `<aside class="notes">` khi cần giải thích giả thiết, lập luận đúng, lỗi dễ mắc, chuyển ý, đáp án hoặc nguồn.
- Ghi chú diễn giả viết thành mạch nói ngắn bằng tiếng Việt; không chỉ chứa siêu dữ liệu và không lặp nguyên văn nội dung hiển thị.
- Bộ trang chiếu phải dùng được bằng bàn phím, có tương phản đủ và không dùng màu làm tín hiệu duy nhất.

## Quy trình đa tác tử

### 1. Điều phối và lập kế hoạch

Điều phối viên kiểm kê nguồn, xác nhận đầu ra và mở dự án bền vững trong Codex Slides. Giao một tác tử lập kế hoạch riêng trước khi phân tích chi tiết hoặc sửa tệp.

Tác tử lập kế hoạch:

- xác định mục tiêu, phạm vi, đối tượng, thời lượng và tiêu chí hoàn thành;
- lập danh mục khái niệm và thuật toán trọng tâm cùng bản đồ chu trình học tập;
- chia việc thành kiểm kê, ánh xạ, soạn, rà soát, chỉnh sửa và kiểm định;
- xác định việc tuần tự, việc có thể chạy song song, đầu vào và đầu ra của từng tác tử;
- nêu rủi ro về thiếu nguồn, hình khó vẽ lại, ký hiệu, chứng minh, quá tải, tràn trang và mã trình diễn;
- không sửa tệp trang chiếu.

Điều phối viên phải kiểm tra và chấp nhận kế hoạch trước khi triển khai.

### 2. Phân tích nguồn và ánh xạ

Giao một tác tử chỉ đọc:

- lập bảng ánh xạ từng trang nguồn sang trang đích;
- ghi quyết định `giữ`, `sửa`, `gộp`, `tách`, `thêm` hoặc `bỏ`;
- trích mục tiêu, định nghĩa, định lý, chứng minh, thuật toán, ví dụ, bài tập, mã và nguồn;
- kiểm kê từng hình và cách vẽ lại thành SVG;
- chỉ ra thiếu giả thiết, sai số, mâu thuẫn, ký hiệu không nhất quán và đoạn khó đọc;
- bàn giao đặc tả cho tác tử soạn, không sửa tệp.

### 3. Soạn và triển khai

Giao một tác tử soạn:

- tạo `outline.md`, `storyboard.md`, HTML và SVG theo đặc tả;
- dịch và biên tập bằng tiếng Việt theo `$no-ai-slop`;
- dùng `$quill` để kiểm tra mạch phần, chuyển ý, thuật ngữ và ký hiệu;
- giữ thứ tự nguồn trừ các thay đổi đã được phê duyệt;
- thêm ghi chú diễn giả và nguồn;
- không sửa RevealJS, tiện ích hoặc CSS dùng chung nếu có thể giải quyết trong tệp bài giảng;
- nếu cần sửa `lecture-style.css`, phải kiểm tra các bài hiện có không bị hỏng.

### 4. Kiểm định storyboard

Giao một tác tử chỉ đọc rà từng trang và từng cụm khái niệm:

- kiểm tra lý do tồn tại của từng trang có cụ thể và kiểm chứng được;
- kiểm tra trang tạo một bước tiến trong lập luận hoặc luyện tập;
- kiểm tra chu trình học tập đúng thứ tự và nối được từ ví dụ sang hình thức, thuật toán và chứng minh;
- phát hiện trang trùng ý, trang trang trí, trang quá tải và khoảng trống cần bổ sung;
- kiểm tra thời lượng 120 phút, kiến thức tiên quyết và quan hệ trước–sau;
- đề xuất quyết định, bằng chứng và tác động đến trang lân cận;
- không sửa tệp.

Sau thay đổi số lượng hoặc thứ tự, phải rà lại các trang bị ảnh hưởng và hai trang lân cận mỗi phía.

### 5. Bốn tác tử rà soát độc lập

Sau bản nháp đầu, chạy song song bốn tác tử chỉ đọc. Mỗi báo cáo dùng các trường `mức độ`, `trang chiếu`, `vấn đề`, `bằng chứng`, `đề xuất sửa`.

- **Góc nhìn sinh viên:** kiểm tra tiên quyết, tải nhận thức, nhịp giảng, khả năng đọc, ví dụ chạy tay, chuyển ý, câu hỏi kiểm tra và khả năng tự học.
- **Chuyên gia giải thuật và khoa học dữ liệu:** kiểm tra độ bao phủ, chiều sâu, thuật ngữ, mạch học thuật, sự phù hợp với học phần và thời lượng 120 phút.
- **Độ chính xác toán học và thuật toán:** kiểm tra đặc tả, giả thiết, chỉ số, trường hợp biên, giả mã, bất biến, chứng minh, hệ thức truy hồi, kết quả số và độ phức tạp.
- **Phản biện học thuật và giảng dạy:** kiểm tra mỗi hình thức hóa có đủ trực giác, ví dụ và tiên quyết; mỗi thuật toán và chứng minh xuất hiện đúng chỗ; thứ tự hiện tại có hỗ trợ suy luận trên lớp hay không. Tác tử này phải nêu rõ khi một công thức hoặc thuật toán đúng riêng lẻ nhưng được đặt sai trình tự hoặc thiếu cầu nối sư phạm.

Mức độ gồm `chặn bàn giao`, `nghiêm trọng`, `trung bình`, `nhẹ`. Mọi lỗi `chặn bàn giao` và `nghiêm trọng` phải được xử lý.

### 6. Chỉnh sửa

Giao một tác tử chỉnh sửa riêng sau khi bốn báo cáo hoàn tất:

- hợp nhất vấn đề trùng lặp và ưu tiên tính đúng, khả năng học, khả năng đọc;
- sửa tuần tự HTML, SVG, outline, storyboard và ghi chú;
- ghi quyết định đối với đề xuất không áp dụng;
- không thay đổi mạch nguồn nếu lỗi có thể sửa cục bộ;
- yêu cầu rà lại độ chính xác cho mọi chứng minh, phân tích độ phức tạp hoặc thuật toán đã đổi đáng kể.

Các tác tử sửa tệp không được chạy song song.

### 7. Kiểm định cuối

Điều phối viên hoặc tác tử kiểm thử riêng phải:

- đối chiếu số trang nguồn, bảng ánh xạ, `data-slide-id` và mục tương ứng trong storyboard;
- kiểm tra HTML, cấu trúc `<section>`, KaTeX, tiện ích, ghi chú diễn giả, đường dẫn, SVG và liên kết;
- tìm mọi tham chiếu ảnh raster; chỉ chấp nhận mục có ngoại lệ đã được người dùng duyệt và ghi trong nhật ký;
- kiểm tra không có tài nguyên hỏng hoặc phụ thuộc mạng cốt lõi;
- chạy `python3 -m reloadserver 8765` tại thư mục gốc; cổng là đối số vị trí, không dùng `--port`;
- mở `http://localhost:8765/2627-1/lecture-NN-<ten-bai>.html` và duyệt mọi trang ngang, trang dọc;
- kiểm tra tràn chữ, chữ nhỏ, chồng lấn, công thức, giả mã, hình, tương phản và bàn phím ở khung 16:9 và một màn hình hẹp;
- dùng Codex Slides để rà soát trực quan sau cùng và xác minh thay đổi hiển thị đúng;
- chạy lại kiểm định sau mỗi lần sửa lỗi chặn bàn giao hoặc nghiêm trọng.

Nếu Codex Slides không khả dụng, phải báo rõ giới hạn, tiếp tục đầy đủ các kiểm tra RevealJS cục bộ và không tuyên bố đã rà bằng Codex Slides.

## Cập nhật `index.html`

- `2627-1/index.html` là danh mục riêng của học phần **Giải thuật nền tảng của Khoa học dữ liệu** cho học kỳ 1 năm học 2026–2027.
- Mỗi bài hoàn thành có một thẻ theo thứ tự số bài, gồm tên bài, mô tả một câu và liên kết duy nhất đến tệp HTML của bài giảng.
- Không đặt liên kết đến `outline.md`, `storyboard.md`, `review-log.md`, `note-for-author.md` hoặc thư mục `planning/` trên trang chỉ mục. Các tệp quy trình chỉ dùng nội bộ trong kho.
- Không thêm bài chưa hoàn thành hoặc liên kết đến tệp chưa tồn tại.
- Giữ giao diện của trang chỉ mục hiện có trừ nội dung nhận diện học phần và danh sách bài.

## Commit và đẩy lên kho từ xa

Mỗi bộ trang chiếu chỉ được coi là hoàn tất sau khi đã vượt toàn bộ tiêu chí kiểm định, được commit và đẩy lên `origin`.

- Trước khi commit, chạy `git status --short` và kiểm tra diff. Không đưa tệp tạm, `.DS_Store`, tệp có tiền tố `._`, bí mật, thông tin xác thực hoặc tài sản ngoài phạm vi bài vào commit.
- Commit phải chứa trọn bộ đầu ra của bài: HTML, SVG, ba tệp quy trình và thay đổi tương ứng trong `2627-1/index.html`. Chỉ kèm thay đổi ở tệp dùng chung hoặc nguồn khi chúng thực sự thuộc cùng công việc và đã được kiểm tra.
- Không gộp thay đổi chưa hoàn tất của bài khác. Không sửa, xóa hoặc hoàn tác thay đổi của người dùng để làm sạch commit.
- Dùng thông điệp commit dạng `feat(lecture-NN): add <ten-bai> slide deck` cho bài mới hoặc `fix(lecture-NN): revise <ten-bai> slide deck` cho lần sửa đáng kể.
- Sau commit, đẩy nhánh `main` bằng `git push origin main`; ở lần đẩy đầu có thể dùng `git push -u origin main`.
- Không dùng `--force`, `--force-with-lease`, rebase hoặc viết lại lịch sử từ xa nếu người dùng không yêu cầu rõ.
- Nếu push thất bại do xác thực, mạng hoặc lịch sử từ xa thay đổi, giữ nguyên commit cục bộ, ghi lại lỗi và báo người dùng. Không tuyên bố đã bàn giao hoàn tất khi commit chưa xuất hiện trên `origin`.

## Tiêu chí hoàn thành

Chỉ bàn giao khi:

- bản RevealJS giữ đúng ý chính và mạch nguồn, còn mọi sai khác đều được ghi;
- nội dung chính bằng tiếng Việt, ngắn, trực tiếp và đã qua `$no-ai-slop`;
- outline, storyboard và nhật ký nằm đúng `planning/lec-NN/`;
- mọi hình đã được vẽ lại thành SVG hoặc có ngoại lệ raster được người dùng duyệt;
- bốn báo cáo độc lập đã có và mọi lỗi bắt buộc đã được xử lý;
- đặc tả, ví dụ chạy tay, giả mã, chứng minh, trường hợp biên và độ phức tạp đã được kiểm tra;
- bộ trang chiếu chạy tại cổng `8765`, không có lỗi hiển thị hoặc tài nguyên hỏng nghiêm trọng;
- `index.html` liên kết đúng tới tệp HTML của bài và không liên kết tới các tệp quy trình;
- nội dung trong kho khớp với bản đã rà trong Codex Slides, hoặc giới hạn công cụ đã được ghi rõ.
- commit của bài đã được đẩy thành công lên nhánh `main` của `origin`.

Khi bàn giao, nêu ngắn gọn: tệp trang chiếu, URL cục bộ, tệp nguồn, hình đã vẽ lại, các kiểm tra đã chạy, sai khác có chủ ý, ngoại lệ và giới hạn còn lại.
