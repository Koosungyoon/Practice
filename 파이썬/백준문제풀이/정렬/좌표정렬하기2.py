import sys
input = sys.stdin.readline

N = int(input())
res = []
# for i in range(N):
#     a,b = map(int, input().split())
#     res.append([b,a])

# for b, a in sorted(res):
#     print(a,b)

for i in range(N):
    a,b = map(int,input().split())
    res.append([a,b])

for a, b in sorted(res,key =lambda x : (x[1],x[0])):
    print(a,b)