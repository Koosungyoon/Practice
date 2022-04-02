#입력 -> 줄단위로 M과N을 입력 받음 
#출력 -> M과N사이의 소수들의 합을 구하고 소수중 최솟값
#만약  M과N사이에 소수가 없다면 -1출력

import sys

M=int(sys.stdin.readline().strip())
N=int(sys.stdin.readline().strip())
cnt_list=[]
for i in range (M,N+1):
    cnt=0
    for j in range(2,i+1):
        if i%j==0:
            cnt+=1
    if cnt==1:
        cnt_list.append(i)
if len(cnt_list)>0:
    print(sum(cnt_list)) #sum 함수를 이용!
    print(min(cnt_list))
else:
    print(-1)