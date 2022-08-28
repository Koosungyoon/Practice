#떡볶이 떡을 손님이 요구하는 m길이 만큼 주기 위해서 우리가 설정해야하는 h값의 최대값을 구하라
#이진 탐색으로 범위를 좁힌다.

import sys

n,m=map(int,sys.stdin.readline().rstrip().split())
#각 떡의 개별 높이 정보를 입력받기
arr=list(map(int,sys.stdin.readline().rstrip().split()))
#이진 탐색을 위한 시작점과 끝점 설정
start=0
end=max(arr)
#이진 탐색 수행(반복적)
result=0
while(start<=end):
    total=0
    mid=(start+end)//2
    for i in arr:
        #잘랐을 떄의 떡의 양 계산
        if i>mid:
           total+=(i-mid)
    #떡의 양이 부족한 경우 더 많이 자르기(왼쪽 부분 탐색)
    if total<m:
        end=mid-1
    #떡의 양이 많은 경우 더 적게 자르기(오른쪽 부분 탐색)
    else:
        result=mid #최대한 덜 잘랐을 떄가 정답이므로, 여기에서 result에 기록
        start=mid+1 
print(result)