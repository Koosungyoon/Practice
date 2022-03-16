# a,b를 입력 
'''
h,m = map(int,input().split())

if m<45:
    if h==0:
        print(h-1+24, m+15)
    else:
        print(h-1, m+15)
else:
    print(h,m-45)
'''

#만약에 알람을 앞서는 시간이 45분이아닌 입력을 받아서 구현한다면

distance = int(input())
h,m = map(int,input().split()) #e두 정수를 입력받음

if m<distance:
    if h==0:
        print(h-1+24, m-distance+60)
    else:
        print(h-1, m-distance+60)
else:
    print(h,m-distance)