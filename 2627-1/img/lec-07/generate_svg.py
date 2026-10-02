#!/usr/bin/env python3
"""Tái tạo các hình vẽ lại trong lượt duyệt Bài 07 bằng thư viện chuẩn Python; không cần mạng.

Các SVG cũ viết tay (chưa vẽ lại) không do tệp này sinh ra.
"""
from pathlib import Path
from html import escape

OUT = Path(__file__).resolve().parent
BLUE, ORANGE, GREEN, INK, GRAY = '#2f3e7a', '#a85b23', '#26704e', '#233247', '#6b7788'
PALE_BLUE, PALE_ORANGE, PALE_GREEN, PALE_GRAY = '#edf4ff', '#fff4e9', '#eef7f2', '#f4f6f9'


def text(x, y, value, size=28, color=INK, anchor='middle', weight='normal', italic=False):
    style = ' font-style="italic"' if italic else ''
    return (f'<text x="{x}" y="{y}" font-size="{size}" fill="{color}" text-anchor="{anchor}" '
            f'font-weight="{weight}"{style}>{escape(str(value))}</text>')


def line(x1, y1, x2, y2, color=BLUE, dash='', arrow=False, width=3):
    return (f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{color}" stroke-width="{width}"'
            + (f' stroke-dasharray="{dash}"' if dash else '')
            + (' marker-end="url(#arrow)"' if arrow else '') + '/>')


def rect(x, y, w, h, fill=PALE_BLUE, color=BLUE, dash=''):
    return (f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="10" fill="{fill}" stroke="{color}" stroke-width="2.5"'
            + (f' stroke-dasharray="{dash}"' if dash else '') + '/>')


def box(x, y, w, h, lines, fill=PALE_BLUE, color=BLUE, size=28, dash=''):
    """Hộp có một hoặc nhiều dòng chữ căn giữa; dòng đầu in đậm."""
    out = rect(x, y, w, h, fill, color, dash)
    n = len(lines)
    gap = size * 1.25
    y0 = y + h / 2 - gap * (n - 1) / 2 + size * 0.35
    for i, value in enumerate(lines):
        out += text(x + w / 2, y0 + i * gap, value, size if i == 0 else size - 3,
                    color if i == 0 else INK, weight='bold' if i == 0 else 'normal')
    return out


def svg(name, w, h, title, desc, body):
    data = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" role="img" aria-labelledby="title desc">
