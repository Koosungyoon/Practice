#입력 -> A,B가 한 줄로 이루어지며 입력 받음
# 추가로 0 0 이 입력되면 while 루프가 끝남
'''
import sys

while(True):
    A,B = map(int,sys.stdin.readline().strip().split())
    if A==0 and B==0:
        break
    print(A+B)
'''



#try except 구문을 사용해서 런타임 오류(코드가 끝나지 않음!)를 해결!
import sys

while (True):
    try:
        A,B=map(int,sys.stdin.readline().strip().split())
        print(A+B)
    except:
        break