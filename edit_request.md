# Yêu cầu chỉnh sửa

## Quy trình

- Ghi mỗi prompt của người dùng bắt đầu bằng “Yêu cầu” thành một mục checklist, theo thứ tự nhận.
- Giữ nguyên nội dung yêu cầu; dùng mã ER-001, ER-002, … để theo dõi. Nếu một prompt có nhiều ý, giữ chúng dưới cùng một yêu cầu.
- Không tự chuyển câu hỏi hoặc trao đổi không có tiền tố “Yêu cầu” thành việc cần sửa.
- Xử lý lần lượt từng yêu cầu. Ghi tệp bị tác động, kết quả kiểm tra và commit tương ứng dưới mục đó.
- Mỗi yêu cầu có commit riêng và được push lên `origin/main` bằng push thường, theo quyền người dùng đã cấp. Không gộp thay đổi ngoài phạm vi.
- Chỉ đánh dấu `[x]` khi đã triển khai, kiểm tra và xác nhận push thành công. Nếu còn lỗi hoặc push thất bại, giữ `[ ]` và ghi rõ phần còn lại.
- Tiếp tục mục chưa hoàn tất hoặc mục kế tiếp trong checklist; khi hết việc, chờ prompt “Yêu cầu” tiếp theo.

## Checklist

- [x] **ER-001** — Yêu cầu: trong section lớn đầu tiên, các ví dụ được đưa ra rất khó hiểu với người mới bắt đầu. Cần nêu rõ bài toán, khó khăn khi dữ liêụ lớn hoặc triển khai phức tạp, trực quan hoá bài toán và vấn đề, hãy chỉnh lại section lớn đầu tiên (section giới thiệu)
  - Trạng thái: hoàn tất; commit nội dung `627d69ee9a214830ee81543faa170b1b50e7e532` đã push và xác nhận bằng `git ls-remote origin refs/heads/main`.
  - Phạm vi: phần ngoài đầu tiên của Bài 01; hình và ghi chú tương ứng; đồng bộ tài liệu kế hoạch, ghi chú tự học và chỉ mục khi cần.
  - Tiêu chí: người mới nhận diện được tình huống, đầu vào, đầu ra, khó khăn và ý nghĩa của hình trên mỗi ví dụ; giữ nguồn, không thêm số liệu thiếu căn cứ.
  - Kết quả: sửa chín slide mở đầu, bỏ hai slide nối lặp; vẽ lại bảy SVG; đồng bộ ghi chú, ba tệp kế hoạch và index. Giữ nguyên HTML từ B00 đến cuối.
  - Kiểm tra: đủ sáu báo cáo độc lập và hai lượt rà lại; 51 slide, 7 phần, 120+60 phút; Chromium rộng/hẹp, công thức, SVG, bàn phím, viewer và bản in đạt. Codex Slides còn dự án nháp cũ; kiểm trực tiếp RevealJS cục bộ.

- [x] **ER-002** — Yêu cầu: tổ chức lại section này, phải có slide giới thiệu về section, các slide cần tham khảo cách thể hiện cuả section trước, rõ bài toán, khó khăn
  - Trạng thái: hoàn tất; commit nội dung `961a5d2b94cdd8b4fb2953b3c9f2ea62f44798f9` đã push và xác nhận bằng `git ls-remote origin refs/heads/main`.
  - Phạm vi: section thứ hai của Bài 01, hiện mở bằng “Từ kho đã lưu đến dữ liệu đang đến”; đồng bộ hình, ghi chú và tài liệu kế hoạch liên quan.
  - Tiêu chí: có slide giới thiệu toàn section; ba cụm dòng dữ liệu, lưu trữ và truy vấn nối rõ; mỗi ví dụ nêu bài toán, đầu ra và khó khăn, hình tương ứng theo cách trình bày section trước.
  - Kết quả: sửa12trang B, vẽ lại9SVG; B00 giới thiệu ba nhóm, B10/B11 mở cụm, các ví dụ dùng bài toán và thẻ khó khăn; đồng bộ ghi chú, ba tệp kế hoạch và index. HTML phần A và C–R không đổi.
  - Kiểm tra: sáu báo cáo độc lập và rà mạch lại; 51slide/7phần/120+60phút, Chromium rộng/hẹp, SVG, công thức, bàn phím, viewer và PDF51trang đạt. Codex Slides vẫn draft/0slide; kiểm RevealJS cục bộ theo ngoại lệ đã báo.

