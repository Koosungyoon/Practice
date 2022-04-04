#베르트랑 공준 
'''
n이 주어지면 2n보다 작거나 같은 소수는 존재한다 ! n을 입력->2n보다 작거나같은 소수 개수 구하기!
'''
import sys

while(True):
    n=int(sys.stdin.readline().strip())
    if n==0:
        break
    a=[False,False]+[True]*(2*n-1)
    prime=[]
    for i in range(2,2*n+1):
        if a[i]:
            prime.append(i)
            for j in range(i*2,2*n+1,i):
                a[j]=False
    cnt=0
    for k in prime:
        if k>n:
            cnt+=1
    print(cnt)
    