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
    seen2, w2 = {'e', 'a', 's', 'b'}, {'a', 'b'}
    for v in GRAPH_POS:
        fill, stroke = '#ffffff', BLUE
        if mode == 'seen2':
            if v in w2:
                b += f'<circle cx="{X(v):.1f}" cy="{Y(v):.1f}" r="34" fill="none" stroke="{BLUE}" stroke-width="5"/>'
            fill, stroke = (PALE_BLUE, BLUE) if v in seen2 else ('#ffffff', '#9aa6b8')
        if mode == 'greedy' and v == 'b':
            fill, stroke = PALE_ORANGE, ORANGE
        if mode == 'beam' and v == 'z':
            fill, stroke = PALE_GREEN, GREEN
        dash_attr = ' stroke-dasharray="6 5"' if mode == 'seen2' and v not in seen2 else ''
        b += f'<circle cx="{X(v):.1f}" cy="{Y(v):.1f}" r="25" fill="{fill}" stroke="{stroke}" stroke-width="4"{dash_attr}/>'
        b += text(f'{X(v):.1f}', f'{Y(v) + 11:.1f}', v, 32, INK, weight='bold')
        dx, dy = GRAPH_LABEL[v]
        b += text(f'{X(v) + dx:.1f}', f'{Y(v) + dy:.1f}', GRAPH_DIST[v], 30, BLUE)
    qx, qy = ox, oy
    b += f'<rect x="{qx - 15}" y="{qy - 15}" width="30" height="30" fill="{ORANGE}" transform="rotate(45 {qx} {qy})"/>'
    b += text(qx - 42, qy + 12, 'q', 34, ORANGE, weight='bold', italic=True)
    b += text(900, 40, 'số màu xanh:', 28, BLUE, 'end')
    b += text(900, 78, 'khoảng cách tới q', 28, BLUE, 'end')
    b += text(900, 116, 'điểm vào: e', 28, INK, 'end')
    if mode == 'seen2':
        b += f'<circle cx="680" cy="168" r="16" fill="{PALE_BLUE}" stroke="{BLUE}" stroke-width="4"/>' + text(900, 178, 'đã thấy (V)', 28, INK, 'end')
        b += f'<circle cx="680" cy="226" r="16" fill="#ffffff" stroke="#9aa6b8" stroke-width="4" stroke-dasharray="6 5"/>' + text(900, 236, 'chưa thấy', 28, INK, 'end')
        b += f'<circle cx="680" cy="284" r="20" fill="none" stroke="{BLUE}" stroke-width="5"/>' + text(900, 294, 'W, ef = 2', 28, INK, 'end')
    if mode in ('base', 'seen2'):
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
        'seen2': ('SEARCH-LAYER với ef bằng 2 dừng sớm',
                  'Với ef bằng 2 và điểm vào e, thuật toán dừng khi đã thấy e, a, s, b; W gồm b và a; '
                  't, u, z chưa được thấy.'),
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


