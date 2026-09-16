#!/usr/bin/env python3
"""Vẽ lại Hình5.12, cách gộp và một vòng theo MMDS5.2; ghi SVG cạnh script."""
from pathlib import Path
from html import escape
N='#2f3e7a'; O='#cc6b32'; L='#edf4ff'; G='#555'
def text(x,y,t,size=30,color=N):
 return f'<text x="{x}" y="{y}" text-anchor="middle" font-size="{size}" fill="{color}">{escape(t)}</text>'
def box(x,y,w,h,label,color=N,fill=L,size=30):
 return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="9" fill="{fill}" stroke="{color}" stroke-width="2"/>'+text(x+w/2,y+h/2+10,label,size,color)
def path(d,color=N):
 return f'<path d="{d}" fill="none" stroke="{color}" stroke-width="3" marker-end="url(#arr)"/>'
def svg(w,h,title,desc,body):
 return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" role="img" aria-labelledby="t d" font-family="Arial,sans-serif"><title id="t">{escape(title)}</title><desc id="d">{escape(desc)}</desc><defs><marker id="arr" viewBox="0 0 10 10" refX="10" refY="5" markerWidth="6" markerHeight="6" orient="auto"><path d="M0,0 L10,5 L0,10 Z" fill="{N}"/></marker></defs>{body}</svg>'
def grid():
 p=[]
 # Dải đầu vào: nhãn nguồn đặt ngay trong hộp r
 for b,lab in enumerate(['A, B','C, D']):
  x=260+b*240
  p.append(box(x,20,180,70,f'r{b+1}: {lab}',size=28))
 # Khung nét đứt nhóm theo cột nguồn (chỉ nhóm, không là cạnh dữ liệu)
 for b,lab in enumerate(['A, B','C, D']):
  x=240+b*240
  p.append(f'<rect x="{x}" y="150" width="220" height="310" rx="12" fill="none" stroke="{G}" stroke-width="2" stroke-dasharray="9,7"/>')
 # Mũi tên thẳng r_b vào khung cột tương ứng
 for b in range(2):
  x=350+b*240
  p.append(path(f'M{x},90 L{x},150'))
 # Khối ma trận và dải kết quả theo hàng
 for a,lab in enumerate(['A, B','C, D']):
  y=170+a*160; cy=y+50
  p += [text(105,cy+9,f'Đích {lab}',28),box(850,y,170,100,f'z{a+1}',O,'#fff3e0',34)]
  for b in range(2):p.append(box(260+b*240,y,180,100,f'M{a+1}{b+1}',size=34))
  # Mũi tên gộp đúng hàng về z_a, xuất phát từ mép phải khung cột thứ hai
  p += [path(f'M350,{y+100} L350,{y+125} L790,{y+125} L790,{cy} L850,{cy}'),path(f'M680,{cy} L850,{cy}')]
 return svg(1080,490,'Một dải đầu vào cho mỗi cột khối; một dải kết quả cho mỗi hàng','r1 cấp cho khung cột chứa M11 và M21; r2 cấp cho khung cột chứa M12 và M22. Khung nét đứt chỉ nhóm theo cột nguồn, không là cạnh dữ liệu. M11 và M12 cùng đóng góp z1; M21 và M22 cùng đóng góp z2. Hàng là đích, cột là nguồn.',''.join(p))
def merge():
 p=[box(35,30,280,100,'M11: B → A'),box(35,240,280,100,'M12: C → A'),path('M315,80 L650,170'),path('M315,290 L650,200'),text(455,95,'(A, 1/8)',34),text(455,308,'(A, 1/4)',34),box(650,125,170,115,'A',O,'#fff3e0',40),text(730,280,'Tổng 3/8',28,O)]
 return svg(850,375,'Hai khối góp về cùng khóa A','M11 tạo cặp A,một phần tám; M12 tạo cặp A,một phần tư. Tổng tại A bằng ba phần tám trước khi nhân beta và cộng phần chung.',''.join(p))
def pipeline():
 labels=['Điểm cũ rᵗ','Map và tổng δ','Combine','Chuyển, nhóm khóa','Reduce','Đo Δ; xét vòng tiếp']
 coords=[(20,30),(370,30),(720,30),(720,220),(370,220),(20,220)]
 p=[box(x,y,300,95,lab,size=29) for (x,y),lab in zip(coords,labels)]
 p += [path('M320,77 L370,77'),path('M670,77 L720,77'),path('M870,125 L870,220'),path('M720,267 L670,267'),path('M370,267 L320,267')]
 return svg(1040,345,'Các giai đoạn trong một vòng','Cùng điểm cũ: tính Map và tổng delta; Combine trước khi chuyển và nhóm theo khóa; Reduce; tính độ thay đổi, dừng hoặc dùng điểm mới ở vòng sau.',''.join(p))
def main():
 out=Path(__file__).resolve().parent.parent
 for name,content in {'rlarge-blocks-grid.svg':grid(),'rlarge-merge-a.svg':merge(),'rlarge-round-pipeline.svg':pipeline()}.items():(out/name).write_text(content)
if __name__=='__main__':main()
