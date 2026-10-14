# Quy trình xây dựng bài giảng và ghi chú bài giảng Giải thuật nền tảng của Khoa học dữ liệu

## Phạm vi

Tệp này áp dụng cho mọi yêu cầu chọn tài liệu trong `sources/` để tạo, sửa hoặc rà soát bộ trang chiếu RevealJS, ghi chú bài giảng và tài liệu học tập công khai của học phần **Giải thuật nền tảng của Khoa học dữ liệu**, học kỳ 1 năm học 2026–2027.

`sources/source.md` là bản đồ nguồn cấp học phần. Tệp này chứa bản trích xuất đề cương, thứ tự bài học đề xuất, ánh xạ từ buổi gốc, chuẩn đầu ra, kiến thức tiên quyết, học liệu và các điểm cần xác minh. Mọi yêu cầu làm một bài phải đọc `sources/source.md` trước khi chọn và phân tích tài liệu chi tiết. Mặc định dùng thứ tự đề xuất trong tệp này; chỉ dùng thứ tự gốc khi người dùng yêu cầu rõ.

`sources/reference-slides/README.md` là bảng ánh xạ slide tham khảo cho 15 buổi đề xuất. Sau khi xác định bài từ `sources/source.md`, phải đọc dòng tương ứng trong bảng này và các tệp cục bộ được chỉ định. Trạng thái “đủ có điều kiện” là một khoảng trống nguồn phải xử lý trước khi hoàn tất deck, không phải giấy phép tự bổ sung mệnh đề.

[slide_authoring_standard.md](slide_authoring_standard.md) là tiêu chuẩn bắt buộc về cách xây dựng kiến thức và thể hiện nội dung cho sinh viên năm 2. Với mọi yêu cầu tạo, viết lại, sửa hoặc rà soát slide, phải đọc tiêu chuẩn này trước khi lập storyboard hoặc sửa nội dung. Áp dụng sáu nhóm yêu cầu: đối tượng, mục đích và mạch của từng slide, thuật toán, ví dụ, đánh giá chi phí và trực quan hóa. Dùng các mục “Điều kiện đạt” cùng phiếu kiểm tra cuối tài liệu để rà bản soạn; ghi bằng chứng, sai khác và quyết định xử lý trong `review-log.md`.

Từ 2026-10-14, cách trình bày của học phần được căn chỉnh theo yêu cầu người dùng với hai học phần cùng tác giả `../math-4-AI` và `../rl-plan` (các tệp `AGENTS.md`, `CLAUDE.md`, trang tiêu đề mạch, chuẩn mật độ và chuẩn giáo trình cho ghi chú), với bộ trang chiếu MAT1101 của tác giả tại `../MAT1101/` cho mặt trang chiếu, và với giáo trình *Học máy thống kê* của tác giả tại `../SML-textbook-main.zip` cho ghi chú bài giảng. Ba nguồn này chỉ là mẫu văn phong, cách dẫn dắt và cách đặt vấn đề; chúng không cung cấp nội dung, số liệu hay thứ tự chủ đề. Các mục "Trang tiêu đề mạch", "Văn phong và mật độ mặt trang chiếu" và "Tiêu chuẩn giáo trình cho ghi chú bài giảng" dưới đây ghi kết quả của đợt căn chỉnh đó.

Một yêu cầu làm trọn bài phải tạo hoặc cập nhật:

- `2627-1/lecture-NN-<ten-bai>.html`;
- `2627-1/materials/lec-NN/lecture-note.md`;
- các hình SVG trong `2627-1/img/lec-NN/`;
- ba tệp quy trình trong `2627-1/planning/lec-NN/`;
- mục tương ứng trong `2627-1/index.html`.

Nếu người dùng chỉ yêu cầu ghi chú bài giảng, không tự viết lại bộ trang chiếu. Khi đó phải tạo hoặc cập nhật `lecture-note.md`, các SVG mà ghi chú thực sự cần, ba tệp quy trình ở phần liên quan và mục tài nguyên của bài trong `index.html`. Nếu thay đổi ký hiệu, giả thiết, ví dụ, kết luận hoặc thứ tự khái niệm dùng chung, phải rà lại bộ trang chiếu cùng bài và ghi tác động trong `review-log.md`.

`NN` lấy theo số bài trong bảng **Thứ tự đề xuất** của `sources/source.md` và luôn có hai chữ số. Ví dụ, bài 1 dùng `lecture-01-<ten-bai>.html`. Tên bài, phạm vi và học liệu phải đối chiếu với mục tương ứng trong `sources/source.md`. Nếu người dùng yêu cầu theo thứ tự gốc, ghi rõ ngoại lệ trong storyboard và nhật ký rà soát.

Điều phối viên phải dùng nhiều tác tử theo quy trình dưới đây. Không giao toàn bộ việc lập kế hoạch, phân tích, soạn, rà soát và chỉnh sửa cho một tác tử.

## Đối tượng và thời lượng

- Đối tượng mặc định là sinh viên năm 2 đã học lập trình, toán rời rạc, đại số tuyến tính và xác suất cơ bản. Kiểm tra tiên quyết theo từng bài; không mặc định đã học cơ sở dữ liệu, hệ phân tán hoặc framework chuyên dụng nếu đề cương chưa xác nhận.
- Mỗi bộ trang chiếu gồm phần giảng được thiết kế cho 120 phút và phần bài tập đủ cho 60 phút recitation, tổng cộng 180 phút học liệu.
- Phần bài tập phải nằm trong cùng tệp HTML, tách thành một phần dọc riêng sau phần giảng. Bài tập phải có dữ kiện, yêu cầu, sản phẩm cần nộp hoặc trình bày, và lời giải hay hướng dẫn chấm trong ghi chú diễn giả. Tổng thời lượng dự kiến của các bài phải đạt 60 phút; ghi thời lượng trong storyboard và ghi chú, không hiển thị thời lượng trên mặt trang chiếu.
- Bài tập recitation phải lấy trực tiếp từ giáo trình hoặc tài liệu nguồn đã được chỉ định cho bài. Ghi số bài, mục và trang nguồn trong storyboard cùng ghi chú diễn giả. Có thể dịch sang tiếng Việt, chia thành các bước nhỏ hoặc lược phần ngoài phạm vi, nhưng không tự đặt dữ kiện, đổi yêu cầu toán học hoặc tạo bài mới. Mọi điều chỉnh phải được ghi trong storyboard và `review-log.md`.
- Chỉ chuyển hoặc chuẩn bị mã trình diễn khi nguồn có nội dung tương ứng. Không tự tạo sổ tay mã hoặc chương trình ngoài phạm vi nguồn nếu người dùng không yêu cầu.

## Ngôn ngữ và biên tập

- Viết thuần Việt. Chỉ giữ tiếng Anh cho tên riêng, tên phần mềm, ký hiệu chuẩn, tên thuật toán hoặc thuật ngữ chưa có cách dịch ổn định.
- Mọi tiêu đề trang chiếu, tiêu đề phần và nhãn bố cục phải viết thuần Việt. Chỉ dùng tiếng Anh trong tiêu đề khi đó là tên riêng, tên thuật toán hoặc thuật ngữ chưa có cách dịch ổn định, hoặc khi cần giữ nguyên công thức và ký hiệu chuẩn. Nếu cần giải thích thuật ngữ tiếng Anh, đặt sau thuật ngữ tiếng Việt và không dùng tiếng Anh thay cho một tiêu đề tiếng Việt đã rõ nghĩa.
- Khi dùng viết tắt lần đầu, viết đầy đủ bằng tiếng Việt rồi đặt dạng viết tắt trong ngoặc.
- Tiêu đề, nội dung trang chiếu, nhãn hình và bảng, ghi chú diễn giả, ghi chú bài giảng và lời giải phải dùng văn phong trang trọng, học thuật. Viết trực tiếp, chính xác; ưu tiên câu ngắn, động từ rõ và thuật ngữ nhất quán.
- Không dùng văn nói mô phỏng, lời trò chuyện hoặc lời chỉ dẫn giảng viên, người soạn trong học liệu và ghi chú diễn giả, chẳng hạn “chúng ta hãy nhìn”, “nhấn mạnh với sinh viên”, “đến đây chuyển sang trang sau”, “người viết cần bổ sung hình”. Diễn đạt bằng đối tượng, giả thiết, phép suy luận và kết luận.
- Chỉ dẫn biên soạn, chọn bố cục, điều phối lớp và việc còn phải làm chỉ nằm trong `outline.md`, `storyboard.md` hoặc `review-log.md`. Không đưa chúng lên mặt trang chiếu, nhãn SVG, chú thích, ghi chú diễn giả hoặc ghi chú bài giảng. Các yêu cầu dành cho người học như “Tính”, “Xác định”, “Chứng minh”, các bước thuật toán và thao tác thực hành vẫn được dùng khi đúng chức năng.
- Không dùng câu hỏi tu từ, câu cảm thán, lời ca tụng, khẩu hiệu hoặc cách diễn đạt quảng bá.
- Không thêm nhận định, số liệu, nguồn hoặc ví dụ không có căn cứ.
- Trong mọi tệp Markdown, chỉ dùng `$...$` cho công thức nội dòng và `$$...$$` cho công thức khối.
- Trong ghi chú bài giảng, được phép mở một mục bằng câu hỏi nghiên cứu thật mà mục đó trả lời ngay sau ("Xác suất bỏ sót một cặp đạt ngưỡng là bao nhiêu? Định lý sau cho biết…"); câu hỏi không có câu trả lời trong cùng mục là câu hỏi tu từ và bị cấm. Trên mặt trang chiếu, câu hỏi chỉ xuất hiện sau nhãn "Câu hỏi:".
- **Giọng kể của ghi chú bài giảng** (theo giáo trình *Học máy thống kê* của tác giả, bản nguồn tại `../SML-textbook-main.zip`, các chương có thuật toán `chapters/01_classification/`, `07_ensemble_learning/`, `09_features/`): ghi chú được viết bằng giọng kể đi cùng người đọc. Dùng "chúng ta" cho câu nêu kế hoạch, nhu cầu, lựa chọn phương pháp và giới hạn ("Để tránh so mọi cặp, chúng ta gom các cột giống nhau vào cùng thùng"); dùng "ta" trong tính toán ("Thế vào (2.3), ta được…", "Như vậy, ta vừa chứng minh…"); "người ta" chỉ dùng cho thực hành chung của cộng đồng, không cho lập luận của bài. Chủ ngữ của câu dẫn dắt là người viết cùng người đọc hoặc chính đối tượng toán học, không phải tài liệu ("Mục này định nghĩa…", "Phần này giới thiệu…" bị cấm). Bên trong khối định nghĩa, định lý, mệnh đề, bổ đề, hệ quả, thuật toán giữ câu khách quan. Vẫn cấm mệnh lệnh dẫn dắt ("hãy", trừ đề bài tập), câu hỏi tu từ, lời giảng viên, lời khen và câu dẫn rỗng. Mặt trang chiếu và ghi chú diễn giả không dùng "chúng ta".
- **Thuật ngữ và định nghĩa trước khi dùng:** thuật ngữ tiếng Anh đặt trong ngoặc ở lần xuất hiện đầu tiên của mỗi tài liệu ("họ nhạy cảm theo tính cục bộ (locality-sensitive family)"); khi một khái niệm có hai cách gọi, viết "X (còn gọi là Y)" ở lần đầu rồi chỉ dùng X. Mọi ký hiệu, giả thiết hoặc kết quả được dùng trên một trang chiếu hoặc trong một mục phải được định nghĩa hoặc nhắc lại trước lần dùng đầu, bằng dòng "Nhắc lại:" hoặc một trang nhắc lại riêng khi kết quả đến từ bài trước; không dựa vào trí nhớ của người đọc. Dùng "Lời giải" cho lời giải bài tập, không dùng "Đáp án". Bảng thuật ngữ Việt–Anh của bài nằm trong `outline.md` và phải thống nhất với các bài đã có.
- Bắt buộc dùng kỹ năng `no-ai-slop` khi soạn, sửa hoặc rà tiêu đề, nội dung hiển thị, ghi chú diễn giả và ghi chú bài giảng; nạp kỹ năng bằng công cụ `Skill` hoặc đọc `SKILL.md` trước khi áp dụng. Tác tử soạn hoặc chỉnh sửa dùng chế độ Edit, tự kiểm theo `no-ai-slop/eval.md` và sửa các mục chưa đạt trước khi bàn giao. Tác tử chỉ đọc dùng chế độ Detect, trích đoạn có vấn đề và đề xuất sửa. Ghi phạm vi cùng kết quả trong `review-log.md`; không dùng điểm từ bộ phát hiện AI hoặc suy đoán tác giả làm bằng chứng.
- Khi áp dụng `no-ai-slop`, giữ nguyên giả thiết, ký hiệu, nguồn, phép suy luận và các phân biệt toán học, thuật toán cần thiết. Văn phong học thuật của học phần được ưu tiên hơn các gợi ý giữ giọng nói, hài hước hoặc câu rời. Cắt lời dẫn rỗng, câu lặp, diễn đạt phô trương và nhịp câu máy móc; giữ định nghĩa, câu hỏi đánh giá và phần tổng kết có chức năng học tập rõ.
- Dùng kỹ năng `quill` (nạp bằng công cụ `Skill`) để rà dàn ý, thứ tự khái niệm, thuật ngữ, ký hiệu và tính liên tục giữa các phần. Không khởi tạo `quill.json`; công việc này không phải dự án sách.

## Thứ tự ưu tiên

Khi có xung đột, tuân theo thứ tự sau:

1. Chỉ dẫn cụ thể của người dùng cho bài đang làm.
2. `sources/source.md` về số bài, tên bài, thứ tự, phạm vi, chuẩn đầu ra, kiến thức tiên quyết và học liệu cần dùng.
3. Bộ trang chiếu hoặc tài liệu chi tiết được chọn trong `sources/` về nội dung, ví dụ, chứng minh, thuật toán, hình và mã của bài.
4. Tài liệu bổ sung và tài sản liên quan do người dùng cung cấp.
5. Mẫu văn phong, dẫn dắt và cách đặt vấn đề của tác giả: các trang chiếu MAT1101 tại `../MAT1101/` cho mặt trang chiếu, giáo trình *Học máy thống kê* tại `../SML-textbook-main.zip` cho ghi chú bài giảng, cùng cách các học phần `../math-4-AI` và `../rl-plan` đã áp dụng hai mẫu đó. Ba nguồn này chỉ làm mẫu cách trình bày; không lấy nội dung, số liệu hay thứ tự chủ đề từ chúng thay cho nguồn ở mục 2 và 3.
6. `slide_authoring_standard.md` về mức độ cho sinh viên năm 2, mạch xây dựng kiến thức và cách thể hiện nội dung slide.
7. `2627-1/lecture-template.html` và `2627-1/lecture-style.css` về giao diện và nền kỹ thuật.
8. Các quy ước trong tệp này.

Giữ mạch cấp học phần theo `sources/source.md`; giữ mạch và ý chính trong từng bài theo tài liệu chi tiết. Chỉ gộp, tách, thêm, lược hoặc sắp xếp cục bộ khi cần sửa lỗi, giảm quá tải, khôi phục tiên quyết, hoàn thiện mạch học tập hoặc bảo đảm khả năng đọc. Mọi sai khác phải có lý do trong storyboard và nhật ký rà soát.

Với bài neo theo *Mining of Massive Datasets* (MMDS), phải kiểm tra cả slide chính thức trên `http://www.mmds.org` và slide Stanford CS246 được ánh xạ cho bài. So sánh theo từng cụm nội dung dựa trên: mức khớp chuẩn đầu ra, độ chính xác và tính hiện thời, chất lượng ví dụ hoặc hình, và khả năng Việt hóa. Nếu hai nguồn tương đương, ưu tiên MMDS; nếu Stanford phù hợp hơn cho một cụm, được dùng Stanford và phải ghi lý do trong storyboard cùng nhật ký. Việt hóa tiêu đề, nội dung, ví dụ và nhãn hình; dùng sách MMDS để kiểm chứng và lấy bài tập. Vẽ lại theo giao diện của học phần; không sao chép CSS, phông chữ, ảnh raster hay tệp nhị phân của MMDS hoặc Stanford vào đầu ra Git. Khi dùng phần đáng kể của slide MMDS, ghi công bằng liên kết `http://www.mmds.org` theo yêu cầu của tác giả.

## Tiếp nhận và kiểm kê

Sau khi người dùng chọn bài học hoặc tệp nguồn, điều phối viên phải:

- đọc `sources/source.md`, xác định bài theo thứ tự đề xuất và trích mục tiêu, tiên quyết, phạm vi, học liệu, ánh xạ buổi gốc cùng các điểm cần xác minh;
- đọc dòng tương ứng trong `sources/reference-slides/README.md`, kiểm tra trạng thái đầy đủ và mở toàn bộ slide cục bộ được ánh xạ cho bài;
- từ mục học liệu của bài, xác định tài liệu chi tiết cần dùng, đọc các tệp tương ứng và kiểm tra tài liệu liên quan trong `sources/`;
- bỏ qua `.DS_Store`, tệp có tiền tố `._` và tệp tạm có tiền tố `~$`;
- xác định số bài, tên bài, mục tiêu, kiến thức tiên quyết và phạm vi từ `sources/source.md`; xác định số trang, phần hoặc chương nguồn và các tài sản từ tài liệu chi tiết;
- đọc `slide_authoring_standard.md`, `2627-1/lecture-template.html`, `2627-1/lecture-style.css` và `2627-1/index.html` trước khi lập kế hoạch;
- kiểm kê định nghĩa, định lý, bổ đề, chứng minh, thuật toán, cấu trúc dữ liệu, ví dụ, bài tập, hình, bảng, công thức và đoạn mã phải chuyển;
- xác định phần nào của nguồn là nội dung, bố cục, ghi chú, tài liệu tham khảo hoặc tài sản trực quan;
- chỉ hỏi người dùng về thông tin không thể suy ra từ kho và có thể làm thay đổi đáng kể kết quả.

