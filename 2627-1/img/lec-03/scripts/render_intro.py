#!/usr/bin/env python3
"""Tạo hai SVG cho Phần 1 Lecture 03: intro-ranking.svg và intro-scale.svg.

SVG chỉ mang vai trò sơ đồ và nhãn; công thức toán nằm trên slide bằng HTML + KaTeX.
Chạy: python3 render_intro.py  (ghi ngay thư mục của script).
"""
from pathlib import Path

OUT = Path(__file__).resolve().parent.parent
NAVY = "#2f3e7a"
GREY = "#666666"
LIGHT = "#edf4ff"
EDGE = "#b0bec5"

RANKING = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1140 330" font-family="Helvetica, Arial, sans-serif" role="img" aria-labelledby="rk-title rk-desc">
  <title id="rk-title">Sơ đồ xếp hạng trang kết quả</title>
  <desc id="rk-desc">Truy vấn dẫn tới các trang liên quan, các trang được sắp thứ tự để hiển thị; liên kết giữa các trang là một tín hiệu góp phần xác định độ quan trọng.</desc>

  <!-- Khối 1: truy vấn -->
  <rect x="20" y="120" width="230" height="90" rx="10" fill="{LIGHT}" stroke="{NAVY}" stroke-width="2"/>
  <text x="135" y="158" text-anchor="middle" font-size="24" fill="{NAVY}" font-weight="bold">Truy vấn</text>
  <text x="135" y="190" text-anchor="middle" font-size="22" fill="{GREY}">Từ khóa người dùng</text>

  <!-- Khối 2: các trang liên quan -->
  <rect x="340" y="120" width="280" height="90" rx="10" fill="{LIGHT}" stroke="{NAVY}" stroke-width="2"/>
  <text x="480" y="158" text-anchor="middle" font-size="24" fill="{NAVY}" font-weight="bold">Các trang liên quan</text>
  <text x="480" y="190" text-anchor="middle" font-size="22" fill="{GREY}">Khớp với truy vấn</text>

  <!-- Khối 3: thứ tự hiển thị -->
  <rect x="710" y="120" width="280" height="90" rx="10" fill="#fff" stroke="{NAVY}" stroke-width="2"/>
  <text x="850" y="158" text-anchor="middle" font-size="24" fill="{NAVY}" font-weight="bold">Sắp thứ tự</text>
  <text x="850" y="190" text-anchor="middle" font-size="22" fill="{GREY}">kết hợp nhiều tín hiệu</text>

  <!-- Mũi tên khối 1 -> 2 -->
  <line x1="250" y1="165" x2="326" y2="165" stroke="{NAVY}" stroke-width="3"/>
  <polygon points="340,165 326,158 326,172" fill="{NAVY}"/>

  <!-- Mũi tên khối 2 -> 3 -->
  <line x1="620" y1="165" x2="696" y2="165" stroke="{NAVY}" stroke-width="3"/>
  <polygon points="710,165 696,158 696,172" fill="{NAVY}"/>

  <!-- Tín hiệu liên kết đi vào bước sắp thứ tự -->
  <rect x="710" y="255" width="280" height="55" rx="10" fill="#fff3e0" stroke="#ef6c00" stroke-width="2"/>
  <text x="850" y="290" text-anchor="middle" font-size="22" fill="#ef6c00">Điểm từ liên kết</text>
  <line x1="850" y1="255" x2="850" y2="222" stroke="#ef6c00" stroke-width="3"/>
  <polygon points="843,224 850,210 857,224" fill="#ef6c00"/>
</svg>
"""

CELL = 40
GRID_X, GRID_Y = 90, 40
N = 7  # lưới minh họa 7x7, phần lớn ô trống
FILLED = {(0, 2), (0, 5), (1, 0), (1, 4), (2, 3), (3, 1), (3, 6),
          (4, 2), (5, 0), (5, 5), (6, 3), (6, 6)}

cells = []
for r in range(N):
    for c in range(N):
        x = GRID_X + c * CELL
        y = GRID_Y + r * CELL
        if (r, c) in FILLED:
            cells.append(f'<rect x="{x}" y="{y}" width="{CELL}" height="{CELL}" fill="{NAVY}"/>')
        else:
            cells.append(f'<rect x="{x}" y="{y}" width="{CELL}" height="{CELL}" fill="#ffffff" stroke="{EDGE}" stroke-width="1"/>')

SCALE = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 460 400" font-family="Arial,sans-serif" role="img" aria-labelledby="sc-title sc-desc">
<title id="sc-title">Lưới minh họa liên kết thưa</title><desc id="sc-desc">Lưới bảy hàng bảy cột; ô có chấm là một liên kết, ô trống là không có liên kết. Đây chỉ là hình minh họa.</desc>
<text x="230" y="25" text-anchor="middle" font-size="24" fill="{NAVY}">Lưới minh họa</text>
{''.join(cells)}
{''.join(f'<circle cx="{GRID_X+c*CELL+20}" cy="{GRID_Y+r*CELL+20}" r="4" fill="white"/>' for r,c in FILLED)}
<text x="230" y="352" text-anchor="middle" font-size="22" fill="{NAVY}">Ô có chấm: có liên kết</text>
<text x="230" y="382" text-anchor="middle" font-size="22" fill="{GREY}">Ô trống: không có liên kết</text>
</svg>"""


def main() -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    for name, svg in (("intro-ranking.svg", RANKING), ("intro-scale.svg", SCALE)):
        path = OUT / name
        path.write_text(svg, encoding="utf-8")
        print(f"Đã ghi {path}")


if __name__ == "__main__":
    main()
