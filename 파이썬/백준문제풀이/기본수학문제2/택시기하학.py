#유클리드 기하학에서 원의 넓이는 pi*R**2 이지만
#택시기하학에서 원의 넓이는 지름이 대각선인 정사각형 넓이 이다

import sys
import math

r=int(sys.stdin.readline().strip())
print(f'{math.pi*r**2:6f}')
print(f'{2*r**2:6f}')