import sys
input = sys.stdin.readline

N = int(input().strip())

for i in range(1,N+1):
    print(' ' * (N - i), end='')
    print("*" *(i*2-1))

for j in range(2,N+1):
    print(' ' * (j-1), end ='')
    print("*" * ((N*2)-(j*2-1)))



n = int(input())

for i in range(n):
    print(' ' * (n-i-1), end='')
    print('*'*(i*2+1))

for i in range(1,n):
    print(' ' * i, end='')
    print('*'*((n*2)-(i*2+1)))