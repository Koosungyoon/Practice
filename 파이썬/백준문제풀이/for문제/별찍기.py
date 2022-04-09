#입력 -> 별을 몇츶까지 쌓을 것인가?
'''
import sys 
N = int(sys.stdin.readline().rstrip())

for i in range(N):
    print("*"*(i+1))
'''
#아래와 같이 하면 앞에 공백문자가 생김!! 이유를 생각해보자
#추측 :sys.stdin.readline().rstrip()에서 앞에 공백 문자가 생긴거 같다!

import sys

N=int(sys.stdin.readline().strip())

for i in range(1,N+1):
    print(" "*(N-i),"*"*i)


a=int(input())
for j in range(1,a+1):
    print(" "*(a-j) + "*"*j)
