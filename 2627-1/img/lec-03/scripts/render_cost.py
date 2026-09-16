from pathlib import Path
from html import escape
N='#2f3e7a'; O='#cc6b32'; G='#555'; L='#edf4ff'
def txt(x,y,t,size=30,color=N):return f'<text x="{x}" y="{y}" text-anchor="middle" font-size="{size}" fill="{color}">{escape(t)}</text>'
def box(x,y,w,h,t,fill=L):return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="8" fill="{fill}" stroke="{N}" stroke-width="2"/>'+txt(x+w/2,y+h/2+9,t)
def arr(d):return f'<path d="{d}" fill="none" stroke="{N}" stroke-width="3" marker-end="url(#a)"/>'
def svg(w,h,title,desc,p):return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" role="img" aria-labelledby="t d" font-family="Arial,sans-serif"><title id="t">{escape(title)}</title><desc id="d">{escape(desc)}</desc><defs><marker id="a" viewBox="0 0 10 10" refX="10" refY="5" markerWidth="6" markerHeight="6" orient="auto"><path d="M0,0L10,5L0,10Z" fill="{N}"/></marker></defs>{''.join(p)}</svg>'
def memory():
 p=[box(15,115,195,80,'Khối trên đĩa'),arr('M210,155L265,155'),box(265,115,230,80,'Bộ đệm đọc khối'),box(570,35,235,80,'Dải điểm vào r_b'),box(570,255,235,80,'Dải tích lũy z_a'),box(570,145,235,60,'Tính đóng góp'),arr('M495,155L570,175'),arr('M685,115L685,145'),arr('M685,205L685,255'),txt(382,230,'B_buf'),txt(685,365,'Mỗi dải: n/k giá trị'),txt(100,230,'Đọc tuần tự',25,G)]
 return svg(830,390,'Bộ nhớ của một tác vụ khối','Khối ma trận đọc qua bộ đệm. Phép tính dùng dải điểm r_b và tích lũy vào z_a. Hai dải mỗi dải n/k số thực.',p)
def combine():
 p=[txt(410,35,'Trong cùng tác vụ M21',31),box(20,80,255,70,'A → D: (D, 1/12)'),box(20,210,255,70,'B → D: (D, 1/8)'),arr('M275,115L510,175'),arr('M275,245L510,200'),box(510,140,290,100,'(D, 5/24)','#e8f4ea'),txt(650,280,'Combine: cộng theo khóa',24,G)]
 return svg(830,330,'Combine gộp hai đóng góp tại D trong M21','A góp một phần mười hai, B góp một phần tám. Combine cùng tác vụ M21 tạo một cặp D,năm phần hai mươi tư.',p)
def timeline():
 p=[];start=200;unit=85
 p += [txt(92,40,'1 máy',28),txt(92,68,'tuần tự',24,G)]
 pos=start
 for lab,count in [('M11',2),('M12',2),('M21',3),('M22',1)]:
  p.append(box(pos,15,count*unit,60,lab));pos+=count*unit
 for row,(lab,count) in enumerate([('M11',2),('M12',2),('M21',3),('M22',1)]):
  y=125+row*65;p.extend([txt(90,y+22,f'Máy {row+1}',26),txt(90,y+46,lab,24,G),box(start,y,count*unit,48,f'{count}cₑ')])
 p.append(f'<path d="M{start},100V410H930" stroke="{G}" fill="none" stroke-width="2"/>')
 for i in range(9):p.extend([f'<path d="M{start+i*unit},410v7" stroke="{G}"/>',txt(start+i*unit,445,str(i),24,G)])
 p.append(txt(910,485,'t / cₑ',25,G));p.append(txt(580,365,'4 tác vụ bắt đầu cùng lúc; xong tại 3cₑ',27,O))
 return svg(1000,500,'Một máy và bốn máy theo mô hình chỉ tính đóng góp','Một máy làm bốn khối nối tiếp 2,2,3,1 đơn vị. Bốn máy mỗi máy một khối cùng bắt đầu, kết thúc sau 3 đơn vị c_e.',p)
if __name__=='__main__':
 out=Path(__file__).resolve().parent.parent
 for name,fn in [('cost-memory.svg',memory),('cost-combine.svg',combine),('cost-timeline.svg',timeline)]: (out/name).write_text(fn())
