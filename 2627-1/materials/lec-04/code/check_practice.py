# -*- coding: utf-8 -*-
"""Kiểm tra tự chạy bài thực hành Lecture 04.

Mặc định kiểm mã tham chiếu (link_analysis.py). Với --student, chỉ kiểm
hits_step trong hits_student.py (khung sinh viên) trên 2 vòng G4, 1 vòng G5
và đồ thị không cạnh.

Số đối chiếu: các phân số là lời giải do môn tự tính từ đề MMDS §5.3–5.5
(đề 5.3.1, 5.4.2, 5.5.1; thuật toán TSP §5.3.2, TrustRank §5.4.4–5.4.5,
HITS §5.5.2), đã đối chiếu độc lập.
"""

import argparse
import sys
import unittest

import link_analysis as ref

TOL_FP = 1e-10   # so sánh điểm bất động
TOL_STEP = 1e-12  # so sánh một bước


def close(a, b, tol):
    return abs(a - b) <= tol


def vec_close(x, y, tol):
    return set(x) == set(y) and all(close(x[k], y[k], tol) for k in x)


class TestTopicPageRank(unittest.TestCase):
    """Bài 1: MMDS 5.3.1 — TSP trên G4, seeds A và A,C."""

    def test_seeds_A(self):
        g = ref.graph("g4")
        res = ref.topic_pagerank(g, ["A"], beta=0.8, tol=1e-12, max_iter=1000)
        self.assertTrue(res["converged"])
        expect = {"A": 3 / 7, "B": 4 / 21, "C": 4 / 21, "D": 4 / 21}
        self.assertTrue(vec_close(res["rank"], expect, TOL_FP), "TSP seeds A")

    def test_seeds_AC(self):
        g = ref.graph("g4")
        res = ref.topic_pagerank(g, ["A", "C"], beta=0.8, tol=1e-12, max_iter=1000)
        self.assertTrue(res["converged"])
        expect = {"A": 27 / 70, "B": 6 / 35, "C": 19 / 70, "D": 6 / 35}
        self.assertTrue(vec_close(res["rank"], expect, TOL_FP), "TSP seeds A,C")

    def test_invalid_seeds(self):
        g = ref.graph("g4")
        with self.assertRaises(ValueError):
            ref.topic_pagerank(g, ["X"])  # seed không có trong đồ thị
        for seeds in ([], [1], [["A"]]):
            with self.subTest(seeds=seeds), self.assertRaises(ValueError):
                ref.topic_pagerank(g, seeds)

    def test_params_validation(self):
        g = ref.graph("g4")
        for bad_tol in (True, float("nan"), float("inf"), 0, -1e-6):
            with self.subTest(tol=bad_tol), self.assertRaises(ValueError):
                ref.topic_pagerank(g, ["A"], tol=bad_tol)
        with self.assertRaises(ValueError):
            ref.topic_pagerank(g, ["A"], beta=1.0)
        with self.assertRaises(ValueError):
            ref.topic_pagerank(g, ["A"], beta=float("nan"))

    def test_duplicate_edges_and_seeds_input_unchanged(self):
        import copy
        g = ref.graph("g4")
        g["A"].append("B")  # cạnh trùng
        snapshot = copy.deepcopy(g)
        res = ref.topic_pagerank(g, ["A", "A", "C"], beta=0.8,
                                 tol=1e-12, max_iter=1000)
        self.assertTrue(res["converged"])
        # Cạnh trùng gộp một lần; seeds trùng gộp: kết quả như seeds {A, C}.
        expect = {"A": 27 / 70, "B": 6 / 35, "C": 19 / 70, "D": 6 / 35}
        self.assertTrue(vec_close(res["rank"], expect, TOL_FP))
        self.assertEqual(g, snapshot, "input không bị sửa")


    def test_all_dangling_balanced(self):
        # Toàn bộ đỉnh cụt: 0.8*(1/2, 1/2) + 0.2*(1, 0) = (0.6, 0.4).
        g = {"A": [], "B": []}
        res = ref.topic_pagerank(g, ["A"], beta=0.8, tol=1e-12, max_iter=100)
        self.assertTrue(res["converged"])
        self.assertLessEqual(abs(sum(res["rank"].values()) - 1.0), 1e-10)
        self.assertTrue(vec_close(res["rank"], {"A": 0.6, "B": 0.4}, TOL_FP))

    def test_max_iter_1(self):
        res = ref.topic_pagerank(ref.graph("g4"), ["A"], beta=0.8,
                                 tol=1e-12, max_iter=1)
        self.assertFalse(res["converged"])
        self.assertEqual(res["iterations"], 1)

