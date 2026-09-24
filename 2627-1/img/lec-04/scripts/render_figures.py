# -*- coding: utf-8 -*-
"""
Sinh 6 SVG minh họa (Hình 5.1, 5.15, 5.18, 5.16, sơ đồ luồng, cặp vai trò HITS).
Chạy: python render_figures.py  -> các SVG được ghi cạnh thư mục scripts.
Thuần Python, không thư viện ngoài, không mạng.
"""

import os

OUT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

STROKE = "#B15A2B"
NODE = "#2F3E7A"
BG = "#edf4ff"
FONT = "Arial, sans-serif"

# ---------------------------------------------------------------- helpers

def header(w, h, fid, title, desc):
    return (
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" '
        f'width="{w}" height="{h}" role="img" aria-labelledby="{fid}-t {fid}-d">\n'
        f'  <title id="{fid}-t">{title}</title>\n'
        f'  <desc id="{fid}-d">{desc}</desc>\n'
        f'  <defs>\n'
        f'    <marker id="{fid}-arw" markerUnits="userSpaceOnUse" markerWidth="12" '
        f'markerHeight="12" refX="10" refY="5" orient="auto">\n'
        f'      <path d="M0,0 L10,5 L0,10 Z" fill="{STROKE}"/>\n'
        f'    </marker>\n'
        f'  </defs>\n'
        f'  <rect x="0" y="0" width="{w}" height="{h}" fill="{BG}"/>\n'
    )

def edge(d, src, dst, extra=""):
    return (f'  <path d="{d}" fill="none" stroke="{STROKE}" stroke-width="2.5" '
            f'marker-end="url(#%s-arw)" data-source="{src}" data-target="{dst}" {extra}/>\n')

def plain_line(x1, y1, x2, y2, label=None, lx=0, ly=0, lsize=22, extra_marker=True):
    m = ' marker-end="url(#ARW)"' if extra_marker else ""
    s = (f'  <line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{STROKE}" '
         f'stroke-width="2.5"{m}/>\n')
    if label:
        s += text(label, (x1 + x2) / 2 + lx, (y1 + y2) / 2 + ly, lsize, anchor="middle")
    return s

def text(s, x, y, size, anchor="middle", fill=NODE, weight="normal"):
    return (f'  <text x="{x}" y="{y}" font-family="{FONT}" font-size="{size}" '
            f'fill="{fill}" font-weight="{weight}" text-anchor="{anchor}">{s}</text>\n')

def node(x, y, r, label, extra="", label_dy=12, label_size=34):
    s = f'  <circle cx="{x}" cy="{y}" r="{r}" fill="#ffffff" stroke="{NODE}" stroke-width="3" {extra}/>\n'
    s += text(label, x, y + label_dy, label_size, weight="bold")
    return s

def box(x, y, w, h, lines, size=26, fill="#ffffff"):
    s = (f'  <rect x="{x}" y="{y}" width="{w}" height="{h}" rx="10" fill="{fill}" '
         f'stroke="{NODE}" stroke-width="2.5"/>\n')
    n = len(lines)
    for i, ln in enumerate(lines):
        ty = y + h / 2 + (i - (n - 1) / 2) * (size + 6) + size * 0.35
        s += text(ln, x + w / 2, ty, size, weight="bold")
    return s

def footer():
    return '</svg>\n'

def write(name, content):
    path = os.path.join(OUT_DIR, name)
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)
    print("đã ghi:", path)

# Danh sách cạnh G4 (đã duyệt): A→B, B→A, A→C, C→A, B→D, D→B, A→D, D→C
G4_EDGES = [
    ("A", "B", "ngang giữa"),
    ("B", "A", "cong phía trên"),
    ("A", "C", "thẳng dọc"),
    ("C", "A", "vòng ngoài trái"),
    ("B", "D", "thẳng dọc"),
    ("D", "B", "vòng ngoài phải"),
    ("A", "D", "chéo giữa"),
    ("D", "C", "ngang dưới"),
]

