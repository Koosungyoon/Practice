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
    for i in range(2,int(math.sqrt(x))+1):
        if x%i==0:
            return False
    return True

n=int(sys.stdin.readline().strip())
for i in range (n):
    a=int(sys.stdin.readline().strip())
    b=a//2
    if is_prime(b):
        print(b,b)
    while(not is_prime(b)):
        b+=1
        #a-b역시 소수인가 봐야함
        if is_prime(b) and is_prime(a-b):
            print(a-b,b)
            break






