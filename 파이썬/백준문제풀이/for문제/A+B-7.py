import sys

N = int(sys.stdin.readline().rstrip())
list=[]
for i in range(N):
    a,b=map(int,sys.stdin.readline().rstrip().split())
    list.append(a+b)
for j in range(N):
    print("Case #%d: %d"%(j+1,list[j]))