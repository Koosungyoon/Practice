#입력 -> 고정비용 가변비용 노트북 가격
#출력 -> 손익분기점이 발생하는 판매량의 수 
#(고정비용+가변비용)<수입비용 -> 손익분기점!
import sys

A,B,C = map(int,sys.stdin.readline().strip().split())

if B>=C:
    print(-1)
else:
    print(A//(C-B)+1)
