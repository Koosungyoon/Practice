import sys

while(True):
    a,b,c=map(int,sys.stdin.readline().strip().split())
    if a==0 and b==0 and c==0:
        break
    res=[a,b,c]
    max_num=res.pop(res.index(max(res))) # or max_num=max(res)\n  res.remove(max_num)
    if max_num**2==res[0]**2+res[1]**2:
        print("right")
    else:
        print("wrong")