# Danh sách cạnh G5 (đã duyệt): G4 trừ C→A, cộng C→E; E không cạnh ra
G5_EDGES = [
    ("A", "B", "ngang giữa"),
    ("B", "A", "cong phía trên"),
    ("A", "C", "thẳng dọc"),
    ("B", "D", "thẳng dọc"),
    ("D", "B", "vòng ngoài phải"),
    ("A", "D", "chéo giữa"),
    ("D", "C", "ngang dưới"),
    ("C", "E", "thẳng dọc xuống"),
]

# Tọa độ G4/G5
AX, AY = 140, 90
BX, BY = 480, 90
CX, CY = 140, 350
DX, DY = 480, 350
EX, EY = 140, 475
R = 42

def g4_edge_paths(fid):
    """8 đường cạnh G4, kết thúc tại mép nút (r=42)."""
    import math
    dx, dy = DX - AX, DY - AY
    L = math.hypot(dx, dy)
    ux, uy = dx / L, dy / L
    return {
        ("A", "B"): f"M {AX+R},{AY} L {BX-R},{AY}",
        ("B", "A"): f"M {BX},{BY-R} Q 310,-20 {AX},{AY-R}",
        ("A", "C"): f"M {AX},{AY+R} L {CX},{CY-R}",
        ("C", "A"): f"M {CX-R},{CY} Q 0,220 {AX-R},{AY}",
        ("B", "D"): f"M {BX},{BY+R} L {DX},{DY-R}",
        ("D", "B"): f"M {DX+R},{DY} Q 620,220 {BX+R},{BY}",
        ("A", "D"): (f"M {AX+R*ux:.1f},{AY+R*uy:.1f} "
                     f"L {DX-R*ux:.1f},{DY-R*uy:.1f}"),
        ("D", "C"): f"M {DX-R},{DY} L {CX+R},{DY}",
    }

# ---------------------------------------------------------------- 1. Hình 5.1

def fig_5_1():
    fid = "h51"
    s = header(620, 440, fid,
               "Hình 5.1: đồ thị G4",
               "Đồ thị có hướng G4 với bốn đỉnh A, B, C, D và tám cạnh; các cạnh ngược chiều "
               "được vẽ bằng hai đường riêng biệt.")
    paths = g4_edge_paths(fid)
    # marker id dùng chung trong tệp này
    s = s.replace(f'url(#{fid}-arw)', 'url(#h51-arw)')
    for a, b, _ in G4_EDGES:
        s += edge(paths[(a, b)], a, b).replace('url(#%s-arw)', 'url(#h51-arw)')
    s += node(AX, AY, R, "A")
    s += node(BX, BY, R, "B")
    s += node(CX, CY, R, "C")
    s += node(DX, DY, R, "D")
    return s + footer()

# ---------------------------------------------------------------- 2. Hình 5.15

def fig_5_15():
    fid = "h515"
    s = header(620, 500, fid,
               "Hình 5.15: G4 với tập chủ đề S",
               "Đồ thị G4 như Hình 5.1; B và D có thêm viền ngoài và chữ S, "
               "thuộc tập chủ đề S.")
    paths = g4_edge_paths(fid)
    for a, b, _ in G4_EDGES:
        s += edge(paths[(a, b)], a, b).replace('url(#%s-arw)', 'url(#h515-arw)')
    s += node(AX, AY, R, "A")
    s += node(CX, CY, R, "C")
    # B và D: viền ngoài + chữ S gần đỉnh, không che nhãn
    for (x, y) in ((BX, BY), (DX, DY)):
        s += f'  <circle cx="{x}" cy="{y}" r="{R+8}" fill="none" stroke="{NODE}" stroke-width="2.5"/>\n'
        s += node(x, y, R, "")
        s += text("S", x, y - 8, 22, weight="bold")
        s += text("B" if y == BY else "D", x, y + 26, 34, weight="bold")
    s += text("B và D thuộc tập chủ đề S", 310, 470, 30, weight="bold")
    return s + footer()

# ---------------------------------------------------------------- 3. Hình 5.18

