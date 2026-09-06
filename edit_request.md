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

- [ ] **ER-001** — Yêu cầu: trong section lớn đầu tiên, các ví dụ được đưa ra rất khó hiểu với người mới bắt đầu. Cần nêu rõ bài toán, khó khăn khi dữ liêụ lớn hoặc triển khai phức tạp, trực quan hoá bài toán và vấn đề, hãy chỉnh lại section lớn đầu tiên (section giới thiệu)
  - Trạng thái: đã triển khai và kiểm định; chờ xác nhận commit/push.
  - Phạm vi: phần ngoài đầu tiên của Bài 01; hình và ghi chú tương ứng; đồng bộ tài liệu kế hoạch, ghi chú tự học và chỉ mục khi cần.
  - Tiêu chí: người mới nhận diện được tình huống, đầu vào, đầu ra, khó khăn và ý nghĩa của hình trên mỗi ví dụ; giữ nguồn, không thêm số liệu thiếu căn cứ.
  - Kết quả: sửa chín slide mở đầu, bỏ hai slide nối lặp; vẽ lại bảy SVG; đồng bộ ghi chú, ba tệp kế hoạch và index. Giữ nguyên HTML từ B00 đến cuối.
  - Kiểm tra: đủ sáu báo cáo độc lập và hai lượt rà lại; 51 slide, 7 phần, 120+60 phút; Chromium rộng/hẹp, công thức, SVG, bàn phím, viewer và bản in đạt. Codex Slides còn dự án nháp cũ; kiểm trực tiếp RevealJS cục bộ.
