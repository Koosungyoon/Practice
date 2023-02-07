import sys

list1 = []
for i in range(9):
    list1.append(list(map(int,sys.stdin.readline().strip().split())))

max,row,col = -1,0,0

for a in range(9):
    for b in range(9):
        if (max < list1[a][b]):
            max = list1[a][b]
            row = a + 1
            col = b + 1

print(max)
print(row,col)

