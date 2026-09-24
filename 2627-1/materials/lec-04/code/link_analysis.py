# -*- coding: utf-8 -*-
"""Mã tham chiếu bài thực hành Lecture 04: PageRank theo chủ đề,
TrustRank/khối lượng rác và HITS.

Nguồn dữ kiện: MMDS 3e, chương 5, §5.3–5.5 (G4: Hình 5.1 và 5.15; G5: Hình 5.18);
ba đề bài gốc 5.3.1 (tr.199/PDF25), 5.4.2 (tr.204/PDF30), 5.5.1 (tr.208/PDF34).
Thuật toán: TSP §5.3.2; TrustRank §5.4.4–5.4.5; HITS §5.5.2.
Mã do môn biên soạn cho mục đích thực hành; chỉ dùng thư viện chuẩn Python 3.

Quy ước: P là ma trận cột-nguồn (mỗi cột tổng 1), L là ma trận hàng-nguồn.
HITS dùng chuẩn hóa max (chia cho phần tử lớn nhất), KHÔNG chuẩn hóa tổng.
"""

import argparse
import json
import math
import sys

# ---------------------------------------------------------------------------
# Đồ thị ví dụ (nguồn: MMDS Hình 5.1 và Hình 5.15 = G4; biến thể Hình 5.18 = G5)
# ---------------------------------------------------------------------------

_GRAPHS = {
    "g4": {
        "A": ["B", "C", "D"],
        "B": ["A", "D"],
        "C": ["A"],
        "D": ["B", "C"],
    },
    "g5": {
        "A": ["B", "C", "D"],
        "B": ["A", "D"],
        "C": ["E"],
        "D": ["B", "C"],
        "E": [],
    },
}


def graph(name):
    """Trả về bản sao đồ thị theo tên ('g4' hoặc 'g5').

    dict: tên nút (str) -> danh sách đích (str). G4: A->[B,C,D], B->[A,D],
    C->[A], D->[B,C]. G5 thay C->[A] thành C->[E], E cụt.
    """
    key = str(name).lower()
    if key not in _GRAPHS:
        raise ValueError("graph không hợp lệ: %r (chọn 'g4' hoặc 'g5')" % (name,))
    return {u: list(vs) for u, vs in _GRAPHS[key].items()}


# ---------------------------------------------------------------------------
# Kiểm tra đầu vào dùng chung (đủ mức cho input JSON/Python đơn giản)
# ---------------------------------------------------------------------------

def _validate_adj(adj):
    if not isinstance(adj, dict) or not adj:
        raise ValueError("adj phải là dict không rỗng: tên nút -> danh sách đích")
    for u, targets in adj.items():
        if not isinstance(u, str):
            raise ValueError("nhãn nút phải là chuỗi, thấy: %r" % (u,))
        if not isinstance(targets, (list, tuple)):
            raise ValueError("danh sách kề của %r phải là list/tuple" % (u,))
        # Kiểm mọi đích là chuỗi TRƯỚC khi tra membership, để dữ liệu JSON sai
        # (ví dụ đích là số) trả ValueError thay vì lỗi tra dict không rõ nghĩa.
        for v in targets:
            if not isinstance(v, str):
                raise ValueError("đích %r của cạnh %r phải là chuỗi" % (v, u))
        for v in targets:
            if v not in adj:
                raise ValueError("đích %r của cạnh %r không được kê trong adj" % (v, u))


def _validate_params(tol, max_iter, beta=None):
    if isinstance(tol, bool) or not isinstance(tol, (int, float)) \
            or not math.isfinite(tol) or tol <= 0:
        raise ValueError("tol phải là số dương hữu hạn (không phải bool)")
    if isinstance(max_iter, bool) or not isinstance(max_iter, int) or max_iter <= 0:
        raise ValueError("max_iter phải là số nguyên dương (không phải bool)")
    if beta is not None:
        if isinstance(beta, bool) or not isinstance(beta, (int, float)) \
                or not math.isfinite(beta):
            raise ValueError("beta phải là số hữu hạn (không phải bool)")
        if not (0 < beta < 1):
            raise ValueError("beta phải thỏa 0 < beta < 1")


def _copy_adj(adj):
    """Bản sao với cạnh trùng được gộp, giữ thứ tự nút gốc.

    Dùng dict.fromkeys để gộp trùng trong thời gian kỳ vọng O(bậc).
    """
    out = {}
    for u, targets in adj.items():
        out[u] = list(dict.fromkeys(targets))
    return out