Nếu người dùng đã nêu số bài hoặc tên bài, dùng `sources/source.md` để xác định các nguồn cần kiểm tra; không yêu cầu lại tên tệp khi ánh xạ đã rõ. Nếu tài liệu được chỉ định trong `sources/source.md` chưa có trong kho, dừng sau bước kiểm kê và yêu cầu người dùng bổ sung hoặc chọn tài liệu thay thế. Nếu người dùng chưa chọn cả bài lẫn tệp nguồn, dừng sau bước kiểm kê danh mục và yêu cầu số bài, tên bài hoặc tên tệp. Không tự chọn bài thay người dùng và không tự bổ sung nội dung thay cho tài liệu còn thiếu.

## Tổ chức tệp

Mỗi bài dùng cấu trúc sau:

```text
2627-1/
├── lecture-NN-<ten-bai>.html
├── materials/
│   └── lec-NN/
│       └── lecture-note.md
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
- `lecture-note.md` là tài liệu tự học công khai, mở rộng lập luận, ví dụ, chứng minh và thuật toán của bài. Không sao chép nguyên văn trang chiếu hoặc ghi chú diễn giả.
- Tệp HTML nằm trực tiếp trong `2627-1/`. Không đặt tệp HTML trong thư mục `planning/` hoặc `img/`.
- Mọi đường dẫn trong HTML phải tương đối và hợp lệ khi máy chủ được mở tại thư mục gốc của kho.

## Ghi chú bài giảng và trình đọc web tĩnh

- Dùng mô hình phát hành của `../math-4-AI/2627-1/`: Markdown là nguồn; `2627-1/material-viewer.html` tải và hiển thị tài liệu. Chỉ kế thừa cấu trúc, hành vi và quy tắc an toàn; không sao chép tên học phần, nội dung, ví dụ hoặc tài sản môn học.
- Trước khi công bố ghi chú đầu tiên, phải có và kiểm định cục bộ `material-viewer.html`, `material-viewer.css`, `material-viewer.js`, `material-index.css`, mẫu trong `materials/_templates/` và các thư viện cục bộ cần thiết. Không dùng CDN hay bước build cho thành phần cốt lõi.
- URL ghi chú dùng đúng dạng `material-viewer.html?doc=materials/lec-NN/lecture-note.md&deck=lecture-NN-<ten-bai>.html`. Viewer chỉ chấp nhận đường dẫn trong `materials/lec-NN/`, buộc số bài của `doc` và `deck` trùng nhau, làm sạch HTML trước khi đưa vào DOM và render công thức bằng KaTeX cục bộ.
- Mỗi tệp bắt đầu bằng heading cấp một; chỉ dùng `$...$` và `$$...$$` cho công thức. Hình dùng đường dẫn `img/lec-NN/<ten-tep>`, có văn bản thay thế cụ thể; bảng có hàng tiêu đề; mã có ngôn ngữ khi xác định được.
- Viewer hỗ trợ mười bốn loại khối không lồng nhau theo cú pháp `::: <loại> Tiêu đề tùy chọn` … `:::`: `definition`, `theorem`, `proposition`, `lemma`, `corollary`, `remark`, `algorithm`, `example`, `application`, `derivation`, `proof`, `exercise`, `hint` và `solution`. Tiêu đề thay cho nhãn mặc định của loại khối và là nơi đặt số hiệu (`::: theorem Định lý 06.2 (Xác suất thành ứng viên)`). Danh sách loại khối và nhãn tiếng Việt nằm ở một chỗ duy nhất, hằng `DIRECTIVE_LABELS` trong `material-viewer.js`. `proof`, `hint` và `solution` gập mặc định, dùng được bằng bàn phím và mở khi in; các khối còn lại luôn mở. Chú thích `<!-- note-topic-id: lec-NN-topic-k -->` trước tiêu đề mục được viewer kiểm tra (đúng quy ước, không lặp) rồi ẩn.
- Ghi chú phải đọc độc lập với trang chiếu nhưng dùng cùng thuật ngữ, ký hiệu, giả thiết và thứ tự khái niệm. Dẫn liên kết về bộ trang chiếu; không giả định người học đã đọc ghi chú diễn giả.
- Chỉ công bố liên kết sau khi Markdown, công thức, hình, nguồn, liên kết, bàn phím, màn hình rộng, màn hình hẹp và bản in đã được kiểm tra.

## Mẫu RevealJS bắt buộc

- Dùng `2627-1/lecture-template.html` làm nền. Chỉ kế thừa cấu trúc, giao diện và cấu hình kỹ thuật; không sao chép chủ đề, nội dung hoặc siêu dữ liệu của bài khác.
- Dùng `2627-1/lecture-style.css`, màu, phông chữ, khoảng cách, thẻ, lưới và chân trang hiện có. Không tạo hệ giao diện mới.
- `2627-1/lecture-style.css` là nguồn duy nhất cho các kiểu trình bày dùng lại giữa các bài: trang tiêu đề, tên môn/học kỳ, mục lục, tiêu đề phần/trang, chữ thân bài, bảng, mã, chú thích, nguồn và badge. Lecture 02 là mẫu đối chiếu ban đầu; Lecture 02, Lecture 03 và các deck được soạn hoặc chỉnh sửa sau này phải liên kết tới CSS này và dùng cùng lớp cho các thành phần cùng vai trò.
- Trước khi thêm kiểu trình bày, kiểm tra lớp hiện có trong CSS chung và mẫu tương ứng ở Lecture 02. Nếu kiểu trong một deck cần dùng lại, chuyển định nghĩa vào CSS chung và cập nhật các deck sử dụng; không sao chép thành nhiều bản riêng. Đồng nhất giao diện phải bao gồm cỡ chữ, độ đậm, chiều cao dòng và khoảng cách của các thành phần tương ứng, không chỉ màu sắc.
- Không chép khối `<style>` hoặc tự đặt lại cỡ chữ, màu, khoảng cách của các thành phần tương ứng trong từng HTML. Khi cần kiểu mới, thêm hoặc mở rộng lớp có ý nghĩa trong CSS chung rồi dùng lớp đó; chỉ giữ kiểu nội dòng cho hình hoặc bố cục đơn lẻ khi thực sự cần, không dùng để ghi đè thang chữ chung.
- CSS riêng cho sơ đồ hoặc bố cục của một bài vẫn đặt trong `lecture-style.css`, giới hạn bằng lớp gốc của bài (ví dụ `.lecture-pagerank`); không để selector chung như `.card`, `h2`, `p` làm đổi các bài khác. Những bài dùng hệ thành phần chung nhận lớp `.course-deck`.
- Khi sửa CSS chung, đối chiếu cỡ chữ và khoảng cách thực tế của các thành phần cùng vai trò; kiểm tra tất cả deck bị ảnh hưởng, ít nhất Lecture 02 và Lecture 03. Kiểm cả tiêu đề, mục lục, nội dung, bảng/mã, tràn khung, công thức và hình; không chỉ kiểm deck đang sửa. Ghi phạm vi ảnh hưởng và kết quả vào `review-log.md`.

- Tham khảo cách tổ chức bố cục trong kho `uet-iai-course/machine-learning`, ưu tiên `SLIDE_STYLE_GUIDE.md` và các tệp `2526-2/lecture-*.html`. Áp dụng nguyên tắc một luận điểm trung tâm, hình hoặc công thức đủ lớn, chú thích nêu kết luận và nhịp mở phần–trực giác–cơ chế–ví dụ–kiểm tra. Không sao chép nội dung, tài sản hoặc CSS từ kho tham khảo.
- Giữ `lang="vi"`, khung `1280 × 720`, `controlsLayout: "edges"`, `slideNumber: true`, `hashOneBasedIndex: true` và `hash: true`.
- Dùng các thư viện cục bộ trong `2627-1/`: RevealJS, `RevealMath.KaTeX`, `RevealNotes` và `RevealHighlight`.
- Dùng `<section>` ngoài cho từng phần và `<section>` trong cho từng trang chiếu.
- Toàn bộ bài dùng từ 5 đến 7 mạch trình bày lớn, mỗi mạch tương ứng với một `<section>` ngoài; số này gồm mạch mở đầu và mạch kết luận. Chỉ dùng ngoài khoảng 5–7 khi nguồn hoặc yêu cầu cụ thể của người dùng đòi hỏi, và phải ghi lý do cùng ảnh hưởng đến mạch bài trong `storyboard.md` và `review-log.md`.
- Mạch mở đầu gồm, theo thứ tự: trang bìa (tên bài, tên học phần, học kỳ, đơn vị và **một câu luận đề** của bài: một câu trần thuật nêu kết quả hoặc cơ chế trung tâm, chẳng hạn "Chỉ xác minh các cặp cùng thùng; đổi lại, cặp đạt ngưỡng có thể bị bỏ sót."); trang **Tiên quyết và quy ước** với dòng "Nhắc lại:" nêu các kết quả của bài trước được dùng lại và dòng "Ký hiệu:" nêu miền, kiểu, kích thước và quy ước chỉ số của bài; trang mục tiêu học tập quan sát được, mỗi mục tiêu ứng với một sản phẩm kiểm tra được; trang **Nội dung** liệt kê đánh số mọi mạch của bài, kể cả mạch mở đầu và mạch kết luận, số và tên trùng với trang tiêu đề mạch tương ứng, có thể thêm một dòng "Đọc trước:" ghi giáo trình, chương, mục (MAT1101 làm vậy ở trang "Sách"); trang **Vấn đề trung tâm** nêu bài toán dữ liệu lớn của bài trong một dòng (dữ liệu, đầu ra, giới hạn tài nguyên) và câu trả lời có điều kiện của từng mạch trong một dòng mỗi mạch, kèm hình khi có; có thể thay bằng một trang gộp "Nhắc lại: <kết quả bài trước>" + "Ví dụ. <trường hợp công cụ cũ còn giải được>" + "Nhu cầu: <giới hạn dẫn tới bài này>". Trang mục tiêu và trang Nội dung có thể gộp khi tổng không vượt trần 80 âm tiết. Mỗi mạch còn lại bắt đầu bằng một trang tiêu đề mạch theo mục "Trang tiêu đề mạch".
- Mạch kết luận cũng mở bằng trang tiêu đề mạch ("Tổng kết và chuyển tiếp" hoặc "Tổng kết và tự kiểm tra") và gồm: bảng tổng kết `Kết quả | Giả thiết không được bỏ | Công thức hoặc thuật toán`, mỗi kết quả chính của bài một hàng (MAT1101 kết bài bằng trang "Tóm tắt" liệt kê các công thức); khi bài có nhiều thuật toán, thêm bảng `Thuật toán | Đầu vào | Bảo đảm | Chi phí` dùng cùng mô hình chi phí; một trang trả lời vấn đề trung tâm bằng kết luận có điều kiện, nêu giả thiết nào cho phép thay phép duyệt mọi cặp, mọi bản ghi hay mọi khối bằng cấu trúc nào; trang **Câu hỏi tự kiểm tra** mở bằng "Câu hỏi: trả lời và nêu kết quả đã dùng." với hai đến bốn câu ngắn, mỗi câu kiểm một giả thiết hoặc một phân biệt, lời giải trong ghi chú diễn giả; trang **Nguồn và tài liệu đọc** ghi tác giả, năm, chương, mục và trang của nguồn đã dùng, ghi công `http://www.mmds.org` khi bài neo theo MMDS, và dòng liên kết "Ghi chú bài giảng" trỏ tới viewer; một dòng nối sang bài kế tiếp khi có căn cứ từ `sources/source.md`. Không đưa khái niệm mới vào mạch kết luận. Phần bài tập recitation vẫn là một `<section>` ngoài riêng sau mạch kết luận theo mục "Đối tượng và thời lượng", và cũng mở bằng trang tiêu đề mạch.
- Mỗi trang có `data-slide-id` duy nhất. Mã này chỉ xuất hiện trong HTML, outline, storyboard và nhật ký; không hiển thị trên mặt trang chiếu hoặc trong ghi chú diễn giả.
- Đặt chân trang ở cuối `.slides` và cập nhật đúng tên học phần, học kỳ và số bài.
- Không phụ thuộc mạng cho các thành phần cốt lõi.
- Chỉ dùng tài sản cốt lõi đã có trong `2627-1/` hoặc tài sản SVG được tạo cho bài đang làm. Không tải phông chữ, thư viện hoặc hình từ mạng.

### Trang tiêu đề mạch

Mỗi mạch, trừ mạch mở đầu, bắt đầu bằng một trang tiêu đề mạch (yêu cầu người dùng 2026-10-12 cho học phần Cơ sở toán học cho AI và Học tăng cường, áp dụng cho học phần này từ 2026-10-14 theo `../rl-plan`). Trang bìa là trang tiêu đề của mạch mở đầu; không thêm trang "Mở đầu" riêng. Trang tiêu đề mạch là `<section>` trong đầu tiên của `<section>` ngoài tương ứng, mang lớp `strand-title`, và gồm:

- số thứ tự của mạch viết bằng chữ số ("2.", "3.", …), trùng với số trên trang "Nội dung" và với chỉ số ngang của RevealJS (`hashOneBasedIndex: true` nên mạch 3 mở tại `#/3`);
- tên mạch là cụm danh từ gọi tên khái niệm, bài toán, thuật toán hay kết quả, không dạng câu hỏi, không kể tiến trình; tên không trùng tiêu đề của trang nội dung đầu tiên trong mạch;
- một dòng dẫn, tối đa 25 âm tiết, nêu nhu cầu hoặc nhiệm vụ mà mạch giải quyết, mở bằng "Muốn …" hoặc nhãn "Nhu cầu:", là câu trần thuật, không kết thúc bằng dấu hỏi; dạng thường dùng là "Muốn <đích của mạch>, (trước hết) phải <việc mạch làm>" ("Muốn chỉ xác minh một phần nhỏ các cặp, phải gom các cột giống nhau vào cùng thùng"; "Muốn dùng phân dải cho vector và chuỗi, phải nêu được độ đo và một họ băm hợp với độ đo ấy");
- tùy chọn một dòng từ khóa, tối đa năm cụm danh từ ngăn bằng " · ".

Cấu trúc HTML: khối `div.strand-title-body` chứa `<h2>` với số thứ tự trong `span.strand-number` đứng trước tên mạch, rồi `p.strand-lead` cho dòng dẫn và `p.strand-keys` cho dòng từ khóa. Kiểu của các lớp này nằm trong `lecture-style.css`, không viết lại theo bài.

Không đặt định nghĩa, công thức trung tâm, giả mã, hình hay bài tập trên trang tiêu đề mạch; không ghi "Mạch", "Phần", "Đầu vào", "Đầu ra" hay mã trang trên mặt trang. Ghi chú diễn giả của trang này dài khoảng 40–100 âm tiết và nêu: kết quả hoặc ký hiệu kế thừa từ mạch trước, nhiệm vụ của mạch, và kết quả mạch giao cho mạch sau. Trang tiêu đề mạch không tính là một mạch và không đổi số mạch của bài. Nếu dòng dẫn nêu đúng nhu cầu của khái niệm đầu tiên trong mạch, storyboard có thể ghi trang này là bước `vấn đề` của khái niệm đó; nếu không, ghi "ngoài chu trình khái niệm". Nhãn phần bằng chữ cái hoặc số nội bộ vẫn được dùng trong storyboard, dàn ý, học liệu và mã trang, nhưng không đặt trên mặt trang tiêu đề mạch.

Mã trang theo quy ước của bài, dạng `<tiền tố mạch>-00` (ví dụ `lec06-s02-00`); nếu mã này đã có, dùng `<tiền tố>-T` và ghi trong storyboard. Thuộc tính `id` của trang tiêu đề mạch là `mach-N`. Không đổi `id` của trang đã được học liệu liên kết tới. Các bộ trang chiếu đã phát hành trước quy định này được bổ sung trang tiêu đề mạch theo từng đợt sửa có nhật ký riêng; không sửa hàng loạt ngoài yêu cầu của người dùng.

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

Đối với bộ trang chiếu, mỗi khái niệm hoặc thuật toán trọng tâm đi theo chu trình:

**tình huống sử dụng dữ liệu lớn → vấn đề → trực giác → ví dụ chạy tay → hình thức hóa → thuật toán và lập luận đúng → ứng dụng và chi phí → kiểm tra**

- **Tình huống sử dụng dữ liệu lớn:** mở đầu bằng một trường hợp cụ thể cần thuật toán. Nêu loại dữ liệu, đầu ra hoặc quyết định cần tạo, giới hạn về bộ nhớ, I/O, băng thông, thời gian hoặc số lượt quét, và lý do cách trực tiếp không phù hợp. Dùng quy mô định lượng khi nguồn cung cấp; không bịa số liệu. Không dùng tình huống chỉ để trang trí hoặc không được dùng lại trong phần lập luận.
- **Vấn đề:** nêu đầu vào, đầu ra, giới hạn hoặc nhu cầu tính toán. Không dùng câu hỏi tu từ.
- **Trực giác:** nêu cấu trúc dữ liệu, phép biến đổi hoặc lựa chọn cục bộ chuẩn bị cho ký hiệu.
- **Ví dụ chạy tay:** dùng một trường hợp đủ nhỏ để theo dõi trạng thái, biến trung gian và kết quả.
- **Hình thức hóa:** nêu miền, kiểu, kích thước, điều kiện trước, điều kiện sau và ký hiệu.
- **Thuật toán và lập luận đúng:** nêu giả mã, bất biến hoặc luận điểm chính của chứng minh, điều kiện dừng và kết luận.
- **Ứng dụng và chi phí:** áp dụng trực tiếp kết quả vừa xây dựng; phân tích thời gian, bộ nhớ và giới hạn thực hành.
- **Kiểm tra:** yêu cầu người học tính, mô phỏng, giải thích, chứng minh, so sánh hoặc sửa thuật toán.

Không bắt buộc tám bước là tám trang riêng. Có thể gộp khi trang vẫn có một luận điểm trung tâm. Với khái niệm phụ, có thể dùng chu trình rút gọn nếu storyboard ghi rõ lý do. Không bỏ ngầm một bước đối với khái niệm trọng tâm. Chỉ sắp xếp lại cục bộ khi cần theo nguồn hoặc chỉ dẫn người dùng, ghi lý do trong storyboard và giữ cầu nối từ trực giác tới hình thức hóa.

## Đề xuất và chọn chủ đề cho ghi chú bài giảng

Trước khi soạn, tác tử kiến trúc nội dung phải lập **bản đồ chủ đề** từ `sources/source.md`, slide của bài, giáo trình được chỉ định và ghi chú đã có. Mỗi chủ đề nhận một trong bốn nhãn:

