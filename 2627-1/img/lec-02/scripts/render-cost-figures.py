from pathlib import Path
from html import escape
p=Path(__file__).resolve().parents[1]
navy='#2f3e7a'; blue='#edf4ff'; darker='#dce8ff'; gray='#526070'
def txt(x,y,s,size=26,anchor='middle',fill=navy):return f'<text x="{x}" y="{y}" text-anchor="{anchor}" font-size="{size}" fill="{fill}">{escape(s)}</text>'
def rect(x,y,w,h,fill=blue):return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="4" fill="{fill}" stroke="{navy}" stroke-width="2"/>'
def line(x,y,xx,yy,extra=''):return f'<line x1="{x}" y1="{y}" x2="{xx}" y2="{yy}" stroke="{gray}" stroke-width="2" {extra}/>'
def svg(body,h,label):return f'<svg xmlns="http://www.w3.org/2000/svg" font-family="Arial, sans-serif" role="img" aria-label="{label}" viewBox="0 0 1120 {h}" width="1120">{body}</svg>'
def axis(origin,scale,values,y,unit):
 out=line(origin,y,origin+scale*max(values),y)
 for v in values:
  x=origin+scale*v;out+=line(x,y-5,x,y+5)+txt(x,y+32,str(v)+unit,24,fill=gray)
 return out
figs={}
x0=160; scale=150
b=axis(x0,scale,range(7),240,' s')
for m,y,ts in [(1,35,[('A',2),('B',2)]),(2,105,[('C',3),('D',3)]),(3,175,[('E',3)])]:
 b+=txt(135,y+31,f'Máy {m}',26,'end'); x=x0
 for name,t in ts:
  w=t*scale;b+=rect(x,y,w,44,darker if m==2 else blue)+txt(x+w/2,y+30,f'{name}: {t} s');x+=w
figs['03']=svg(b,290,'Ba máy chạy từ thời điểm 0. Máy 1: A và B, mỗi tác vụ 2 giây; máy 2: C và D, mỗi tác vụ 3 giây; máy 3: E dài 3 giây. Pha kết thúc ở giây 6.')
x0=160;scale=60
b=txt(135,54,'1 máy',26,'end')+rect(x0,24,900,40)+txt(610,52,'15τ')+line(25,86,1090,86)
b+=txt(45,111,'4 máy',24)
for m,y in [(1,118),(2,162),(3,206),(4,250)]:
 b+=txt(135,y+26,f'Máy {m}',24,'end')+rect(x0,y,180,34)+txt(250,y+25,'3τ',24)
 if m==1:b+=rect(340,y,180,34,darker)+txt(430,y+25,'3τ',24)
b+=txt(645,156,'Map: cộng 4 số, 3 phép cộng.',26,'start')
b+=txt(645,203,'Reduce: gộp 4 tổng, 3 phép cộng.',26,'start')
b+=txt(645,250,'Kết thúc sau 6τ.',26,'start')
b+=axis(x0,scale,[0,3,6,9,12,15],310,'τ')
figs['04']=svg(b,352,'Cùng trục thời gian: một máy cộng 16 số trong 15 tau. Map trên bốn máy cộng cục bộ từ 0 đến 3 tau, sau đó Reduce trên máy 1 gộp từ 3 đến 6 tau. Các thanh và mốc dùng 60 pixel cho một tau.')
b='<defs><marker id="cost-input-arrow" markerWidth="8" markerHeight="8" refX="7" refY="4" orient="auto"><path d="M0,0 L8,4 L0,8 Z" fill="#2f3e7a"/></marker></defs>'
for x,w,labels in [(10,220,['Đầu vào Map','I = 100 MB']),(275,100,['Map']),(420,220,['Đầu vào Reduce','H = 40 MB']),(685,135,['Reduce']),(865,245,['Kết quả cuối','Không tính vào C'])]:
 b+=rect(x,45,w,95)
 for i,s in enumerate(labels):b+=txt(x+w/2,85+i*32,s,24 if w>135 else 26)
for x,xx in [(232,267),(377,412),(642,677),(822,857)]:b+=line(x,94,xx,94,'marker-end="url(#cost-input-arrow)"')
figs['05']=svg(b,175,'Đầu vào Map I bằng 100 MB đi vào các tác vụ Map; 40 MB trung gian H đi vào Reduce; đầu ra cuối không được cộng vào chi phí C theo quy ước sách.')
b='<defs><marker id="cost-rack-arrow" markerWidth="8" markerHeight="8" refX="7" refY="4" orient="auto"><path d="M0,0 L8,4 L0,8 Z" fill="#2f3e7a"/></marker></defs>'
b+=rect(20,40,300,245,'#f8fafc')+txt(170,28,'Tủ rack gửi',28)
for m,y in enumerate([60,115,170,225],1):b+=rect(40,y,260,42)+txt(170,y+29,f'Máy {m}: 100 MB',26)
b+=rect(860,40,240,245,'#f8fafc')+txt(980,28,'Tủ rack nhận',28)
b+=rect(880,120,200,75,darker)+txt(980,166,'Máy nhận',28)
b+=line(320,158,870,158,'marker-end="url(#cost-rack-arrow)"')
b+=txt(580,106,'Một đường nối dùng chung',26)+txt(580,140,'B = 100 MB/s',26)+txt(580,202,'V = 4 × 100 = 400 MB',26)
figs['07']=svg(b,305,'Bốn máy trong rack gửi, mỗi máy 100 MB; tất cả 400 MB qua một đường nối 100 MB mỗi giây tới máy nhận trong rack khác.')
b=axis(80,100,[0,1,5,8,10],178,' s')
for x,w,ylabel,t,label,fill in [(80,100,0,1,'',blue),(180,400,0,4,'Map: 4 s',darker),(580,300,0,3,'Truyền và nhóm: 3 s',blue),(880,200,0,2,'Reduce: 2 s',darker)]:
 b+=rect(x,100,w,55,fill)
 if label:b+=txt(x+w/2,135,label,24)
b+=txt(130,60,'Điều phối: 1 s',26)+line(130,69,130,95)
figs['09']=svg(b,220,'Bốn pha nối tiếp: điều phối từ 0 đến 1 giây, Map từ 1 đến 5 giây, truyền và nhóm từ 5 đến 8 giây, Reduce từ 8 đến 10 giây.')
b=axis(140,38,[0,10,24],175,' s')
for y,t,label in [(25,24,'1 máy'),(100,10,'4 máy')]:b+=txt(120,y+34,label,26,'end')+rect(140,y,t*38,48)+txt(140+t*19,y+33,f'{t} giây',28)
figs['10']=svg(b,220,'Cùng công việc: một máy 24 giây, bốn máy 10 giây. Hai thanh dùng chung thang thời gian, tỷ lệ 2,4.')
for n,s in figs.items():(p/('cost-'+n+'.svg')).write_text(s)
print('Deterministic SVG replacements:',list(figs))