class TestTrustRank(unittest.TestCase):
    """Bài 2: MMDS 5.4.2 — TrustRank seeds B, khối lượng rác, mass B âm."""

    def test_trust_B_and_mass(self):
        g = ref.graph("g4")
        res = ref.topic_pagerank(g, ["B"], beta=0.8, tol=1e-12, max_iter=1000)
        expect_trust = {"A": 66 / 245, "B": 263 / 735,
                        "C": 116 / 735, "D": 158 / 735}
        self.assertTrue(vec_close(res["rank"], expect_trust, TOL_FP),
                        "TrustRank seeds B (beta 4/5)")
        baseline = {"A": 1 / 3, "B": 2 / 9, "C": 2 / 9, "D": 2 / 9}  # beta = 1
        mass = ref.spam_mass(baseline, res["rank"])
        expect_mass = {"A": 47 / 245, "B": -299 / 490,
                       "C": 71 / 245, "D": 8 / 245}
        self.assertTrue(vec_close(mass, expect_mass, TOL_FP),
                        "spam mass; B âm là hợp lệ theo nguồn")

    def test_rank_zero_raises(self):
        with self.assertRaises(ValueError):
            ref.spam_mass({"A": 0.0}, {"A": 0.5})

    def test_mass_validation(self):
        for bad_r in (0.0, -0.5, float("nan"), float("inf"), True):
            with self.subTest(r=bad_r), self.assertRaises(ValueError):
                ref.spam_mass({"A": bad_r}, {"A": 0.5})
        for bad_t in (-0.1, float("nan"), float("inf"), False):
            with self.subTest(t=bad_t), self.assertRaises(ValueError):
                ref.spam_mass({"A": 0.5}, {"A": bad_t})
        with self.assertRaises(ValueError):
            ref.spam_mass({"A": 1.0}, {"B": 0.5})  # khóa lệch
        # mass âm giữ nguyên, không kẹp.
        m = ref.spam_mass({"A": 0.5}, {"A": 0.8})
        self.assertAlmostEqual(m["A"], -0.6, delta=TOL_FP)


class TestHITS(unittest.TestCase):
    """Bài 3: MMDS 5.5.1 — HITS trên G4/G5, chuẩn max."""

    def test_g4_two_rounds(self):
        g = ref.graph("g4")
        h = {v: 1.0 for v in g}
        a1, h1 = ref.hits_step(g, h)
        self.assertTrue(vec_close(a1, {"A": 1, "B": 1, "C": 1, "D": 1}, TOL_STEP))
        self.assertTrue(vec_close(h1, {"A": 1, "B": 2 / 3, "C": 1 / 3, "D": 2 / 3},
                                  TOL_STEP), "G4 vòng 1")
        a2, h2 = ref.hits_step(g, h1)
        self.assertTrue(vec_close(a2, {"A": 3 / 5, "B": 1, "C": 1, "D": 1}, TOL_STEP))
        self.assertTrue(vec_close(h2, {"A": 1, "B": 8 / 15, "C": 1 / 5, "D": 2 / 3},
                                  TOL_STEP), "G4 vòng 2")

    def test_g5_one_round(self):
        g = ref.graph("g5")
        h = {v: 1.0 for v in g}
        a1, h1 = ref.hits_step(g, h)
        self.assertTrue(vec_close(a1, {"A": 0.5, "B": 1, "C": 1, "D": 1, "E": 0.5},
                                  TOL_STEP), "G5 vòng 1 authority")
        self.assertTrue(vec_close(h1, {"A": 1, "B": 0.5, "C": 1 / 6,
                                       "D": 2 / 3, "E": 0}, TOL_STEP),
                        "G5 vòng 1 hub")

    def test_g4_convergence_tau_1e_3(self):
        res = ref.hits(ref.graph("g4"), tol=0.001, max_iter=1000)
        self.assertTrue(res["converged"])
        self.assertEqual(res["iterations"], 11,
                         "G4 đạt ngưỡng dừng sau 11 vòng tại tau=1e-3")

    def test_no_edges_degenerate(self):
        no_edges = {"A": [], "B": [], "C": [], "D": []}
        res = ref.hits(no_edges, tol=1e-12, max_iter=10)
        self.assertTrue(res["degenerate"])
        self.assertFalse(res["converged"])
        self.assertTrue(all(v == 0.0 for v in res["authority"].values()))
        self.assertTrue(all(v == 0.0 for v in res["hub"].values()))

    def test_budget_exhausted(self):
        res = ref.hits(ref.graph("g4"), tol=1e-12, max_iter=1)
        self.assertFalse(res["converged"])
        self.assertEqual(res["iterations"], 1)


