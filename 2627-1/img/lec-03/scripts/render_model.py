#!/usr/bin/env python3
"""Tạo các SVG cho Phần 3 Lecture 03 (Mô hình và thuật toán PageRank).

Sinh các hình model-*.svg ngay thư mục của script:
  model-one-round.svg    — bước j chia điểm cho các đích (slide 01)
  model-column-a.svg     — cột A của ma trận liên kết M0 (slide 02)
  model-dead-end.svg     — biến thể Hình 5.3, C thành nút cụt (slide 04)
  model-spider-trap.svg  — biến thể Hình 5.6, C trỏ vào chính nó (slide 05)
  model-teleport.svg     — hai nhánh di chuyển tại một bước (slide 06)
  model-dead-redistribute.svg — sơ đồ bù phân phối điểm của C (slide 07)

SVG chỉ mang vai trò sơ đồ; phân số và công thức chi tiết nằm trên slide bằng HTML + KaTeX.
Chạy: python3 render_model.py (ghi ngay thư mục của script).
Dùng hàm vẽ cạnh nội bộ của chính script, không import file khác.
"""
from pathlib import Path

NAVY = "#2f3e7a"
ORANGE = "#cc6b32"
GREY = "#666666"
LIGHT = "#edf4ff"
EDGE = "#b0bec5"
ORANGE_LIGHT = "#fff3e0"

R = 42


def node(x, y, name, sub=None, fill=LIGHT, stroke=NAVY, stroke_width=3):
    parts = [
        f'<circle cx="{x}" cy="{y}" r="{R}" fill="{fill}" stroke="{stroke}" stroke-width="{stroke_width}"/>',
        f'<text x="{x}" y="{y + 9}" text-anchor="middle" font-size="30" font-weight="bold" fill="{stroke}">{name}</text>',
    ]
    if sub:
        parts.append(
            f'<text x="{x}" y="{y + R + 26}" text-anchor="middle" font-size="24" fill="{GREY}">{sub}</text>')
    return "".join(parts)


def _fallback_arrow(a, b, curve=0.0, color=NAVY, width=3, label=None,
                    label_dx=0, label_dy=-16):
    """Bản vẽ cạnh nội bộ của script."""
    import math
    ax, ay = a
    bx, by = b
    dx, dy = bx - ax, by - ay
    L = math.hypot(dx, dy)
    ux, uy = dx / L, dy / L
    px, py = -uy, ux
    mx = (ax + bx) / 2 + px * curve * 2
    my = (ay + by) / 2 + py * curve * 2
    s_len = math.hypot(mx - ax, my - ay)
    sx, sy = ax + R * (mx - ax) / s_len, ay + R * (my - ay) / s_len
    f_len = math.hypot(bx - mx, by - my)
    fx, fy = (bx - mx) / f_len, (by - my) / f_len
    tipx, tipy = bx - R * fx, by - R * fy
    ex, ey = tipx - 14 * fx, tipy - 14 * fy
    l1x, l1y = ex - 8 * fy, ey + 8 * fx
    l2x, l2y = ex + 8 * fy, ey - 8 * fx
    parts = [
        f'<path d="M{sx:.1f},{sy:.1f} Q{mx:.1f},{my:.1f} {ex:.1f},{ey:.1f}" fill="none" stroke="{color}" stroke-width="{width}"/>',
        f'<polygon points="{tipx:.1f},{tipy:.1f} {l1x:.1f},{l1y:.1f} {l2x:.1f},{l2y:.1f}" fill="{color}"/>',
    ]
    if label:
        parts.append(
            f'<text x="{mx + label_dx:.1f}" y="{my + label_dy:.1f}" text-anchor="middle" '
            f'font-size="24" font-weight="bold" fill="{color}">{label}</text>')
    return "".join(parts)


_arrow = _fallback_arrow

def arrow(a, b, curve=0.0, color=NAVY, width=3, label=None, label_dx=0, label_dy=-16):
    return _arrow(a, b, curve=curve, color=color, width=width, label=label,
                  label_dx=label_dx, label_dy=label_dy)


def svg_doc(width, height, title_id, title, desc_id, desc, body):
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" '
            f'width="{width}" font-family="Helvetica, Arial, sans-serif" role="img" '
            f'aria-labelledby="{title_id} {desc_id}">\n'
            f'<title id="{title_id}">{title}</title>\n'
            f'<desc id="{desc_id}">{desc}</desc>\n{body}\n</svg>\n')


