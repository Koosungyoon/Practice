#N을 입력 받으면 오름차순으로 소인수 출력

import sys
N=int(sys.stdin.readline().strip())
i=2
if N==1:
    print()
while(N>1):
    if N%i==0:
        N/=i
        print(i)
    else:
        i+=1