class TestStudentHITSStep(unittest.TestCase):
    """Chế độ --student: chỉ kiểm hits_step của sinh viên."""

    def test_g4_two_rounds(self):
        from hits_student import hits_step
        g = ref.graph("g4")
        snapshot = {u: list(vs) for u, vs in g.items()}
        h = {v: 1.0 for v in g}
        a1, h1 = hits_step(g, h)
        self.assertTrue(vec_close(a1, {"A": 1, "B": 1, "C": 1, "D": 1}, TOL_STEP))
        self.assertTrue(vec_close(h1, {"A": 1, "B": 2 / 3, "C": 1 / 3, "D": 2 / 3},
                                  TOL_STEP))
        a2, h2 = hits_step(g, h1)
        self.assertTrue(vec_close(a2, {"A": 3 / 5, "B": 1, "C": 1, "D": 1}, TOL_STEP))
        self.assertTrue(vec_close(h2, {"A": 1, "B": 8 / 15, "C": 1 / 5, "D": 2 / 3},
                                  TOL_STEP))
        self.assertEqual(g, snapshot, "input không bị sửa")

    def test_g5_one_round(self):
        from hits_student import hits_step
        g = ref.graph("g5")
        a1, h1 = hits_step(g, {v: 1.0 for v in g})
        self.assertTrue(vec_close(a1, {"A": 0.5, "B": 1, "C": 1, "D": 1, "E": 0.5},
                                  TOL_STEP))
        self.assertTrue(vec_close(h1, {"A": 1, "B": 0.5, "C": 1 / 6,
                                       "D": 2 / 3, "E": 0}, TOL_STEP))

    def test_no_edges(self):
        from hits_student import hits_step
        no_edges = {"A": [], "B": [], "C": [], "D": []}
        a1, h1 = hits_step(no_edges, {v: 1.0 for v in no_edges})
        # Kiểm đủ khóa và hai vector 0, không all() trên dict rỗng.
        self.assertEqual(set(a1), set(no_edges))
        self.assertEqual(set(h1), set(no_edges))
        self.assertTrue(all(v == 0.0 for v in a1.values()))
        self.assertTrue(all(v == 0.0 for v in h1.values()))


def run_student():
    """Chạy chế độ --student với thông báo rõ ràng nếu khung chưa cài."""
    from hits_student import hits_step
    # Thử một bước G4 trước: chỉ bắt NotImplementedError của khung.
    try:
        hits_step(ref.graph("g4"), {v: 1.0 for v in ref.graph("g4")})
    except NotImplementedError:
        sys.stderr.write(
            "Chưa hoàn thiện hits_student.hits_step: hãy cài hits_step "
            "(cộng theo cạnh, chuẩn hóa max) rồi chạy lại.\n")
        sys.exit(1)
    suite = unittest.TestSuite()
    suite.addTest(unittest.defaultTestLoader.loadTestsFromTestCase(
        TestStudentHITSStep))
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)
    if not result.wasSuccessful():
        # Khung đã cài nhưng kết quả sai: suite đã chỉ ra assertion ở trên.
        sys.exit(1)


def main(argv=None):
    parser = argparse.ArgumentParser(description="Kiểm tra bài thực hành Lecture 04")
    parser.add_argument("--student", action="store_true",
                        help="chỉ kiểm hits_step trong hits_student.py")
    args = parser.parse_args(argv)
    if args.student:
        run_student()
        return
    # Suite tường minh, chỉ gồm ba lớp kiểm mã tham chiếu; không dùng
    # unittest.main(module=None) vì có thể báo "Ran 0 tests".
    suite = unittest.TestSuite()
    for cls in (TestTopicPageRank, TestTrustRank, TestHITS):
        suite.addTest(unittest.defaultTestLoader.loadTestsFromTestCase(cls))
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)
    if result.testsRun == 0:
        sys.stderr.write("Lỗi: suite không có test nào.\n")
        sys.exit(1)
    sys.exit(0 if result.wasSuccessful() else 1)


if __name__ == "__main__":
    main()
