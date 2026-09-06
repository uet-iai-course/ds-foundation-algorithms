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

Chưa có prompt bắt đầu bằng “Yêu cầu” được gửi theo quy trình này. Các trao đổi trước thời điểm thiết lập không tự được chuyển thành mục mới.
