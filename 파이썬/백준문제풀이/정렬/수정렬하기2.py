import sys
input = sys.stdin.readline
n=int(input())

res = []

for i in range(n):
    res.append(int(input()))

for i in sorted(res):
    print(i)


