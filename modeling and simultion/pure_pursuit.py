import math
import random

xb=random.randint(1,1000)
yb=random.randint(1,1000)                                                                       #Y coordinates of the bomber
xf=random.randint(1,1000)                                                                       #  X of fighter
yf=random.randint(1,1000)                                                                       # Y of fighter
sf=20                                                                                           #speed of the fighter                       
status=True
t=0                                                                                     #status true means bomber escaped
while(status):
    d=math.sqrt((xb-xf)*(xb-xf)+(yb-yf)*(yb-yf))
    print(f'time {t} : fighter\'s coordinates: ({xf},{yf})  Bomber\'s coordinates: ({xb},{yb})')
    if(d<=100):
        status=False
        print(f'Bomber Plane destroyed at time t = {t}units')
    elif(d>900):
        status=False
        print(f'Bomber Plane escaped at time t = {t}units ')
    else:
        xf+=round(sf*(xb-xf)/d)
        yf+=round(sf*(yb-yf)/d)
        xb=random.randint(1,1000)
        yb=random.randint(1,1000)
        t+=1