- `cốt lõi`: trực tiếp thực hiện mục tiêu và phạm vi đã quy định;
- `cầu nối`: khôi phục tiên quyết, thống nhất ký hiệu hoặc nối hai bước suy luận;
- `bổ sung`: lấp một khoảng trống khiến định nghĩa, ví dụ, định lý, thuật toán, chứng minh hoặc phân tích chi phí chưa tạo thành mạch hoàn chỉnh;
- `đọc thêm`: hữu ích nhưng không cần để đạt mục tiêu của bài.

Mỗi đề xuất phải ghi nguồn, vai trò trong mạch, kiến thức đầu vào, sản phẩm học tập, vị trí dự kiến, quan hệ với chủ đề trước–sau và tác động đến phạm vi. Chỉ thêm chủ đề `cầu nối` hoặc `bổ sung` khi chỉ ra được một khoảng trống cụ thể, chẳng hạn đại lượng chưa định nghĩa, ví dụ không dẫn tới đặc tả, định lý thiếu công cụ chứng minh, thuật toán thiếu điều kiện áp dụng hoặc kết luận không thu hồi tình huống mở đầu. Không thêm để làm tài liệu có vẻ đầy đặn, cập nhật xu hướng hoặc mở rộng sang một bài khác.

Được đề xuất nội dung chưa có trong nguồn chi tiết, nhưng chưa được soạn thành mệnh đề học thuật cho tới khi có nguồn phù hợp và được điều phối viên duyệt. Ưu tiên giáo trình đã chỉ định, tài liệu gốc của thuật toán, bài báo gốc hoặc tài liệu chính thức. Nếu không tìm được nguồn đủ thẩm quyền, chuyển đề xuất sang `đọc thêm`, loại khỏi phạm vi hoặc dừng phần phụ thuộc; không tự bịa nội dung để khép mạch.

Tác tử lập kế hoạch và tác tử phân tích nguồn đề xuất độc lập. Điều phối viên hợp nhất hai bản, ghi quyết định `giữ`, `thêm`, `gộp`, `tách`, `chuyển bài`, `đọc thêm` hoặc `bỏ` cùng lý do trong `outline.md` và `review-log.md` trước khi writer bắt đầu.

## Cách trình bày một chủ đề trong ghi chú bài giảng

Mỗi chủ đề trọng tâm dùng cấu trúc dưới đây theo đúng thứ tự suy luận. Mục không áp dụng phải được đánh dấu trong dàn ý cùng lý do; không tạo đề mục rỗng chỉ để đủ khuôn.

1. **Vai trò và nhu cầu:** nêu bài toán dữ liệu, đầu ra cần tạo, giới hạn tính toán và liên hệ với phần trước.
2. **Định nghĩa hoặc đặc tả:** nêu miền, kiểu dữ liệu, kích thước, lượng từ, ký hiệu, điều kiện trước và điều kiện sau trước khi sử dụng.
3. **Ví dụ chạy tay:** dùng dữ kiện nhỏ nhưng đủ đại diện; ghi trạng thái trung gian, phép tính và kết quả có thể kiểm tra. Một ví dụ dẫn nhập có số đã xuất hiện ở bước 1 để nêu nhu cầu; ví dụ ở bước này là ví dụ có lời giải áp dụng định nghĩa vừa phát biểu và chỉ ra định nghĩa bao hàm ví dụ dẫn nhập ở chỗ nào.
4. **Ý nghĩa trực quan và hình học:** giải thích đối tượng nào được bảo toàn, xấp xỉ, phân hoạch, cắt bỏ hoặc hội tụ. Hình phải hỗ trợ đúng lập luận và không thay thế phát biểu hình thức.
5. **Định lý, bổ đề hoặc mệnh đề:** tách rõ tên, giả thiết, kết luận, phạm vi áp dụng và trường hợp biên. Không gọi một quan sát thực nghiệm là định lý.
6. **Thuật toán:** nêu đầu vào, đầu ra, biểu diễn dữ liệu, giả mã, bất biến hoặc luận điểm đúng, điều kiện dừng, chi phí thời gian–bộ nhớ–I/O và giới hạn thực hành.
7. **Chứng minh:** mở bằng mệnh đề cần chứng minh và ý tưởng; trình bày các bước then chốt, chỉ rõ nơi dùng từng giả thiết, xử lý cơ sở hoặc biên và kết thúc bằng đúng kết luận. Phân biệt chứng minh đầy đủ với phác thảo.
8. **Ứng dụng, lỗi dễ mắc và kiểm tra:** dùng trực tiếp kết quả vừa xây dựng; nêu điều kiện khiến phương pháp không còn đúng; kết thúc bằng một câu hỏi hoặc bài ngắn đo đúng mục tiêu.

Một mục có thể đổi vị trí giữa ví dụ và trực quan khi ví dụ dẫn nhập làm rõ nhu cầu tốt hơn, nhưng bản đồ chủ đề phải ghi lý do. Dùng cùng dữ kiện và ký hiệu xuyên suốt từ ví dụ sang định nghĩa, giả mã, chứng minh và phân tích chi phí khi có thể. Mỗi phần lớn phải có câu nối vào, đầu ra cho phần sau và một đoạn tổng hợp ngắn không lặp lại nguyên văn nội dung vừa trình bày.

Đây là chu trình riêng cho tài liệu tự học: sau khi thiết lập vai trò, nhu cầu và ví dụ dẫn nhập, ghi chú đặt định nghĩa trước ví dụ có lời giải, rồi dùng ví dụ để xây ý nghĩa trực quan hoặc hình học trước khi phát biểu định lý, thuật toán và chứng minh. Chu trình trang chiếu ở mục trước vẫn ưu tiên trực giác trước hình thức hóa. Không dùng tiêu chí thứ tự của loại sản phẩm này để bác loại sản phẩm kia. Mức chi tiết, giọng kể, môi trường đánh số và cấu trúc chương của ghi chú theo mục "Tiêu chuẩn giáo trình cho ghi chú bài giảng"; khi hai mục khác nhau về chi tiết, mục đó quyết định.

Với yêu cầu chỉ làm ghi chú, ba tệp quy trình được cập nhật theo chủ đề thay vì theo trang chiếu:

- `outline.md` bổ sung goal, vấn đề trung tâm, bản đồ chủ đề, đồ thị tiên quyết, thuật ngữ và ánh xạ nguồn;
- `storyboard.md` dùng `note-topic-id` duy nhất cho mỗi chủ đề, ghi vai trò, kết nối vào–ra, kiến thức đầu vào, sản phẩm học tập và các thành phần trình bày áp dụng; không bắt buộc `data-slide-id` hoặc thời lượng 120+60 phút;
- `review-log.md` ghi báo cáo, quyết định với chủ đề bổ sung, sai khác so với slide và phạm vi rà lại.

Các yêu cầu về mã trang, số `<section>` và thời lượng trong phần dưới chỉ áp dụng cho bộ trang chiếu. Khi một yêu cầu làm đồng thời slide và ghi chú, storyboard giữ cả `data-slide-id` và `note-topic-id` cùng ánh xạ giữa chúng.

Storyboard phải chỉ ra cho từng cụm:

- mạch trình bày chứa cụm, chức năng của mạch, kết nối vào từ mạch trước, đầu ra cho mạch sau và đóng góp vào mục tiêu bài học;
- mã trang thực hiện từng bước;
- kiến thức đầu vào và sản phẩm học tập;
- dữ liệu, giới hạn quy mô và đầu ra của tình huống mở bài; cách tình huống này được dùng lại trong ví dụ, đặc tả, phân tích chi phí hoặc kiểm tra;
- dữ kiện, trạng thái trung gian hoặc ký hiệu được truyền từ ví dụ sang giả mã và chứng minh;
- bước được gộp hoặc ghi `không áp dụng`, kèm lý do;
- câu nối giữa các bước;
- thời lượng dự kiến của cụm; tổng phần giảng 120 phút và tổng phần bài tập recitation 60 phút.

## Tiêu chuẩn giáo trình cho ghi chú bài giảng

Mục này quy định `materials/lec-NN/lecture-note.md` (áp dụng từ 2026-10-14 theo chuẩn đã dùng ở `../math-4-AI` và `../rl-plan`, lấy mẫu từ giáo trình *Học máy thống kê* của tác giả tại `../SML-textbook-main.zip`). Ghi chú bài giảng là một chương giáo trình tự chứa: sinh viên đọc được trọn vẹn mà không cần mở bộ trang chiếu, không cần nghe giảng và không cần công cụ hỗ trợ bên ngoài. Bộ trang chiếu là bản tóm lược của ghi chú, không phải ngược lại; khi hai bên mâu thuẫn, ghi chú là bản đầy đủ và được sửa trước. Mục "Cách trình bày một chủ đề trong ghi chú bài giảng" ở trên giữ thứ tự suy luận; mục này quy định mức chi tiết, giọng kể, môi trường và cấu trúc chương.

### Tiêu chuẩn thứ nhất: trình bày theo ngữ cảnh để hiểu được bằng cách đọc

Phép thử duy nhất: một sinh viên năm 2 có đủ kiến thức tiên quyết, đọc tệp từ đầu đến cuối theo thứ tự, không mở trang chiếu, không tra cứu ngoài và không dùng công cụ hỗ trợ, phải hiểu được từng câu tại chỗ câu đó xuất hiện. Mọi quy tắc dưới đây phục vụ phép thử này.

- **Vấn đề đi trước công cụ.** Mỗi mục `##` mở bằng một đoạn nêu bài toán dữ liệu cụ thể (dữ liệu, đầu ra, giới hạn bộ nhớ, I/O hoặc số phép so, có số liệu khi nguồn cho) mà công cụ hiện có chưa giải được, và nêu điều mục này sẽ làm rõ, viết như câu hỏi mà người đọc cùng tác giả đặt ra ("Để trả lời câu hỏi này, chúng ta cần…"). Giáo trình của tác giả mở mục Q-learning bằng giới hạn của quy hoạch động; ghi chú của học phần này mở mục phân dải bằng số cặp $\binom C2$ còn lại sau khi đã có chữ ký. Không mở mục bằng định nghĩa, công thức, giả mã hay danh sách.
- **Mỗi công thức được bao bởi lời.** Trước công thức có câu nói công thức tính gì và vì sao cần nó; sau công thức có câu đọc công thức bằng lời, nêu từng thành phần nghĩa là gì và đại lượng thu được dùng vào đâu. Không để hai công thức đứng liền nhau mà không có câu nối.
- **Ký hiệu được gọi tên khi xuất hiện.** Lần đầu một ký hiệu xuất hiện, câu chứa nó nêu tên gọi, kiểu và miền ("ma trận chữ ký $\mathrm{SIG}\in V^{n\times C}$ có một cột cho mỗi tài liệu"). Bảng ký hiệu ở đầu chương là chỗ tra lại, không thay cho câu giới thiệu tại chỗ. Khi ký hiệu của học phần khác ký hiệu của sách nguồn, bảng ký hiệu nêu tương ứng một lần.
- **Mỗi bước suy diễn nêu lý do.** Trong suy diễn, chứng minh và phép đếm chi phí, mỗi dấu bằng, bất đẳng thức hoặc số hạng đi kèm căn cứ: định nghĩa nào, giả thiết nào, kết quả số hiệu nào, dòng giả mã nào (giáo trình của tác giả ghi "[do ERM]" bên cạnh dòng biến đổi). Không có bước "dễ thấy", "suy ra ngay" hoặc dấu ba chấm.
- **Phát biểu toán học và thuật toán có bản đọc bằng lời.** Sau mỗi định nghĩa, định lý và thuật toán có một đoạn nói lại nội dung bằng tiếng Việt thường, nêu vai trò từng giả thiết và điều xảy ra khi bỏ một giả thiết, kèm ít nhất một ví dụ và một phản ví dụ hoặc trường hợp giới hạn (giáo trình của tác giả sau định lý PAC: đọc kết quả với $\epsilon=1\%$, $n=100\,000$, rồi hỏi giả thiết hữu hạn có thực tế không và trả lời bằng mô hình 64 bit). Dạng chuẩn: câu mở "Các giả thiết của kết quả có vai trò riêng, và mỗi giả thiết bị bỏ đều có phản ví dụ", rồi một danh sách "Bỏ <giả thiết>: <phản ví dụ cụ thể>" cho từng giả thiết, rồi một câu chỉ ra bước nào của chứng minh dùng giả thiết nào.
- **Ví dụ cụ thể trước phát biểu tổng quát.** Mỗi khái niệm và thuật toán trọng tâm có một ví dụ với số liệu được tính tay xuất hiện trước định nghĩa, định lý hoặc giả mã tổng quát, rồi được nhắc lại sau phát biểu để chỉ ra phát biểu tổng quát bao hàm ví dụ này ở chỗ nào. Với thuật toán, ví dụ là một bước hoặc một lượt chạy tay có trạng thái trung gian; giả mã dùng đúng ký hiệu của ví dụ.
- **Nối mục bằng kết quả, không bằng lời dẫn.** Cuối mỗi mục có đoạn kết nêu ba điều: đã thu được kết quả gì (dẫn số hiệu), kết quả đó còn thiếu gì hoặc giả thiết nào còn hạn chế, và mục kế tiếp giải quyết thiếu hụt đó như thế nào. Ba điều này được kể trong một hoặc hai đoạn văn xuôi liền mạch ("Như vậy, chúng ta đã…", "Tuy nhiên, …", "Trong Mục N+1, chúng ta…"), không dùng nhãn "Kết mục" hay danh sách. Ở mỗi ranh giới mục, câu nối chỉ đặt ở một phía. Không dùng câu dẫn rỗng kiểu "tiếp theo ta xét".
- **Không tham chiếu ra ngoài tệp mà không đủ nội dung.** Cấm "như trên trang chiếu", "đã nói trong bài", "xem bài giảng". Kết quả của bài trước được dẫn bằng số hiệu và được phát biểu lại trong một câu đủ để dùng ngay. Tham chiếu tiến phải nêu rõ điều đang được tạm chấp nhận.
- **Câu đủ thành phần, đoạn có luận điểm.** Không chép câu mảnh kiểu gạch đầu dòng của trang chiếu thành văn ghi chú. Mỗi đoạn có một câu luận điểm. Danh sách chỉ dùng cho các mục thực sự song song (các bước thuật toán, các giả thiết, các trường hợp, các hàng của một phép đếm).
- **Nhầm lẫn thường gặp được nói thẳng.** Ở mỗi khái niệm, nêu cách hiểu sai phổ biến và lý do nó sai, bằng phản ví dụ hoặc chỉ ra giả thiết bị vi phạm (ước lượng $\widehat s$ không phải $s$; xác suất theo cặp không phải tỷ lệ lỗi của kho; chi phí kỳ vọng không phải chi phí xấu nhất).
- **Hình được đọc trong văn bản.** Mỗi hình có đoạn văn trước hoặc sau nói cần nhìn điều gì trên hình và điều đó ứng với công thức, giả mã hay kết quả nào; `alt` mô tả đủ nội dung toán học.
- **Độ dài phục vụ việc đọc hiểu.** Ghi chú viết cho người đọc lần đầu, ưu tiên rõ ràng hơn ngắn gọn, và dài hơn phần ghi chú diễn giả của cùng bài. Độ dài đo bằng số âm tiết tách theo khoảng trắng của tệp Markdown (kể cả công thức và khối mã), vì tiếng Việt đếm theo âm tiết. Một chương thường dài 12 000 đến 32 000 âm tiết (ghi chú Bài 05 của `../rl-plan` là 26 000, Bài 06 của học phần này là 31 000); dưới 9 000 âm tiết cần lý do ghi trong `review-log.md`; trên 32 000 âm tiết phải xét tách phần bài tập hoặc chuyển nội dung sang đọc thêm. Độ dài không được đạt bằng cách lặp lại, dẫn dắt rỗng hay chép lại trang chiếu.

### Các nguyên tắc còn lại

- **Tự chứa.** Mọi ký hiệu, giả thiết, đối tượng và kết quả được dùng phải được định nghĩa hoặc phát biểu trong cùng tệp, hoặc dẫn tới số hiệu cụ thể trong ghi chú của bài trước (`Định lý 05.2`) kèm phát biểu lại.
- **Đầy đủ, không cắt cụt.** Mỗi lập luận được viết hết các bước; mỗi ví dụ tính đến kết quả số và kiểm tra lại; mỗi bài tập có lời giải.
- **Ví dụ, tình huống và bài tập tự chứa tại chỗ.** Mỗi khối `example`, `application`, `exercise` nêu lại đầy đủ dữ kiện ngay trong khối: tập, ma trận, tham số, ngưỡng, kết quả của bước trước mà khối dùng tới. Không viết "với dữ liệu của Ví dụ 06.2" rồi để sinh viên tua lại; nếu ví dụ nối tiếp một ví dụ trước, mở bằng một đoạn "Dữ kiện" chép lại các giá trị cần dùng kèm số hiệu nguồn trong ngoặc.
- **Hình thức.** Kiến thức được trình bày theo các môi trường có nhãn và số hiệu: Định nghĩa, Định lý, Mệnh đề, Bổ đề, Hệ quả, Ví dụ, Nhận xét, Chứng minh, Thuật toán, Bài tập, Tình huống áp dụng. Không trộn định nghĩa vào giữa đoạn văn giải thích; không phát biểu kết quả bằng lời rồi bỏ qua dạng toán học.
- **Giữ chu trình học tập.** Chu trình của bộ trang chiếu (tình huống → vấn đề → trực giác → ví dụ → hình thức hóa → thuật toán và tính đúng → chi phí → kiểm tra) được giữ đầy đủ trong ghi chú với mức chi tiết của giáo trình và theo thứ tự riêng của ghi chú ở mục "Cách trình bày một chủ đề trong ghi chú bài giảng".
- **Bài tập recitation.** Các bài sách dùng trong phần recitation của bộ trang chiếu được giải đầy đủ trong ghi chú, cùng số hiệu `Bài tập NN.k`, có ghi số bài, mục và trang sách; lời giải trong ghi chú và trong ghi chú diễn giả cho cùng kết quả.

### Tham khảo cách diễn giải của giáo trình