# ---------------------------------------------------------------------------
# Bài 1: PageRank theo chủ đề (MMDS §5.3.2, đề 5.3.1)
# ---------------------------------------------------------------------------

def topic_step(adj, rank, teleport, beta):
    """Một bước lũy thừa của PageRank theo chủ đề (helper đã kiểm định đầu vào).

    Input: adj (dict nút -> list đích, không cạnh trùng), rank (dict phân phối trên cùng khóa),
    teleport (dict phân phối trên cùng khóa), beta với 0 < beta < 1.
    Output: dict điểm mới trên cùng khóa.

    Công thức: quét danh sách kề để cộng beta * rank[u]/deg(u) vào mỗi đích v;
    khối lượng cụt delta = tổng rank[u] với deg(u)=0 được bù đều beta*delta/n;
    cộng thêm (1-beta)*teleport[v] cho mọi v. Không cập nhật tại chỗ.
    Nguồn: MMDS §5.3.2, phương trình điểm bất động với P cột tổng 1.
    """
    nodes = list(adj.keys())
    n = len(nodes)
    new = {v: (1.0 - beta) * teleport[v] for v in nodes}
    dangling = 0.0
    for u, targets in adj.items():
        ru = rank[u]
        if targets:
            share = beta * ru / len(targets)
            for v in targets:
                new[v] += share
        else:
            dangling += ru
    if dangling:
        bump = beta * dangling / n
        for v in nodes:
            new[v] += bump
    return new


def topic_pagerank(adj, seeds, beta=0.8, tol=1e-12, max_iter=1000):
    """PageRank theo chủ đề bằng lặp lũy thừa (MMDS §5.3.2, đề 5.3.1).

    Input: adj (dict không rỗng, nhãn chuỗi, mọi đích được kê), seeds (tập/list
    tên nút không rỗng), beta trong (0,1), tol dương, max_iter nguyên dương.
    Output: dict {'rank', 'iterations', 'delta', 'converged'}.
    teleport đều trên seeds; khởi tạo r = teleport; dừng khi chênh L1 giữa hai
    vector liên tiếp <= tol và trả về vector MỚI. Hết budget trả vector cuối
    với converged=False. Không lưu vết toàn bộ hay ma trận đặc.
    Lưu ý: tol đo độ thay đổi liên tiếp, không phải chặn sai số tới nghiệm.
    Chi phí chuẩn bị kỳ vọng O(n + m + k), với k là số phần tử seeds ban đầu;
    mỗi vòng Theta(n + m); bộ nhớ O(n + m) ngoài đầu vào seeds.
    """
    _validate_adj(adj)
    _validate_params(tol, max_iter, beta)
    if isinstance(seeds, str) or not isinstance(seeds, (list, tuple, set)) or not seeds:
        raise ValueError("seeds phải là tập/list/tuple tên nút không rỗng")
    if any(not isinstance(seed, str) for seed in seeds):
        raise ValueError("mọi hạt giống phải là tên nút dạng chuỗi")
    # Gộp trùng giữ thứ tự đầu vào, kiểm membership trên set một lần (O(k)).
    seeds = list(dict.fromkeys(seeds))
    seed_set = set(seeds)
    for s in seeds:
        if s not in adj:
            raise ValueError("seed %r không có trong đồ thị" % (s,))
    adj = _copy_adj(adj)
    nodes = list(adj.keys())
    n = len(nodes)
    teleport = {v: (1.0 / len(seeds) if v in seed_set else 0.0) for v in nodes}
    rank = dict(teleport)
    for it in range(1, max_iter + 1):
        new = topic_step(adj, rank, teleport, beta)
        delta = sum(abs(new[v] - rank[v]) for v in nodes)
        rank = new
        if delta <= tol:
            return {"rank": rank, "iterations": it, "delta": delta, "converged": True}
    return {"rank": rank, "iterations": max_iter, "delta": delta, "converged": False}


# ---------------------------------------------------------------------------
# Bài 2: TrustRank và khối lượng rác (MMDS §5.4.4–5.4.5, đề 5.4.2)
# ---------------------------------------------------------------------------

