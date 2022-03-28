#입력 -> 달팽이가 낮에 올라가는거리, 밤에 내려오는 거리, 올라가야할 거리
#출력 -> 몇일이 걸리는지!
#ceil함수 이용 -> 올림함수!!!!!!!!!!
import sys
import math

A,B,V=map(int,sys.stdin.readline().strip().split())
#나무 높이 -> (A-B)*day+A=V ->> day=(V-A)/(A-B)
day=math.ceil((V-A)/(A-B)) + 1
print(day)

