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


def main():
    truy_hoi_ngu_nghia()
    do_thu_hoi()


if __name__ == '__main__':
    main()
