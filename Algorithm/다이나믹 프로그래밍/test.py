#적절한 1로 만들기

import sys

d=[0]*30001
x=int(sys.stdin.readline().rstrip())

#다이나믹 프로그래밍 보텀업
for i in range(2,x+1):
    #1을 뺴는 경우
    d[i]=d[i-1]+1
    #2나누어 떨어지는 경우
    if i%2==0:
        d[i]=min(d[i],d[i//2]+1)
    #3으로 나누어 떨어지는 경우
    if i%3==0:
        d[i]=min(d[i],d[i//3]+1)
    #5로 나누어 떨어지는 경우
    if i%5==0:
        d[i]=min(d[i],d[i//5]+1)
    