def canh_dai_mot_chieu():
    # H06B: ví dụ một chiều dựng lại theo Princeton lớp 9 tr.12–13; q ở tọa độ 6,4.
    names = ['s'] + [f'p{i}' for i in range(1, 12)]
    X = lambda i: 70 + 78 * i
    q = 6.4
    b = ''
    rows = [(150, 'Chỉ cạnh ngắn: s → p1 → … → p6, 6 bước', [], ['s', 'p1', 'p2', 'p3', 'p4', 'p5', 'p6']),
            (400, 'Thêm cạnh dài: s → p4 → p5 → p6, 3 bước', [(0, 4), (4, 8), (8, 11)], ['s', 'p4', 'p5', 'p6'])]
    for y, title, longs, path in rows:
        b += text(40, y - 95, title, 30, INK, 'start', weight='bold')
        hop = set(zip(path, path[1:]))
        for i in range(11):
            on = (names[i], names[i + 1]) in hop
            b += line(X(i) + 18, y, X(i + 1) - 18, y, ORANGE if on else '#9aa6b8', width=6 if on else 3)
        for i, j in longs:
            on = (names[i], names[j]) in hop
            mid, r = (X(i) + X(j)) / 2, (X(j) - X(i)) / 2
            b += (f'<path d="M{X(i)},{y - 18} A{r},{r * 0.42} 0 0 1 {X(j)},{y - 18}" fill="none" '
                  f'stroke="{ORANGE if on else "#9aa6b8"}" stroke-width="{6 if on else 3}"'
                  + ('' if on else ' stroke-dasharray="10 7"') + '/>')
        for i, v in enumerate(names):
            stroke = ORANGE if v in path else BLUE
            b += f'<circle cx="{X(i)}" cy="{y}" r="18" fill="#ffffff" stroke="{stroke}" stroke-width="4"/>'
            b += text(X(i), y + 52, v, 24, INK)
        qx = 70 + 78 * q
        b += line(qx, y - 38, qx, y - 4, ORANGE, '4 4', width=2)
        b += f'<rect x="{qx - 11}" y="{y - 59}" width="22" height="22" fill="{ORANGE}" transform="rotate(45 {qx} {y - 48})"/>'
        b += text(qx + 26, y - 38, 'q', 28, ORANGE, 'start', weight='bold', italic=True)
    b += line(560, 520, 612, 520, ORANGE, width=6) + text(624, 530, 'đường tham lam từ s', 26, INK, 'start')
    svg('canh-dai-mot-chieu.svg', 1000, 545, 'Cạnh dài rút ngắn đường đi',
        'Mười hai điểm s, p1 đến p11 trên một đường thẳng, q nằm giữa p6 và p7, gần p6 hơn. '
        'Chỉ có cạnh giữa hai điểm liền kề thì tham lam từ s cần 6 bước tới p6; '
        'thêm cạnh dài s–p4, p4–p8, p8–p11 thì chỉ cần 3 bước s, p4, p5, p6.', b)


