import sys

res = []
for _ in range(5):
    res.append(int(sys.stdin.readline().strip()))
res.sort()

avg = sum(res) / 5
mean = res[2]
print(f'{avg:.0f}')
print(mean)