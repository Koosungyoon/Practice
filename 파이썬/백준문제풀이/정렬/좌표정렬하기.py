import sys
input = sys.stdin.readline

N = int(input())
tmp = []

for i in range(N):
    x, y = map(int,input().split())
    tmp.append((x, y))

# print(tmp)
# print(sorted(tmp))
for i in sorted(tmp):
    print(i[0],i[1])

