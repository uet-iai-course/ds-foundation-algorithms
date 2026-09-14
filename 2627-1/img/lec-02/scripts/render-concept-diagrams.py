from pathlib import Path
import html,json
p=Path(__file__).resolve().parents[1]
def svg(name,title,desc,body):
 text='<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1080 300" role="img" aria-labelledby="title desc"><title id="title">'+html.escape(title)+'</title><desc id="desc">'+html.escape(desc)+'</desc><defs><marker id="arrow" markerWidth="8" markerHeight="8" refX="7" refY="4" orient="auto"><path d="M0 0L8 4L0 8Z" fill="#2f3e7a"/></marker></defs><g font-family="sans-serif" font-size="26" fill="#263238">'+body+'</g></svg>'
 (p/name).write_text(text)
def txt(x,y,s,size=26,anchor='middle'):return f'<text x="{x}" y="{y}" font-size="{size}" text-anchor="{anchor}">{html.escape(s)}</text>'
def rect(x,y,w,h,fill='#edf4ff',stroke='#2f3e7a'):return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="10" fill="{fill}" stroke="{stroke}" stroke-width="2"/>'
def path(d,color='#2f3e7a',arrow=False,dash=False):return f'<path d="{d}" fill="none" stroke="{color}" stroke-width="3"'+(' marker-end="url(#arrow)"' if arrow else '')+(' stroke-dasharray="8 5"' if dash else '')+'/>'
b=path('M540 66 V90 H265 V117')+path('M540 90 H815 V117')+rect(325,8,430,58)+txt(540,45,'Bộ chuyển mạch liên tủ')
for x,label in [(40,'Tủ A'),(590,'Tủ B')]:
 b+=rect(x,117,450,175)+txt(x+225,151,label)+txt(x+225,184,'Mạng nội tủ',24)+path(f'M{x+45} 198 H{x+405}')
 for dx in [35,175,315]:b+=path(f'M{x+dx+50} 198 V220')+rect(x+dx,220,100,52,'#fff0df')+txt(x+dx+50,254,'Máy',24)
svg('ch2-mang-tu-may.svg','Mạng trong tủ và giữa các tủ','Sơ đồ khái niệm dựa Hình 2.1: hai tủ nối qua bộ chuyển mạch; mỗi tủ có mạng nối nhiều máy. Số máy chỉ minh họa.',b)
b=path('M166 157 H397',arrow=True)+path('M506 145 L837 77',arrow=True)+path('M506 171 L837 241',arrow=True)+path('M123 124 C165 63 645 63 837 53',arrow=True,dash=True)
b+=txt(450,28,'Cạnh trực tiếp: một cạnh',24)+txt(282,145,'L₁',28)+txt(670,107,'L₂',28)+txt(670,238,'L₂',28)
for x,y,label,color in [(100,157,'url1','#edf4ff'),(450,157,'url2','#fff0df'),(900,64,'url3','#edf4ff'),(900,250,'url4','#edf4ff')]:b+=rect(x-65,y-30,130,60,color)+txt(x,y+9,label,28)
b+=txt(450,230,'Đỉnh giữa',26)
svg('ch2-noi-hai-canh.svg','Hai đường đi qua url2','Đồ thị đúng bốn cạnh Links. url1 đến url2 và url3; url2 đến url3 và url4. L1 và L2 đánh dấu vai trò cạnh trước và sau trong hai đường đi hai cạnh.',b)
