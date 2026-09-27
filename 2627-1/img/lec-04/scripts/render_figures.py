# -*- coding: utf-8 -*-
"""
Sinh các SVG Bài 04 theo đồ thị và mô hình MMDS Chương 5.
Chạy: python render_figures.py  -> các SVG được ghi cạnh thư mục scripts.
Thuần Python, không thư viện ngoài, không mạng.
"""

import os
from html import escape

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
            f'fill="{fill}" font-weight="{weight}" text-anchor="{anchor}">{escape(s)}</text>\n')

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
               "Các trang vùng giữa trỏ tới t với tổng đóng góp từ ngoài; "
               "đích và m trang hỗ trợ H1, H2, Hm trỏ qua lại nhau trong vùng sở hữu.")
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
    # vùng giữa: một vài trang trỏ tới t, nhãn đóng góp từ ngoài
    ty = 260
    for y in (180, 260, 340):
        s += node(470, y, 30, "", label_size=20)
        s += f'  <path d="M 502,{y} Q 660,{y} 826,{ty}" fill="none" stroke="{STROKE}" stroke-width="2.5" marker-end="url(#h516-arw)"/>\n'
    s += text("Đóng góp từ ngoài", 630, 130, 26, weight="bold")
    # vùng sở hữu: t và các trang hỗ trợ
    s += node(860, ty, 34, "Đích", label_size=24)
    helpers = ((1010, 150, "H₁"), (1010, 260, "H₂"), (1010, 370, "Hₘ"))
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
    s += text("m trang hỗ trợ", 920, 430, 26)
    return s + footer()

# ---------------------------------------------------------------- 5. Luồng hạng trong cụm

def fig_flow():
    fid = "flow"
    s = header(900, 430, fid, "Ba nguồn điểm tại trang đích", "Đóng góp từ ngoài x đã gồm beta, tổng beta m p từ hỗ trợ và bước dịch chuyển b cùng đi vào đích có điểm y.")
    s += box(25, 55, 230, 90, ["Bên ngoài"], 28)
    s += box(620, 55, 255, 90, ["m trang hỗ trợ", "mỗi trang điểm p"], 26)
    s += box(335, 230, 230, 100, ["Trang đích", "điểm y"], 30)
    s += box(25, 310, 230, 85, ["Dịch chuyển"], 27)
    s += edge("M 140,145 Q 140,250 335,260", "ngoai", "dich").replace("%s", fid)
    s += edge("M 745,145 Q 745,270 565,270", "ho-tro", "dich").replace("%s", fid)
    s += edge("M 255,350 L 335,305", "dich-chuyen", "dich", 'stroke-dasharray="9 7"').replace("%s", fid)
    s += text("x", 240, 215, 34, weight="bold")
    s += text("βmp", 650, 230, 34, weight="bold")
    s += text("b", 295, 370, 34, weight="bold")
    return s + footer()

# ---------------------------------------------------------------- 6. Cặp vai trò HITS

def fig_hits():
    fid = "hits"
    W, H = 900, 420
    s = header(W, H, fid,
               "Ví dụ 5.13: điểm trung tâm và điểm uy tín",
               "Danh mục học phần là trang trung tâm; các trang học phần là "
               "trang uy tín; mũi tên là liên kết từ danh mục tới trang học phần.")
    s = s.replace(f'id="{fid}-arw"', 'id="hits-arw"')
    s += box(40, 150, 260, 120, ["Danh mục học phần", "trang trung tâm"])
    s += box(580, 60, 280, 110, ["Trang học phần 1", "trang uy tín"])
    s += box(580, 250, 280, 110, ["Trang học phần 2", "trang uy tín"])
    s += f'  <line x1="300" y1="185" x2="580" y2="120" stroke="{STROKE}" stroke-width="2.5" marker-end="url(#hits-arw)"/>\n'
    s += f'  <line x1="300" y1="235" x2="580" y2="300" stroke="{STROKE}" stroke-width="2.5" marker-end="url(#hits-arw)"/>\n'
    s += text("liên kết", 440, 140, 24, weight="bold")
    s += text("liên kết", 440, 290, 24, weight="bold")
    return s + footer()

