import sys
input = sys.stdin.readline

N = int(input().strip())

for i in range(1,N+1):
    print(" " * (N - i) + "*" * (i),end='')
    print("*" *(i - 1) + " " * (N - i))

for j in range(2,N+1):
    print(" " * (j-1) + "*" * (N-j),end ='')
    print("*" * (N-j+1) + " " * (j-1))