Khi soạn hoặc sửa một ghi chú, tác tử soạn phải đối chiếu với cách các giáo trình chuẩn trình bày cùng chủ đề và ghi vào `review-log.md` giáo trình nào, mục nào đã được tham khảo cho từng mục của chương. Giáo trình chuẩn của học phần theo `sources/source.md`: Leskovec, Rajaraman và Ullman (2020) *Mining of Massive Datasets*, ấn bản 3, cho năm bài neo theo MMDS; Silberschatz, Korth và Sudarshan (2019) *Database System Concepts*, ấn bản 7, cho lưu trữ, sắp xếp ngoài bộ nhớ, chỉ mục và nối; Nelson và Gailly cho nén dữ liệu; bài báo gốc hoặc giáo trình được ghi trong `sources/reference-slides/README.md` cho các cụm còn lại; Cormen, Leiserson, Rivest và Stein (2022) *Introduction to Algorithms*, ấn bản 4, cho cách phát biểu bất biến vòng lặp, quy nạp và phân tích chi phí khi nguồn trục không trình bày; giáo trình *Học máy thống kê* của tác giả (`../SML-textbook-main.zip`) cho giọng kể, cách dẫn dắt, đoạn "Trong thực hành" và thuật ngữ tiếng Việt. Tài liệu chi tiết được chọn trong `sources/` vẫn quyết định phạm vi và thứ tự.

Những điều cần học từ giáo trình và chuyển vào ghi chú:

- **Thứ tự dẫn dắt**: giáo trình đưa khái niệm nào trước, nêu nhu cầu bằng ví dụ nào, chỗ nào dừng lại giải thích trước khi phát biểu tổng quát. Khi ghi chú đổi thứ tự so với giáo trình, ghi lý do.
- **Cách đọc một định nghĩa, định lý hoặc thuật toán bằng lời**: câu diễn giải sau phát biểu, vai trò từng giả thiết, trường hợp đặc biệt và phản ví dụ mà giáo trình chọn. Ưu tiên các ví dụ của sách nguồn (Ví dụ 3.8 của MMDS, quan hệ của db-book) hơn là bịa ví dụ mới.
- **Hình vẽ chuẩn**: ma trận chữ ký và dải, đường cong S, miền gần–xa, sơ đồ luồng dữ liệu, cây và trang chỉ mục. Vẽ lại bằng SVG cục bộ với số liệu của chương, không sao chép hình.
- **Thuật ngữ và ký hiệu**: dùng thuật ngữ tiếng Việt đã quy ước trong học phần, ghi thuật ngữ gốc trong ngoặc ở lần đầu, giữ ký hiệu của sách nguồn khi không xung đột với bài.
- **Nhận xét và cảnh báo**: những điểm giáo trình nêu dưới dạng nhận xét, chú thích hoặc bài tập có lời giải mà sinh viên hay hiểu sai.
- **Mức chặt chẽ**: theo mức giáo trình chọn cho đối tượng đại học; khi giáo trình bỏ qua một chứng minh, ghi chú bổ sung chứng minh ở mức đó hoặc dẫn nguồn có số trang, không phát biểu như thể đã chứng minh.

Giới hạn: tham khảo cách diễn giải, không dịch hoặc chép đoạn văn của giáo trình. Trích dẫn nguồn theo tác giả, năm, mục và trang trong "Hướng dẫn đọc thêm và tài liệu tham khảo", và dẫn tại chỗ khi một lập luận, ví dụ hay hình lấy ý từ giáo trình.

### Đoạn văn móc nối: quan hệ giữa khái niệm, kết quả và thực hành

Ghi chú không phải danh mục các định nghĩa, định lý và giả mã đứng cạnh nhau. Mỗi đối tượng mới phải được gắn vào mạng kiến thức đã có bằng những đoạn văn móc nối viết rõ, có tên quan hệ và có số hiệu:

- **Khái niệm với khái niệm.** Ngay sau một định nghĩa mới có đoạn nêu quan hệ của nó với các khái niệm đã định nghĩa: là trường hợp đặc biệt của gì, tổng quát hóa gì, bổ sung cho gì, khác gì với khái niệm dễ nhầm (họ nhạy cảm với MinHash; khoảng cách góc với độ tương đồng cosin; chi phí kỳ vọng với chi phí xấu nhất). Quan hệ được phát biểu bằng toán học khi có thể và được dẫn số hiệu.
- **Kết quả với kết quả.** Trước mỗi định lý có câu nêu định lý này cần kết quả nào trước đó; sau định lý có đoạn nêu nó mạnh hơn, yếu hơn hay mở rộng kết quả nào đã có, đổi giả thiết nào và trả giá bằng gì. Khi một định lý là hệ quả hay trường hợp riêng của định lý khác, viết thành `corollary` và chỉ ra bước suy ra.
- **Thuật toán với thuật toán.** Khi giới thiệu biến thể, nêu giới hạn cần khắc phục, thành phần thay đổi (khóa, cấu trúc dữ liệu, số lượt quét, cách chia khối) và hệ quả đối với tính đúng, bộ nhớ, I/O hoặc chi phí; giữ ký hiệu chung để so sánh.
- **Chuỗi suy luận của chương.** Mỗi mục `##` kể lại chuỗi định nghĩa → kết quả → thuật toán của mục bằng văn xuôi trong đoạn kết mục, dẫn số hiệu. Tóm tắt chương kể lại chuỗi này cho toàn bài trong một đoạn văn 5–8 câu đặt trước danh mục số hiệu.
- **Kết quả với thực hành.** Ngay sau mỗi định lý hoặc thuật toán chính có đoạn "Trong thực hành" (cách gọi của giáo trình *Học máy thống kê*) nêu cụ thể: đối tượng của kết quả ứng với gì khi cài đặt (bảng băm, danh sách thùng, tệp trên đĩa, tác vụ MapReduce); giả thiết của kết quả được bảo đảm hay vi phạm ra sao trên dữ liệu thật (hàm băm không lý tưởng, phân bố khóa lệch, bộ nhớ không đủ, dữ liệu không độc lập); kết luận cho phép làm gì hoặc giải thích hiện tượng gì đã quan sát. Đoạn này dẫn tới tình huống áp dụng ở cuối chương hoặc bài khác của học phần. Không viết câu chung chung kiểu "kết quả này rất quan trọng trong thực tế".
- **Ứng dụng ngược về lý thuyết.** Mỗi tình huống áp dụng ở cuối chương dẫn ngược số hiệu của các định nghĩa, định lý và thuật toán mà nó dùng, và nêu bước nào của tình huống tương ứng với giả thiết nào.
- **Móc nối với bài trước và bài sau.** Mở chương nêu kết quả cụ thể của bài trước mà chương này xây tiếp (số hiệu, phát biểu lại một câu) và giới hạn của kết quả đó mà chương này vượt qua. Kết chương nêu giới hạn còn lại và bài nào của học phần xử lý tiếp. Chỉ dẫn tới bài đã có trong kho.

Mỗi đoạn móc nối là văn xuôi có luận điểm, không phải một dòng "Liên hệ: …".

### Cấu trúc bắt buộc của một chương

1. **Tiêu đề** cấp một: `# Bài NN — Tên bài`.
2. **Giới thiệu chương**: tối đa một đoạn ngắn, hoặc bỏ hẳn; dòng liên kết về bộ trang chiếu đặt ngay sau. Bài toán trung tâm được nêu ở đầu mục nội dung thứ nhất.
3. **Mục tiêu học tập**: danh sách kết quả quan sát được, mỗi mục dẫn tới mục của chương.
4. **Kiến thức tiên quyết**: mỗi mục là một gạch đầu dòng mở bằng tên nhóm kiến thức in đậm kèm số hiệu trong ngoặc ("**Định lý MinHash** (Định lý 05.3).") rồi phát biểu lại kết quả trong một đến hai câu đủ để dùng ngay; mở mục bằng một câu quy ước cách đọc số hiệu ("Số hiệu `05.k` chỉ ghi chú Bài 05"). Với bài trước chưa đánh số hiệu, dẫn theo mục của ghi chú đó.
5. **Bảng ký hiệu**: bảng ba cột `Ký hiệu | Ý nghĩa | Miền hoặc kiểu`, khoảng 15–25 dòng, chỉ gồm ký hiệu dùng xuyên suốt chương. Trước bảng một câu nêu phạm vi của bảng và quy tắc "mỗi chữ giữ một nghĩa trong cả chương"; sau bảng một đoạn nêu các quy ước đọc (chỉ số, dấu thập phân, số liệu nào của sách và số liệu nào là áp dụng của bản soạn).
6. **Bản đồ chủ đề** bốn nhóm `cốt lõi`, `cầu nối`, `bổ sung`, `đọc thêm` theo mục "Đề xuất và chọn chủ đề", mỗi chủ đề ghi mục tương ứng và `note-topic-id`.
7. **Các mục nội dung** đánh số `## 1.`, `## 2.`, …; mỗi mục ứng với một mạch của bộ trang chiếu và tuân thủ mẫu ở phần "Mẫu trình bày một khái niệm". Mỗi chủ đề mang một `note-topic-id` duy nhất, ghi bằng chú thích HTML `<!-- note-topic-id: lec-NN-topic-k -->` ngay trước tiêu đề mục; viewer kiểm tra và ẩn chú thích này. Mục 1 mở bằng: kết quả của bài trước mà chương xây tiếp (số hiệu, một câu phát biểu lại), bài toán dữ liệu cụ thể có số liệu mà công cụ cũ chưa giải được, điều chương này chứng minh hoặc xây dựng, và hình minh họa cấu trúc của chương có đoạn đọc hình. Mỗi mục sau mở bằng một đoạn nhắc lại thiếu hụt của mục trước trên chính ví dụ xuyên suốt rồi nêu việc của mục.
8. **Tình huống áp dụng và ứng dụng**: mục riêng ở cuối phần nội dung (xem dưới).
9. **Tóm tắt chương**: mở bằng một đoạn văn 5–8 câu kể lại câu chuyện của chương (câu hỏi xuất phát, các bước đã đi, kết quả đích, giới hạn còn lại), dẫn số hiệu ngay trong câu; rồi đến **Định nghĩa và kết quả theo mục**, **Công thức và thuật toán cần nhớ** trên dòng hiển thị, và **Giả thiết hay bị bỏ quên**.
10. **Bài tập củng cố**: ít nhất một bài cho mỗi mục tiêu học tập, chia ba tiểu mục `### Mức nhận biết`, `### Mức tính toán hoặc chứng minh`, `### Mức vận dụng`; mỗi bài có `hint` và `solution`. Các bài sách của phần recitation được xếp vào đây với số bài, mục và trang sách.
11. **Hướng dẫn đọc thêm và tài liệu tham khảo**: tác giả, năm, tên, chương hoặc mục, trang hoặc trang chiếu của bản nguồn; nêu mục nào của chương dựa trên nguồn nào; ghi công `http://www.mmds.org` khi dùng MMDS.

### Môi trường và đánh số

- Số hiệu theo bài và thứ tự xuất hiện trong bài, dùng chung một bộ đếm cho Định nghĩa, Định lý, Mệnh đề, Bổ đề, Hệ quả, Nhận xét và Thuật toán (`Định nghĩa 06.1`, `Định lý 06.2`, `Thuật toán 06.3`), một bộ đếm riêng cho Ví dụ (`Ví dụ 06.1`), một bộ đếm riêng cho Tình huống (`Tình huống 06.1`) và một bộ đếm riêng cho Bài tập (`Bài tập 06.1`). Mọi tham chiếu chéo dùng số hiệu, không dùng "định lý ở trên".
- Nhãn và số hiệu đặt ở tiêu đề khối: `::: theorem Định lý 06.2 (Xác suất thành ứng viên)`. Tên gọi quen thuộc đặt trong ngoặc sau số hiệu.
- Khối `proof` đi ngay sau kết quả mà nó chứng minh và kết thúc bằng dấu $\square$. Chứng minh dài hơn một trang được tách bổ đề. Khối `algorithm` ghi đầu vào, đầu ra, giả thiết, khởi tạo, tham số, các bước đánh số, điều kiện dừng, trường hợp biên và chi phí mỗi bước; giả mã dạng khối mã đặt trong khối này hoặc ngay sau.
- Viewer hỗ trợ mười bốn loại khối không lồng nhau: `definition`, `theorem`, `proposition`, `lemma`, `corollary`, `remark`, `algorithm`, `example`, `application`, `derivation`, `proof`, `exercise`, `hint`, `solution`. `proof`, `hint` và `solution` gập mặc định, dùng được bằng bàn phím và được mở khi in.

### Mẫu trình bày một khái niệm

Mỗi khái niệm hoặc thuật toán trọng tâm đi qua đủ các bước sau, theo thứ tự này, trong một hoặc nhiều tiểu mục `###`:

1. **Vấn đề**: quyết định, giới hạn hoặc bài toán chưa trả lời được bằng công cụ trước đó, nêu bằng ví dụ cụ thể có số liệu khi có thể.
2. **Trực giác**: mô tả bằng quan hệ giữa dữ liệu, khóa, nhóm, bước xử lý hoặc chi phí (lời hoặc hình SVG có `alt`) điều khái niệm nắm bắt; mở bằng "Một cách trực quan", "Về mặt ý tưởng" và có một câu nói rõ đây chưa phải định nghĩa.
3. **Định nghĩa hoặc đặc tả**: môi trường `definition`, ghi đủ miền, kiểu và kích thước của mọi đối tượng, chỉ số, điều kiện trước và sau, các giả thiết, ký hiệu được đưa vào. Ngay sau đó là một đoạn diễn giải từng thành phần và một hoặc hai ví dụ, phản ví dụ.
4. **Kết quả hoặc thuật toán**: môi trường `theorem`, `proposition` hoặc `lemma` theo mẫu bốn phần: giả thiết, kết luận, điều kiện áp dụng, phạm vi hoặc giới hạn; phân biệt $=$, $\approx$, $\le$, kỳ vọng và xấu nhất. Với thuật toán, dùng `algorithm` và trước đó một ví dụ thực hiện bằng tay một bước hoặc một lượt; sau giả mã là lập luận tính đúng (bất biến, quy nạp, trao đổi hoặc phản chứng) và phép đếm chi phí theo bảng bước–số lần–chi phí–đóng góp.
5. **Chứng minh**: môi trường `proof` viết đủ các bước; khi chứng minh vượt phạm vi học phần, ghi rõ "Chứng minh nằm ngoài phạm vi học phần" kèm nguồn có số trang và nêu ý tưởng chính trong một đoạn.
6. **Ví dụ có lời giải**: môi trường `example` với dữ kiện đầy đủ, tính toán từng bước, kết quả số và một dòng kiểm tra lại. Ít nhất một ví dụ tính được bằng tay cho mỗi kết quả chính.
7. **Nhận xét**: môi trường `remark` cho giới hạn áp dụng, nhầm lẫn thường gặp, quan hệ với kết quả trước, điều gì thay đổi khi bỏ một giả thiết, và đoạn "Trong thực hành".
8. **Bài tập ngay sau mục**: một đến ba bài `exercise` kiểm tra đúng mục tiêu của tiểu mục, kèm `hint` và `solution` đầy đủ.

Các bước có thể gộp trong một tiểu mục nhưng không được đổi thứ tự và không được bỏ bước. Không mở một khái niệm bằng định nghĩa khi chưa có vấn đề và trực giác. Với khái niệm phụ (một độ đo, một trường hợp riêng), chu trình rút gọn phải được ghi trong bản đồ chủ đề kèm lý do.

### Tình huống áp dụng và ứng dụng

- **Tình huống áp dụng** (`application`) là một bài toán dữ liệu lớn cụ thể được giải trọn vẹn bằng công cụ của chương: nêu bài toán và dữ liệu, mô hình hóa thành đối tượng của chương, xác minh các giả thiết của kết quả được dùng, áp dụng kết quả hoặc thuật toán, tính chi phí, diễn giải kết luận trở lại bài toán ban đầu, nêu giới hạn. Mỗi chương có ít nhất hai tình huống, trong đó một tình huống nêu trường hợp giả thiết không thỏa và hậu quả. Ưu tiên các ứng dụng mà sách nguồn trình bày (đối sánh thực thể, vân tay, bản tin gần trùng của MMDS §3.8) hơn là bịa tình huống mới.
- **Ứng dụng** là danh mục ngắn các chỗ khái niệm xuất hiện trong các bài sau của học phần hoặc trong các hệ thống được nguồn nêu, mỗi mục một hoặc hai câu nêu khái niệm nào của chương được dùng và dẫn tới bài hoặc nguồn tương ứng. Không liệt kê suông tên lĩnh vực.

### Trình bày sáng sủa: chứng minh và diễn giải

Chứng minh, phép đếm chi phí và đoạn diễn giải phải đọc được từng ý một:

- **Một ý một đoạn.** Đoạn văn diễn giải chỉ chứa một luận điểm và tối đa khoảng bốn câu. Không nối hai ý bằng dấu chấm phẩy hoặc "và" để tiết kiệm dòng.
- **Chứng minh theo bước.** Mỗi chứng minh dài hơn ba câu được chia thành các bước có nhãn in đậm trên dòng riêng (`**Bước 1 (khởi tạo).**`): câu đầu nêu điều bước này thiết lập, các câu sau là lập luận, câu cuối nêu căn cứ. Chuỗi biến đổi nhiều hơn hai dấu bằng hoặc bất đẳng thức đặt trong `$$...$$` với `\begin{aligned}`, mỗi dấu một dòng, căn cứ ghi ở cột phải bằng `&&\text{(...)}` hoặc ở câu ngay sau công thức.
- **Trường hợp và điều kiện thành danh sách.** Phân chia trường hợp, kiểm tra nhiều điều kiện, hoặc nhiều kết luận (a), (b), (c) viết thành danh sách, mỗi mục một dòng.
- **Công thức quan trọng trên dòng riêng.** Công thức dài hơn nửa dòng, công thức được tham chiếu về sau (đánh số `\tag{3.4}` theo số mục) và kết luận của một bước luôn đặt ở `$$...$$`.
- **Tách phần của phát biểu.** Trong định lý, bốn phần Giả thiết, Kết luận, Điều kiện áp dụng, Phạm vi mỗi phần là một đoạn riêng; trong định nghĩa, các đối tượng được định nghĩa liên tiếp tách dòng; trong thuật toán, Đầu vào, Đầu ra, Giả thiết, Các bước, Dừng, Chi phí mỗi phần một đoạn hoặc một danh sách.
- **Ví dụ và lời giải.** Các giai đoạn (lập mô hình, kiểm giả thiết, tính, diễn giải, kiểm tra lại) mở bằng nhãn in đậm trên dòng riêng. Mỗi phép tính có kết quả trung gian được ghi; với vết chạy thuật toán ghi trạng thái trước, thao tác và trạng thái sau.
- **Hạn chế ngoặc đơn lồng.** Không quá một ngoặc đơn trong một câu; chú thích dài chuyển thành câu riêng.

