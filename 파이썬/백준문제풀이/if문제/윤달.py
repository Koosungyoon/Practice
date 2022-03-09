#윤년 4의배수and not100배수 or 400  배수
#-> 4의배수 전체 -100의 배수 +400의 배수 
'''
a = int(input())

if a % 4 == 0:
    if a % 100 ==0:
        if a % 400 == 0:
           print(1)
        else :
            print(0)
    else :
        print(1)        
else :
    print (0)
'''
#숏코딩 

a = int(input())

if (a%4==0 and a%100!=0) or a%400==0:
    print(1)
else :
    print(0)