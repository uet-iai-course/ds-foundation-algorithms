#!/usr/bin/env python3
"""Tạo bốn SVG cho Phần 2 Lecture 03 (Bài toán Xếp hạng trang web).

Sinh: graph-pages.svg (đồ thị 4 trang, Hình 5.1 MMDS),
graph-inlinks.svg (nổi bật các cạnh vào A),
graph-distribute.svg (A chia 1/12 cho mỗi liên kết ra),
graph-receive.svg (B và C đóng góp vào A).

SVG chỉ mang vai trò sơ đồ; phân số và công thức chi tiết nằm trên slide bằng HTML + KaTeX.
Chạy: python3 render_problem.py  (ghi ngay thư mục của script).
Khi copy vào scripts/ của bài, output sẽ đi theo .parent.parent (thư mục hình của bài).
"""
from pathlib import Path
import math

NAVY = "#2f3e7a"
GREY = "#666666"
LIGHT = "#edf4ff"
EDGE = "#b0bec5"
ORANGE = "#ef6c00"
ORANGE_LIGHT = "#fff3e0"

R = 42          # bán kính nút
HEAD = 14       # chiều dài mũi tên
HALF = 8        # nửa bề rộng mũi tên

def node(x, y, name, sub=None, fill=LIGHT, stroke=NAVY, stroke_width=3):
    parts = [
        f'<circle cx="{x}" cy="{y}" r="{R}" fill="{fill}" stroke="{stroke}" stroke-width="{stroke_width}"/>',
        f'<text x="{x}" y="{y + 9}" text-anchor="middle" font-size="30" font-weight="bold" fill="{stroke}">{name}</text>',
    ]
    if sub:
        parts.append(
            f'<text x="{x}" y="{y + R + 26}" text-anchor="middle" font-size="24" fill="{GREY}">{sub}</text>')
    return "".join(parts)

def arrow(a, b, curve=0.0, color=NAVY, width=3, label=None, label_dx=0, label_dy=-16):
    """Cạnh cong từ nút a tới nút b, mũi tên dừng ở biên nút đích."""
    ax, ay = a
    bx, by = b
    dx, dy = bx - ax, by - ay
    L = math.hypot(dx, dy)
    ux, uy = dx / L, dy / L
    px, py = -uy, ux
    mx = (ax + bx) / 2 + px * curve * 2
    my = (ay + by) / 2 + py * curve * 2
    start_len = math.hypot(mx-ax, my-ay)
    sx, sy = ax + R*(mx-ax)/start_len, ay + R*(my-ay)/start_len
    finish_len = math.hypot(bx-mx, by-my)
    fx, fy = (bx-mx)/finish_len, (by-my)/finish_len
    tipx, tipy = bx-R*fx, by-R*fy
    ex, ey = tipx-HEAD*fx, tipy-HEAD*fy
    l1x, l1y = ex-fy*HALF, ey+fx*HALF
    l2x, l2y = ex+fy*HALF, ey-fx*HALF
    parts = [
        f'<path d="M{sx:.1f},{sy:.1f} Q{mx:.1f},{my:.1f} {ex:.1f},{ey:.1f}" fill="none" stroke="{color}" stroke-width="{width}"/>',
        f'<polygon points="{tipx:.1f},{tipy:.1f} {l1x:.1f},{l1y:.1f} {l2x:.1f},{l2y:.1f}" fill="{color}"/>',
    ]
    if label:
        lx = mx + label_dx
        ly = my + label_dy
        parts.append(
            f'<text x="{lx:.1f}" y="{ly:.1f}" text-anchor="middle" font-size="24" font-weight="bold" fill="{color}">{label}</text>')
    return "".join(parts)

def svg_doc(width, height, title_id, title, desc_id, desc, body):
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" '
            f'width="{width}" font-family="Helvetica, Arial, sans-serif" role="img" '
            f'aria-labelledby="{title_id} {desc_id}">\n'
            f'<title id="{title_id}">{title}</title>\n'
            f'<desc id="{desc_id}">{desc}</desc>\n{body}\n</svg>\n')

# Đồ thị Hình 5.1: A→B,C,D; B→A,D; C→A; D→B,C
POS = {"A": (220, 110), "B": (580, 110), "C": (220, 270), "D": (580, 270)}
FULL_EDGES = [
    ("A", "B", 24), ("B", "A", 24),
    ("A", "C", 24), ("C", "A", 24),
    ("A", "D", 0),
    ("B", "D", 24), ("D", "B", 24),
    ("D", "C", 24),
]

