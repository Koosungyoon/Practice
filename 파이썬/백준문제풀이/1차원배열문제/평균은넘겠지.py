#입력 -> 우선C(케이스 종류)\n ,학생수, 각 학생의 점수 입력
# 출력-> 평균을 넘는 친구들의 비율
''' 케이스가 한 가지일 경우 구현
import sys
sum = 0
res = 0 
cnt = 0
#케이스 종류수 입력 
C = int(sys.stdin.readline().strip())
#학생 수와 점수 입력
A = list(map(int,sys.stdin.readline().strip().split()))
#학생들 평균 구하기
for i in range(1,len(A)):
    sum += A[i]
    res = sum/A[0]
#평균 넘는 친구들 카운트 해주기
for j in range(1,len(A)):
    if A[j]>res:
        cnt += 1
print(f'{(cnt*100)/A[0]:.3f}%')
'''

#케이스 많은 경우 구현
import sys

#케이스 종류수 입력 
C = int(sys.stdin.readline().strip())
#케이스마다 학생수와 점수 입력
for k in range(C):
    #케이스 마다 변수 초기화!
    sum = 0
    res = 0 
    cnt = 0
    A = list(map(int,sys.stdin.readline().strip().split()))
    #학생들 평균 구하기
    for i in range(1,len(A)):
        sum += A[i]
        res = sum/A[0]
    #평균 넘는 친구들 카운트 해주기
    for j in range(1,len(A)):
        if A[j]>res:
            cnt += 1
    print(f'{(cnt*100)/A[0]:.3f}%')

