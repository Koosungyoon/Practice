#재귀 함수로 이진 탐색 구현
import sys
def binary_search(arr,target,start,end):
    #존재하지 않는다면 None출력
    if start>end:
        return None
    #중간점을 의미
    mid=(start+end)//2
    if arr[mid]==target:
        return mid
    elif arr[mid]>target:
        return binary_search(arr,target,start,mid-1)
    else:
        return binary_search(arr,target,mid+1,end)
#n(원소의 개수)과 target(찾고자 하는 문자열)을 입력받기
n,target=list(map(int,sys.stdin.readline().split()))
#전체 원소 입력받기
arr=list(map(int,sys.stdin.readline().split()))

result=binary_search(arr,target,0,n-1)
if result==None:
    print("원소가 존재 하지 않습니다.")
else:
    print(result+1)


#반복문으로 구현한 이진 탐색 소스코드

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

#n(원소의 개수)과 target(찾고자 하는 문자열)을 입력받기
n,target=list(map(int,sys.stdin.readline().split()))
#전체 원소 입력받기
arr=list(map(int,sys.stdin.readline().split()))

result=binary_search(arr,target,0,n-1)
if result==None:
    print("원소가 존재 하지 않습니다.")
else:
    print(result+1)