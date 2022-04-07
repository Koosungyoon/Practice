'''
골드바흐의 추측
2보다 큰 모든 짝수는 두가지 소수의 합으로 표현된다.
2보다 큰 짝수가 주어지면 골드바흐 파티션을 출력해라!
'''
'''
시간 초과!!!!
import sys

n=int(sys.stdin.readline().strip())
for i in range(n):
    a=int(sys.stdin.readline().strip())
    b=[False,False]+[True]*(a-1)
    prime=[]
    for j in range(2,a+1):
        if b[j]:
            prime.append(j)
            for k in range(j*2,a+1,j):
                b[k]=False
    c=a-prime[len(prime)//2]
    while(True):
        i=1
        if c in prime:
            if c>(a-c):
                print((a-c),c)
            else:
                print(c,(a-c))
            break
        else:
            c=a-prime[len(prime)//2+i]
            i+=1
'''
import sys
import math
def is_prime(x):
    if x==1:
        return False
    for i in range(2,int(math.sqrt(x))+1):
        if x%i==0:
            return False
    return True

n=int(sys.stdin.readline().strip())
for i in range (n):
    a=int(sys.stdin.readline().strip())
    b=a//2
    for x in range(b,1,-1):  #반목문 활용시 반대로 카운트 하는 것도 생각해보자
        if is_prime(a-x) and is_prime(x):
            print(x,a-x)
            break
    '''
    #while반복분 사용
    while(True):
        #a-b역시 소수인가 봐야함
        if is_prime(b) and is_prime(a-b):
            print(a-b,b)
            break
        b+=1
    '''
    #집합을 활용
import sys
#소수는 2를 제외하고 홀수이므로 2와 홀수 전체 집합에서 홀수의 배수를 제거 하는방법!
nums={x for x in range(2,10001) if x==2 or x%2==1}
for odd in range(3,101,2): #100=sqrt(10000)
    nums-={i for i in range(2*odd,10001,odd) if i in nums}


n=int(sys.stdin.readline().strip())
for i in range(n):
    a=int(sys.stdin.readline().strip())
    b=a//2
    for x in range(b,1,-1):
        if (a-x)in nums and x in nums:
            print(x,a-x)
            break