def fig_5_18():
    fid = "h518"
    s = header(620, 540, fid,
               "Hình 5.18: đồ thị G5",
               "Đồ thị G5 với đỉnh A, B, C, D, E và tám cạnh: A→B, B→A, A→C, "
               "B→D, D→B, A→D, D→C, C→E; E không có cạnh ra.")
    import math
    dx, dy = DX - AX, DY - AY
    L = math.hypot(dx, dy)
    ux, uy = dx / L, dy / L
    paths = g4_edge_paths(fid)
    paths[("C", "E")] = f"M {CX},{CY+R} L {EX},{EY-R}"
    for a, b, _ in G5_EDGES:
        s += edge(paths[(a, b)], a, b).replace('url(#%s-arw)', 'url(#h518-arw)')
    s += node(AX, AY, R, "A")
    s += node(BX, BY, R, "B")
    s += node(CX, CY, R, "C")
    s += node(DX, DY, R, "D")
    s += node(EX, EY, R, "E")
    s += text("không cạnh ra", EX + R + 14, EY + 12, 30, anchor="start", weight="bold")
    return s + footer()

# ---------------------------------------------------------------- 4. Hình 5.16

def fig_5_16():
    fid = "h516"
    W, H = 1100, 480
    s = header(W, H, fid,
               "Hình 5.16: cụm thao túng",
               "Ba vùng: Không thể tác động, Có thể tác động, Trang sở hữu. "
               "Các trang vùng giữa trỏ tới t với tổng đóng góp ngoài x; "
               "t và q trang hỗ trợ H1, H2, Hq trỏ qua lại nhau trong vùng sở hữu.")
    # marker riêng
    s = s.replace(f'id="{fid}-arw"', 'id="h516-arw"')
    # vùng
    for (x, w, l1, l2) in ((20, 320, "Không thể", "tác động"),
                           (360, 380, "Có thể", "tác động"),
                           (760, 320, "Trang sở hữu", None)):
        s += f'  <rect x="{x}" y="20" width="{w}" height="440" rx="12" fill="#ffffff" stroke="{NODE}" stroke-width="2"/>\n'
        s += text(l1, x + w / 2, 62, 34, weight="bold")
        if l2:
            s += text(l2, x + w / 2, 102, 34, weight="bold")
    # vùng trái: trang không mũi tên đi ra
    for y in (200, 280, 360):
        s += node(180, y, 30, "", label_size=20)
    s += text("ngoài quyền tác động", 180, 430, 22)
    # vùng giữa: một vài trang trỏ tới t, nhãn x ở nhóm đầu vào
    ty = 260
    for y in (180, 260, 340):
        s += node(470, y, 30, "", label_size=20)
        s += f'  <path d="M 502,{y} Q 660,{y} 826,{ty}" fill="none" stroke="{STROKE}" stroke-width="2.5" marker-end="url(#h516-arw)"/>\n'
    s += text("x đã gộp hệ số β", 630, 130, 26, weight="bold")
    # vùng sở hữu: t và các trang hỗ trợ
    s += node(860, ty, 34, "t", label_size=34)
    helpers = ((1010, 150, "H₁"), (1010, 260, "H₂"), (1010, 370, "H_q"))
    for (hx, hy, lab) in helpers:
        s += node(hx, hy, 28, lab, label_size=24)
        # t → hỗ trợ (đường trên) và hỗ trợ → t (đường dưới), cách biệt ≥10
        if hy == ty:
            s += f'  <path d="M 894,{ty-8} L {hx-28},{ty-8}" fill="none" stroke="{STROKE}" stroke-width="2.5" marker-end="url(#h516-arw)"/>\n'
            s += f'  <path d="M {hx-28},{ty+8} L 894,{ty+8}" fill="none" stroke="{STROKE}" stroke-width="2.5" marker-end="url(#h516-arw)"/>\n'
        else:
            s += f'  <path d="M 890,{ty-14} Q 950,{hy-14} {hx-28},{hy}" fill="none" stroke="{STROKE}" stroke-width="2.5" marker-end="url(#h516-arw)"/>\n'
            s += f'  <path d="M {hx-28},{hy+10} Q 950,{hy+10} 892,{ty+14}" fill="none" stroke="{STROKE}" stroke-width="2.5" marker-end="url(#h516-arw)"/>\n'
    s += text("⋮", 1010, 325, 34)
    s += text("q trang hỗ trợ", 920, 430, 26)
    return s + footer()