<title id="title">{escape(title)}</title><desc id="desc">{escape(desc)}</desc>
<defs><marker id="arrow" markerWidth="10" markerHeight="10" refX="9" refY="4.5" orient="auto"><path d="M0,0 L9,4.5 L0,9 Z" fill="{BLUE}"/></marker></defs>
<g font-family="Arial, sans-serif">{body}</g></svg>
'''
    (OUT / name).write_text(data, encoding='utf-8')


def truy_hoi_ngu_nghia():
    # P01: quy trình truy hồi ngữ nghĩa theo BIODS 271 bài 12 tr.16; số liệu kho theo tr.17.
    b = ''
    b += box(20, 40, 240, 90, ['Đoạn văn bản', '10¹⁰ đoạn'])
    b += box(20, 230, 240, 90, ['Câu truy vấn'], PALE_ORANGE, ORANGE)
    b += box(345, 40, 230, 280, ['Mô hình nhúng', 'cùng một mô hình'], PALE_GRAY, INK)
    b += line(266, 85, 337, 85, arrow=True) + line(266, 275, 337, 275, arrow=True)
    b += box(660, 40, 300, 90, ['Kho véc-tơ', '10¹⁰ véc-tơ × 3072 chiều'])
    b += box(660, 230, 300, 90, ['Véc-tơ truy vấn q', '3072 chiều'], PALE_ORANGE, ORANGE)
    b += line(581, 85, 652, 85, arrow=True) + line(581, 275, 652, 275, arrow=True)
    b += box(1050, 135, 230, 90, ['K đoạn', 'gần q nhất'], PALE_GREEN, GREEN)
    b += line(966, 100, 1042, 160, arrow=True) + line(966, 260, 1042, 200, arrow=True)
    b += text(1005, 362, 'so khoảng cách giữa q và mọi véc-tơ trong kho', 24, GRAY, 'middle', italic=True)
    svg('truy-hoi-ngu-nghia.svg', 1300, 380, 'Truy hồi ngữ nghĩa bằng véc-tơ nhúng',
        'Mười tỷ đoạn văn bản và câu truy vấn đi qua cùng một mô hình nhúng, thành véc-tơ 3072 chiều. '
        'Kết quả là K đoạn có véc-tơ gần véc-tơ truy vấn q nhất.', b)


def do_thu_hoi():
    # A01: ví dụ độ thu hồi tại 5; tập đúng {a,b,c,d,e}, tập trả về {c,d,e,f,g}.
    b = ''
    b += f'<circle cx="250" cy="230" r="170" fill="{PALE_BLUE}" fill-opacity="0.85" stroke="{BLUE}" stroke-width="4"/>'
    b += f'<circle cx="470" cy="230" r="170" fill="{PALE_ORANGE}" fill-opacity="0.6" stroke="{ORANGE}" stroke-width="4" stroke-dasharray="14 8"/>'
    b += text(190, 40, 'Tập đúng', 32, BLUE, weight='bold') + text(530, 40, 'Tập trả về', 32, ORANGE, weight='bold')
    for label, x, y in [('a', 165, 195), ('b', 165, 275), ('c', 360, 165), ('d', 360, 235), ('e', 360, 305),
                        ('f', 555, 195), ('g', 555, 275)]:
        b += text(x, y, label, 40, INK, weight='bold')
    b += text(360, 440, 'giao gồm c, d, e', 30, INK)
    svg('do-thu-hoi.svg', 720, 460, 'Độ thu hồi tại 5',
        'Tập đúng gồm a, b, c, d, e; tập chỉ mục trả về gồm c, d, e, f, g. Phần giao có ba phần tử c, d, e.', b)


# Đồ thị ví dụ H00–H06: tọa độ thật, khoảng cách tới q (gốc) là 9, 7, 5, 8, 4, 2, 1.
GRAPH_POS = {'e': (-9, 0), 'a': (-4.9, 5), 'b': (-1.5, 4.77), 's': (-6, -5.29),
             't': (-2, -3.46), 'u': (0.6, -1.9), 'z': (1, 0)}
GRAPH_DIST = {'e': 9, 'a': 7, 'b': 5, 's': 8, 't': 4, 'u': 2, 'z': 1}
GRAPH_EDGES = [('e', 'a'), ('a', 'b'), ('e', 's'), ('s', 't'), ('t', 'u'), ('u', 'z')]
# Vị trí nhãn so với tâm đỉnh, tránh đè cạnh.
GRAPH_LABEL = {'e': (-14, -40), 'a': (0, -42), 'b': (0, -42), 's': (0, 62),
               't': (-10, 62), 'u': (40, 52), 'z': (66, 10)}


def do_thi_vi_du(name, mode):
    """mode: 'base' (cấu trúc), 'greedy' (đường tham lam), 'beam' (đường của tìm kiếm chùm)."""
    sc, ox, oy = 40, 410, 290
    X = lambda v: ox + sc * GRAPH_POS[v][0]
    Y = lambda v: oy - sc * GRAPH_POS[v][1]
    greedy = {('e', 'a'), ('a', 'b')}
    beam = {('e', 's'), ('s', 't'), ('t', 'u'), ('u', 'z')}
    b = ''
    for u, v in GRAPH_EDGES:
        color, width, dash = '#9aa6b8', 4, ''
        if mode == 'greedy' and (u, v) in greedy:
            color, width = ORANGE, 7
        if mode == 'beam' and (u, v) in beam:
            color, width, dash = GREEN, 7, '14 8'
        b += line(X(u), Y(u), X(v), Y(v), color, dash, width=width)
    for v in GRAPH_POS:
        fill, stroke = '#ffffff', BLUE
        if mode == 'greedy' and v == 'b':
            fill, stroke = PALE_ORANGE, ORANGE
        if mode == 'beam' and v == 'z':
            fill, stroke = PALE_GREEN, GREEN
        b += f'<circle cx="{X(v):.1f}" cy="{Y(v):.1f}" r="25" fill="{fill}" stroke="{stroke}" stroke-width="4"/>'
        b += text(f'{X(v):.1f}', f'{Y(v) + 11:.1f}', v, 32, INK, weight='bold')
        dx, dy = GRAPH_LABEL[v]
        b += text(f'{X(v) + dx:.1f}', f'{Y(v) + dy:.1f}', GRAPH_DIST[v], 30, BLUE)
    qx, qy = ox, oy
    b += f'<rect x="{qx - 15}" y="{qy - 15}" width="30" height="30" fill="{ORANGE}" transform="rotate(45 {qx} {qy})"/>'
    b += text(qx - 42, qy + 12, 'q', 34, ORANGE, weight='bold', italic=True)
    b += text(900, 40, 'số màu xanh:', 28, BLUE, 'end')
    b += text(900, 78, 'khoảng cách tới q', 28, BLUE, 'end')
    b += text(900, 116, 'điểm vào: e', 28, INK, 'end')
    if mode == 'base':
        pass
    elif mode == 'greedy':
        b += line(716, 176, 768, 176, ORANGE, width=7) + text(900, 186, 'tham lam', 28, INK, 'end')
    else:
        b += line(640, 176, 692, 176, GREEN, '14 8', width=7) + text(900, 186, 'tìm kiếm chùm', 28, INK, 'end')
    titles = {
        'base': ('Đồ thị lân cận ví dụ',
                 'Bảy đỉnh e, a, b, s, t, u, z có khoảng cách tới q lần lượt 9, 7, 5, 8, 4, 2, 1; '
                 'cạnh e–a, a–b, e–s, s–t, t–u, u–z; điểm vào là e.'),
        'greedy': ('Tìm kiếm tham lam dừng ở b',
                   'Từ e, tham lam đi qua a tới b (khoảng cách 5) rồi dừng vì lân cận duy nhất của b là a; '
                   'z ở khoảng cách 1 nằm trên nhánh s, t, u.'),
        'beam': ('Tìm kiếm chùm đi tới z',
                 'Tìm kiếm chùm với ef bằng 3 giữ s trong hàng đợi, sau khi b không còn lân cận mới thì mở s, '
                 'rồi đi qua t, u tới z ở khoảng cách 1.'),
    }
    svg(name, 910, 590, titles[mode][0], titles[mode][1], b)


def trang_thai_search_layer():
    # H04: trạng thái của SEARCH-LAYER trên đồ thị ví dụ sau khi mở b, ef = 3.
    b = rect(20, 20, 820, 380, PALE_GRAY, INK)
    b += text(45, 66, 'V: đỉnh đã thấy', 30, INK, 'start', weight='bold')
    b += rect(230, 90, 300, 290, PALE_ORANGE, ORANGE, '12 7')
    b += rect(410, 150, 410, 210, PALE_BLUE, BLUE)
    b += text(250, 130, 'C: chưa mở', 28, ORANGE, 'start', weight='bold')
    b += text(800, 190, 'W: ef đỉnh gần q nhất', 28, BLUE, 'end', weight='bold')
    b += text(125, 270, 'e : 9', 34, INK, weight='bold')
    b += text(470, 270, 's : 8', 34, INK, weight='bold')
    b += text(670, 255, 'b : 5', 34, INK, weight='bold') + text(670, 320, 'a : 7', 34, INK, weight='bold')
    svg('search-layer-trang-thai.svg', 860, 420, 'Ba tập của SEARCH-LAYER',
        'Sau khi mở b với ef bằng 3: V gồm e, a, b, s; C gồm s; W gồm b, a, s. '
        'C và W là hai tập con của V; s thuộc cả C và W; e chỉ thuộc V.', b)


def main():
    truy_hoi_ngu_nghia()
    do_thu_hoi()
    do_thi_vi_du('do-thi-vi-du.svg', 'base')
    do_thi_vi_du('do-thi-tham-lam.svg', 'greedy')
    do_thi_vi_du('do-thi-chum.svg', 'beam')
    trang_thai_search_layer()


if __name__ == '__main__':
    main()
