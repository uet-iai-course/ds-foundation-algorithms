# Thực hành 04 — PageRank theo chủ đề, TrustRank, HITS

Mã do môn biên soạn cho bài thực hành 60 phút; dữ kiện từ MMDS 3e §5.3–5.5
(G4: Hình 5.1 và 5.15; G5: Hình 5.18; đề 5.3.1 tr.199/PDF25, 5.4.2 tr.204/PDF30,
5.5.1 tr.208/PDF34; thuật toán TSP §5.3.2, TrustRank §5.4.4–5.4.5, HITS §5.5.2).
Python 3, chỉ thư viện chuẩn, không tải mạng.

## Bản đồ tệp

| Tệp | Vai trò |
|---|---|
| `link_analysis.py` | Mã tham chiếu: `graph`, `topic_step`, `topic_pagerank`, `spam_mass`, `hits_step`, `hits` và chương trình dòng lệnh |
| `hits_student.py` | Khung bài tập: sinh viên tự cài `hits_step` |
| `check_practice.py` | Kiểm tra tự chạy (mặc định mã tham chiếu; `--student` cho khung) |

## Lệnh chạy (từ thư mục `code` đã tải về, hoặc `2627-1/materials/lec-04/code`)

```bash
# Bài 1 — PageRank theo chủ đề (MMDS 5.3.1)
python3 link_analysis.py topic --graph g4 --seeds A C --beta 0.8 --tol 1e-12 --max-iter 1000

# Bài 2 — TrustRank + khối lượng rác (MMDS 5.4.2, cố định G4)
python3 link_analysis.py trust --seeds B --tol 1e-12 --max-iter 1000

# Bài 3 — HITS (MMDS 5.5.1)
python3 link_analysis.py hits --graph g4 --tol 0.001 --max-iter 1000

# Kiểm tra toàn bộ mã tham chiếu / kiểm khung sinh viên
python3 check_practice.py
python3 check_practice.py --student
```

## Đối chiếu số (đề từ MMDS, phân số là lời giải do môn tự tính)

Các đề bài và thuật toán lấy từ MMDS; các phân số dưới đây là lời giải môn
tự tính và đã được đối chiếu độc lập (không chép đáp án từ sách).

- **Bài 1 (TSP, $\beta=4/5$):** tập hạt giống $\{A\}$ → $r = (3/7, 4/21, 4/21, 4/21)$;
  tập hạt giống $\{A,C\}$ → $r = (27/70, 6/35, 19/70, 6/35)$.
- **Bài 2:** PageRank nền của đề nguồn là PageRank **$\beta=1$** lấy từ Ví dụ 5.2
  (dùng lại trong Ví dụ 5.12 và đề 5.4.2): $r = (1/3, 2/9, 2/9, 2/9)$.
  TrustRank dùng **$\beta=4/5$**, tập tin cậy $T=\{B\}$: $t = (66/245, 263/735, 116/735, 158/735)$.
  Khối lượng rác $s = (r - t)/r = (47/245, -299/490, 71/245, 8/245)$;
  **$s_B$ âm là hợp lệ** (nghĩa là điểm Trust của B cao hơn PageRank nền, không phải
  xác suất hay phân loại). Hai quy ước beta khác nhau chỉ là quy ước của đề
  MMDS; khi ứng dụng đối chiếu điểm phải nhất quán beta và bù cụt.
- **Bài 3 (HITS, chuẩn max):** G4 vòng 1: $a = (1,1,1,1)$, $h = (1, 2/3, 1/3, 2/3)$;
  vòng 2: $a = (3/5, 1, 1, 1)$, $h = (1, 8/15, 1/5, 2/3)$. G5 vòng 1:
  $a = (1/2, 1, 1, 1, 1/2)$, $h = (1, 1/2, 1/6, 2/3, 0)$. G4 đạt ngưỡng dừng
  $\tau=10^{-3}$ sau **11 vòng** (đây là ngưỡng dừng, không khẳng định nghiệm).

## Trạng thái dừng

- TSP: dừng khi chênh $L_1$ giữa hai vector liên tiếp ≤ tol; tol là độ thay đổi
  liên tiếp, **không được đồng nhất với sai số tới nghiệm**.
- HITS: dừng khi **cả hai** chênh $L_\infty$ của điểm thẩm quyền và điểm trung tâm không vượt $\tau$; trả vector mới.
- `converged: false` không phải lỗi chương trình: chương trình vẫn in kết quả và trạng thái.
- Đồ thị không cạnh: HITS trả hai vector 0, `iterations: 0`, `delta: 0`,
  `converged: false`, `degenerate: true` — bài toán suy biến, không phải đã hội tụ.

## Sinh viên nộp gì

1. `hits_student.py` đã cài `hits_step` (hai TODO: cộng theo cạnh, chuẩn hóa max).
2. Chạy `python3 check_practice.py --student` đạt hết. Nếu khung chưa cài,
   chương trình báo "Chưa hoàn thiện hits_student.hits_step" và thoát mã 1;
   chỉ khi cài đúng mới đạt.
3. `report.md` gồm 4 hàng (2 TSP, 1 Trust/mass, 1 HITS) kèm tham số và trạng thái
   (converged/iterations/delta), cùng 3 giải thích ngắn.

## Chi phí

Mỗi vòng lặp quét cạnh và đỉnh: thời gian $\Theta(n+m)$ mỗi vòng, bộ nhớ
$O(n+m)$; không lưu toàn bộ vết lặp, không dựng ma trận $L$, $L^T$ đặc.
