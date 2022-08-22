#다이나믹 프로그래밍 문제는 작은 부분을 해결하여 그 결과를 DP 테이블에 저장하고 
#점차적으로 큰 문제로 증가하는 그런 방식으로 푸는 것이다.

import sys
#한 번 계산된 결과를 저장하는 DP 테이블 초기화 
d=[0]*101

n=int(sys.stdin.readline().rstrip())
arr=list(map(int,sys.stdin.readline().strip().split()))
d[0]=arr[0]
d[1]=max(d[0],arr[1])

for i in range(2,n):
    d[i]=max(d[i-1],d[i-2]+arr[i]) #d[i-1]까지 약탈한 식량의 최댓값과 d[i-2]까지 약탈한 식량의 최댓값 + arr[i](i칸에 존재하는 식량)중 큰 값을 d[i]라 함

print(d[n-1])


