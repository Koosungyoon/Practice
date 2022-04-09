#두 원의 교점을 구하는 것!
#교점이 두개 -> 반지름의 합이 거리보다 크다 & 반지름의 차가 거리보다 작다
# 교점이 한개-> 반지름의 합이 거리와 같다(외접) or 반지름의 차가 거리와 같다(내접)
# 교점이 없다-> 반지름의 합이 거리보다 작다! & 반지름의 차가 거리보다 크다

import sys
import math
n=int(sys.stdin.readline().strip())
for i in range(n):
    x1,y1,r1,x2,y2,r2=map(int,sys.stdin.readline().strip().split())
    d=math.sqrt((x1-x2)**2+(y1-y2)**2)
    if d==0:
        if r1==r2:
            print(-1)
        else:
            print(0)
    elif r1+r2>d and abs(r1-r2)<d:
        print(2)
    elif r1+r2==d or abs(r1-r2)==d:
        print(1)
    else:
        print(0)
    