# Sơ đồ bổ trợ: dữ kiện và quan hệ, không thay bảng số hoặc công thức KaTeX.
def arrow(fid, d, dashed=False):
    extra = 'stroke-dasharray="9 7"' if dashed else ''
    return edge(d, "", "", extra).replace("%s", fid)

def fig_pair():
    fid = "pair"
    s = header(520, 420, fid, "Điểm tại một hỗ trợ", "Đích có điểm y truyền beta y trên m tới mỗi hỗ trợ; bước dịch chuyển b cũng vào hỗ trợ.")
    s += box(130, 25, 260, 90, ["Đích: điểm y"], 29)
    s += box(130, 270, 260, 100, ["Một hỗ trợ", "điểm p"], 29)
    s += arrow(fid, "M 260,115 L 260,270")
    s += text("βy/m", 345, 200, 34, weight="bold")
    s += arrow(fid, "M 25,320 L 130,320", True)
    s += text("b", 72, 294, 34, weight="bold")
    return s + footer()

def fig_variant(back):
    fid = "variant-c" if back else "variant-a"
    title = "(c) Khuyên và liên kết tới đích" if back else "(a) Chỉ tự liên kết"
    s = header(400, 360, fid, title, "Đích vẫn trỏ tới mỗi hỗ trợ. Hỗ trợ có khuyên" + (" và cạnh quay về đích." if back else "; không còn cạnh quay về đích."))
    s += text("(c)" if back else "(a)", 40, 35, 30, weight="bold")
    s += node(90, 210, 45, "Đích", label_size=30, label_dy=10)
    s += node(305, 210, 45, "H", label_size=32, label_dy=11)
    s += arrow(fid, "M 130,190 Q 200,135 265,190")
    s += text("m hỗ trợ", 200, 130, 30)
    s += arrow(fid, "M 280,173 C 215,65 395,65 330,173")
    s += text("H → H", 305, 70, 30)
    if back:
        s += arrow(fid, "M 265,230 Q 200,285 130,230")
        s += text("H → đích", 200, 310, 30)
    return s + footer()

def fig_chain():
    fid = "chain"
    s = header(1100, 220, fid, "Chuỗi có khuyên tại đỉnh 1", "Cạnh 1 tới 1 và các cạnh i tới i cộng 1; n ít nhất 1. Dấu chấm lửng biểu diễn các đỉnh giữa khi có.")
    for x, lab in [(120,"1"),(360,"2"),(720,"n−1"),(970,"n")]:
        s += node(x,145,37,lab,label_size=29,label_dy=10)
    s += arrow(fid,"M 103,112 C 25,10 215,10 137,112")
    s += text("1 → 1",120,32,28)
    s += arrow(fid,"M 157,145 L 323,145")
    s += arrow(fid,"M 397,145 L 485,145")
    s += text("⋯",555,155,44)
    s += arrow(fid,"M 625,145 L 683,145")
    s += arrow(fid,"M 757,145 L 933,145")
    return s+footer()

def fig_storage():
    fid="storage"; s=header(1100,350,fid,"Hai cách lưu điểm xếp hạng","Hàng đầu lưu vector toàn web cho mỗi người dùng. Hàng sau lưu vector toàn web theo chủ đề và trọng số chủ đề cho người dùng.")
    s+=box(30,30,280,95,["Mỗi người dùng"],30)
    s+=box(620,30,430,95,["Vector điểm toàn web"],30)
    s+=arrow(fid,"M 310,77 L 620,77")
    s+=box(30,160,280,70,["Các chủ đề"],30)
    s+=box(620,160,430,70,["Vector điểm toàn web"],30)
    s+=arrow(fid,"M 310,195 L 620,195")
    s+=box(30,255,280,70,["Mỗi người dùng"],30)
    s+=box(620,255,430,70,["Trọng số chủ đề"],30)
    s+=arrow(fid,"M 310,290 L 620,290")
    return s+footer()

