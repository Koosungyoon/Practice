# a,b를 입력 
h,m = map(int,input().split())

if m<45 :
    if h>0:
        print(h-1,m+15)
    if h ==0:
        print(h-1+24,m+15)
    else:
        print(h+24,m+15)
else:
    print(h,m-45)

