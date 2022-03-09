#qudrant 문제 
#x,y좌표 입력 -> x의 좌표가 양수라면 1,4분면 음수라면 2,3분면 
#            -> y의 좌표가 양수라면 1,2분면 음수라면 3,4분면

x = int(input())
y = int(input())

if x>0 :
    if y>0:
        print(1)
    else:
        print(4)
else :
    if y>0:
        print(2)
    else:
        print(3)