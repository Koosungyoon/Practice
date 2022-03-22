#입력 -> 첫 줄에 N이 주어진다! 0<=N<=99
#만약 26 이면 2+6=8 6+8=14 8+4=12 4+2=6 ->다시 26이니까 사이클은 4


#나눗셈(//) +나머지(%) 연산자를 이용할 것이다
# while 조건문에 입력값(N) == c값이 같으면 정지! 

import sys
N=int(sys.stdin.readline().strip())

a=N//10
b=N%10
c=-1
f=0

while(N!=c):
    c= b*10+(a+b)%10
    f+=1
    a=c//10
    b=c%10
print(f)   
    


