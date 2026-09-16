from pathlib import Path
from html import escape
OUT=Path(__file__).resolve().parents[1]
C='#2f3e7a'
def text(x,y,s,size=25):return f'<text x="{x}" y="{y}" text-anchor="middle" font-family="Arial,sans-serif" font-size="{size}" fill="{C}">{escape(s)}</text>'
def box(x,y,w,h,lines,fill='#edf4ff',size=25):
 return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="8" fill="{fill}" stroke="{C}" stroke-width="2"/>'+''.join(text(x+w/2,y+h/2+(i-(len(lines)-1)/2)*31+8,t,size) for i,t in enumerate(lines))
def arrow(x,y,u,v):return f'<path d="M{x} {y}L{u} {v}" fill="none" stroke="{C}" stroke-width="2.5" marker-end="url(#a)"/>'
def save(name,body,h,alt):
 (OUT/(name+'.svg')).write_text(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1120 {h}" role="img" aria-label="{escape(alt,quote=True)}"><defs><marker id="a" markerWidth="8" markerHeight="8" refX="7" refY="4" orient="auto"><path d="M0 0L8 4L0 8Z" fill="{C}"/></marker></defs>{body}</svg>')
b=text(275,30,'HDFS: lưu dữ liệu',28)+text(845,30,'YARN: chạy tác vụ',28)
b+=box(145,55,260,80,['NameNode','Vị trí khối'])+box(715,55,260,80,['ResourceManager','Cấp tài nguyên'])
for x,t in [(20,'DataNode 1'),(300,'DataNode 2')]:b+=box(x,205,240,88,[t,'Khối và bản sao'],'#e8f5e9')+arrow(275,140,x+120,198)
for x,t in [(580,'NodeManager 1'),(860,'NodeManager 2')]:b+=box(x,205,240,88,[t,'Chạy Map / Reduce'])+arrow(845,140,x+120,198)
b+=text(560,350,'Một mạng Docker · Sáu container · Chung CPU, RAM của một máy',25)
save('lab-cluster',b,380,'HDFS gồm NameNode quản lý vị trí và hai DataNode lưu khối với bản sao. YARN gồm ResourceManager cấp tài nguyên và hai NodeManager chạy tác vụ. Sáu container nối cùng mạng Docker trên một máy vật lý.')
b=box(10,55,315,155,['Map bằng Python','stdin: dòng văn bản','stdout: từ TAB số đếm'])+arrow(332,130,395,130)
b+=box(405,55,310,155,['Hadoop','Phân phối, sắp xếp','Cùng khóa liền nhau'])+arrow(722,130,785,130)
b+=box(795,55,315,155,['Reduce bằng Python','stdin: dòng cùng khóa','stdout: từ TAB tổng'],'#e8f5e9',24)
b+=text(560,268,'Ví dụ một khóa: mèo TAB 1, mèo TAB 1 → mèo TAB 2',26)+text(560,318,'Tạm chưa dùng Combine; các dòng được đọc lần lượt.',24)
save('lab-streaming',b,350,'Hadoop cấp dòng văn bản cho Map Python, nhận cặp từ và số đếm qua tab; phân phối và sắp xếp để Reduce đọc dòng cùng khóa liền nhau rồi cộng. Minh họa khóa mèo khi chưa dùng Combine.')
b=box(15,60,300,170,['Map tạo','5 cặp','Map output records'])+arrow(322,145,397,145)+box(405,60,310,170,['Sau Combine','4 cặp','Combine output records'])+arrow(722,145,797,145)+box(805,60,300,170,['Reduce trả','3 cặp','Reduce output records'],'#e8f5e9',24)
b+=text(560,295,'Số bản ghi từ lần chạy mẫu; không phải số byte hay thời gian.',25)
save('lab-counters',b,330,'Bộ đếm lần chạy mẫu: năm cặp đầu ra Map, bốn cặp đầu ra Combine, ba cặp đầu ra Reduce. Đây là số bản ghi, không phải thời gian hay số byte.')
