#입력 -> 케이스의 개수(N), 각각의 케이스별로 OX문제 결과
import sys

N = int(sys.stdin.readline().strip())

#각 케이스별 입력받고 리스트로 형변환
for i in range(N):
    A=(sys.stdin.readline().strip())
    S=list(A)
    #res,x는 케이스마다 다음과 같이 초기화해야한다!
    res=0
    x=1
    #S의 요소들 모두 확인하는 것!
    for j in S:
        if j=='O':
            res+=x
            x+=1
        else:
            x=1
    print(res)