# ---------------------------------------------------------------- 5. Luồng hạng trong cụm

def fig_flow():
    fid = "flow"
    W, H = 900, 420
    s = header(W, H, fid,
               "Sơ đồ luồng hạng trong cụm",
               "Bên ngoài cho vào trang đích t lượng x; t và q trang hỗ trợ trao đổi: "
               "mỗi trang hỗ trợ nhận beta*y/q và tổng beta*q*z trở về t; "
               "dải dưới ghi dịch chuyển đều (1-beta)/N cho mỗi trang.")
    s = s.replace(f'id="{fid}-arw"', 'id="flow-arw"')
    s += box(40, 90, 200, 90, ["Bên ngoài"])
    s += box(340, 80, 220, 110, ["Trang đích t", "hạng y"])
    s += box(640, 80, 230, 110, ["q trang hỗ trợ,", "mỗi trang hạng z"])
    # ngoài → đích, nhãn x
    s += f'  <line x1="240" y1="135" x2="340" y2="135" stroke="{STROKE}" stroke-width="2.5" marker-end="url(#flow-arw)"/>\n'
    s += text("x", 290, 122, 26, weight="bold")
    # đích → hỗ trợ (đường trên)
    s += f'  <path d="M 560,115 Q 600,100 640,115" fill="none" stroke="{STROKE}" stroke-width="2.5" marker-end="url(#flow-arw)"/>\n'
    s += text("mỗi trang nhận βy/q", 600, 70, 22, weight="bold")
    # hỗ trợ → đích (đường dưới)
    s += f'  <path d="M 640,155 Q 600,170 560,155" fill="none" stroke="{STROKE}" stroke-width="2.5" marker-end="url(#flow-arw)"/>\n'
    s += text("tổng βqz", 600, 200, 22, weight="bold")
    # dải dưới
    s += f'  <rect x="40" y="300" width="830" height="70" rx="10" fill="#ffffff" stroke="{NODE}" stroke-width="2"/>\n'
    s += text("Dịch chuyển đều: mỗi trang nhận (1−β)/N", 455, 343, 26, weight="bold")
    return s + footer()

# ---------------------------------------------------------------- 6. Cặp vai trò HITS

def fig_hits():
    fid = "hits"
    W, H = 900, 420
    s = header(W, H, fid,
               "Ví dụ 5.13: điểm trung tâm và điểm thẩm quyền",
               "Danh mục học phần là trang trung tâm; các trang học phần là "
               "trang thẩm quyền; mũi tên là liên kết từ danh mục tới trang học phần.")
    s = s.replace(f'id="{fid}-arw"', 'id="hits-arw"')
    s += box(40, 150, 260, 120, ["Danh mục học phần", "trang trung tâm"])
    s += box(580, 60, 280, 110, ["Trang học phần 1", "trang thẩm quyền"])
    s += box(580, 250, 280, 110, ["Trang học phần 2", "trang thẩm quyền"])
    s += f'  <line x1="300" y1="185" x2="580" y2="120" stroke="{STROKE}" stroke-width="2.5" marker-end="url(#hits-arw)"/>\n'
    s += f'  <line x1="300" y1="235" x2="580" y2="300" stroke="{STROKE}" stroke-width="2.5" marker-end="url(#hits-arw)"/>\n'
    s += text("liên kết", 440, 140, 24, weight="bold")
    s += text("liên kết", 440, 290, 24, weight="bold")
    return s + footer()

# ---------------------------------------------------------------- main

def main():
    write("hinh-5-1-trung-tinh.svg", fig_5_1())
    write("hinh-5-15.svg", fig_5_15())
    write("hinh-5-18.svg", fig_5_18())
    write("hinh-5-16-cum-thao-tung.svg", fig_5_16())
    write("luong-hang-trong-cum.svg", fig_flow())
    write("cap-vai-tro-hits.svg", fig_hits())

if __name__ == "__main__":
    main()
