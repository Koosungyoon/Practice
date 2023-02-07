import sys

N, k = map(int, sys.stdin.readline().strip().split())
res = list(map(int, sys.stdin.readline().strip().split()))

res.sort()
print(res[N-k])