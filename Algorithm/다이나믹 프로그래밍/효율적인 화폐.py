#ai는  금액 i를 만들 수 잇는 최소한의 화폐 개수,
#화폐의 단위를 k라고 할때 a(i-k)는 금액(i-k)를 만들 수 있는 최소한의 화폐 개수이다.
# 따라서 k화폐를 확인 할때 i-k금액을 만들 수 있으면 ->d[i]=min(ai,a(i-k)+1)

import sys

n,m=int(sys.stdin.readline().strip().split())

arr=[]
for i in range(n):
    arr.append(int(sys.stdin.readline().strip()))

#한 번 계산된 결과가 저장되어있는 DP 테이블 초기화
d=[10001]*(m+1)
#다이나믹 프로그래밍
d[0]=0
#내가 가지고 있는 화폐단위를 하나하나 비교
for i in range(n):
    for j in range(arr[i],m+1):
        if d[j-arr[i]] != 10001: #(i-k)원을 만드는 방법이 존재하는 경우
            d[j]=min(d[j],d[j-arr[i]]+1)
if d[m]==10001:
    print(-1)
else:
    print(d[m])







