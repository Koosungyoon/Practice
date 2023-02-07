import sys

n, m = map(int,sys.stdin.readline().strip().split())

list1 = []
list2 = []
res = []
for i in range(n):
    list1.append(list(map(int, sys.stdin.readline().strip().split())))

for j in range(n):
    list2.append(list(map(int, sys.stdin.readline().strip().split())))

for a in range(n):
    tmp = []
    for b in range(m):
        tmp.append(list1[a][b] + list2[a][b])
    res.append(tmp)

for i in res:
    for j in i:
        print(j, end =' ')
    print()



