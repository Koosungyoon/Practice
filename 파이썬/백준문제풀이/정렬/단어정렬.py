import sys
input = sys.stdin.readline

N = int(input())

res = []    
for i in range(N):
    tmp = []
    tmp = input().strip()
    tmp_len = len(tmp)
    res.append([tmp,tmp_len])
    # res_len.append(len(tmp))
res1 = set(list(map(tuple,res)))
res_sorted = sorted(res1)

for a in sorted(res_sorted,key = lambda x: x[1]):
    print(a[0])
