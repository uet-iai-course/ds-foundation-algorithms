# Thực hành PageRank — Lecture 03

## Môi trường

- Python 3 (chỉ thư viện chuẩn: `argparse`, `json`, `math`, `sys`).
- Không cần pip, không cần Docker, không cần Hadoop.
- Chạy trên một máy để kiểm công thức; đây không phải đo hiệu năng.

## Dữ liệu

Ba biến thể theo MMDS, nút nhãn chuỗi A, B, C, D:

| Variant | Danh sách kề | Nguồn |
|---|---|---|
| `base` | A:[B,C,D], B:[A,D], C:[A], D:[B,C] | Hình 5.1 |
| `dead` | như base nhưng C:[] (xóa C→A, C là nút cụt) | Hình 5.3 |
| `trap` | như base nhưng C:[C] (bẫy một nút) | Hình 5.6 |

Toàn bộ nút được giữ, kể cả nút không có liên kết vào hoặc không có liên kết ra. Hàm pagerank gộp cạnh trùng trong bản sao và giữ nguyên dữ liệu đầu vào. Hàm step nhận danh sách đã gộp.

## Lệnh chạy

Từ thư mục `2627-1` bên trong kho:

```bash
python3 materials/lec-03/code/pagerank.py --variant base --beta 0.8 --tol 1e-8 --max-iter 100
```

Đổi `--variant` thành `dead` hoặc `trap` để chạy hai biến thể kia. Chương trình in JSON gồm `rank`, `converged`, `iterations`, `delta`, `rank_sum`.

## Kết quả mong đợi

Với `base`, `beta=0.8`: điểm hội tụ là

- A = 9/28 ≈ 0.321428571
- B = C = D = 19/84 ≈ 0.226190476

Lần chạy kiểm chứng với các tham số trên: 20 vòng, `converged=true`, `delta` xấp xỉ `5.4975583e-9`, `rank_sum=1.0`. Sai khác làm tròn nhỏ có thể xuất hiện giữa môi trường chạy.

## Cách kiểm

1. **Tổng và dấu:** tổng các giá trị `rank` xấp xỉ 1, mọi giá trị không âm (dùng dung sai, không so sánh float bằng `==`).
2. **Một bước trên `base`**: từ `r0` đều 1/4, `beta=0.8`, gọi `step(adj, r0, 0.8)`. Kết quả đúng là A = 7/20, B = C = D = 13/60 (khớp bảng một vòng ở phần 3 bài giảng).
3. **Một bước trên `dead`**: xóa C→A, cùng `r0` đều, `beta=0.8`. Kết quả đúng là A = 1/5, B = C = D = 4/15 (khớp bảng nút cụt ở phần 3).
4. Dung sai so sánh: `abs(got - want) <= 1e-12` cho các kiểm một bước.

## Ghi chú bổ sung

- **Toàn bộ nút cụt:** nếu mọi nút không có liên kết ra, `delta = 1` và phần chung là `((1-beta) + beta)/n = 1/n`: mỗi vòng trả lại phân phối đều, không lỗi chia không.
- **Một nút có vòng lặp lên chính nó:** nút A với `A: ["A"]` vẫn hoạt động bình thường; `d_A = 1`, A giữ lại toàn bộ phần theo liên kết của mình.
- `tol` là ngưỡng độ thay đổi giữa hai vòng liên tiếp, không phải chặn sai số so với nghiệm.
- Các kiểm trên là kiểm chứng chương trình, không thay thế bài tập recitation về nguồn.
