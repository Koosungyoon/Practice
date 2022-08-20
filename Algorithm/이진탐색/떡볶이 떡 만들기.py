#떡볶이 떡을 손님이 요구하는 m길이 만큼 주기 위해서 우리가 설정해야하는 h값의 최대값을 구하라
#나는 중앙값을 이용하여 구하고자 한다.

import sys

def sum_fnc(arr,mid):
    sum=0
    for i in arr:
        if i-mid>0:
            sum+=(i-mid)
    return sum

n,m=map(int,sys.stdin.readline().rstrip().split())
arr=list(map(int,sys.stdin.readline().rstrip().split()))
arr.sort()
sum1=0
mid=arr[(len(arr)-1)//2]

while True:
    sum1=sum_fnc(arr,mid)
    if sum1==m:
        print(mid)
        break
    elif sum1>m:
        mid+=1
    else:
        mid-=1