# ---------------------------------------------------------------- slide 01
# Nút nguồn j chia điểm cho ba đích tại bước t.
def one_round():
    src = (150, 175)
    t1, t2, t3 = (650, 60), (650, 175), (650, 290)
    parts = [
        arrow(src, t1, curve=0, width=3.5, label="rⱼ/dⱼ", label_dy=-18),
        arrow(src, t2, curve=0, width=3.5, label="rⱼ/dⱼ", label_dy=-18),
        arrow(src, t3, curve=0, width=3.5, label="rⱼ/dⱼ", label_dy=-18),
        node(*src, "j", sub="điểm cũ rⱼ"),
        node(*t1, "1"), node(*t2, "2"), node(*t3, "3"),
        f'<text x="400" y="340" text-anchor="middle" font-size="26" fill="{GREY}">bước t → t+1</text>',
    ]
    return svg_doc(800, 360, "mr-title", "Một trang chia điểm cho các đích của nó",
                   "mr-desc",
                   "Nút j bên trái mang điểm cũ rⱼ; ba mũi tên tới ba trang đích bên phải, "
                   "mỗi mũi tên mang nhãn rⱼ/dⱼ là phần bằng nhau của điểm cũ chia theo số liên kết ra.",
                   "".join(parts))


# ---------------------------------------------------------------- slide 02
# Cột A của ma trận M0: A trỏ tới i thì hàng i có 1/d_A.
POS = {"A": (220, 110), "B": (580, 110), "C": (220, 270), "D": (580, 270)}


def column_a():
    spec = [("A","B",24),("B","A",24),("A","C",24),("C","A",24),
            ("A","D",0),("B","D",24),("D","B",24),("D","C",24)]
    parts=[arrow(POS[a],POS[b],curve=c,color=NAVY if a=="A" else EDGE,width=5 if a=="A" else 2) for a,b,c in spec]
    parts += [node(x,y,name,fill=ORANGE_LIGHT if name=="A" else LIGHT,stroke=ORANGE if name=="A" else NAVY) for name,(x,y) in POS.items()]
    return svg_doc(800,360,"ca-title","Cột A: các liên kết ra của A","ca-desc",
        "Ba cạnh A tới B, C, D vẽ đậm. Cột nguồn A có giá trị một phần ba tại hàng B, C, D và không tại hàng A.","".join(parts))


# ---------------------------------------------------------------- slides 04, 05, 07, 10
# Đồ thị Hình 5.1 gốc: A→B,C,D; B→A,D; C→A; D→B,C
FULL_EDGES = [
    ("A", "B", 24), ("B", "A", 24),
    ("A", "C", 24), ("C", "A", 24),
    ("A", "D", 0),
    ("B", "D", 24), ("D", "B", 24),
    ("D", "C", 24),
]


def variant_graph(mode):
    """mode = 'dead' xóa C→A (C thành nút cụt); mode = 'trap' đổi C→A thành C→C."""
    parts = []
    for a, b, curve in FULL_EDGES:
        if mode == "dead" and (a, b) == ("C", "A"):
            continue
        if mode == "trap" and (a, b) == ("C", "A"):
            # Vòng lặp C→C: vẽ cung tròn ra khỏi nút C rồi trở lại.
            parts.append(f'<path d="M190,241 C65,158 65,383 181,287" fill="none" stroke="{NAVY}" stroke-width="3"/>')
            parts.append(f'<polygon points="186,294 169,297 180,311" fill="{NAVY}"/>')
            continue
        parts.append(arrow(POS[a], POS[b], curve=curve, color=NAVY, width=3))
    for name, (x, y) in POS.items():
        if mode == "dead" and name == "C":
            parts.append(node(x, y, name, sub="không có liên kết ra",
                              fill=ORANGE_LIGHT, stroke=ORANGE, stroke_width=5))
        elif mode == "trap" and name == "C":
            parts.append(node(x, y, name, fill=ORANGE_LIGHT, stroke=ORANGE, stroke_width=5))
        else:
            parts.append(node(x, y, name))
    return parts


def dead_end():
    return svg_doc(800, 360, "de-title", "Biến thể: C là nút cụt",
                   "de-desc",
                   "Đồ thị bốn trang như Hình 5.1 nhưng đã xóa cạnh C tới A; "
                   "nút C không còn mũi tên đi ra và được tô cam nhạt với chú thích không có liên kết ra.",
                   "".join(variant_graph("dead")))