def do_thi_nhieu_tang(name='do-thi-nhieu-tang.svg', compact=False):
    # H07 (đầy đủ) và H09 (gọn): ba tầng trên cùng 12 điểm của ví dụ một chiều; q ở tọa độ 6,4.
    names = ['s'] + [f'p{i}' for i in range(1, 12)]
    if compact:
        x0, dx, ys, r, fs, left = 105, 58, (55, 175, 295), 15, 30, 10
    else:
        x0, dx, ys, r, fs, left = 150, 72, (70, 215, 360), 17, 28, 20
    X = lambda v: x0 + dx * names.index(v)
    layers = [(2, ys[0], ['s', 'p4', 'p8']), (1, ys[1], ['s', 'p2', 'p4', 'p6', 'p8', 'p10']), (0, ys[2], names)]
    path = {2: ['s', 'p4', 'p8'], 1: ['p8', 'p6'], 0: ['p6']}
    Y = {lv: y for lv, y, _ in layers}
    b = ''
    for v in names:  # đường dọc nối cùng một điểm qua các tầng
        top = min(y for lv, y, nodes in layers if v in nodes)
        b += line(X(v), top, X(v), ys[2], '#d5dae2', '3 6', width=2)
    for lv, y, nodes in layers:
        b += text(left, y + 9, f'tầng {lv}' if not compact else f'{lv}', fs, INK, 'start', weight='bold')
        hop = set(zip(path[lv], path[lv][1:]))
        for a, c in zip(nodes, nodes[1:]):
            on = (a, c) in hop or (c, a) in hop
            b += line(X(a) + r, y, X(c) - r, y, ORANGE if on else '#9aa6b8', width=6 if on else 3)
        for v in nodes:
            on = v in path[lv]
            b += f'<circle cx="{X(v)}" cy="{y}" r="{r}" fill="#ffffff" stroke="{ORANGE if on else BLUE}" stroke-width="4"/>'
    for v in names:
        if not compact or v in ('s', 'p4', 'p6', 'p8'):
            b += text(X(v), ys[2] + 50, v, fs - 4 if not compact else fs, INK)
    for v, a, c in [('p8', 2, 1), ('p6', 1, 0)]:
        x = X(v) - 28
        b += line(x, Y[a] + 12, x, Y[c] - 34, ORANGE, width=5)
        b += f'<path d="M{x - 11},{Y[c] - 36} L{x + 11},{Y[c] - 36} L{x},{Y[c] - 16} Z" fill="{ORANGE}"/>'
    qx = x0 + dx * 6.4
    qy = ys[2] - 44
    b += line(qx, qy + 19, qx, ys[2] - 3, ORANGE, '4 4', width=2)
    b += f'<rect x="{qx - 10}" y="{qy - 10}" width="20" height="20" fill="{ORANGE}" transform="rotate(45 {qx} {qy})"/>'
    b += text(qx + 20, qy + 9, 'q', fs - 2, ORANGE, 'start', weight='bold', italic=True)
    if compact:
        svg(name, 780, 360, 'Truy vấn trên đồ thị ba tầng',
            'Ba tầng trên mười hai điểm. Tầng 2 đi s, p4, p8; tầng 1 đi từ p8 sang p6; tầng 0 bắt đầu từ p6, gần q.', b)
        return
    b += text(990, ys[0] + 9, 's → p4 → p8', 26, ORANGE, 'start') + text(990, ys[1] + 9, 'p8 → p6', 26, ORANGE, 'start')
    b += text(990, ys[2] + 9, 'tìm quanh p6', 26, ORANGE, 'start')
    svg(name, 1180, 430, 'Đồ thị nhiều tầng',
        'Tầng 0 chứa mười hai điểm s, p1 đến p11 với cạnh ngắn; tầng 1 chứa s, p2, p4, p6, p8, p10; tầng 2 chứa s, p4, p8. '
        'Truy vấn q ở giữa p6 và p7: ở tầng 2 tham lam đi s, p4, p8; xuống tầng 1 từ p8 sang p6; xuống tầng 0 tìm quanh p6.', b)


def chen_vi_du():
    # H10: chèn x ở tọa độ 2,6 với tầng l = 1, M = 2 vào đồ thị ba tầng của H07.
    names = ['s'] + [f'p{i}' for i in range(1, 12)]
    x0, dx, ys, r, fs = 105, 58, (115, 245, 375), 15, 30
    X = lambda v: x0 + dx * names.index(v)
    layers = [(2, ys[0], ['s', 'p4', 'p8']), (1, ys[1], ['s', 'p2', 'p4', 'p6', 'p8', 'p10']), (0, ys[2], names)]
    Y = {lv: y for lv, y, _ in layers}
    b = ''
    for v in names:
        top = min(y for lv, y, nodes in layers if v in nodes)
        b += line(X(v), top, X(v), ys[2], '#d5dae2', '3 6', width=2)
    for lv, y, nodes in layers:
        b += text(10, y + 9, f'{lv}', fs, INK, 'start', weight='bold')
        for a, c in zip(nodes, nodes[1:]):
            on = lv == 2 and (a, c) == ('s', 'p4')
            b += line(X(a) + r, y, X(c) - r, y, ORANGE if on else '#9aa6b8', width=6 if on else 3)
        for v in nodes:
            on = lv == 2 and v in ('s', 'p4')
            b += f'<circle cx="{X(v)}" cy="{y}" r="{r}" fill="#ffffff" stroke="{ORANGE if on else BLUE}" stroke-width="4"/>'
    xx = x0 + dx * 2.6
    for lv, nbrs in [(1, ['p2', 'p4']), (0, ['p3', 'p2'])]:
        y = Y[lv] - 48
        for v in nbrs:
            b += line(xx, y, X(v), Y[lv] - r, GREEN, '9 6', width=4)
        b += f'<circle cx="{xx}" cy="{y}" r="{r + 2}" fill="{PALE_GREEN}" stroke="{GREEN}" stroke-width="4"/>'
        b += text(xx, y + 10, 'x', fs - 4, GREEN, weight='bold')
    x = X('p4') + 24
    b += line(x, Y[2] + 14, x, Y[1] - 70, ORANGE, width=5)
    b += f'<path d="M{x - 10},{Y[1] - 72} L{x + 10},{Y[1] - 72} L{x},{Y[1] - 54} Z" fill="{ORANGE}"/>'
    for v in ('s', 'p2', 'p3', 'p4', 'p8'):
        b += text(X(v), ys[2] + 50, v, fs, INK)
    b += line(30, 30, 72, 30, ORANGE, width=6) + text(84, 40, 'pha 1: tìm điểm vào', 26, INK, 'start')
    b += line(430, 30, 472, 30, GREEN, '9 6', width=4) + text(484, 40, 'pha 2: cạnh mới', 26, INK, 'start')
    svg('chen-vi-du.svg', 780, 440, 'Chèn x vào đồ thị ba tầng',
        'Điểm mới x ở tọa độ 2,6 có tầng 1, M bằng 2. Pha 1 ở tầng 2 đi từ s tới p4. '
        'Pha 2 nối x với p2 và p4 ở tầng 1, với p3 và p2 ở tầng 0.', b)


