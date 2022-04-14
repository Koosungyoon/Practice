#M이상 N이하의 소수를 구하는 프로그램

'''
import sys
M,N=map(int,sys.stdin.readline().strip().split())
cnt_list=[]
for i in range(M,N+1):
    cnt=0
    for j in range(2,i+1):
        if i%j==0:
            cnt+=1
            if cnt>1:
                break
    if cnt==1:
        print(i)
'''

#에라토스테네스의 체로 구현해보자! ->시간 절약!
#에라토스테네스의 체 : 범위에서 합성수를 지우는 방식으로 소수를 찾는 방법. 1. 1은 제거 2. 지워지지 않은 수 중 제일 작은 2를 소수로 채택하고,
#나머지 2의 배수를 모두 지운다. 3. 지워지지 않은 수 중 제일 작은 3을 소수로 채택하고,
#나머지 3의 배수를 모두 지운다. 4. 지워지지 않은 수 중 제일 작은 5를 소수로 채택하고, 
#나머지 5의 배수를 모두 지운다. 5. (반복)
'''
우선 약수의 성질을 보면
모든 약수가 가운데 약수를 기준으로 곱셈 연산에 대해 대칭을 이룬다!
따라서 우리는 특정한 자연수의 모든 약수를 찾을 떄 가운데 약수(제곱근)까지만 확인하면됨!
---예를 들면 16이 2로도 나누어 지는 것은 8로도 나누어 떨어진다는 것을 의미
'''
'''
#일단 소수 판별 함수 만들어보기!
import math
import sys
def is_prime_num(x):
    if x==1:
        return False
    #2부터 x의 제곱근 까지 모든수 확인!
    for i in range(2,int(math.sqrt(x))+1):
        #x가 나누어 떨어지면 소수 아님
        if x%i==0:
            return False
    return True

M,N=map(int,sys.stdin.readline().strip().split())

for i in range(M,N+1):
    if is_prime_num(i):
        print(i)
'''
'''
import sys

M,N=map(int,sys.stdin.readline().strip().split())
a=[False,False]+[True]*(N-1)
prime=[]
for i in range(2,N+1):
    if a[i]:
        prime.append(i)
        for j in range(i*2,N+1,i):
            a[j]=False
for k in prime:
    if k>=M:
        print(k)
'''
'''
위의 코드는 N까지의 소수를 구한다음 -> M과N사이의 소수를 출력하게끔 구현!'''    
     

#정수 n이 n의 제곱근 이하의 어떤 소수로도 나누어 떨어지지 않으면 n은 소수이다!
import sys

prime =[None]*500
ptr=0

prime[ptr]=2
ptr+=1
prime[ptr]=3
ptr+=1
for n in range(5,1001,2): #어차피 4이상의 짝수는 모두 합성수이므로 제외
    i=1 #2는 짝수이므로 제외 하고 prime[1]부터 확인하는것 이다!
    while prime[i]**2<=n: #이표현이 n이하의 제곱근이하의  -> n이하의 n제곱근 이면 실행 한다! 
        if n%prime[i]==0:  
            break
        i+=1
    else:                 #소수로 나누어떨어지지 않으면
        prime[ptr]=n  
        ptr+=1

for i in range(ptr):
    print(prime[i])