def fig_branches():
    fid="branches"; s=header(650,420,fid,"Hai nhánh di chuyển","Nhánh liên kết đi tới đích của một cạnh ra từ trang hiện tại với xác suất beta; nhánh dịch chuyển nét đứt đi tới tập S với xác suất một trừ beta.")
    s+=box(20,145,160,105,["Trang", "hiện tại"],29)
    s+=box(380,35,240,105,["Đích của", "liên kết ra"],29)
    s+=box(380,285,240,105,["Tập chủ đề S"],29)
    s+=arrow(fid,"M 180,175 L 380,90")
    s+=arrow(fid,"M 180,220 L 380,330",True)
    s+=text("β",260,108,34,weight="bold")
    s+=text("1−β",260,310,34,weight="bold")
    return s+footer()

def fig_weighted():
    fid="weighted"; s=header(420,460,fid,"Kết hợp các vector chủ đề","Các vector chủ đề một tới k được kết hợp bằng các trọng số w một tới w k.")
    s+=box(30,30,185,70,["Chủ đề 1"],29)
    s+=box(30,325,185,70,["Chủ đề k"],29)
    s+=text("⋮",120,230,46)
    s+=box(270,175,130,105,["Tổng có", "trọng số"],25)
    s+=arrow(fid,"M 215,65 Q 300,65 325,175")
    s+=arrow(fid,"M 215,360 Q 300,360 325,280")
    s+=text("w₁",305,105,32);s+=text("wₖ",305,360,32)
    return s+footer()

def fig_pipeline():
    fid="pipeline"; s=header(1100,380,fid,"Tiền tính và xếp hạng truy vấn","Hàng trên chọn chủ đề, tập dịch chuyển, rồi tính và lưu vector. Hàng dưới kết hợp trọng số truy vấn với điểm đã lưu để xếp hạng các ứng viên.")
    s+=text("Tiền tính",40,32,29,anchor="start",weight="bold")
    for x,lines in [(35,["Chọn chủ đề"]),(390,["Tập dịch chuyển"]),(745,["Tính và lưu", "vector điểm"])]:s+=box(x,60,315,90,lines,28)
    s+=arrow(fid,"M 350,105 L 390,105");s+=arrow(fid,"M 705,105 L 745,105")
    s+=text("Truy vấn",40,255,29,anchor="start",weight="bold")
    s+=box(35,280,315,80,["Trọng số chủ đề"],28)
    s+=box(390,280,315,80,["Lấy hoặc ghép điểm"],28)
    s+=box(745,280,315,80,["Xếp hạng ứng viên"],28)
    s+=arrow(fid,"M 350,320 L 390,320");s+=arrow(fid,"M 705,320 L 745,320")
    s+=arrow(fid,"M 900,150 L 900,200 L 550,200 L 550,280")
    s+=text("điểm đã lưu",725,190,28)
    return s+footer()

def fig_trust():
    fid="trust";s=header(650,430,fid,"Tập tin cậy và lan truyền điểm","Tập T được đánh giá bên ngoài đồ thị. Các liên kết ra từ T truyền điểm tới các trang ngoài T.")
    s+='<rect x="20" y="80" width="270" height="290" rx="20" fill="#fff" stroke="#2F3E7A" stroke-width="3"/>\n'
    s+='<rect x="29" y="89" width="252" height="272" rx="15" fill="none" stroke="#2F3E7A" stroke-width="2"/>\n'
    s+=text("Tập tin cậy T",155,125,29,weight="bold")
    s+=text("Đánh giá bên ngoài",155,45,28)
    s+=node(150,205,30,"",label_size=24);s+=node(150,305,30,"",label_size=24)
    for x,y in [(505,130),(505,260),(570,370)]:s+=node(x,y,30,"",label_size=24)
    s+=arrow(fid,"M 180,195 L 475,138");s+=arrow(fid,"M 180,212 L 475,252");s+=arrow(fid,"M 180,310 L 540,365")
    return s+footer()