def lan_can_da_dang():
    # H11: x tại gốc; c1, c2, c3 cùng một phía, c4 phía đối diện; M = 2.
    pts = {'c1': (2, 0.3), 'c2': (2.6, 0.9), 'c3': (2.4, -0.6), 'c4': (-3, 0.5)}
    panels = [(0, 'Chọn 2 đỉnh gần nhất', ['c1', 'c3'], ORANGE, ''),
              (470, 'Quy tắc đa dạng', ['c1', 'c4'], GREEN, '')]
    b = ''
    for ox, title, chosen, color, dash in panels:
        X = lambda v: ox + 225 + 62 * (0 if v == 'x' else pts[v][0])
        Y = lambda v: 210 - 62 * (0 if v == 'x' else pts[v][1])
        b += rect(ox + 10, 20, 440, 330, '#ffffff', '#c5ccd8')
        b += text(ox + 230, 60, title, 28, color, weight='bold')
        for v in chosen:
            b += line(X('x'), Y('x'), X(v), Y(v), color, width=6)
        for v in pts:
            b += f'<circle cx="{X(v):.1f}" cy="{Y(v):.1f}" r="16" fill="#ffffff" stroke="{BLUE}" stroke-width="4"/>'
            dy = -26 if v != 'c3' else 46
            b += text(f'{X(v):.1f}', f'{Y(v) + dy:.1f}', v, 26, INK, weight='bold')
        b += f'<circle cx="{X("x"):.1f}" cy="{Y("x"):.1f}" r="18" fill="{PALE_GREEN}" stroke="{GREEN}" stroke-width="4"/>'
        b += text(f'{X("x"):.1f}', f'{Y("x") + 9:.1f}', 'x', 26, GREEN, weight='bold')
        b += text(ox + 230, 325, '{' + ', '.join(chosen) + '}', 28, INK)
    svg('lan-can-da-dang.svg', 920, 370, 'Chọn lân cận gần nhất và chọn đa dạng',
        'Điểm mới x có bốn ứng viên: c1, c2, c3 cùng một phía, c4 ở phía đối diện. '
        'Chọn hai đỉnh gần nhất cho c1 và c3 cùng phía; quy tắc đa dạng cho c1 và c4 ở hai phía.', b)


