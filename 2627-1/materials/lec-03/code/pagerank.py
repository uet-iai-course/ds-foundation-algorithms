# -*- coding: utf-8 -*-
"""Tính PageRank theo mô hình đầy đủ của Lecture 03 (mục 5.1 MMDS).

Mô hình cập nhật (bài giảng phần 3):
    r_i^{t+1} = beta * sum_{j: j->i} r_j^t / d_j  +  ((1 - beta) + beta * delta^t) / n
với delta^t là tổng điểm của các nút cụt (không có liên kết ra) và
r^0 đều 1/n. Đây là quy tắc "bù điểm nút cụt" của bài: nút cụt trong
nhánh theo liên kết được coi như trỏ đều tới cả n trang, khác với
công thức taxation thiếu khối lượng trên ma trận có cột 0 trong sách
(MMDS mục 5.1.5, trang 186–187). Nguồn dữ liệu: MMDS Hình 5.1 (base),
Hình 5.3 (dead-end), Hình 5.6 (spider trap).

Chỉ dùng thư viện chuẩn Python 3, không cần cài thêm gì.
"""

import argparse
import json
import math
import sys


def step(adj, r, beta):
    """Thực hiện đúng một vòng cập nhật và trả về vector điểm mới.

    adj: dict ánh xạ tên nút (str) -> danh sách đích (str), đã hợp lệ:
         mọi đích là khóa của adj, không có cạnh trùng, n >= 1.
    r:   dict điểm cũ, cùng tập khóa adj, giá trị không âm, tổng 1.
    beta: 0 < beta < 1.

    Hàm không thay đổi r; điểm mới nằm hoàn toàn trong dict trả về.
    """
    n = len(adj)
    # delta: tổng điểm của các nút cụt, tính từ vector cũ.
    delta = sum(r[j] for j in adj if not adj[j])
    common = (1.0 - beta + beta * delta) / n
    new = {i: common for i in adj}
    for j, targets in adj.items():
        if not targets:
            continue
        share = beta * r[j] / len(targets)
        for i in targets:
            new[i] += share
    return new


def _validate(adj, beta, tol, max_iter):
    """Kiểm tham số và tạo bản sao đồ thị đơn, giữ nguyên thứ tự đỉnh/cạnh."""
    if not isinstance(adj, dict) or not adj:
        raise ValueError("adj phải là dict khác rỗng (n >= 1).")
    clean = {}
    for j, targets in adj.items():
        if not isinstance(j, str) or not isinstance(targets, (list, tuple)):
            raise ValueError("Mã nút phải là chuỗi, các đích phải nằm trong list hoặc tuple.")
        for i in targets:
            if not isinstance(i, str) or i not in adj:
                raise ValueError("Mỗi đích phải là chuỗi có trong tập nút của đồ thị.")
        clean[j] = list(dict.fromkeys(targets))
    for name, value in (("beta", beta), ("tol", tol)):
        if isinstance(value, bool) or not isinstance(value, (int, float)) or not math.isfinite(value):
            raise ValueError(name + " phải là số hữu hạn.")
    if not 0 < beta < 1:
        raise ValueError("beta phải thỏa 0 < beta < 1.")
    if tol <= 0:
        raise ValueError("tol phải dương.")
    if isinstance(max_iter, bool) or not isinstance(max_iter, int) or max_iter < 1:
        raise ValueError("max_iter phải là số nguyên dương.")
    return clean


def pagerank(adj, beta=0.8, tol=1e-8, max_iter=100):
    """Tính PageRank trên dict danh sách kề.

    adj: dict[str] -> list[str]. Giữ mọi nút, kể cả nút không có
         liên kết vào hay không có liên kết ra. Cạnh trùng được gộp
         trong bản sao; hàm không sửa adj.

    Trả về dict:
        rank:       dict[str] -> float, điểm của từng nút.
        converged:  bool, True nếu đạt ngưỡng dừng.
        iterations: int, số vòng đã thực hiện.
        delta:      float, tổng |r_new - r_old| ở vòng cuối.

    tol là ngưỡng độ thay đổi giữa hai vòng liên tiếp, không phải
    chặn sai số so với nghiệm r*.
    """
    adj = _validate(adj, beta, tol, max_iter)
    n = len(adj)
    r = {i: 1.0 / n for i in adj}
    converged = False
    delta = 0.0
    iterations = 0
    for _ in range(max_iter):
        new = step(adj, r, beta)
        delta = sum(abs(new[i] - r[i]) for i in adj)
        r = new
        iterations += 1
        if delta <= tol:
            converged = True
            break
    return {
        "rank": dict(r),
        "converged": converged,
        "iterations": iterations,
        "delta": delta,
    }


def _build_graph(variant):
    """Ba đồ thị ví dụ của MMDS, nút A, B, C, D, nhãn chuỗi đúng như bài giảng."""
    if variant == "base":
        # MMDS Hình 5.1: A->{B,C,D}, B->{A,D}, C->{A}, D->{B,C}.
        return {"A": ["B", "C", "D"], "B": ["A", "D"], "C": ["A"], "D": ["B", "C"]}
    if variant == "dead":
        # MMDS Hình 5.3: xóa cạnh C->A; C là nút cụt.
        return {"A": ["B", "C", "D"], "B": ["A", "D"], "C": [], "D": ["B", "C"]}
    if variant == "trap":
        # MMDS Hình 5.6: thay C->A bằng C->C; C là bẫy một nút.
        return {"A": ["B", "C", "D"], "B": ["A", "D"], "C": ["C"], "D": ["B", "C"]}
    raise ValueError("variant phải là base, dead hoặc trap.")


def main(argv=None):
    parser = argparse.ArgumentParser(
        description="Tính PageRank theo mô hình Lecture 03 (bước nhảy + bù nút cụt)."
    )
    parser.add_argument("--variant", choices=["base", "dead", "trap"],
                        default="base", help="Đồ thị ví dụ theo MMDS.")
    parser.add_argument("--beta", type=float, default=0.8, help="Hệ số theo liên kết, 0<beta<1.")
    parser.add_argument("--tol", type=float, default=1e-8, help="Ngưỡng độ thay đổi giữa hai vòng.")
    parser.add_argument("--max-iter", type=int, default=100, help="Giới hạn số vòng.")
    args = parser.parse_args(argv)

    try:
        adj = _build_graph(args.variant)
        result = pagerank(adj, beta=args.beta, tol=args.tol, max_iter=args.max_iter)
    except ValueError as exc:
        print("Lỗi tham số: %s" % exc, file=sys.stderr)
        return 2

    payload = {
        "variant": args.variant,
        "beta": args.beta,
        "tol": args.tol,
        "max_iter": args.max_iter,
        "rank": result["rank"],
        "converged": result["converged"],
        "iterations": result["iterations"],
        "delta": result["delta"],
        "rank_sum": sum(result["rank"].values()),
    }
    print(json.dumps(payload, indent=2, sort_keys=True, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    sys.exit(main())