def spider_trap():
    return svg_doc(800, 380, "st-title", "Biến thể: C là bẫy liên kết",
                   "st-desc",
                   "Đồ thị bốn trang như Hình 5.1 nhưng cạnh C tới A được thay bằng vòng lặp C tới chính C; "
                   "nút C tô cam nhạt và nhãn C tới C đặt trên vòng lặp.",
                   "".join(variant_graph("trap")))


# ---------------------------------------------------------------- slide 06
def teleport():
    body=f'''<rect x="30" y="125" width="180" height="90" rx="12" fill="{LIGHT}" stroke="{NAVY}" stroke-width="3"/>
    <text x="120" y="179" text-anchor="middle" font-size="26" fill="{NAVY}">Trang hiện tại</text>
    <path d="M210,150 L360,65 L450,65" fill="none" stroke="{NAVY}" stroke-width="3"/>
    <polygon points="460,65 446,58 446,72" fill="{NAVY}"/>
    <path d="M210,195 L360,275 L450,275" fill="none" stroke="{ORANGE}" stroke-width="3" stroke-dasharray="9,6"/>
    <polygon points="460,275 446,268 446,282" fill="{ORANGE}"/>
    <text x="330" y="42" text-anchor="middle" font-size="30" fill="{NAVY}">β</text>
    <text x="330" y="322" text-anchor="middle" font-size="30" fill="{ORANGE}">1 − β</text>
    <rect x="460" y="20" width="310" height="90" rx="12" fill="{LIGHT}" stroke="{NAVY}" stroke-width="3"/>
    <text x="615" y="74" text-anchor="middle" font-size="28" fill="{NAVY}">Một đích liên kết</text>
    <rect x="460" y="230" width="310" height="90" rx="12" fill="{ORANGE_LIGHT}" stroke="{ORANGE}" stroke-width="3"/>
    <text x="615" y="284" text-anchor="middle" font-size="28" fill="{ORANGE}">Một trang bất kỳ</text>'''
    return svg_doc(800,350,"tp-title","Hai cách chọn trang tiếp theo","tp-desc",
       "Từ trang hiện tại, nhánh xác suất beta chọn một đích liên kết; nhánh một trừ beta chọn đều một trang bất kỳ.",body)


# ---------------------------------------------------------------- slide 07
def dead_redistribute():
    src=(145,200); targets=[(660,55),(660,150),(660,245),(660,340)]
    parts=[]
    for name,dst in zip("ABCD",targets):
        parts.append(arrow(src,dst,color=ORANGE,width=3,label="βδ/n",label_dy=-14).replace('fill="none" stroke=', 'fill="none" stroke-dasharray="8,6" stroke='))
        parts.append(node(*dst,name))
    parts.append(node(*src,"δ",sub="điểm nút cụt",fill=ORANGE_LIGHT,stroke=ORANGE))
    return svg_doc(800,395,"dr-title","Bù đều cho mọi trang, kể cả nút cụt","dr-desc",
       "Điểm gom ở nút cụt được chia theo mô hình tới cả bốn trang A, B, C, D. Mỗi trang nhận beta nhân delta chia n. Mũi tên nét đứt không phải liên kết của đồ thị.","".join(parts))


# ---------------------------------------------------------------- slide 13
def collect_contributions():
    b,c,a=(180,80),(180,280),(650,180)
    parts=[arrow(b,a,label="1/8"),arrow(c,a,label="1/4"),
           node(*b,"B",sub="1/4 chia 2"),node(*c,"C",sub="1/4 chia 1"),
           node(*a,"A",sub="tổng đóng góp 3/8",fill=ORANGE_LIGHT,stroke=ORANGE)]
    return svg_doc(840,370,"co-title","Cộng đóng góp theo trang đích","co-desc",
        "B đóng góp một phần tám và C đóng góp một phần tư tới A; tổng tại A là ba phần tám, chưa nhân beta và chưa cộng thành phần chung.","".join(parts))


FIGURES = {
    "model-collect.svg": collect_contributions(),
    "model-one-round.svg": one_round(),
    "model-column-a.svg": column_a(),
    "model-dead-end.svg": dead_end(),
    "model-spider-trap.svg": spider_trap(),
    "model-teleport.svg": teleport(),
    "model-dead-redistribute.svg": dead_redistribute(),
}


def main() -> None:
    out = Path(__file__).resolve().parent.parent
    for name, svg in FIGURES.items():
        (out / name).write_text(svg, encoding="utf-8")
    print(f"Đã sinh {len(FIGURES)} SVG trong {out}")


if __name__ == "__main__":
    main()
