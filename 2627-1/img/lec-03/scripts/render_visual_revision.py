#!/usr/bin/env python3
"""Vẽ các quan hệ của Lecture 03; chạy độc lập để tái sinh visual-*.svg."""
from pathlib import Path
from html import escape
OUT=Path(__file__).resolve().parent.parent
NAVY='#2f3e7a'; ORANGE='#bd6834'
def text(x,y,s,size=26,color=NAVY,anchor='middle'):
    return f'<text x="{x}" y="{y}" text-anchor="{anchor}" font-size="{size}" fill="{color}">{escape(s)}</text>'
def rect(x,y,w,h,fill='#f7f9ff'):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="8" fill="{fill}" stroke="#c8d0e8" stroke-width="2"/>'
def line(x,y,x2,y2,dashed=False):
    attrs='stroke-dasharray="6 5"' if dashed else 'marker-end="url(#arrow)"'
    return f'<line x1="{x}" y1="{y}" x2="{x2}" y2="{y2}" stroke="{NAVY}" stroke-width="2" {attrs}/>'
def doc(name,w,h,title,desc,body):
    svg=f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" role="img" aria-labelledby="title desc" font-family="Arial, sans-serif">
<title id="title">{escape(title)}</title><desc id="desc">{escape(desc)}</desc>
<defs><marker id="arrow" markerWidth="8" markerHeight="8" refX="7" refY="4" orient="auto"><path d="M0,0 L8,4 L0,8 Z" fill="{NAVY}"/></marker></defs>
{''.join(body)}</svg>\n'''
    (OUT/name).write_text(svg)
b=[text(78,35,'Nguồn'),text(230,35,'Đích'),text(428,35,'Cột A'),rect(365,50,125,260)]
b += [f'<circle cx="78" cy="180" r="29" fill="#fff3e0" stroke="{ORANGE}" stroke-width="2"/>',text(78,189,'A',30,ORANGE)]
for label,y in [('B',110),('C',185),('D',260)]:
    b += [line(108,180,196,y),f'<circle cx="230" cy="{y}" r="29" fill="#edf4ff" stroke="{NAVY}" stroke-width="2"/>',text(230,y+9,label,30)]
# Cạnh A→B/C/D nối đúng hàng B/C/D; hàng A không có cạnh tương ứng.
for label,value,y in [('A','0',78),('B','1/3',145),('C','1/3',212),('D','1/3',279)]:
    b += [text(388,y+9,label),text(454,y+9,value)]
for sy,ty in [(110,145),(185,212),(260,279)]: b += [line(261,sy,363,ty,True)]
b += [text(80,243,'3 đích',24),text(260,337,'A không trỏ tới chính A: hàng A bằng 0.',24)]
doc('visual-column-a.svg',520,355,'Ba cạnh ra tạo cột A','A trỏ tới B, C, D. Đường nét đứt ánh xạ đúng tới các hàng B, C, D có giá trị một phần ba; hàng A bằng không.',b)
b=[text(180,30,'Hai phân phối ban đầu',28),text(870,30,'Sau cùng một phép cập nhật',28)]
for y,left,right in [(50,'x','F(x)'),(140,'y','F(y)')]:
    b += [rect(100,y,160,62),text(180,y+42,left,32),line(275,y+31,775,y+31),text(520,y+20,'F',30),rect(790,y,160,62),text(870,y+42,right,32)]
b += [text(525,238,'So sánh khoảng cách giữa hai phân phối, không so sánh riêng từng điểm.',27)]
doc('visual-contraction.svg',1100,260,'Hai phân phối qua cùng phép cập nhật','Hai hàng riêng: x qua F thành F(x), y qua cùng F thành F(y). Công thức trên slide so sánh khoảng cách giữa hai phân phối trước và sau.',b)
b=[rect(15,20,510,220),rect(750,20,330,220),text(270,53,'Máy 1',28),text(915,53,'Máy 2',28)]
b += [rect(45,90,180,70,'#edf4ff'),text(135,133,'Combine',28),rect(305,140,185,60),text(397,179,'Reduce',28),rect(780,90,265,70),text(912,133,'Reduce',28)]
b += [line(226,122,774,122),rect(555,71,152,38,'#fff3e0'),text(631,99,'Qua mạng',25,ORANGE)]
b += [line(226,145,300,171),text(269,210,'Cục bộ',24),text(637,190,'Góp vào Q',26,ORANGE)]
doc('visual-network.svg',1100,260,'Byte qua mạng phụ thuộc vị trí Reduce','Bản ghi của Combine trên máy 1 có thể tới Reduce cùng máy theo nhánh cục bộ, hoặc qua mạng tới Reduce máy 2. Chỉ nhánh qua mạng góp vào Q.',b)
