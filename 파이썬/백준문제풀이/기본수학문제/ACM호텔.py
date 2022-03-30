#입력 -> 케이스 종류 , 다음줄 층,호수,몇번째 사람?
#출력 -> 몇호인지 출력

import sys

T=int(sys.stdin.readline().strip())
for i in range(T):
    H,W,N=map(int,sys.stdin.readline().strip().split())
    #층수
    if N%H==0:
        floor=H
    else:
        floor=N%H
    #호수
    if N%H==0:
        num=N//H
    else:
        num=N//H+1
    print(floor*100+num)

    '''
    처음에는 단순히 층수는 N%H 호수는 N//H +1로 했는데 
    N이 H의 짝수 이면 문제가 발생함 
    층수는 0층이 되고 호수는 +1호가 되버린다
    따라서 짝수인경우에는 층=H이고 호수=N//H이다 ! 

    '''