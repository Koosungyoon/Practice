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
    while(True):
        #a-b역시 소수인가 봐야함
        if is_prime(b) and is_prime(a-b):
            print(a-b,b)
            break
        b+=1