def full_graph(edges_spec):
    parts = []
    for a, b, curve in edges_spec:
        parts.append(arrow(POS[a], POS[b], curve=curve, color=NAVY, width=3))
    for name, (x, y) in POS.items():
        parts.append(node(x, y, name))
    return "".join(parts)

PAGES = svg_doc(800, 350, "pg-title", "Đồ thị ví dụ bốn trang web",
                "pg-desc",
                "Bốn nút A và B ở hàng trên, C và D ở hàng dưới; tám mũi tên có hướng: "
                "A tới B, C, D; B tới A và D; C tới A; D tới B và C.",
                full_graph(FULL_EDGES))

IN_SPEC = [("B", "A", 24, NAVY, 5), ("C", "A", 24, NAVY, 5)]
OUT_SPEC = [(a, b, c, EDGE, 2.5) for a, b, c in FULL_EDGES if (a, b) not in {("B", "A"), ("C", "A")}]
IN_PARTS = []
for a, b, curve, color, w in OUT_SPEC + IN_SPEC:
    IN_PARTS.append(arrow(POS[a], POS[b], curve=curve, color=color, width=w))
for name, (x, y) in POS.items():
    if name == "A":
        IN_PARTS.append(node(x, y, name, fill=ORANGE_LIGHT, stroke=ORANGE, stroke_width=5))
    else:
        IN_PARTS.append(node(x, y, name))
IN_PARTS.append(
    f'<text x="220" y="35" text-anchor="middle" font-size="24" font-weight="bold" fill="{ORANGE}">A nhận 2 liên kết vào</text>')
INLINKS = svg_doc(800, 350, "il-title", "Đếm liên kết vào của trang A",
                  "il-desc",
                  "Cùng đồ thị bốn trang; hai cạnh vào A là B tới A và C tới A được vẽ đậm màu xanh đậm; "
                  "các cạnh còn lại nhạt màu. Nút A tô màu cam nhạt. Trên nút A ghi chú A nhận 2 liên kết vào.",
                  "".join(IN_PARTS))

# A chia đều cho ba đích
DA, DB, DC, DD = (140, 175), (640, 55), (640, 175), (640, 295)
DIST_PARTS = [
    arrow(DA, DB, curve=0, width=3.5, label="1/12", label_dy=-18),
    arrow(DA, DC, curve=0, width=3.5, label="1/12", label_dy=-18),
    arrow(DA, DD, curve=0, width=3.5, label="1/12", label_dy=-18),
    node(*DA, "A", sub="điểm cũ 1/4"),
    node(*DB, "B"), node(*DC, "C"), node(*DD, "D"),
]
DISTRIBUTE = svg_doc(800, 350, "dt-title", "Trang A chia điểm cho ba liên kết ra",
                     "dt-desc",
                     "Nút A bên trái có điểm cũ 1/4; ba mũi tên tới B, C, D bên phải, "
                     "mỗi mũi tên mang nhãn 1/12: một phần ba của 1/4.",
                     "".join(DIST_PARTS))

# B và C đóng góp vào A
RA = (620, 175)
RB = (180, 70)
RC = (180, 280)
REC_PARTS = [
    arrow(RB, RA, curve=-30, width=3.5, label="1/8", label_dx=0, label_dy=-20),
    arrow(RC, RA, curve=30, width=3.5, label="1/4", label_dx=0, label_dy=34),
    node(*RB, "B", sub="1/4 chia 2"),
    node(*RC, "C", sub="1/4 chia 1"),
    node(*RA, "A", sub="điểm mới 3/8", fill=ORANGE_LIGHT, stroke=ORANGE, stroke_width=5),
]
RECEIVE = svg_doc(800, 350, "rc-title", "Cộng điểm tại trang A",
                  "rc-desc",
                  "Hai mũi tên từ B và C vào A; B đóng góp 1/8 vì có hai liên kết ra, "
                  "C đóng góp cả 1/4 vì chỉ có một liên kết ra; điểm mới của A là 3/8.",
                  "".join(REC_PARTS))


def main() -> None:
    out = Path(__file__).resolve().parent.parent
    for name, svg in (("graph-pages.svg", PAGES),
                      ("graph-inlinks.svg", INLINKS),
                      ("graph-distribute.svg", DISTRIBUTE),
                      ("graph-receive.svg", RECEIVE)):
        (out / name).write_text(svg, encoding="utf-8")


if __name__ == "__main__":
    main()