Tác tử rà mạch viết kiểm tiêu chí này ở mọi khối `proof`, `derivation`, `solution` và mọi đoạn diễn giải; chỗ không đạt ghi mức `trung bình`.

### Kiểm định ghi chú bài giảng

Trước khi công bố trên chỉ mục, tác tử rà soát lập bảng đối chiếu theo các mục sau, ghi kết quả vào `review-log.md`:

- mỗi mục tiêu học tập có ít nhất một kết quả hoặc ví dụ và một bài tập tương ứng;
- mỗi khái niệm trọng tâm của `storyboard.md` đi đủ tám bước của mẫu trình bày; mỗi thuật toán có bước tính tay trước giả mã, lập luận tính đúng, phép đếm chi phí, và hai bản (ghi chú và trang chiếu) cho kết quả nhất quán;
- mỗi ký hiệu dùng trong chương có mặt trong bảng ký hiệu; miền, chỉ số và quy ước được nêu trước khi dùng;
- mỗi định lý có đủ bốn phần và có chứng minh hoặc nguồn có số trang; không có tuyên bố đúng, tối ưu, kỳ vọng hoặc cận thiếu giả thiết quyết định;
- mỗi ví dụ có kết quả số và dòng kiểm tra lại; các con số được tính lại độc lập bởi tác tử rà toán;
- mỗi bài tập có `hint` và `solution` đầy đủ; bài sách có số bài, mục và trang;
- không có tham chiếu "xem trang chiếu", không có câu mảnh, không có bước suy diễn bị bỏ;
- chứng minh chia bước có nhãn, chuỗi biến đổi trong `aligned` mỗi dấu một dòng, trường hợp thành danh sách, đoạn diễn giải một ý một đoạn;
- số hiệu liên tục, tham chiếu chéo trỏ đúng, các khối không lồng nhau và render đúng ở màn rộng, màn hẹp và bản in;
- mỗi định nghĩa có đoạn nêu quan hệ với khái niệm đã có; mỗi kết quả có đoạn nêu quan hệ với kết quả trước và đoạn "Trong thực hành" nêu đúng đối tượng, giả thiết và kết luận; mỗi mục kể được chuỗi suy luận bằng văn xuôi ở đoạn kết mục; mở và kết chương có móc nối với bài trước và bài sau;
- mỗi công thức có câu dẫn trước và câu đọc sau; mỗi ký hiệu được gọi tên tại lần xuất hiện đầu; giọng kể "chúng ta/ta" đúng quy định và tài liệu không làm chủ ngữ;
- mỗi mục có ghi trong `review-log.md` giáo trình và mục đã tham khảo cách diễn giải; không có đoạn dịch hoặc chép;
- nội dung, ký hiệu và giả thiết nhất quán với bộ trang chiếu cùng bài; chỗ lệch được ghi và sửa ở bộ trang chiếu.

Tiêu chuẩn này áp dụng cho ghi chú mới và là đích rà soát lại cho các ghi chú đã công bố. Việc nâng cấp một ghi chú đã có đi qua quy trình đa tác tử rút gọn: tác tử soạn viết lại theo mẫu, tác tử rà toán tính lại toàn bộ số liệu, tác tử rà mạch viết kiểm tra tám bước và liên kết mục, điều phối viên duyệt rồi mới cập nhật chỉ mục.

## Phân loại phần lớn và thiết kế mạch cho sinh viên năm 2

Mục này cụ thể hóa “Cấu trúc học tập” và `slide_authoring_standard.md` ở cấp section. Dùng khi lập outline, storyboard và rà soát deck; không thay thế quy tắc nguồn, thời lượng, đặc tả hay kiểm định. Các loại dưới đây là chức năng sư phạm, không phải yêu cầu mọi bài có đúng bảy section. Một loại có thể xuất hiện nhiều lần; có thể gộp các loại gần nhau khi mạch vẫn rõ. Chọn 5–7 phần; chỉ dùng ngoài khoảng này khi nguồn hoặc yêu cầu cụ thể của người dùng đòi hỏi, và ghi lý do trong storyboard cùng nhật ký theo quy định hiện có.

### Chọn loại, đầu ra học tập và nhãn

| Loại phần | Sinh viên cần làm được khi kết thúc |
|---|---|
| Giới thiệu và động lực | Nêu bài toán, giới hạn của cách quen thuộc và nhu cầu của phương pháp mới |
| Khái niệm hoặc mô hình | Giải thích cơ chế qua ví dụ, đọc đặc tả và xác định điều kiện áp dụng |
| Thuật toán và ví dụ vận dụng | Chọn biểu diễn, đặc tả thuật toán, chạy tay và lập luận tính đúng |
| Chi phí và lợi ích | Lập phép đếm, tính chi phí, so sánh phương án theo cùng mô hình |
| Hệ thống và cơ chế thực thi | Theo dõi dữ liệu, tác vụ, tài nguyên và phạm vi phục hồi khi có lỗi |
| Thực hành | Cài môi trường, chuyển đặc tả thành mã, chạy và kiểm chứng kết quả |
| Tổng kết và bài tập | Chọn phương pháp cho bài toán nguồn, giải thích lựa chọn và hoàn thành sản phẩm được giao |

Trong outline, mỗi section ghi loại chính, mục tiêu quan sát được, tiên quyết, ví dụ dùng xuyên suốt, kết quả chuyển cho phần sau và thời lượng. Nếu gộp nhiều loại, ghi thứ tự các cụm và lý do. Các loại này không buộc bài lý thuyết phải có hệ thống hoặc thực hành ngoài phạm vi nguồn.

- Phần tùy chọn có nhãn **Đọc thêm** trên mọi slide thuộc phần và trong mục lục. Không đặt kiến thức tiên quyết của phần chính vào phần đọc thêm; nếu cần, đưa phần tối thiểu trở lại mạch chính.
- Phần hướng dẫn thao tác và chạy mã có nhãn **Thực hành** trên mọi slide thuộc phần và được nhận diện trong mục lục. “Thực hành” không mặc nhiên có nghĩa là tùy chọn hoặc thay thế recitation.
- Dùng lớp CSS chung cho nhãn. Nhãn loại phần được phép hiển thị; mã nội bộ và nhãn quy trình tác tử vẫn không hiển thị.
- Phân bổ 120 phút chính và 60 phút recitation theo quy định; ghi riêng thời gian đọc thêm và chuẩn bị môi trường trước lớp, không tính hai lần. Khi gộp tổng kết và bài tập trong một section ngoài, tách thành hai cụm slide dọc liên tiếp, bài tập nằm sau phần giảng.

### 1. Giới thiệu và động lực

**Mạch:** tên bài và vị trí trong học phần → nội dung, mục tiêu → tình huống thực tế → giới hạn của cách quen thuộc → các nhu cầu chung → ví dụ đơn giản dẫn vào phương pháp.

- Slide tiêu đề có tên bài, tên môn và học kỳ. Slide “Nội dung” dùng tên các phần thực sự có trong deck; cập nhật ngay khi thêm, bỏ hoặc đổi phần. Mục tiêu dùng động từ như tính, mô phỏng, đặc tả, giải thích, cài đặt, thay cho “nắm được”.
- Slide tình huống chỉ rõ dữ liệu gì, cần đầu ra gì và vướng tài nguyên nào. Nếu nguồn có quy mô, ghi số lượng và đơn vị ngay cạnh đối tượng; phân biệt số liệu nguồn với giả định minh họa. Không tự ấn định mọi bài phải lấy ví dụ Google.
- Slide nhu cầu nhóm 2–3 ý liên quan, mỗi ý có icon hoặc hình nhỏ mang nghĩa và một câu giải thích. Các nhu cầu phải được giải quyết lại trong phần mô hình, chi phí hoặc hệ thống.
- Slide trực giác dùng thao tác quen thuộc và dữ liệu đủ nhỏ để tính được. Nêu tính chất cho phép biến đổi cách tính trước khi thay thao tác cụ thể bằng toán tử tổng quát. Giữ rõ điều kiện toán học và giới hạn số học máy khi chúng ảnh hưởng kết quả.
- Với dữ liệu phân tán, hình phân biệt tệp, khối, bản sao, máy và rack; cùng một khối dùng cùng nhãn ở các bản sao. Mũi tên và chú thích thể hiện chi phí di chuyển hoặc vị trí xử lý.

**Điều kiện đạt:** sinh viên nói được phương pháp sắp học giải quyết giới hạn nào; phần tiếp theo dùng lại ít nhất một nhu cầu hoặc ví dụ đã đặt ra.

### 2. Khái niệm hoặc mô hình

**Mạch:** khả năng cần có → bài toán minh họa → các thành phần trên bài toán ấy → quan hệ và thứ tự thực hiện → chạy tay → hình thức hóa tổng quát → điều kiện, giới hạn → kiểm tra.

- Slide mở phần nêu mô hình cho phép làm gì và điều kiện chính; không dùng danh sách tên thành phần thay cho khả năng. Mỗi ý có biểu tượng dễ hiểu, tránh hình trang trí.
- Slide bài toán ghi đầu vào, đầu ra, kích thước và giả thiết. Có thể đặt chữ/công thức bên trái khoảng 70%, hình minh họa bên phải khoảng 30%; điều chỉnh nếu hình cần lớn hơn. Nhãn phải gắn đúng từng đối tượng.
- Các slide cơ chế tách rõ từng thành phần và một slide thể hiện quan hệ giữa chúng. Dùng sơ đồ luồng với đầu vào–đầu ra có nhãn; chỉ rõ người lập trình quyết định gì, hệ thống làm gì nếu có hai vai trò này.
- Slide chạy tay giữ một bộ dữ liệu qua các pha; hiển thị trạng thái trung gian và kết quả có thể kiểm tra. Với quy trình nhiều pha, không bỏ ngầm bước phân phối, nhóm hoặc kết hợp quyết định kết quả.
- Slide hình thức hóa đặt ví dụ đã biết cạnh miền, kiểu và ánh xạ tổng quát. Định nghĩa ký hiệu trước khi dùng; nêu điều kiện ghép các hàm hoặc bước. Tách đặc tả từng hàm khỏi đặc tả toàn quy trình nếu quá tải.
- Tối ưu hóa phải có cơ chế và điều kiện bảo toàn kết quả. Chẳng hạn gộp cục bộ cần trạng thái gộp phù hợp; không suy từ một ví dụ phép cộng sang mọi hàm xử lý.

**Điều kiện đạt:** sinh viên ánh xạ được dữ liệu cụ thể vào ký hiệu, chạy được một lượt và chỉ ra trường hợp mô hình hoặc tối ưu hóa không áp dụng.

### 3. Thuật toán và ví dụ vận dụng

**Mạch:** phát biểu bài toán → ứng dụng → đặc điểm, khó khăn → ý tưởng → ví dụ dẫn nhập → đặc tả → vết chạy đối chiếu → chứng minh → chi phí hoặc nối sang phần chi phí → kiểm tra.

Ví dụ dẫn nhập có thể là một bước nhỏ để tạo trực giác; vết chạy sau đặc tả phải đủ để đối chiếu với giả mã. Nếu dùng một ví dụ cho cả hai vai trò, ghi cách nối trong storyboard. Khi mô hình đã được học và nguồn đặt đặc tả trước vết chạy, ghi lý do sắp xếp cục bộ; không bỏ cầu nối từ trực giác sang ký hiệu.

- Slide bài toán dùng công thức đầu vào–đầu ra, miền chỉ số, kích thước tổng quát và điều kiện trước. Không thu hẹp đặc tả chỉ vì ví dụ chạy tay dùng dữ liệu đặc biệt, như ma trận vuông.
- Slide ứng dụng nằm ngay sau phát biểu bài toán khi có ứng dụng phù hợp nguồn. Ánh xạ dữ liệu, biến và kết quả toán học vào tình huống sử dụng; không chỉ liệt kê tên ngành.
- Slide đặc điểm có icon kèm câu nêu khó khăn cụ thể: dữ liệu không vừa RAM, cần đọc lặp, trạng thái phụ thuộc nhau hoặc tải không đều. Slide ý tưởng cho thấy lựa chọn giúp xử lý khó khăn ấy.
- Slide đặc tả nêu đơn vị đầu vào thật của thuật toán: phần tử, dòng, khối, cạnh hoặc nhóm. Nếu xử lý theo khối, thể hiện vòng lặp trong khối. Giả mã dùng `return` cho giá trị trả về, `yield` cho luồng kết quả khi phù hợp; phân biệt trả kết quả với gửi dữ liệu qua mạng.
- Tách các hàm có vai trò riêng và chỉ ra kiểu đầu ra của hàm trước khớp đầu vào hàm sau. Với bước tối ưu tùy chọn, thuật toán vẫn phải đúng khi bước ấy bị bỏ hoặc được áp dụng theo các cách hệ thống cho phép.
- Slide “Ví dụ” dùng bảng trạng thái, ô dữ liệu hoặc sơ đồ; chỉ rõ bước đang chạy, dữ liệu vào, trạng thái đổi và đầu ra. Giữ nguyên ký hiệu, phân hoạch và giá trị giữa hình, giả mã, chứng minh và phép tính chi phí.
- Slide tính đúng nêu mệnh đề, giả thiết và ý tưởng chứng minh; các bước dài tách thành nhiều slide. Ví dụ đúng không thay cho chứng minh. Xử lý đầu vào rỗng, phần tử lặp và các ca biên ảnh hưởng kết luận.

**Điều kiện đạt:** sinh viên viết lại được đặc tả, mô phỏng ví dụ, giải thích vì sao đúng và chuyển các bước chính thành mã mà không phải tự đoán giao diện dữ liệu.

### 4. Chi phí và lợi ích

**Mạch:** quyết định cần so sánh → đại lượng cần đo → mô hình và giả thiết → nơi phát sinh chi phí → đếm từng bước → công thức → thay số → diễn giải lợi ích và giới hạn → bài áp dụng.

- Slide mở phần nói phép đo giúp chọn phương án hoặc dự báo giới hạn nào. Tách tổng lượng công việc, thời gian hoàn thành, bộ nhớ và lượng truyền; chọn các đại lượng thực sự cần cho bài.
- Với tính toán phân tán hoặc song song, phân biệt mô hình chi phí, mô hình thời gian chạy và mô hình băng thông. Không suy thời gian trực tiếp từ số tác vụ hoặc số bản ghi.
- Slide định nghĩa đại lượng giải thích tên, đơn vị, phạm vi và lý do đo. Chỉ đưa ký hiệu sẽ dùng ngay; không nhét toàn bộ bảng ký hiệu của chương. Dùng nhãn “Quy ước”; nguồn ghi riêng.
- Slide phép đếm dùng bảng bước–số lần–chi phí mỗi lần–đóng góp. Mỗi số hạng truy được về giả mã hoặc hình. Đưa biểu thức đếm trước ký hiệu tiệm cận.
- Slide thời gian dùng trục thời gian hoặc hàng theo máy/tác vụ để thấy bước nối tiếp và đồng thời. Nêu giả thiết về cân tải, số tài nguyên, chồng lấp và chi phí khởi động/truyền. Không mặc định cộng mọi pha hoặc chia thời gian cho số máy nếu lịch thực thi không cho phép.
- Slide băng thông chỉ rõ dữ liệu qua đường truyền nào, kích thước, đơn vị và tài nguyên dùng chung. Phân biệt tổng byte, tải của đường truyền nặng nhất và thời gian truyền theo mô hình đã chọn.
- Slide thay số dùng lại ví dụ trước. Ghi rõ số nào đếm từ thuật toán, số nào giả định, số nào đo thực nghiệm; không để số xuất hiện mà không có phép tính hoặc nguồn gốc.
- Slide lợi ích so sánh cùng bài toán, dữ liệu và phạm vi. Với hệ số tăng tốc $S_P=T_1/T_P$, giải thích các đại lượng và điều kiện; chỉ rõ chi phí nào giảm, giữ nguyên hoặc tăng. Không coi giảm trung gian là giảm thời gian cùng tỷ lệ.

**Điều kiện đạt:** sinh viên tự lập phép đếm và thay số cho bài tập nguồn, giải thích được lựa chọn tốt hơn theo tiêu chí nào và khi nào kết luận không còn đúng.

### 5. Hệ thống và cơ chế thực thi

**Mạch:** yêu cầu từ mô hình → kiến trúc và vai trò → dữ liệu được lưu ở đâu → tạo, phân chia và gán tác vụ → di chuyển, nhóm và xử lý → theo dõi → lỗi → phục hồi → giới hạn → kiểm tra.

- Slide kiến trúc dùng sơ đồ có nhãn vai trò và quan hệ; phân biệt đối tượng logic với tài nguyên vật lý, chẳng hạn tác vụ, lần thực thi, tiến trình, container, máy và rack.
- Slide phân phối chỉ rõ đơn vị chia, hàm/quy tắc phân phối và quyết định lập lịch. Tách “dữ liệu thuộc tác vụ nào” khỏi “tác vụ chạy trên máy nào”. Nêu quan hệ một–nhiều khi cần; không vẽ một máy luôn tương ứng một tác vụ.
- Slide lưu trữ thể hiện nơi giữ đầu vào, trung gian và đầu ra; bản sao có cùng mã khối. Với hệ thống tệp phân tán, giải thích hỗ trợ cục bộ dữ liệu và phục hồi bằng đúng cơ chế, không chỉ ghi tên phần mềm.
- Mỗi slide lỗi dùng một tình huống: trạng thái trước lỗi → thành phần mất → dữ liệu còn → phần phải chạy lại → kết quả được chấp nhận. Phân biệt sao chép dữ liệu với chạy lại hoặc chạy dự phòng; không cộng trùng kết quả của các lần thực thi.
- Nêu phạm vi chịu lỗi và điều kiện của phiên bản hoặc mô hình đang dạy. Chi tiết tùy chọn gắn “Đọc thêm”; phần thực hành phải có đủ kiến thức tối thiểu để làm mà không phụ thuộc nội dung đã đánh dấu tùy chọn.

