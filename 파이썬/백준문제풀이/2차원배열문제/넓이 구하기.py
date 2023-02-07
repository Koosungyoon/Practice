import sys

n = int(sys.stdin.readline().strip())
total = [[0] * 100 for _ in range(100)]

for _ in range(n):
    a, b = map(int, sys.stdin.readline().strip().split())
    
    for i in range(a,a+10):
        for j in range(b,b+10):
            total[i][j] = 1

res = 0

for i in range(100):
    for j in range(100):
        if total[i][j]:
            res += 1

print(res)