def spam_mass(rank, trust):
    """Khối lượng rác s = (r - t)/r theo từng nút (MMDS §5.4.5).

    Input: rank và trust là hai dict cùng khóa; r hữu hạn và > 0 tại mọi nút;
    t hữu hạn và >= 0. Giá trị âm giữ nguyên (không kẹp).
    Output: dict (r - t)/r. Raise ValueError nếu khóa lệch, r <= 0, t < 0
    hoặc giá trị không phải số hữu hạn (bool bị bác).
    """
    if set(rank) != set(trust):
        raise ValueError("rank và trust phải có cùng tập khóa")
    out = {}
    for v, r in rank.items():
        if isinstance(r, bool) or not isinstance(r, (int, float)) \
                or not math.isfinite(r) or r <= 0:
            raise ValueError("rank tại nút %r phải là số hữu hạn dương" % (v,))
        t = trust[v]
        if isinstance(t, bool) or not isinstance(t, (int, float)) \
                or not math.isfinite(t) or t < 0:
            raise ValueError("trust tại nút %r phải là số hữu hạn không âm" % (v,))
        out[v] = (r - t) / r
    return out


# ---------------------------------------------------------------------------
# Bài 3: HITS (thuật toán MMDS §5.5.2, đề 5.5.1; chuẩn hóa max theo sách)
# ---------------------------------------------------------------------------

def hits_step(adj, hub):
    """Một cặp cập nhật HITS trên dữ liệu đã hợp lệ (helper).

    Input: adj (dict nút -> list đích, không cạnh trùng), hub (dict điểm hub không âm).
    Output: tuple (authority_new, hub_new) là hai dict mới trên cùng khóa.

    Bước 1: authority mới của v = tổng hub CŨ của mọi nguồn u có cạnh u->v;
    chuẩn hóa bằng chia cho max (nếu max = 0, trả hai dict 0, không chia 0).
    Bước 2: hub mới của u = tổng authority MỚI của các đích kề u; chuẩn max.
    Không teleport, không đổi input. Nguồn: MMDS §5.5.2 (G5: Hình 5.18).
    Đây là helper cho đầu vào ĐÃ hợp lệ: không kiểm lại toàn bộ mỗi vòng.
    """
    nodes = list(adj.keys())
    a_new = {v: 0.0 for v in nodes}
    for u, targets in adj.items():
        hu = hub[u]
        for v in targets:
            a_new[v] += hu
    m = max(a_new.values()) if a_new else 0.0
    if m == 0:
        zero = {v: 0.0 for v in nodes}
        return zero, dict(zero)
    a_new = {v: x / m for v, x in a_new.items()}
    h_new = {u: sum(a_new[v] for v in targets) for u, targets in adj.items()}
    m = max(h_new.values())
    if m == 0:
        zero = {v: 0.0 for v in nodes}
        return dict(zero), zero
    h_new = {u: x / m for u, x in h_new.items()}
    return a_new, h_new


def hits(adj, tol=1e-12, max_iter=1000):
    """Phác thảo lũy thừa HITS (thuật toán MMDS §5.5.2, đề 5.5.1).

    Input: adj (dict không rỗng, nhãn chuỗi, mọi đích được kê), tol dương,
    max_iter nguyên dương. Output: dict {'authority', 'hub', 'iterations',
    'delta', 'converged', 'degenerate'}.
    Khởi tạo h0 = ones, a0 = zeros chỉ là mốc đo chênh. Mỗi vòng chạy một
    hits_step; delta = max của hai chênh Linf (authority và hub) giữa hai
    vector liên tiếp; dừng khi delta <= tol và trả vector MỚI. Hết budget trả
    vector cuối với converged=False. Đồ thị không cạnh: hai vector 0,
    iterations=0, delta=0, converged=False, degenerate=True — nghĩa là bài toán
    suy biến, KHÔNG phải đã hội tụ. Chi phí Theta(n + m) mỗi vòng, không tạo
    ma trận L, L^T đặc và không lưu toàn bộ vết.
    """
    _validate_adj(adj)
    _validate_params(tol, max_iter)
    adj = _copy_adj(adj)
    nodes = list(adj.keys())
    has_edge = any(adj[u] for u in nodes)
    if not has_edge:
        zero = {v: 0.0 for v in nodes}
        return {"authority": dict(zero), "hub": dict(zero),
                "iterations": 0, "delta": 0.0,
                "converged": False, "degenerate": True}
    h_old = {v: 1.0 for v in nodes}
    a_old = {v: 0.0 for v in nodes}
    for it in range(1, max_iter + 1):
        a_new, h_new = hits_step(adj, h_old)
        delta = max(
            max(abs(a_new[v] - a_old[v]) for v in nodes),
            max(abs(h_new[v] - h_old[v]) for v in nodes),
        )
        a_old, h_old = a_new, h_new
        if delta <= tol:
            return {"authority": a_new, "hub": h_new, "iterations": it,
                    "delta": delta, "converged": True, "degenerate": False}
    return {"authority": a_old, "hub": h_old, "iterations": max_iter,
            "delta": delta, "converged": False, "degenerate": False}