def luong_tu_hoa_vec_to():
    # Q00: ba tâm c0=(0,0), c1=(2,0), c2=(0,2); ranh giới ô: x=1 (c0|c1), y=1 (c0|c2), y=x (c1|c2).
    sc, ox, oy = 140, 110, 450
    X = lambda u: ox + sc * u
    Y = lambda v: oy - sc * v
    lo, hi = -0.6, 2.7
    b = ''
    # ô của c0: u<1, v<1; ô của c1: u>1, v<u; ô của c2: v>1, v>u
    b += f'<polygon points="{X(lo)},{Y(lo)} {X(1)},{Y(lo)} {X(1)},{Y(1)} {X(lo)},{Y(1)}" fill="{PALE_GRAY}"/>'
    b += f'<polygon points="{X(1)},{Y(lo)} {X(hi)},{Y(lo)} {X(hi)},{Y(hi)} {X(1)},{Y(1)}" fill="{PALE_BLUE}"/>'
    b += f'<polygon points="{X(lo)},{Y(1)} {X(1)},{Y(1)} {X(hi)},{Y(hi)} {X(lo)},{Y(hi)}" fill="{PALE_ORANGE}"/>'
    b += line(X(1), Y(lo), X(1), Y(1), INK, '8 6', width=2) + line(X(lo), Y(1), X(1), Y(1), INK, '8 6', width=2)
    b += line(X(1), Y(1), X(hi), Y(hi), INK, '8 6', width=2)
    for (u, v), name in [((0, 0), 'c0'), ((2, 0), 'c1'), ((0, 2), 'c2')]:
        b += f'<rect x="{X(u) - 11}" y="{Y(v) - 11}" width="22" height="22" fill="{BLUE}"/>'
        b += text(X(u) + 18, Y(v) + 40, name, 30, BLUE, 'start', weight='bold')
    b += text(X(-0.45), Y(0.75), 'ô của c0', 26, INK, 'start')
    b += text(X(1.75), Y(-0.45), 'ô của c1', 26, INK, 'middle')
    b += text(X(0.25), Y(2.45), 'ô của c2', 26, INK, 'start')
    xu, xv = 1.7, 0.4
    b += line(X(xu), Y(xv), X(2) - 8, Y(0) - 6, GREEN, width=4)
    b += f'<circle cx="{X(xu)}" cy="{Y(xv)}" r="11" fill="{GREEN}"/>'
    b += text(X(xu) - 14, Y(xv) - 18, 'x', 32, GREEN, 'end', weight='bold', italic=True)
    svg('luong-tu-hoa-vec-to.svg', 520, 560, 'Lượng tử hóa véc-tơ với ba tâm',
        'Ba tâm c0 tại (0, 0), c1 tại (2, 0), c2 tại (0, 2) chia mặt phẳng thành ba ô; ranh giới là các đường tọa độ thứ nhất bằng 1, tọa độ thứ hai bằng 1 và hai tọa độ bằng nhau. '
        'Điểm x tại (1,7; 0,4) nằm trong ô của c1 nên được thay bằng c1.', b)


def pq_tach_doan():
    # Q04: D = 8, m = 4 đoạn 2 chiều, mỗi đoạn một bộ mã con 256 tâm, mã 4 × 8 = 32 bit.
    fills = [PALE_BLUE, PALE_ORANGE, PALE_GREEN, PALE_GRAY]
    strokes = [BLUE, ORANGE, GREEN, INK]
    b = text(20, 52, 'x ∈ ℝ⁸', 30, INK, 'start', weight='bold')
    for j in range(4):
        x0 = 150 + j * 200
        for t in range(2):
            b += rect(x0 + t * 90, 20, 86, 56, fills[j], strokes[j])
            b += text(x0 + t * 90 + 43, 58, f'x{2 * j + t + 1}', 26, INK)
        b += text(x0 + 88, 112, f'đoạn {j + 1}', 26, strokes[j], weight='bold')
        b += line(x0 + 88, 124, x0 + 88, 160, strokes[j], arrow=True)
        b += box(x0 + 8, 168, 160, 74, [f'bộ mã {j + 1}', '256 tâm'], fills[j], strokes[j], size=24)
        b += line(x0 + 88, 248, x0 + 88, 284, strokes[j], arrow=True)
        b += box(x0 + 38, 290, 100, 56, [f'i{j + 1}'], '#ffffff', strokes[j], size=28)
        b += text(x0 + 88, 376, '8 bit', 24, INK)
    b += text(20, 326, 'mã PQ', 28, INK, 'start', weight='bold')
    b += text(550, 418, 'mã (i1, i2, i3, i4) dài 4 × 8 = 32 bit', 28, INK)
    svg('pq-tach-doan.svg', 980, 435, 'Lượng tử hóa tích với bốn đoạn',
        'Véc-tơ tám chiều chia thành bốn đoạn hai chiều. Mỗi đoạn được mã hóa bằng bộ mã con riêng 256 tâm thành một chỉ số 8 bit; '
        'mã PQ là bộ bốn chỉ số, dài 32 bit.', b)


