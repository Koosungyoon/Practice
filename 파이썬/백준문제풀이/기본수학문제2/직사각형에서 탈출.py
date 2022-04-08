import sys

x,y,w,h=map(int,sys.stdin.readline().strip().split())

res={x,y,w-x,h-y}
print(min(res))
