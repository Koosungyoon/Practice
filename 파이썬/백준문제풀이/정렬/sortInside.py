import sys
input = sys.stdin.readline
n = (input())

# k = len(n)
tmp = []
for i in sorted(n,reverse= True):
    print(i,end='')