def fig_hits_contribution():
    fid="hits-contribution";s=header(440,440,fid,"Hai chiều đóng góp qua một cạnh","Cạnh i tới j cộng điểm trung tâm h_i vào uy tín a_j; uy tín mới a_j được cộng về trung tâm h_i.")
    s+=node(85,215,43,"i",label_size=36);s+=node(355,215,43,"j",label_size=36)
    s+=arrow(fid,"M 128,205 L 312,205")
    s+=text("cạnh i → j",220,180,29)
    s+=arrow(fid,"M 100,170 Q 220,35 340,170",True)
    s+=text("hᵢ → aⱼ",220,70,31,weight="bold")
    s+=arrow(fid,"M 340,260 Q 220,395 100,260",True)
    s+=text("aⱼ mới → hᵢ",220,380,31,weight="bold")
    return s+footer()

def fig_internal_edges():
    fid="internal-edges"
    s=header(1000,290,fid,"Hai nhóm cạnh nội bộ", "Đích có m cạnh ra tới m hỗ trợ; mỗi hỗ trợ có một cạnh quay lại đích. Tổng là hai m cạnh nội bộ.")
    s+=box(45,80,240,120,["Trang đích"],36)
    s+=box(675,80,280,120,["m trang hỗ trợ"],34)
    s+=arrow(fid,"M 285,105 L 675,105")
    s+=arrow(fid,"M 675,175 L 285,175")
    s+=text("m cạnh đi tới hỗ trợ",480,70,32,weight="bold")
    s+=text("m cạnh quay lại đích",480,230,32,weight="bold")
    return s+footer()

# ---------------------------------------------------------------- main

def main():
    write("hinh-5-1-trung-tinh.svg", fig_5_1())
    write("hinh-5-15.svg", fig_5_15())
    write("hinh-5-18.svg", fig_5_18())
    write("hinh-5-16-cum-thao-tung.svg", fig_5_16())
    write("luong-hang-trong-cum.svg", fig_flow())
    write("cap-vai-tro-hits.svg", fig_hits())
    write("hinh-5-15-tin-cay.svg", fig_5_15().replace("tập chủ đề S", "tập tin cậy T").replace("chữ S", "chữ T").replace(">S<", ">T<"))
    write("hinh-5-1-kiem-tra.svg", fig_5_1().replace('data-source="B" data-target="A"', 'data-source="B" data-target="A" stroke-dasharray="8 3"') .replace('</svg>', text("Bậc ra của B: 2",310,425,28)+"</svg>"))
    write("hinh-5-18-kiem-tra.svg", fig_5_18().replace('data-source="B"', 'stroke-dasharray="8 3" data-source="B"'))
    write("diem-mot-ho-tro.svg", fig_pair())
    write("ho-tro-tu-khuyen.svg", fig_variant(False))
    write("ho-tro-khuyen-va-dich.svg", fig_variant(True))
    write("chuoi-co-khuyen.svg", fig_chain())
    write("luu-vector-theo-chu-de.svg", fig_storage())
    write("hai-nhanh-di-chuyen.svg", fig_branches())
    write("tong-vector-chu-de.svg", fig_weighted())
    write("tien-tinh-va-truy-van.svg", fig_pipeline())
    write("tap-tin-cay.svg", fig_trust())
    write("dong-gop-hits.svg", fig_hits_contribution())
    write("hai-nhom-canh-noi-bo.svg", fig_internal_edges())

if __name__ == "__main__":
    main()
