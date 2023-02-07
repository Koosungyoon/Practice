import sys

N = int(sys.stdin.readline().strip())

res = []

for _ in range(N):
    res.append(int(sys.stdin.readline().strip()))


#res.sort()
#삽입 정렬로 해보기
# for i in range(len(res)):
#     for j in range(i,0,-1):
#         if res[j] < res[j-1]:
#             res[j],res[j-1] = res[j-1],res[j]
#         else:
#             break
#버블 정렬
for i in range(len(res)):
    for j in range(len(res)):
        if res[i] < res[j]:
            res[i],res[j] = res[j],res[i]
    print(res)

for i in range(len(res)):
    print(res[i])