- [x] **ER-003** — Yêu cầu: có slide mở đầu "Phân tích thuật toán xử lý dữ liệu lớn" --> gồm đặc tả & đánh giá
  - Các slide cần có kết nối.
  - Các tiêu chí, khía cạnh đánh giá cần có slide tổng và slide riêng có khái niệm, ví dụ cụ thể, hình minh hoạ.
  - Trạng thái: hoàn tất; commit nội dung `5661db9e23f2e75565b27107c85e6a842b940faa` đã push và xác nhận bằng `git ls-remote origin refs/heads/main`.
  - Phạm vi: section thứ ba của Bài 01, hiện mở bằng “Các giới hạn cần phân tích”; đồng bộ ghi chú, hình và tài liệu kế hoạch, giữ các phần khác khi không cần thay đổi.
  - Tiêu chí: trang mở phần đúng tên yêu cầu; mạch đặc tả → lời giải → đánh giá liền lạc; có tổng quan các tiêu chí và trang riêng giải thích bằng ví dụ, hình.
  - Kết quả triển khai: thay tám trang phân tích bằng 17 trang; dùng cặp tài liệu gần trùng, tách 10 tiêu chí đánh giá; thêm 11 SVG; đồng bộ ghi chú, kế hoạch, chỉ mục và các câu nối/tự kiểm còn nhắc ví dụ cũ. Toàn bài 60 trang, 7 phần, 120+60 phút.
  - Kiểm tra: Chromium rộng/hẹp toàn bộ 60 trang; KaTeX, SVG, bàn phím, viewer, chỉ mục và bản in đạt. Kiểm số học và 1.200 trường hợp thuật toán hữu hạn; không còn lỗi nghiêm trọng/chặn. Codex Slides vẫn nháp cũ, dùng RevealJS cục bộ theo ngoại lệ đã báo.
- Bổ sung của người dùng: “đừng dùng tử tổng byte, ngoài ra ví dụ này quá đơn giản, không nêu hết ý nghĩa”. Bỏ ví dụ cộng dồn khỏi phần phân tích; dùng tìm cặp tài liệu gần trùng cho đặc tả, nhiều ứng dụng cho các tiêu chí. Không dùng cách gọi bị phản đối trong học liệu hiện hành.

- [ ] **ER-004** — Yêu cầu: với các section lớn còn lại hãy:
  - nêu section muốn nói gì
  - nêu mạch thể hiện của section
  - bổ sung các slide mở đầu với tiêu đề thể hiện nội dung section, các slide kết nối
  - Mỗi khái niệm trong section cần lý giải, minh hoạ, ví dụ để làm rõ
  - sau khi hoàn thiện mỗi section hãy commit / push, tôi cho phép push lên origin
  - Phạm vi: D, E, F, R của Bài 01; đồng bộ ghi chú, hình và ba tệp kế hoạch. Giữ A–C.
  - [x] D — Nội dung học phần và các nhóm phương pháp: nhu cầu → cơ chế đại diện → bài sẽ học → bảo đảm/chi phí.
    - Hoàn tất11trang D,4SVG, đồng bộ ghi chú và kế hoạch; Chromium rộng/hẹp, viewer, PDF63trang, sáu báo cáo và rà mạch lại đạt. Commit `9ca7a455a9738a170a28906a8216a4d36458ed04` đã push, xác nhận bằng `git ls-remote origin refs/heads/main`.
  - [ ] E — Kiến thức, kỹ năng và cách học: nền cần ôn → vận dụng → sản phẩm → trách nhiệm.
  - [ ] F — Mô hình ngẫu nhiên và giới hạn suy luận: bài toán lưu trú → mô hình → xác suất → kỳ vọng → diễn giải.
  - [ ] R — Bài tập về phép đếm và suy luận: mô hình gốc → thay quy mô → đổi tiêu chuẩn → tập mặt hàng.
  - Trạng thái: đang lập kế hoạch; kiểm tra, commit/push riêng từng phần trước khi đánh dấu hoàn tất.
