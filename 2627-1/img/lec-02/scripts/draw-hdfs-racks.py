from pathlib import Path
parts=['''<svg xmlns="http://www.w3.org/2000/svg" width="1160" height="330" viewBox="0 0 1160 330" role="img" aria-labelledby="title desc"><title id="title">Các rack, kết nối mạng và bản sao khối trong HDFS</title><desc id="desc">Tệp chia thành A và B. Rack 1 gồm máy 1 lưu A B, máy 2 lưu B; rack 2 gồm máy 3 lưu A B, máy 4 lưu A. Mỗi rack có bộ chuyển mạch nối tới mạng liên rack. Mỗi khối có ba bản sao trên hai rack.</desc><style>text{font-family:Arial,sans-serif;fill:#2f3e7a;font-size:22px} .small{font-size:20px} .line{stroke:#526070;stroke-width:3;fill:none}</style>''']
def rect(x,y,w,h,fill='#edf4ff',stroke='#2f3e7a'):
 parts.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="7" fill="{fill}" stroke="{stroke}" stroke-width="2"/>')
def text(x,y,t,cls=''):
 parts.append(f'<text x="{x}" y="{y}" text-anchor="middle" class="{cls}">{t}</text>')
def line(d):parts.append(f'<path d="{d}" class="line"/>')
text(153,26,'Tệp → khối A, B')
rect(408,4,344,40);text(580,31,'Bộ chuyển mạch liên rack')
line('M408 24 H292 V106 M752 24 H868 V106')
for x,r in [(22,1),(602,2)]:
 rect(x,62,536,226,'#f8fafc','#a5afc0');text(x+90,92,f'Tủ rack {r}');line(f'M{x+270} 62 V106')
 rect(x+152,106,232,38);text(x+268,133,'Bộ chuyển mạch')
 line(f'M{x+268} 144 V164 H{x+135} V188 M{x+268} 164 H{x+403} V188')
 for offset,m,blocks in [(30,1 if r==1 else 3,'AB'),(298,2 if r==1 else 4,'B' if r==1 else 'A')]:
  bx=x+offset;rect(bx,188,208,77,'white');text(bx+50,216,f'Máy {m}','small')
  for i,c in enumerate(blocks):
   rect(bx+96+i*49,200,40,46,'#edf4ff' if c=='A' else '#fff3e0','#2f3e7a' if c=='A' else '#b66b22');text(bx+116+i*49,231,c)
text(580,319,'Cùng nhãn = cùng dữ liệu · Mỗi khối có 3 bản sao trên 2 rack','small')
parts.append('</svg>')
Path('2627-1/img/lec-02/hdfs-racks.svg').write_text('\n'.join(parts))
