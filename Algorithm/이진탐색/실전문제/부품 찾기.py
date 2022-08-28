#부품 찾기
'''
가게에 있는 부품중에서 손님이 찾고자 하는 부품이 있으면 yes,없으면 no라고 출력 하는 프로그램 작성
'''

#집합 자료형 이용하여 구현 
import sys

n=int(sys.stdin.readline().rstrip())
n_arr=set(map(int,sys.stdin.readline().rstrip().split()))

m=int(sys.stdin.readline().rstrip())
m_arr=list(map(int,sys.stdin.readline().rstrip().split()))

def search(arr,target):
    if target in arr:
        print("yes")
    else:
        print("no")

for i in m_arr:
    search(n_arr,i)


#이진 탐색이용 구현
import sys

def binary_search(arr,target,start,end):
    while start<=end:
        mid=(start+end)//2

        if arr[mid]==target:
            return mid
        elif arr[mid]>target:
            end=mid-1
        else:
            start=mid+1
    return None

n=int(sys.stdin.readline().rstrip())
n_arr=list(map(int,sys.stdin.readline().rstrip().split()))
n_arr.sort()

m=int(sys.stdin.readline().rstrip())
m_arr=list(map(int,sys.stdin.readline().rstrip().split()))

for i in m_arr:
    result=binary_search(n_arr,i,0,n-1)
    if result !=None:
        print("yes",end=' ')
    else:
        print("no",end=' ')


#계수 정렬을 이용하여 구현

import sys

n=int(sys.stdin.readline().rstrip())
arr=[0]*10001

for i in input().split():
    arr[int(i)]=1
m=int(sys.readline().rstrip())
m_arr=list(map(int,sys.readline().rstrip().split()))

for i in m_arr:
    if i in arr:
        print('yes',end=' ')
    else:
        print('no',end=' ')

