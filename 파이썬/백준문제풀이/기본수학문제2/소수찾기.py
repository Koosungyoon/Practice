#N개의 수를 받고 소수의 개수를 출력하자

import sys

N=int(sys.stdin.readline().strip())
a=list(map(int,sys.stdin.readline().strip().split()))
cnt_list=[]

for i in a:
    cnt=0 #약수의 개수 
    for j in range(1,i+1):#1부터 자기자신까지 약수를 탐색하기 위한 반복문 
        if i%j==0:#약수 있을때마다 +1
            cnt+=1
    if cnt==2:#약수가 1과 자기자신인 경우 
        cnt_list.append(i)
print(len(cnt_list))