# ---------------------------------------------------------------------------
# Giao diện dòng lệnh
# ---------------------------------------------------------------------------

def _fail(msg):
    sys.stderr.write("Lỗi đầu vào: %s\n" % msg)
    sys.exit(2)


def _pack(method, gname, order, results, params):
    return {"method": method, "graph": gname, "order": order,
            "results": results, "params": params}


def main(argv=None):
    parser = argparse.ArgumentParser(
        description="Thực hành Lecture 04: PageRank theo chủ đề, TrustRank, HITS.")
    sub = parser.add_subparsers(dest="cmd", required=True)

    p_topic = sub.add_parser("topic", help="PageRank theo chủ đề (MMDS 5.3.1)")
    p_topic.add_argument("--graph", required=True, choices=["g4", "g5"])
    p_topic.add_argument("--seeds", nargs="+", required=True)
    p_topic.add_argument("--beta", type=float, default=0.8)
    p_topic.add_argument("--tol", type=float, default=1e-12)
    p_topic.add_argument("--max-iter", type=int, default=1000)

    p_trust = sub.add_parser("trust", help="TrustRank + khối lượng rác (MMDS 5.4.2)")
    p_trust.add_argument("--seeds", nargs="+", required=True)
    p_trust.add_argument("--tol", type=float, default=1e-12)
    p_trust.add_argument("--max-iter", type=int, default=1000)

    p_hits = sub.add_parser("hits", help="HITS (MMDS 5.5.1)")
    p_hits.add_argument("--graph", required=True, choices=["g4", "g5"])
    p_hits.add_argument("--tol", type=float, default=1e-12)
    p_hits.add_argument("--max-iter", type=int, default=1000)

    args = parser.parse_args(argv)
    try:
        if args.cmd == "topic":
            adj = graph(args.graph)
            res = topic_pagerank(adj, args.seeds, beta=args.beta,
                                 tol=args.tol, max_iter=args.max_iter)
            order = list(adj.keys())
            out = _pack("topic_pagerank", args.graph, order,
                        {"rank": res["rank"], "iterations": res["iterations"],
                         "delta": res["delta"], "converged": res["converged"]},
                        {"seeds": list(dict.fromkeys(args.seeds)),
                         "beta": args.beta, "tol": args.tol,
                         "max_iter": args.max_iter})
        elif args.cmd == "trust":
            # Cố định G4 theo đề MMDS 5.4.2. Baseline là PageRank beta = 1
            # của Ví dụ 5.2 (dùng lại trong Ví dụ 5.12 và đề 5.4.2):
            # r = (1/3, 2/9, 2/9, 2/9); TrustRank dùng beta = 4/5
            # với hạt giống Trust = B (thuật toán §5.4.4–5.4.5).
            # Hai quy ước beta khác nhau phải giữ rõ.
            adj = graph("g4")
            order = list(adj.keys())
            baseline_rank = {"A": 1 / 3, "B": 2 / 9, "C": 2 / 9, "D": 2 / 9}
            res = topic_pagerank(adj, args.seeds, beta=0.8,
                                 tol=args.tol, max_iter=args.max_iter)
            mass = spam_mass(baseline_rank, res["rank"])
            out = _pack("trustrank", "g4", order,
                        {"baseline_beta": 1, "baseline_rank": baseline_rank,
                         "trust_rank": res["rank"], "spam_mass": mass,
                         "iterations": res["iterations"],
                         "delta": res["delta"],
                         "converged": res["converged"]},
                        {"seeds": list(dict.fromkeys(args.seeds)),
                         "trust_beta": 0.8, "tol": args.tol,
                         "max_iter": args.max_iter})
        else:
            adj = graph(args.graph)
            res = hits(adj, tol=args.tol, max_iter=args.max_iter)
            order = list(adj.keys())
            out = _pack("hits", args.graph, order,
                        {"authority": res["authority"], "hub": res["hub"],
                         "iterations": res["iterations"], "delta": res["delta"],
                         "converged": res["converged"],
                         "degenerate": res["degenerate"]},
                        {"tol": args.tol, "max_iter": args.max_iter})
    except ValueError as exc:
        _fail(str(exc))
    print(json.dumps(out, ensure_ascii=False, indent=2))
    # converged=False không phải lỗi chương trình: đã in kết quả và trạng thái.


if __name__ == "__main__":
    main()
