#그냥 라이브러리로 간단하게 풀면 가능할 듯
#내림차순으로 정렬 

from audioop import reverse


N=int(input())
arr=[]
for i in range(N):
    arr.append(int(input()))

arr=sorted(arr,reverse=True)

for i in arr:
    print(i,end=' ')