def pq_vi_du(name='pq-vi-du.svg', with_query=False):
    # Q05/Q06: hai đoạn hai chiều; bộ mã đoạn 1 {(0,2),(2,0)}, đoạn 2 {(0,0),(3,0)};
    # x = (0,2; 1,8 | 2,7; 0,1); q = (0,1; 1,9 | 2,5; 0,2).
    panels = [(0, 'đoạn 1', [(0, 2), (2, 0)], (0.2, 1.8), (0.1, 1.9), 0),
              (470, 'đoạn 2', [(0, 0), (3, 0)], (2.7, 0.1), (2.5, 0.2), 1)]
    sc = 95
    b = ''
    for ox, title, cents, xp, qp, code in panels:
        X = lambda u: ox + 70 + sc * u
        Y = lambda v: 300 - sc * v
        b += rect(ox + 10, 15, 440, 345, '#ffffff', '#c5ccd8')
        b += text(ox + 230, 52, title, 28, INK, weight='bold')
        b += line(X(-0.3), Y(0), X(3.4), Y(0), '#c5ccd8', width=2) + line(X(0), Y(-0.3), X(0), Y(2.4), '#c5ccd8', width=2)
        for t, (u, v) in enumerate(cents):
            chosen = t == code
            b += f'<rect x="{X(u) - 12}" y="{Y(v) - 12}" width="24" height="24" fill="{BLUE if chosen else "#ffffff"}" stroke="{BLUE}" stroke-width="4"/>'
            ly = Y(v) - 26 if v > 1 else Y(v) + 46
            b += text(X(u), ly, f'tâm {t}', 28, BLUE, 'middle', weight='bold' if chosen else 'normal')
        cu, cv = cents[code]
        b += line(X(xp[0]), Y(xp[1]), X(cu), Y(cv), GREEN, '6 5', width=3)
        b += f'<circle cx="{X(xp[0])}" cy="{Y(xp[1])}" r="10" fill="{GREEN}"/>'
        if code == 0:
            b += text(X(xp[0]) + 18, Y(xp[1]) + 26, 'x', 32, GREEN, 'start', weight='bold', italic=True)
        else:
            b += text(X(xp[0]) + 2, Y(xp[1]) - 20, 'x', 32, GREEN, 'start', weight='bold', italic=True)
        if with_query:
            b += f'<rect x="{X(qp[0]) - 9}" y="{Y(qp[1]) - 9}" width="18" height="18" fill="{ORANGE}" transform="rotate(45 {X(qp[0])} {Y(qp[1])})"/>'
            if code == 0:
                b += text(X(qp[0]) + 18, Y(qp[1]) - 10, 'q', 32, ORANGE, 'start', weight='bold', italic=True)
            else:
                b += text(X(qp[0]) - 10, Y(qp[1]) - 24, 'q', 32, ORANGE, 'end', weight='bold', italic=True)
    desc = ('Đoạn 1 có tâm 0 tại (0; 2) và tâm 1 tại (2; 0); x ở (0,2; 1,8) gần tâm 0. '
            'Đoạn 2 có tâm 0 tại (0; 0) và tâm 1 tại (3; 0); x ở (2,7; 0,1) gần tâm 1. Mã của x là (0, 1).')
    if with_query:
        desc += ' Truy vấn q ở (0,1; 1,9) trong đoạn 1 và (2,5; 0,2) trong đoạn 2.'
    svg(name, 920, 375, 'Mã hóa PQ với hai đoạn', desc, b)


