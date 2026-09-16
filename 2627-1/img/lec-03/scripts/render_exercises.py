#!/usr/bin/env python3
"""Tạo các SVG cho Phần 7 Lecture 03 (Tổng kết và bài tập vận dụng).

Sinh các hình ex-*.svg ngay thư mục của script:
  ex-fig-57.svg — Đồ thị Hình 5.7 MMDS, 3 nút a, b, c (slide 04, 05, 07)
  ex-fig-54.svg — Đồ thị Hình 5.4 MMDS, 5 nút A–E (slide 07)

Dữ kiện cạnh giữ nguyên theo nguồn:
  Fig 5.7 (7 cạnh): a→a, a→b, a→c; b→a, b→c; c→b, c→c.
  Fig 5.4 (8 cạnh): A→B,C,D; B→A,D; C→E; D→B,C. E không có liên kết ra.

Chạy: python3 render_exercises.py (ghi ngay thư mục của script).
Script chỉ dùng Python stdlib; hàm vẽ text dùng đúng chữ ký node(x, y, name).
"""
import math
from pathlib import Path

NAVY = "#2f3e7a"
GREY = "#666666"
LIGHT = "#edf4ff"

R = 42


def node(x, y, name, fill=LIGHT, stroke=NAVY):
    """Vẽ một nút tròn với nhãn ở giữa; chữ ký node(x, y, name)."""
    return (
        f'<circle cx="{x}" cy="{y}" r="{R}" fill="{fill}" stroke="{stroke}" '
        f'stroke-width="3"/>'
        f'<text x="{x}" y="{y + 11}" text-anchor="middle" font-size="34" '
        f'font-weight="bold" fill="{stroke}">{name}</text>'
    )


def arrow(a, b, curve=0.0, width=3):
    """Cạnh có hướng từ a tới b, cong theo hệ số curve (đơn vị ~ px tại giữa)."""
    ax, ay = a
    bx, by = b
    dx, dy = bx - ax, by - ay
    L = math.hypot(dx, dy)
    ux, uy = dx / L, dy / L
    px, py = -uy, ux
    mx = (ax + bx) / 2 + px * curve
    my = (ay + by) / 2 + py * curve
    # Điểm xuất phát và điểm mũi tên dừng ở biên nút (bán kính R), không cắt hình.
    s_len = math.hypot(mx - ax, my - ay)
    sx, sy = ax + R * (mx - ax) / s_len, ay + R * (my - ay) / s_len
    tipx, tipy = bx - R * (bx - mx) / math.hypot(bx - mx, by - my), \
        by - R * (by - my) / math.hypot(bx - mx, by - my)
    fx, fy = (bx - mx), (by - my)
    fl = math.hypot(fx, fy)
    fx, fy = fx / fl, fy / fl
    ex, ey = tipx - 14 * fx, tipy - 14 * fy
    l1x, l1y = ex - 8 * fy, ey + 8 * fx
    l2x, l2y = ex + 8 * fy, ey - 8 * fx
    return (
        f'<path d="M{sx:.1f},{sy:.1f} Q{mx:.1f},{my:.1f} {ex:.1f},{ey:.1f}" '
        f'fill="none" stroke="{NAVY}" stroke-width="{width}"/>'
        f'<polygon points="{tipx:.1f},{tipy:.1f} {l1x:.1f},{l1y:.1f} '
        f'{l2x:.1f},{l2y:.1f}" fill="{NAVY}"/>'
    )


def selfloop(x, y, path_d, points):
    """Vòng lặp trên một nút: cung rời nút rồi trở lại, mũi tên chỉ vào nút."""
    return (
        f'<path d="{path_d}" fill="none" stroke="{NAVY}" stroke-width="3"/>'
        f'<polygon points="{points}" fill="{NAVY}"/>'
    )


def svg_doc(width, height, title_id, title, desc_id, desc, body):
    return (
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" '
        f'width="{width}" font-family="Helvetica, Arial, sans-serif" role="img" '
        f'aria-labelledby="{title_id} {desc_id}">\n'
        f'<title id="{title_id}">{title}</title>\n'
        f'<desc id="{desc_id}">{desc}</desc>\n{body}\n</svg>\n'
    )


# ------------------------------------------------------------------ Fig 5.7
P57 = {"a": (170, 110), "b": (630, 110), "c": (400, 300)}


def fig57():
    parts = [
        # 7 cạnh theo dữ kiện nguồn: a→a, a→b, a→c; b→a, b→c; c→b, c→c.
        arrow(P57["a"], P57["b"], curve=0),          # a→b
        arrow(P57["b"], P57["a"], curve=36),         # b→a
        arrow(P57["a"], P57["c"], curve=24),         # a→c
        arrow(P57["b"], P57["c"], curve=24),         # b→c
        arrow(P57["c"], P57["b"], curve=24),         # c→b
        # Vòng lặp a→a: cung phía trên nút a, mũi tên chỉ xuống nút.
        selfloop(170, 110,
                 "M140,80 C90,-10 260,-10 200,80",
                 "200,80 201.1,63.9 214.4,72.8"),
        # Vòng lặp c→c: cung phía dưới nút c, mũi tên chỉ lên nút.
        selfloop(400, 300,
                 "M370,330 C320,420 480,420 430,330",
                 "430,330 443.8,338.3 429.8,346.1"),
    ]
    parts += [node(x, y, n) for n, (x, y) in P57.items()]
    return svg_doc(
        800, 435, "ex57-title", "Đồ thị Hình 5.7: ba trang a, b, c",
        "ex57-desc",
        "Ba nút a, b, c. Cạnh có hướng: a tới a, a tới b, a tới c, "
        "b tới a, b tới c, c tới b, c tới c — tổng cộng bảy cạnh, "
        "gồm hai vòng lặp trên a và trên c.",
        "".join(parts))


# ------------------------------------------------------------------ Fig 5.4
P54 = {"A": (150, 100), "B": (560, 100), "C": (150, 300),
       "D": (560, 300), "E": (390, 395)}


def fig54():
    parts = [
        # 8 cạnh theo dữ kiện nguồn: A→B,C,D; B→A,D; C→E; D→B,C; E không có cạnh ra.
        arrow(P54["A"], P54["B"], curve=0),    # A→B
        arrow(P54["B"], P54["A"], curve=30),   # B→A
        arrow(P54["A"], P54["C"], curve=0),    # A→C
        arrow(P54["A"], P54["D"], curve=30),   # A→D
        arrow(P54["B"], P54["D"], curve=0),    # B→D
        arrow(P54["D"], P54["B"], curve=36),   # D→B
        arrow(P54["D"], P54["C"], curve=26),   # D→C
        arrow(P54["C"], P54["E"], curve=0),    # C→E
    ]
    parts += [node(x, y, n) for n, (x, y) in P54.items()]
    return svg_doc(
        720, 470, "ex54-title", "Đồ thị Hình 5.4: năm trang A, B, C, D, E",
        "ex54-desc",
        "Năm nút A, B, C, D, E. Cạnh có hướng: A tới B, C, D; B tới A, D; "
        "C tới E; D tới B, C. Nút E không có mũi tên đi ra.",
        "".join(parts))


FIGURES = {
    "ex-fig-57.svg": fig57(),
    "ex-fig-54.svg": fig54(),
}


def main() -> None:
    out = Path(__file__).resolve().parent.parent
    for name, svg in FIGURES.items():
        (out / name).write_text(svg, encoding="utf-8")
    print(f"Đã sinh {len(FIGURES)} SVG trong {out}")


if __name__ == "__main__":
    main()