**Điều kiện đạt:** sinh viên theo dõi được một đầu vào qua hệ thống và xác định phần nào phải phục hồi trong một tình huống lỗi cụ thể.

### 6. Thực hành và chuyển đặc tả thành mã

**Mạch:** mục tiêu và kết quả mong đợi → môi trường tối thiểu → kiểm tra sẵn sàng → dữ liệu và giao diện → mã từng thành phần → lệnh chạy → kết quả → kiểm chứng → thay đổi có kiểm soát và chẩn đoán lỗi.

Chỉ thêm phần này khi mục tiêu bài, nguồn hoặc yêu cầu người dùng có nội dung thực hành. Ngôn ngữ và công cụ phải phục vụ thuật toán, không tạo một nhánh học framework ngoài phạm vi.

- Slide mở phần ghi sinh viên sẽ chạy gì, cần chuẩn bị gì và thu được sản phẩm gì. Tách cài đặt dài sang hướng dẫn tải về; phân biệt bước chuẩn bị trước lớp với thời gian thực hành trên lớp.
- Slide môi trường có sơ đồ tối thiểu và vai trò thành phần. Với bài mô phỏng cụm trên một máy, ưu tiên image sẵn từ nguồn chính thức hoặc đáng tin cậy trên Docker Hub và Docker Compose; kiểm tra phiên bản, kiến trúc, tài nguyên, cổng và khả năng chạy tại thời điểm soạn. Không áp đặt Docker cho mọi bài.
- Slide dữ liệu ghi cấu trúc tệp/bản ghi, mẫu nhỏ và đầu ra mong đợi. Slide giao diện nối đối tượng toán học với kiểu dữ liệu, định dạng dòng, tham số hoặc luồng vào–ra mà mã thật dùng.
- Mỗi slide mã tập trung một chức năng, kèm câu giải thích nó thực hiện bước nào của đặc tả. Dùng khối mã có tô cú pháp, `data-trim`, chữ đọc được; mã hoàn chỉnh đặt trong tài nguyên tải về. Không lược phần quyết định tính đúng hoặc giao thức mà không chỉ rõ.
- Slide chạy ghi thư mục làm việc, lệnh có thể sao chép, đầu vào và nơi nhận kết quả. Giải thích chỗ sinh viên cần thay, điều kiện đường dẫn tồn tại/chưa tồn tại và ảnh hưởng của lệnh dọn môi trường.
- Slide kiểm chứng đối chiếu kết quả thật với chạy tay; dùng trạng thái công việc, bộ đếm và tệp đầu ra khi phù hợp. Tiến trình hoặc container đang chạy chưa chứng minh chương trình đúng.
- Chạy thử mã và lệnh từ đúng gói phát hành. Kiểm dữ liệu mẫu và ca biên có ý nghĩa, ghi phiên bản và giới hạn đã thử. Cụm container trên một host chỉ mô phỏng cơ chế; không dùng nó làm bằng chứng tăng tốc hoặc chịu lỗi của nhiều máy vật lý.

**Điều kiện đạt:** sinh viên làm theo tài liệu từ môi trường đã nêu đến kết quả kiểm chứng được, giải thích được mã tương ứng bước thuật toán nào và biết tìm thông tin lỗi ở đâu.

### 7. Tổng kết, kiểm tra và bài tập vận dụng

**Mạch:** quay lại nhu cầu đầu bài → hệ thống hóa lựa chọn → kiểm tra khái niệm → vận dụng qua bài tập nguồn → đối chiếu lời giải và giới hạn.

- Slide tổng kết liên kết bài toán, ý tưởng, điều kiện áp dụng và chi phí; không chép lại mục lục. Có thể dùng bảng ít cột để so sánh các phương pháp đã học.
- Cuối mỗi phần nội dung chính có slide “Câu hỏi kiểm tra”, hoặc một nhiệm vụ kiểm tra được ghi rõ trong storyboard nếu phần ngắn. Câu hỏi yêu cầu tính, truy vết, chọn, giải thích, chứng minh hoặc sửa một bước; tránh chỉ hỏi nhớ tên. Các lời mời tương tác trên slide vẫn dùng nhãn “Câu hỏi:”.
- Bài tập recitation giữ quy tắc lấy từ nguồn đã chỉ định. Ghi dữ kiện, yêu cầu và sản phẩm: đặc tả, vết chạy, chứng minh, phép tính chi phí hoặc mã khi bài nguồn có yêu cầu tương ứng. Không tự thêm yêu cầu lập trình vào mọi bài tập.
- Độ khó đi từ thực hiện một bước đã học tới kết hợp hoặc lựa chọn phương pháp, trong phạm vi bài nguồn. Lời giải, tiêu chí chấm và lỗi thường gặp nằm trong notes; thời lượng thuộc kế hoạch/ghi chú theo quy định, không trên mặt slide.

**Điều kiện đạt:** nhiệm vụ kiểm tra đo đúng đầu ra của phần; các bài tập có thể giải bằng kiến thức đã xây trong deck, không cần đoán một khái niệm hoặc công cụ chưa giới thiệu.

### Storyboard và rà soát theo khả năng vận dụng

Ngoài các trường bắt buộc hiện có, storyboard ghi cho từng slide: loại phần; thao tác sinh viên cần làm; đối tượng trung tâm; dữ kiện/ký hiệu kế thừa; và bằng chứng để kiểm tra đầu ra học tập. Không bắt mỗi slide có một bài tập riêng; chỉ rõ slide ấy chuẩn bị cho nhiệm vụ nào.

Trước khi chốt một phần, người soạn và reviewer phải kiểm tra:

1. Các khái niệm mới có tình huống hoặc ví dụ dẫn vào; ký hiệu được định nghĩa trước khi dùng.
2. Tiêu đề, hình/công thức/mã và câu chốt cùng phục vụ một mục đích; không thu nhỏ chữ để ghép nhiều mục đích.
3. Sinh viên theo được từ dữ liệu cụ thể tới đặc tả, chạy tay, lập luận và phép tính; có cầu nối tới mã nếu phần thực hành thuộc phạm vi.
4. Ví dụ, hình, công thức, mã và kết quả dùng cùng giả thiết; số liệu có nguồn hoặc được ghi là giả định.
5. Nhiệm vụ kiểm tra buộc sinh viên áp dụng điều vừa học; phần tùy chọn không giữ tiên quyết của nhiệm vụ bắt buộc.
6. Mục lục, nhãn phần, outline và storyboard khớp nội dung thực tế. Khi sửa một phần, rà các phần dùng chung ký hiệu, ví dụ hoặc kết quả.

Với quy trình xây bài từng phần, hoàn tất kế hoạch, nội dung, rà soát và kiểm định của phần trước khi chuyển mốc bàn giao. Commit/push sau mỗi phần theo quy định phát hành và chỉ dẫn hiện hành của người dùng; nếu người dùng yêu cầu chỉ commit hoặc chưa push thì tuân theo. Commit từng phần chỉ gồm sản phẩm của phần đã hoàn tất và cập nhật liên quan, không buộc đưa vào phần chưa xây xong. Khi viết lại từ đầu theo yêu cầu, lập mạch từ mục tiêu và nguồn; không dùng bố cục bản cũ làm khuôn mặc định.

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

## Văn phong và mật độ mặt trang chiếu

Mặt trang chiếu là văn bản toán học và thuật toán ngắn gồm tiêu đề, vài dòng mệnh đề, công thức, giả mã, bảng và nhãn. Diễn giải, động cơ chi tiết, đối chiếu ký hiệu và nguồn nằm trong ghi chú diễn giả; diễn giải dài hơn mức cần cho buổi giảng thuộc về ghi chú bài giảng. Các chuẩn trong mục này lấy từ bài giảng MAT1101 (Xác suất thống kê) của cùng tác giả tại `../MAT1101/` (13 bộ, 532 trang; trung vị 20 âm tiết chữ mỗi trang, 3 dòng, 6 âm tiết mỗi dòng; số đo và quyết định ghi tại `../math-4-AI/2627-1/planning/style-revision-2026-10-12.md`), đã được hai học phần `../math-4-AI` và `../rl-plan` áp dụng, và áp dụng cho mọi bộ trang chiếu của học phần này (yêu cầu người dùng 2026-10-14). Khi mục này và `slide_authoring_standard.md` cùng nói về một điểm, mục này cho số đo cụ thể, tiêu chuẩn cho cách xây dựng kiến thức; hai bên không mâu thuẫn.

### Mật độ chữ

Âm tiết được đếm bằng số từ tách theo khoảng trắng, không tính tiêu đề, công thức KaTeX, khối giả mã, ô số của bảng, nhãn trong hình và ghi chú diễn giả. Script đếm dùng chung của kho (nếu có) được ghi trong `review-log.md` kèm kết quả.

- Mỗi trang nội dung nhắm tới không quá 40 âm tiết chữ; trần cứng 60 âm tiết. Trang mục tiêu, nội dung, tổng kết, bảng so sánh và bảng chi phí có trần 80 âm tiết. Trang đề bài recitation chép nguyên bài sách có trần 80 âm tiết.
- Không quá sáu dòng nội dung, không tính tiêu đề; mỗi gạch đầu dòng, câu, dòng nhãn, hàng bảng hoặc khối công thức hiển thị tính là một dòng. Bảng vết chạy và bảng chi phí được tính theo số hàng thực tế nhưng không quá tám hàng.
- Mỗi dòng chữ không quá 20 âm tiết. Câu dài hơn được tách, rút thành mệnh đề, hoặc chuyển sang ghi chú.
- Không quá ba khối công thức hiển thị; một hệ `aligned` tính là một khối. Giả mã dài hơn tám dòng đứng một mình trên trang, kèm nhiều nhất một câu dẫn và một bảng trạng thái nhỏ; giả mã dài hơn hai mươi dòng tách theo chức năng sang các trang liên tiếp.
- Mỗi trang có nhiều nhất một khung nhấn chứa câu văn (`.question-box`, `.ex-card` có chữ, hoặc tương đương); khung không chứa quá hai câu. Các thẻ `.ex-card` chỉ chứa công thức hoặc số không tính là khung nhấn.
- Không dùng lớp hay thuộc tính thu nhỏ chữ (`.dense`, `font-size` nội dòng) để đạt các trần trên. Trang vượt trần phải được tách hoặc chuyển phần diễn giải sang ghi chú, và storyboard ghi quyết định `tách` hoặc `sửa` kèm số âm tiết trước và sau.
- Trang được phép vượt trần chỉ khi có ngoại lệ ghi trong `storyboard.md` kèm lý do. Tác tử rà soát xếp trang vượt trần không có ngoại lệ ở mức `trung bình`, trang vượt quá 1,5 lần trần ở mức `nghiêm trọng`.

### Câu trên mặt trang

- Viết mệnh đề toán học và thuật toán ngắn theo lối văn bản toán: "Đặt …", "Suy ra …", "Thế vào được …", "Do … nên …", "Với mỗi dải $j$ và cột $c$, tạo khóa …", "Giữ cặp có Jaccard gốc ít nhất $t$". Không dùng "ta thấy", "rõ ràng", "chúng ta", lời chỉ đường hay câu hỏi tu từ trên mặt trang; "ta" chỉ xuất hiện trong dòng tính toán ("ta được …") khi không bỏ được.
- Định nghĩa viết bằng "là" hoặc "gọi là"; không dùng dấu "=" thay cho động từ. Đặc tả thuật toán dùng hai dòng "Đầu vào:" và "Đầu ra:".
- Một trang có nhiều nhất một câu kết luận cuối trang. Câu đó phải là một kết luận có điều kiện hoặc một con số ("Với $b=20$, $r=5$, cặp có $s=0{,}8$ bị bỏ sót với xác suất xấp xỉ $0{,}00036$"); không dùng khẩu hiệu, ẩn dụ hay chuỗi mũi tên tóm tắt.
- Nguồn của trang (trang sách, số trang chiếu nguồn, mục giáo trình) ghi trong ghi chú diễn giả và trên trang "Nguồn và tài liệu đọc" của mạch kết luận, không ghi ở chân từng trang. Ghi công `http://www.mmds.org` đặt ở trang bìa hoặc trang nguồn.

### Mở một khái niệm hoặc một thuật toán

Trang vấn đề mở bằng một câu "Muốn …" hoặc nhãn "Nhu cầu:", tiếp theo là một đến ba ví dụ dẫn nhập cụ thể, có số liệu hoặc đối tượng đếm được, theo đúng cách MAT1101 mở "Khái niệm xác suất có điều kiện" bằng "Muốn đánh giá xác suất khi có một phần thông tin" rồi ba ví dụ (hai xúc sắc, xét nghiệm dương tính, từ ghép). Trong học phần này, ví dụ dẫn nhập là một bộ dữ liệu nhỏ tính tay được (bốn tập đặc trưng, một ma trận chữ ký hai hàng, năm phần tử của một dòng, một quan hệ vài khối) hoặc một quy mô có nguồn (số tài liệu, số cặp, số byte, số khối I/O lấy từ ví dụ của sách). Trang hình thức kế tiếp có thể giữ cùng tiêu đề với trang vấn đề. Bước trực giác đứng trước phát biểu hình thức; nhãn "Ý nghĩa:" sau một kết quả là diễn giải bổ sung, không thay cho bước trực giác.

Khi một phương pháp mới được đưa ra, mặt trang nêu giới hạn của phương pháp trước thành một dòng cụ thể (giáo trình *Học máy thống kê* của tác giả: "hàm chuyển và hàm phần thưởng thường không được biết trước nên hai thuật toán quy hoạch động không áp dụng được"; trong học phần này: "chữ ký đã vừa bộ nhớ nhưng số cặp vẫn là $\binom C2$") rồi mới nêu ý tưởng mới. Không mở một thuật toán bằng tên, viết tắt hoặc giả mã.

Một cụm thuật toán đi theo thứ tự mà giáo trình *Học máy thống kê* dùng cho KNN, cây quyết định và dò ngưỡng, cộng thêm các yêu cầu về tính đúng và chi phí của học phần:

1. giới hạn của cách làm trước, một dòng có số;
2. ý tưởng bằng lời, đặt cạnh thuật toán đã biết bằng cặp "tương tự … nhưng khác ở …" khi có thuật toán để so (giáo trình: "Cây quyết định cũng ước lượng $P(y\mid x)$ trong một lân cận như KNN, nhưng tính lân cận trong pha huấn luyện");
3. nhận xét cấu trúc cho phép làm tốt hơn cách ngây thơ (giáo trình: "dù chọn $\theta$ thế nào cũng chỉ có $n+1$ khả năng phân chia");
4. ví dụ chạy tay một bước hoặc một lượt trên dữ kiện nhỏ, có trạng thái trung gian kiểm tra được;
5. câu "Thuật toán có đầu vào là …, đầu ra là …" hoặc hai dòng "Đầu vào:", "Đầu ra:" ngay trước giả mã; giả mã dùng đúng ký hiệu của ví dụ;
6. đoạn đọc giả mã nêu thao tác quyết định và chỗ khung còn để ngỏ mà trang sau lấp (điều kiện dừng, cách chọn tham số, bước xác minh);
7. lập luận tính đúng theo `slide_authoring_standard.md`;
8. một câu chi phí có tham số gọi tên gắn vào dòng giả mã ("dựng thùng đọc $bC$ tuple dài $r$"), rồi mới đến bảng đếm và ký hiệu tiệm cận.

Nhược điểm của một thuật toán được chứng minh bằng một ví dụ cực đoan cụ thể trước khi nêu biến thể khắc phục (giáo trình: thuộc tính "số thẻ tín dụng" làm mỗi nhánh của ID3 chỉ còn một mẫu).

### Trang phát biểu kết quả

Một trang định lý, mệnh đề, bất đẳng thức hoặc tính chất của thuật toán gồm:

1. Phát biểu có giả thiết và kết luận.
2. Tùy chọn một dòng "Ý nghĩa:" đọc kết quả bằng lời (MAT1101: "Nếu phương sai nhỏ thì biến không quá xa khỏi kỳ vọng của nó"; ở đây: "Cặp càng tương đồng thì càng dễ trùng ít nhất một dải").
3. Tùy chọn một dòng "Chứng minh." nêu ý chính khi chứng minh gói trong một đến hai dòng ("Lấy biến cố bù của 'không dải nào trùng' và dùng độc lập giữa các dải").

Chứng minh dài hơn đặt ở trang riêng có tiêu đề "Chứng minh: <tên kết quả>", chia bước, mỗi trang một kết quả. Lập luận tính đúng của thuật toán đặt ở trang "Tính đúng: <tên thuật toán>" với bảng khởi tạo–duy trì–kết thúc hoặc các bước được đánh số. Không đặt định lý, chứng minh nhiều bước, ví dụ và nhận xét phạm vi trên cùng một trang. Với kết quả xác suất, kỳ vọng hoặc cận, phát biểu nêu rõ giả thiết quyết định (độc lập, phân phối chọn hàm, tập hữu hạn không rỗng, mô hình chi phí) ngay trên mặt trang.

### Trang thuật toán và trang chi phí

- Trang đặc tả có tiêu đề "Thuật toán: <tên>" hoặc tên thuật toán, hai dòng "Đầu vào:" và "Đầu ra:", rồi khối giả mã; nhiều nhất một câu dẫn nêu thao tác quyết định (nhóm, chia, chọn, cập nhật, loại bỏ). Vết chạy đối chiếu đặt cạnh giả mã khi vừa khung, nếu không thì ở trang kế tiếp cùng tiêu đề.
- Trang chi phí có tiêu đề "Chi phí: <đối tượng>" hoặc tên đại lượng; dòng đầu là "Mô hình:" nêu đơn vị và quy tắc đếm; bảng `Bước | Số lần | Chi phí mỗi lần | Đóng góp` theo `slide_authoring_standard.md`; một dòng tổng; nhiều nhất một câu kết luận có điều kiện. Tách trang khi cần cả bảng đếm lẫn bảng thay số.
- Phần tùy chọn của thuật toán, mô hình chi phí thay thế hoặc chứng minh cận chỉ dành cho người đọc tự học đặt trong ghi chú bài giảng, không trên mặt trang.

### Trang ví dụ