# Ví dụ tệp đảo I00–I04: bốn tâm thô, mười sáu điểm, truy vấn q = (6; 3,5).
IVF_MU = [(2, 2), (8, 2), (2, 8), (8, 8)]
IVF_PTS = [(1, 1.5), (2.5, 1), (4.5, 3.8), (1.5, 3.2), (7, 1), (9, 1.5), (8.5, 3), (6.5, 2.5),
           (1, 7), (3, 7.5), (2, 9), (3.5, 8.8), (7, 7), (9, 8.5), (8, 9.2), (6.5, 8)]
IVF_Q = (6, 3.5)


def tep_dao(name, mode):
    """mode: 'cells' (ô, danh sách, nprobe = 2) hoặc 'residual' (phần dư trong L1 và L0)."""
    sc, ox, oy = (50, 20, 520) if mode != 'residual' else (88, 20, 470)
    show = (lambda v: True) if mode != 'residual' else (lambda v: v <= 5)
    X = lambda u: ox + sc * u
    Y = lambda v: oy - sc * v
    b = ''
    opened = {1, 0} if mode != 'plain' else set()
    fills = {0: PALE_ORANGE, 1: PALE_BLUE, 2: '#ffffff', 3: '#ffffff'} if mode != 'plain' else {i: '#ffffff' for i in range(4)}
    cells = {0: (0, 0, 5, 5), 1: (5, 0, 10, 5), 2: (0, 5, 5, 10), 3: (5, 5, 10, 10)}
    for i, (u0, v0, u1, v1) in cells.items():
        if not show(v0 + 0.1):
            continue
        b += f'<rect x="{X(u0)}" y="{Y(v1)}" width="{sc * (u1 - u0)}" height="{sc * (v1 - v0)}" fill="{fills[i]}" stroke="{INK}" stroke-width="2" stroke-dasharray="{"" if (i in opened or mode == 'plain') else "8 6"}"/>'
        b += text(X(u1) - 10, Y(v1) + 34, f'L{i}' + (' (mở)' if i in opened else ''), 28, INK, 'end', weight='bold')
    for i, (u, v) in enumerate(IVF_MU):
        if not show(v):
            continue
        b += f'<rect x="{X(u) - 11}" y="{Y(v) - 11}" width="22" height="22" fill="{BLUE}"/>'
        if mode == 'residual' and i == 1:
            b += text(X(u) + 16, Y(v) + 34, f'μ{i}', 28, BLUE, 'start', weight='bold')
        else:
            b += text(X(u) - 16, Y(v) - 14, f'μ{i}', 28, BLUE, 'end', weight='bold')
    for k, (u, v) in enumerate(IVF_PTS):
        if not show(v):
            continue
        b += f'<circle cx="{X(u)}" cy="{Y(v)}" r="7" fill="{INK}"/>'
    if mode in ('cells', 'plain'):
        b += text(X(4.5) - 12, Y(3.8) + 8, 'y3', 26, INK, 'end', weight='bold')
        b += text(X(6.5) - 4, Y(2.5) + 34, 'y8', 26, INK, 'end', weight='bold')
    qu, qv = IVF_Q
    if mode == 'residual':
        for (mu, y, lab) in [(IVF_MU[1], IVF_PTS[7], 'r(y8)')]:
            x1, y1, x2, y2 = X(mu[0]), Y(mu[1]), X(y[0]), Y(y[1])
            L = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
            ux, uy = (x2 - x1) / L, (y2 - y1) / L
            bx, by = x2 - 9 * ux, y2 - 9 * uy
            b += line(x1, y1, bx - 12 * ux, by - 12 * uy, GREEN, width=5)
            b += (f'<path d="M{bx:.1f},{by:.1f} L{bx - 18 * ux - 8 * uy:.1f},{by - 18 * uy + 8 * ux:.1f} '
                  f'L{bx - 18 * ux + 8 * uy:.1f},{by - 18 * uy - 8 * ux:.1f} Z" fill="{GREEN}"/>')
            b += text(X(y[0]) - 6, Y(y[1]) + 40, 'y8', 30, GREEN, 'end', weight='bold')
            b += text((X(mu[0]) + X(y[0])) / 2 - 14, (Y(mu[1]) + Y(y[1])) / 2 + 46, 'r(y8)', 28, GREEN, 'middle', weight='bold')
        b += f'<line x1="{X(IVF_MU[1][0])}" y1="{Y(IVF_MU[1][1])}" x2="{X(qu)}" y2="{Y(qv)}" stroke="{ORANGE}" stroke-width="4" stroke-dasharray="9 6"/>'
        b += f'<line x1="{X(IVF_MU[0][0])}" y1="{Y(IVF_MU[0][1])}" x2="{X(qu)}" y2="{Y(qv)}" stroke="{ORANGE}" stroke-width="4" stroke-dasharray="9 6"/>'
    b += f'<rect x="{X(qu) - 11}" y="{Y(qv) - 11}" width="22" height="22" fill="{ORANGE}" transform="rotate(45 {X(qu)} {Y(qv)})"/>'
    b += text(X(qu) + 16, Y(qv) - 12, 'q', 34, ORANGE, 'start', weight='bold', italic=True)
    if mode in ('cells', 'plain'):
        w, title = 540, 'Tệp đảo với bốn danh sách'
        desc = ('Bốn tâm thô μ0 đến μ3 chia mặt phẳng thành bốn ô; mỗi ô ứng với một danh sách đảo L0 đến L3 gồm bốn điểm. '
                'Truy vấn q ở (6; 3,5) gần μ1 nhất rồi đến μ0' + ('; với nprobe bằng 2, chỉ L1 và L0 được mở.' if mode == 'cells' else '; điểm y3 thuộc ô của μ0, sát ranh giới với ô của μ1.'))
    else:
        w, title = 920, 'Véc-tơ dư trong tệp đảo'
        desc = ('Mũi tên xanh từ μ1 tới y8 là phần dư r(y8) được mã hóa bằng PQ. '
                'Hai đoạn nét đứt từ μ1 và μ0 tới q là truy vấn dư dùng khi quét L1 và L0.')
    svg(name, w, 540 if mode != 'residual' else 490, title, desc, b)


def main():
    truy_hoi_ngu_nghia()
    do_thu_hoi()
    do_thi_vi_du('do-thi-vi-du.svg', 'base')
    do_thi_vi_du('do-thi-tham-lam.svg', 'greedy')
    do_thi_vi_du('do-thi-chum.svg', 'beam')
    trang_thai_search_layer()
    do_thi_vi_du('do-thi-ef2.svg', 'seen2')
    canh_dai_mot_chieu()
    do_thi_nhieu_tang()
    do_thi_nhieu_tang('do-thi-nhieu-tang-gon.svg', compact=True)
    chen_vi_du()
    lan_can_da_dang()
    luong_tu_hoa_vec_to()
    pq_tach_doan()
    pq_vi_du()
    pq_vi_du('pq-vi-du-adc.svg', with_query=True)
    tep_dao('tep-dao.svg', 'cells')
    tep_dao('tep-dao-du.svg', 'residual')
    tep_dao('tep-dao-o.svg', 'plain')


if __name__ == '__main__':
    main()
