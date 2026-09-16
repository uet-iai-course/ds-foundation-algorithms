from pathlib import Path
import runpy
base=Path(__file__).resolve().parent
# Reuse the deck's native diagram helpers without introducing a new style.
d=runpy.run_path(str(base/'render-cost-diagrams.py'))
txt,box,save=d['txt'],d['box'],d['save']
b=txt(175,45,'Một máy: nối tiếp',28)+txt(175,175,'Hai máy: đồng thời',28)
x=360;unit=150
b+=box(x,10,unit*2,65,'R0: 2c')+box(x+unit*2,10,unit*3,65,'R1: 3c','#ef6c00')
b+=txt(175,225,'Máy A',25)+txt(175,305,'Máy B',25)+box(x,185,unit*2,65,'R0: 2c')+box(x,265,unit*3,65,'R1: 3c','#ef6c00')
for k in range(6):b+=txt(x+k*unit,135,str(k)+'c',24)
b+='<path d="M360,110 L1110,110" stroke="#334155" stroke-width="2"/>'
b+=txt(1100,190,'Thời gian →',24)
save('cost-parallel-time','Cùng năm đơn vị công việc: thời gian từ năm c còn ba c','Một máy chạy R0 hai c rồi R1 ba c. Hai máy chạy hai tác vụ đồng thời, hoàn tất sau ba c. Tổng công việc không đổi.',b)