Tiêu đề có dạng "Ví dụ: <đối tượng>", trong đó đối tượng là cụm danh từ ("Ví dụ: bốn tập đặc trưng", "Ví dụ: hai dải, một hàng mỗi dải", "Ví dụ: kho một triệu tài liệu"). Trang theo thứ tự:

1. Dữ kiện có số: tập, ma trận, vector, tham số, ngưỡng, giá trị khởi tạo.
2. Yêu cầu bằng động từ học tập ("Tính …", "Xác định …", "Liệt kê …").
3. Các bước, mỗi bước một dòng hoặc một hàng bảng; với thuật toán ghi rõ trạng thái trước, thao tác và trạng thái sau.
4. Kết quả kèm "Diễn giải:" hoặc dòng kiểm tra.

Khi một ví dụ kéo dài nhiều trang, mỗi trang thêm tên bước sau dấu phẩy, ví dụ "Ví dụ: bốn tập đặc trưng, thùng của dải 2".

### Trang bài tập

Tiêu đề có dạng "Bài tập: <chủ đề>"; nhiều phần thì thêm "(a)", "(b)". Đề bài mở bằng nhãn "Câu hỏi:", được gõ bằng chữ và KaTeX, không chụp ảnh từ sách; dữ kiện dạng bảng dùng cùng khuôn bảng với ví dụ dẫn nhập để sinh viên nhận ra cấu trúc chung. Ghi chú diễn giả của trang đề bài nêu bài tập kiểm tra năng lực nào và một dòng "Gợi ý:" về bước mở đầu.

- **Bài tập có lời giải mẫu:** lời giải trình bày trên mặt trang dưới nhãn "Lời giải:" ở trang kế tiếp cùng tiêu đề (học phần không dùng `fragment`), mỗi dòng một bước lập luận, kết thúc bằng một kết luận ngắn (MAT1101: "Alice đúng", "Khi $\epsilon$ giảm còn một nửa thì $n$ cần tăng 4 lần").
- **Bài tập để người học tự làm** và các trang "Câu hỏi" cuối mạch: gợi ý và lời giải đặt trong ghi chú diễn giả.
- **Bài tập recitation:** giữ quy tắc lấy nguyên bài sách ở mục "Đối tượng và thời lượng"; tiêu đề "Bài tập: <chủ đề>" kèm số bài sách trong ghi chú diễn giả và storyboard.

Mỗi mạch nội dung chính có ít nhất một bài tập có lời giải mẫu trên mặt trang hoặc một trang "Câu hỏi" có lời giải trong ghi chú; storyboard ghi bài tập thuộc loại nào. Khi ghi chú bài giảng có bài trùng với bài tập trên trang chiếu, hai lời giải phải cho cùng kết quả.

### Ví dụ xuyên suốt

Mỗi bài chọn một đến hai bộ dữ liệu hoặc tình huống nhỏ, tính tay được, và dùng lại qua nhiều khái niệm. Mỗi lần dùng lại phải trả lời một câu hỏi mới hoặc so sánh hai công cụ trên cùng số liệu (MAT1101 so cận Chebyshev với định lý giới hạn trung tâm trên cùng bài khảo sát ý kiến; trong học phần này: hai cấu hình $(b,r)$ trên cùng chữ ký, hai thứ tự ghép AND/OR trên cùng họ cơ sở, hai thuật toán nối trên cùng quan hệ). Gọi ví dụ bằng tên đối tượng ("bốn tập đặc trưng", "kho một triệu tài liệu", "quan hệ 10 000 khối"), không bằng mã ("V02", "VD1"). Dữ kiện được nêu lại trên trang dùng lại. Tình huống dữ liệu lớn mở bài phải là một trong các ví dụ xuyên suốt hoặc được thu hồi ở mạch kết luận bằng con số.

### Bảng

Dùng bảng so sánh khi hai đến bốn phương án được đối chiếu theo cùng tiêu chí (các độ đo trên cùng hai điểm; các cấu hình $(b,r)$; các thuật toán nối theo số khối I/O). Một phép tính lặp lại nhiều lần (bảng thùng theo dải, bảng vết chạy, bảng chi phí) dùng một khuôn bảng cố định với cùng tên cột trong toàn bài.

### Nhãn dẫn dắt

Chỉ dùng các nhãn sau, viết đậm:
- **Môi trường hình thức, kết thúc bằng dấu chấm:** "Định nghĩa.", "Định lý.", "Mệnh đề.", "Bổ đề.", "Hệ quả.", "Nhận xét.", "Thuật toán.", "Chứng minh.", "Trực quan.", "Ví dụ.".
- **Nhãn dẫn, kết thúc bằng dấu hai chấm:** "Nhu cầu:", "Ý nghĩa:", "Diễn giải:", "Lưu ý:", "Nhắc lại:", "Cách khác:", "Dạng khác:", "Ký hiệu:", "Quy ước:", "Giả thiết:", "Kết luận:", "Đầu vào:", "Đầu ra:", "Bất biến:", "Điều kiện dừng:", "Trường hợp biên:", "Mô hình:", "Câu hỏi:", "Gợi ý:", "Lời giải:", "Đọc trước:", "Nguồn:".

Nhãn loại phần "Đọc thêm" và "Thực hành" theo mục "Phân loại phần lớn" vẫn được dùng. Không dùng nhãn quy trình, nhãn cảm thán hay nhãn quảng bá.

### Mã nội bộ của bài khác

Mặt trang phát biểu giả thiết và kết quả bằng lời, và gọi ví dụ bằng tên đối tượng. Mã nội bộ kiểu "N02", "V02", "HT3", "MT1" không xuất hiện trên mặt trang. Sau phát biểu bằng lời được kèm số hiệu kết quả của ghi chú bài giảng, dạng "(Định lý 06.3)", tối đa một lần mỗi trang.

### Những điểm của MAT1101 và giáo trình không áp dụng

Không bắt chước từ MAT1101: dấu cách trước dấu hỏi; câu hỏi không có nhãn; tiêu đề "Bài tập" không có chủ đề; đề bài dạng ảnh; dấu "=" thay cho "là"; thuật ngữ tiếng Anh hay viết tắt chưa giải thích; địa chỉ web trên mặt trang ngoài trang nguồn; lịch sử dạng danh sách năm–tên; trang thiếu ghi chú diễn giả hoặc ghi chú chỉ là ghi chú biên soạn; trang "Nội dung" không đánh số; ví dụ xác suất thuần túy thay cho tình huống dữ liệu lớn của học phần.

Không bắt chước từ giáo trình *Học máy thống kê*: giọng quảng bá của lời nói đầu; mở chương bằng đoạn chung chung lấy tài liệu làm chủ ngữ; tên hàm hoặc viết tắt tiếng Anh chưa giải thích (`chooseAttribute`, "DT"); ví dụ chạy tay chỉ xuất hiện ở bài tập cuối chương; chi phí viết thành một câu $O(\cdot)$ không có phép đếm và không phân biệt xấu nhất với kỳ vọng; hình raster; "dễ thấy".

## Tiêu chuẩn trang chiếu và ghi chú diễn giả

- Mỗi trang chiếu có một luận điểm trung tâm. Tách chứng minh, giả mã, bảng vết chạy hoặc công thức truy hồi quá dài thay vì thu nhỏ chữ.
- Tiêu đề ngắn, trang trọng và gọi đúng khái niệm, thuật toán hoặc kết quả trung tâm. Không đặt tiêu đề dưới dạng câu hỏi như “Tại sao...?”, “Vì sao...?”, câu kể tiến trình như “Từ ... đến ...”, lời trò chuyện hoặc lời chỉ dẫn người soạn. Dùng tên nội dung cụ thể, chẳng hạn “Bất biến vòng lặp” hoặc “Chi phí truyền dữ liệu”; đặt động cơ và quan hệ suy luận trong nội dung hoặc ghi chú. Được dùng tiền tố chức năng trước cụm danh từ: `Ví dụ: <đối tượng>`, `Bài tập: <chủ đề>`, `Chứng minh: <tên kết quả>`, `Tính đúng: <tên thuật toán>`, `Thuật toán: <tên>`, `Chi phí: <đối tượng>`; tiền tố không đứng một mình. Tiêu đề được lặp qua nhiều trang khi một khái niệm hay ví dụ kéo dài.
- Văn bản thân bài nên từ `0.75em` trở lên. Chỉ dùng dưới `0.65em` cho chú thích ngắn đã được tác tử góc nhìn sinh viên xác nhận là đọc được.
- Mỗi gạch đầu dòng không quá hai dòng ở khung 16:9. Chuyển diễn giải dài sang ghi chú diễn giả.
- Công thức, giả mã và hình trung tâm phải đủ lớn, có khoảng trắng và không bị cắt.
- Mọi lời mời tương tác trên mặt trang chiếu dùng nhãn **“Câu hỏi:”**.
- Không hiển thị mã nội bộ, nhãn quy trình, phân tuyến hoặc thời lượng trên mặt trang chiếu hay trong ghi chú diễn giả.
- Mỗi trang nội dung có `<aside class="notes">` khi cần giải thích giả thiết, lập luận đúng, lỗi dễ mắc, chuyển ý, đáp án hoặc nguồn.
- Ghi chú diễn giả là phần diễn giải học thuật ngắn, thuần Việt: giả thiết, giải thích công thức hoặc hình, lập luận đúng, phân biệt dễ nhầm, quan hệ với nội dung kế tiếp và gợi ý hoặc lời giải bài tập. Gợi ý phải nêu cách lập luận hoặc bước toán học, không hướng dẫn giảng viên phải nói, nhấn mạnh hay điều phối lớp thế nào. Không chỉ chứa siêu dữ liệu và không lặp nguyên văn nội dung hiển thị.
- Câu nối phải nêu kết quả được kế thừa, giả thiết thay đổi hoặc giới hạn dẫn tới nội dung kế tiếp. Không dùng lời chỉ đường như “tiếp theo chúng ta…” thay cho quan hệ suy luận.
- Ghi chú diễn giả nên dài khoảng 40–150 âm tiết; trang chứng minh, tính đúng hoặc lời giải có thể tới khoảng 250 âm tiết. Khoảng này là khuyến nghị: ghi chú dài hơn chỉ bị xếp mức `nhẹ`, và mọi ghi chú vẫn phải có đủ giả thiết, diễn giải, phân biệt dễ nhầm và lời giải khi trang có bài tập. Không mở ghi chú bằng “Trang này …”, “Slide này …” hoặc câu lấy tài liệu làm chủ ngữ; mở bằng đối tượng toán học hoặc kết quả kế thừa.
- Nguồn của trang (số trang hoặc trang chiếu của bản nguồn, mục của giáo trình) ghi trong ghi chú diễn giả và trên trang "Nguồn và tài liệu đọc" của mạch kết luận, không ghi ở chân từng trang. Dòng nguồn trên mặt trang chỉ còn ở trang bìa (ghi công MMDS) và trang đề bài recitation (số bài sách).
- Bộ trang chiếu phải dùng được bằng bàn phím, có tương phản đủ và không dùng màu làm tín hiệu duy nhất.

## Quy trình đa tác tử cho bộ trang chiếu

### 1. Điều phối và lập kế hoạch

Điều phối viên kiểm kê nguồn và xác nhận đầu ra. Giao một tác tử lập kế hoạch riêng trước khi phân tích chi tiết hoặc sửa tệp.

Tác tử lập kế hoạch:

- dùng `slide_authoring_standard.md` để xác định mục đích từng trang, kiến thức đầu vào, sản phẩm học tập và kết nối vào–ra của từng cụm;
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

- áp dụng `slide_authoring_standard.md` cho từng cụm thuật toán, ví dụ, đánh giá chi phí và hình minh họa; phân bổ các yêu cầu của cả cụm qua các slide, không dồn tất cả lên một trang;
- tạo `outline.md`, `storyboard.md`, HTML và SVG theo đặc tả;
- dịch và biên tập tiêu đề, nội dung, nhãn hình và ghi chú bằng tiếng Việt học thuật theo kỹ năng `no-ai-slop`; tự kiểm bằng `eval.md`, loại văn nói và chỉ dẫn nội bộ;
- dùng kỹ năng `quill` để kiểm tra mạch phần, chuyển ý, thuật ngữ và ký hiệu;
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
- kiểm tra mỗi mạch trừ mạch mở đầu có trang tiêu đề mạch đúng mục "Trang tiêu đề mạch", số và tên khớp trang "Nội dung", và trang nội dung đầu mạch không trùng tiêu đề với tên mạch; kiểm tra mạch mở đầu và mạch kết luận có các trang quy định ở mục "Mẫu RevealJS bắt buộc";
- đo số âm tiết chữ, số dòng và âm tiết mỗi dòng của từng trang theo mục "Văn phong và mật độ mặt trang chiếu"; liệt kê trang vượt trần và đối chiếu với ngoại lệ trong storyboard;
- kiểm tra thời lượng 120 phút, kiến thức tiên quyết và quan hệ trước–sau;
- kiểm tra phần bài tập đủ 60 phút recitation, có lời giải hoặc hướng dẫn chấm trong ghi chú và sử dụng đúng kiến thức của phần giảng;
- đề xuất quyết định, bằng chứng và tác động đến trang lân cận;
- không sửa tệp.

Sau thay đổi số lượng hoặc thứ tự, phải rà lại các trang bị ảnh hưởng và hai trang lân cận mỗi phía.

### 5. Năm tác tử rà soát độc lập

Sau bản nháp đầu, giao năm tác tử chỉ đọc rà soát độc lập. Chạy song song trong giới hạn tác tử khả dụng; chia thành các đợt nếu cần và chờ đủ năm báo cáo trước khi chỉnh sửa. Mỗi báo cáo dùng các trường `mức độ`, `trang chiếu`, `vấn đề`, `bằng chứng`, `đề xuất sửa`.

- **Góc nhìn sinh viên:** kiểm tra tiên quyết, tải nhận thức, nhịp giảng, khả năng đọc, ví dụ chạy tay, chuyển ý, câu hỏi kiểm tra và khả năng tự học. Đo số âm tiết chữ của từng trang theo mục "Văn phong và mật độ mặt trang chiếu"; trang vượt trần mà không có ngoại lệ ghi trong storyboard xếp mức `trung bình`, trang vượt quá 1,5 lần trần xếp mức `nghiêm trọng`.
- **Chuyên gia giải thuật và khoa học dữ liệu:** kiểm tra độ bao phủ, chiều sâu, thuật ngữ, mạch học thuật, sự phù hợp với học phần và thời lượng 120 phút.
- **Độ chính xác toán học và thuật toán:** kiểm tra đặc tả, giả thiết, chỉ số, trường hợp biên, giả mã, bất biến, chứng minh, hệ thức truy hồi, kết quả số và độ phức tạp.
- **Phản biện học thuật và giảng dạy:** kiểm tra mỗi hình thức hóa có đủ trực giác, ví dụ và tiên quyết; mỗi thuật toán và chứng minh xuất hiện đúng chỗ; thứ tự hiện tại có hỗ trợ suy luận trên lớp hay không. Rà tiêu đề, nội dung, nhãn hình và ghi chú theo kỹ năng `no-ai-slop`, bảo toàn độ chính xác; chỉ rõ văn nói, lời trò chuyện và chỉ dẫn dành cho người soạn còn xuất hiện. Tác tử này phải nêu rõ khi một công thức hoặc thuật toán đúng riêng lẻ nhưng được đặt sai trình tự hoặc thiếu cầu nối sư phạm.
- **Kết nối và mạch viết:** kiểm tra xương sống lập luận của toàn bài, điểm xuất phát, đích đến và sự tích lũy ý nghĩa qua từng phần; xác nhận bài có từ 5 đến 7 mạch trình bày lớn tương ứng với các `<section>` ngoài, gồm mạch mở đầu và mạch kết luận, trừ ngoại lệ đã được ghi rõ. Với mỗi phần, xác định chức năng, kết nối vào từ phần trước, đầu ra cho phần sau và đóng góp vào mục tiêu bài học; với mỗi trang, kiểm tra vai trò trong mạch cùng câu nối với trang liền trước và liền sau. Phát hiện bước nhảy lập luận, chuyển phần đột ngột, trang đứng riêng lẻ, phần lặp chức năng, tuyến không tiến triển, kết luận không thu hồi vấn đề mở đầu hoặc nhiều trang tranh cùng một luận điểm trung tâm. Vai này không thay thế kiểm định storyboard, rà độ chính xác hay rà tải nhận thức. Trong `bằng chứng` và `đề xuất sửa`, phải nêu rõ `vai trò trong mạch`, `kết nối vào` và `kết nối ra` của trang hoặc cụm trang bị ảnh hưởng.

Mức độ gồm `chặn bàn giao`, `nghiêm trọng`, `trung bình`, `nhẹ`. Mọi lỗi `chặn bàn giao` và `nghiêm trọng` phải được xử lý.

Đối với vai kết nối và mạch viết, dùng mức `chặn bàn giao` khi thiếu mạch mở đầu hoặc mạch kết luận, số mạch ngoài khoảng 5–7 mà không có ngoại lệ hợp lệ, không xác định được tuyến chính hoặc kết luận mâu thuẫn với vấn đề đã thiết lập; `nghiêm trọng` khi một phần trọng tâm bị đứt khỏi tuyến chính, lặp chức năng hoặc không tạo bước tiến; `trung bình` khi điểm vào, đầu ra hay câu chuyển giữa hai phần còn mờ; `nhẹ` khi mạch đúng nhưng tín hiệu chuyển ý hoặc thứ bậc nhấn chưa rõ. Sau khi thêm, bỏ, gộp, tách, đổi thứ tự trang hoặc sửa câu chuyển làm thay đổi mạch bài, phải giao lại vai này rà các trang bị ảnh hưởng, hai trang lân cận mỗi phía và mọi ranh giới phần liên quan. Nếu thay đổi mở bài, kết bài hoặc luận điểm trung tâm, phải rà lại toàn bộ bộ trang chiếu.

### 6. Chỉnh sửa

Giao một tác tử chỉnh sửa riêng sau khi năm báo cáo hoàn tất:

- hợp nhất vấn đề trùng lặp và ưu tiên tính đúng, khả năng học, khả năng đọc;
- sửa tuần tự HTML, SVG, outline, storyboard và ghi chú;
- ghi quyết định đối với đề xuất không áp dụng;
- không thay đổi mạch nguồn nếu lỗi có thể sửa cục bộ;
- yêu cầu rà lại độ chính xác cho mọi chứng minh, phân tích độ phức tạp hoặc thuật toán đã đổi đáng kể.
- yêu cầu tác tử kết nối và mạch viết rà lại theo phạm vi ở mục 5 sau mọi thay đổi cấu trúc, thứ tự, câu chuyển hoặc luận điểm trung tâm.

Các tác tử sửa tệp không được chạy song song.

### 7. Kiểm định cuối

Điều phối viên hoặc tác tử kiểm thử riêng phải:

- đối chiếu sáu nhóm yêu cầu và phiếu kiểm tra trong `slide_authoring_standard.md`; rà nội dung trên bản trình chiếu thực, ghi kết quả cùng lỗi cần sửa vào `review-log.md`;
- đối chiếu số trang nguồn, bảng ánh xạ, `data-slide-id` và mục tương ứng trong storyboard;
- kiểm tra HTML, cấu trúc `<section>`, KaTeX, tiện ích, ghi chú diễn giả, đường dẫn, SVG và liên kết;
- kiểm tra bài có từ 5 đến 7 `<section>` ngoài, gồm mạch mở đầu và mạch kết luận, hoặc có ngoại lệ hợp lệ đã được ghi trong storyboard và nhật ký;
- tìm mọi tham chiếu ảnh raster; chỉ chấp nhận mục có ngoại lệ đã được người dùng duyệt và ghi trong nhật ký;
- chạy phép đếm mật độ (âm tiết chữ, số dòng, âm tiết mỗi dòng) cho mọi trang và đính kèm kết quả vào `review-log.md`; xác nhận không trang nào vượt trần mà không có ngoại lệ ghi trong storyboard, và không trang nào dùng lớp thu nhỏ chữ để đạt trần;
- kiểm tra mọi trang tiêu đề mạch hiển thị đúng ở 1600×900 và 390×844, số mạch khớp `#/N` và trang "Nội dung"; kiểm tra trang bìa có câu luận đề, mạch mở đầu và mạch kết luận có đủ các trang quy định;
- kiểm tra không có tài nguyên hỏng hoặc phụ thuộc mạng cốt lõi;
- chạy `python3 -m reloadserver 8765` tại thư mục gốc; cổng là đối số vị trí, không dùng `--port`;
- mở `http://localhost:8765/2627-1/lecture-NN-<ten-bai>.html` và duyệt mọi trang ngang, trang dọc;
- kiểm tra tràn chữ, chữ nhỏ, chồng lấn, công thức, giả mã, hình, tương phản và bàn phím ở khung 16:9 và một màn hình hẹp;
- rà soát trực quan sau cùng bằng trình duyệt, lưu ảnh chụp màn hình ở khung 16:9 và màn hình hẹp cho các trang bị ảnh hưởng, và xác minh thay đổi đã được lưu trong tệp của kho và hiển thị đúng;
- kiểm tra đủ năm báo cáo độc lập; mọi vấn đề về vai trò trong mạch, kết nối vào–ra và tuyến lập luận phải có quyết định cùng bằng chứng rà lại;
- chạy lại kiểm định sau mỗi lần sửa lỗi chặn bàn giao hoặc nghiêm trọng.

Nếu không mở được trình duyệt để rà soát trực quan, phải báo rõ giới hạn, tiếp tục đầy đủ các kiểm tra tĩnh còn lại và không tuyên bố đã kiểm tra trực quan.

## Cập nhật `index.html`

- `2627-1/index.html` là danh mục riêng của học phần **Giải thuật nền tảng của Khoa học dữ liệu** cho học kỳ 1 năm học 2026–2027.
- Mỗi bài hoàn thành có một `article.term-card` theo thứ tự số bài, gồm nhãn `Bài N`, tên bài, mô tả một câu và nhóm tài nguyên có nhãn rõ.
- Nhóm tài nguyên luôn có `Bài giảng` và `Ghi chú bài giảng`. `Bài giảng` liên kết tới `lecture-NN-<ten-bai>.html`. `Ghi chú bài giảng` liên kết qua `material-viewer.html?doc=materials/lec-NN/lecture-note.md&deck=lecture-NN-<ten-bai>.html` chỉ sau khi Markdown đã vượt kiểm định; trước đó hiển thị `Chưa có` dưới dạng trạng thái, không tạo liên kết giả.
- Nếu sau này có tệp bài tập công khai riêng đã được kiểm định, thêm tài nguyên `Bài tập` theo cùng mẫu. Phần recitation đang nằm trong bộ trang chiếu không được trình bày như một tệp bài tập độc lập.
- Không đặt liên kết đến `outline.md`, `storyboard.md`, `review-log.md`, `note-for-author.md` hoặc thư mục `planning/` trên trang chỉ mục. Các tệp quy trình chỉ dùng nội bộ trong kho.
- Không thêm bài chưa hoàn thành hoặc liên kết đến tệp chưa tồn tại.
- Kế thừa cách nhóm tài nguyên và trạng thái `Chưa có` từ `../math-4-AI/2627-1/index.html`, nhưng giữ nhận diện, mô tả và đường dẫn của học phần này. Dùng lớp CSS dùng chung; không tạo kiểu nội dòng nếu chưa có nhu cầu được kiểm chứng.
- Sau khi sửa, kiểm tra tiêu đề, nhãn học kỳ, thứ tự thẻ, đường dẫn tương đối, bàn phím và hiển thị ở màn hình rộng lẫn hẹp.

## Commit và đẩy lên kho từ xa

Mỗi bộ trang chiếu hoặc ghi chú bài giảng công khai chỉ được coi là hoàn tất sau khi đã vượt toàn bộ tiêu chí kiểm định, được commit và đẩy lên `origin`.

- Trước khi commit, chạy `git status --short` và kiểm tra diff. Không đưa tệp tạm, `.DS_Store`, tệp có tiền tố `._`, bí mật, thông tin xác thực hoặc tài sản ngoài phạm vi bài vào commit.
- Commit phải chứa trọn bộ đầu ra của bài: HTML, SVG, ba tệp quy trình và thay đổi tương ứng trong `2627-1/index.html`. Chỉ kèm thay đổi ở tệp dùng chung hoặc nguồn khi chúng thực sự thuộc cùng công việc và đã được kiểm tra.
- Với yêu cầu chỉ làm ghi chú bài giảng, commit phải chứa `lecture-note.md`, SVG mới hoặc đã sửa, các thay đổi quy trình liên quan, mục tài nguyên trong `index.html` và hạ tầng viewer thực sự cần. Không buộc đưa HTML bài giảng vào commit nếu tệp đó không thay đổi.
- Không gộp thay đổi chưa hoàn tất của bài khác. Không sửa, xóa hoặc hoàn tác thay đổi của người dùng để làm sạch commit.
- Dùng thông điệp commit dạng `feat(lecture-NN): add <ten-bai> slide deck` cho bài mới hoặc `fix(lecture-NN): revise <ten-bai> slide deck` cho lần sửa đáng kể.
- Dùng `feat(materials-NN): add <ten-bai> lecture note` cho ghi chú mới hoặc `fix(materials-NN): revise <ten-bai> lecture note` cho lần sửa đáng kể.
- Sau commit, đẩy nhánh `main` bằng `git push origin main`; ở lần đẩy đầu có thể dùng `git push -u origin main`.
- Không dùng `--force`, `--force-with-lease`, rebase hoặc viết lại lịch sử từ xa nếu người dùng không yêu cầu rõ.
- Nếu push thất bại do xác thực, mạng hoặc lịch sử từ xa thay đổi, giữ nguyên commit cục bộ, ghi lại lỗi và báo người dùng. Không tuyên bố đã bàn giao hoàn tất khi commit chưa xuất hiện trên `origin`.

## Tiêu chí hoàn thành

Chỉ bàn giao một bộ trang chiếu khi:

- các yêu cầu áp dụng của `slide_authoring_standard.md` đã được kiểm tra, mọi lỗi bắt buộc đã được xử lý và ngoại lệ có lý do được ghi trong storyboard cùng nhật ký;
- bản RevealJS giữ đúng ý chính và mạch nguồn, còn mọi sai khác đều được ghi;
- tiêu đề, nội dung, nhãn hình và ghi chú bằng tiếng Việt, đạt văn phong trang trọng, học thuật, đã biên tập và tự kiểm theo kỹ năng `no-ai-slop`; không còn văn nói hay chỉ dẫn biên soạn, điều phối nội bộ;
- outline, storyboard và nhật ký nằm đúng `planning/lec-NN/`;
- mọi hình đã được vẽ lại thành SVG hoặc có ngoại lệ raster được người dùng duyệt;
- năm báo cáo độc lập đã có và mọi lỗi bắt buộc đã được xử lý;
- bài có 5–7 mạch lớn gồm mở đầu và kết luận, hoặc ngoại lệ đã được ghi và duyệt; mỗi mạch trừ mạch mở đầu có trang tiêu đề mạch; báo cáo kết nối và mạch viết không còn lỗi bắt buộc;
- không trang nào vượt trần mật độ mà không có ngoại lệ trong storyboard; kết quả đếm mật độ nằm trong `review-log.md`;
- đặc tả, ví dụ chạy tay, giả mã, chứng minh, trường hợp biên và độ phức tạp đã được kiểm tra;
- bộ trang chiếu chạy tại cổng `8765`, không có lỗi hiển thị hoặc tài nguyên hỏng nghiêm trọng;
- `index.html` liên kết đúng tới tệp HTML của bài và không liên kết tới các tệp quy trình;
- bản RevealJS trong kho là đúng phiên bản đã được rà soát trực quan trên trình duyệt, hoặc giới hạn công cụ đã được ghi rõ;
- commit của bài đã được đẩy thành công lên nhánh `main` của `origin`.

Chỉ bàn giao một ghi chú bài giảng khi:

- goal, bản đồ chủ đề và phạm vi nguồn đã được điều phối viên duyệt;
- Markdown đọc độc lập với slide, có nguồn truy nguyên và dùng cùng ký hiệu, giả thiết, ví dụ cùng bài;
- tiêu đề, diễn giải và lời giải đạt văn phong trang trọng, học thuật, đã biên tập và tự kiểm theo kỹ năng `no-ai-slop`; không còn văn nói hay chỉ dẫn dành cho người soạn;
- mọi chủ đề `cốt lõi`, `cầu nối` và `bổ sung` đã được xử lý theo quyết định; nội dung `đọc thêm` được tách rõ;
- định nghĩa, ví dụ, trực quan hoặc hình học, định lý, thuật toán, chứng minh, trường hợp biên, chi phí và câu hỏi kiểm tra đã được trình bày khi áp dụng;
- năm báo cáo dành cho ghi chú đã có, mọi lỗi `chặn bàn giao` và `nghiêm trọng` đã được sửa và phần thay đổi đã được rà lại;
- viewer hiển thị đúng Markdown, công thức, SVG, khối nội dung, mục lục và liên kết trên màn hình rộng, màn hình hẹp, bàn phím và bản in;
- `index.html` chỉ liên kết tới ghi chú đã vượt kiểm định và không lộ tài liệu quy trình;
- commit của ghi chú đã được đẩy thành công lên nhánh `main` của `origin`.

Khi bàn giao, nêu ngắn gọn: tệp sản phẩm, URL cục bộ, nguồn chính, chủ đề bổ sung đã duyệt, hình đã vẽ lại, các kiểm tra đã chạy, sai khác có chủ ý, ngoại lệ và giới hạn còn lại.

## Điều phối mô hình trong dự án

- Phiên Claude Code chính giữ vai trò điều phối viên kiêm kiểm soát chất lượng và chạy **Claude Fable 5.1** (`claude-fable-5-1`) (chỉ dẫn thường trực của người dùng 2026-10-07 cho `../math-4-AI`, được `../rl-plan` và học phần này áp dụng từ 2026-10-14): phân rã công việc, viết brief, duyệt kế hoạch, hợp nhất kết quả, đọc diff và chấp nhận hoặc bác bỏ từng đầu ra của tác tử con. Điều phối viên không tự đảm nhận vai soạn, rà soát hay chỉnh sửa. Nếu phiên đang chạy mô hình khác, báo rõ trước khi giao việc và đề nghị người dùng chuyển mô hình; không tự coi phiên đó là điều phối viên hợp lệ.
- Mọi tác tử con, kể cả tác tử do tác tử con tạo tiếp, phải dùng **Claude Opus 5.5** (`claude-opus-5-5`) với mức suy luận (reasoning effort) `high` qua cơ chế tác tử gốc của Claude Code. Tạo tác tử bằng công cụ `Agent` với loại `general-purpose`, `model: "opus"` và `effort: "high"`, hoặc loại tác tử có định nghĩa trong `.claude/agents/` khai báo mô hình `claude-opus-5-5` và mức suy luận `high`. Không dùng loại `fork` cho vai trong quy trình, vì `fork` kế thừa mô hình của điều phối viên và bỏ qua tham số mô hình. Không giao vai trong quy trình cho loại tác tử cố định mô hình hoặc mức suy luận khác. Tiếp tục nhiệm vụ của tác tử đã tạo bằng `SendMessage`; lời gọi `Agent` mới tạo một tác tử mới.
- Mọi đầu ra của tác tử con chỉ đi tiếp sang giai đoạn sau, vào tệp của kho hoặc tới người dùng sau khi điều phối viên đã rà: với kế hoạch và báo cáo, đối chiếu từng phát hiện với tệp hoặc dòng được dẫn và tính lại số liệu; với tệp đã ghi, đọc diff và chạy các kiểm tra quy định; ghi quyết định `chấp nhận | yêu cầu sửa | bác bỏ` kèm lý do trong `review-log.md`. Một tác tử con rà tác tử con khác không thay cho việc duyệt của điều phối viên.
- Không dùng OpenRouter, cầu nối trong `openrouter-mcp/`, các script OpenRouter, Codex hoặc lời gọi mô hình qua API/CLI để thay cơ chế tác tử gốc của Claude Code. Các ủy quyền và chỉ dẫn OpenRouter, Codex hoặc GPT-6-Astra cũ trong `.codex/`, script, prompt hay hồ sơ lịch sử không áp dụng cho quy trình hiện hành; chỉ kế thừa phần phạm vi học thuật còn phù hợp.
- Không đọc, nạp hoặc gửi `.env`, `.env.*` ở bất kỳ thư mục nào; không dùng khóa API hay bí mật để tạo hoặc xác thực tác tử. Không đưa bí mật, kể cả trong tệp có tên thông thường, vào lời nhắc, tệp đính kèm, kết quả công cụ hoặc nhật ký.
- Dùng tác tử chỉ đọc cho kiểm kê, lập kế hoạch, phân tích nguồn, kiểm định storyboard và các lượt rà soát độc lập. Tác tử soạn hoặc chỉnh sửa chỉ được ghi vào danh sách tệp đã giao. Mỗi nhiệm vụ phải có vai trò, đầu vào, đầu ra và điều kiện hoàn thành cụ thể.
- Tác tử chỉ đọc có thể chạy song song trong giới hạn khả dụng; chia thành các đợt khi số vai trò vượt giới hạn. Chỉ một tác tử được ghi tệp tại một thời điểm. Điều phối viên phải chờ đủ kết quả liên quan, chấp nhận hoặc bác bỏ đầu ra trước giai đoạn phụ thuộc và tự xác minh trước khi bàn giao.
- Ghi tên tác tử, vai trò, loại tác tử, mô hình và mức suy luận đã chỉ định từ lời gọi công cụ hoặc định nghĩa tác tử trong nhật ký. Chỉ ghi mô hình thực chạy hoặc tuyến xác thực khi công cụ cung cấp bằng chứng; không coi lời tự khai của tác tử là bằng chứng thực thi.
- Nếu không tạo được tác tử Claude Opus 5.5 với mức suy luận `high` qua cơ chế gốc, báo rõ giới hạn và dừng phần việc phụ thuộc. Tiếp tục các việc độc lập đã được phép; không chuyển ngầm sang mô hình khác, OpenRouter hoặc script gọi mô hình.

### Quy trình tác tử gốc cho một ghi chú bài giảng

1. Điều phối viên chốt mục tiêu, phạm vi, đầu ra và tiêu chí đạt theo `sources/source.md` cùng các yêu cầu ghi chú trong tệp này; chưa giao tác tử soạn ở bước này.
2. Giao một tác tử lập kế hoạch và một tác tử phân tích nguồn độc lập bằng công cụ `Agent`, theo mô hình và phạm vi chỉ đọc ở trên. Hai nhiệm vụ có thể chạy song song khi đầu vào đã ổn định.
3. Giao một tác tử chỉ đọc riêng lập bản đồ chủ đề, gồm các chủ đề bổ sung có lý do và nguồn. Điều phối viên hợp nhất, duyệt phạm vi rồi mới cho phép soạn.
4. Giao một tác tử soạn dựa trên hồ sơ nguồn và đặc tả đã duyệt, giới hạn danh sách Markdown và SVG được ghi. Có thể dùng thư mục tạm để kiểm tra bản nháp trước khi áp dụng vào kho. Điều phối viên kiểm tra diff và đầu ra; không chạy hai tác tử ghi song song.
5. Sau bản nháp, giao năm tác tử chỉ đọc rà soát độc lập: góc nhìn sinh viên; chuyên gia giải thuật và khoa học dữ liệu; độ chính xác toán học và thuật toán; phản biện học thuật và giảng dạy; kết nối, nguồn và mạch viết. Chạy theo các đợt trong giới hạn khả dụng. Mỗi báo cáo dùng `mức độ`, `vị trí`, `vấn đề`, `bằng chứng`, `đề xuất sửa`.
6. Điều phối viên hợp nhất đủ năm báo cáo. Một tác tử chỉnh sửa riêng sửa tuần tự. Mọi thay đổi định nghĩa, định lý, thuật toán, chứng minh hoặc độ phức tạp phải được tác tử độ chính xác rà lại; thay đổi cấu trúc phải được tác tử mạch viết rà lại.
7. Điều phối viên kiểm định Markdown, viewer, công thức, SVG, liên kết, index, màn hình rộng, màn hình hẹp, bàn phím và bản in. Chỉ công bố khi không còn lỗi `chặn bàn giao` hoặc `nghiêm trọng`.
