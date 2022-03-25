#입력 -> T케이스 종류 수 
#        R이라는 반복할 횟수, S(QR Code "alphanumeric")로 이루어진 문자열

#출력 -> P라는 새로운 문자열 

import sys

T=int(sys.stdin.readline().strip())
for i in range(T):
    P='' #매 케이스마다 문자열 초기화 해주기
    R,S=sys.stdin.readline().strip().split()
    for j in S:
        P += j*int(R) #문자열P에 R번 반복한것 추가해주기
    print(P)

