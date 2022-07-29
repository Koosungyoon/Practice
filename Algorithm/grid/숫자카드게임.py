#숫자카드게임으로 적당한 행과열로 이루어진 배열에서 1.행을 고르고 2. 행중에서 가장 작은수를 뽑아야한다.
# 결론은 조건을 만족하는 큰 수를 찾아라
'''
단순하게 행중에서 가장 작은 수를 서로 비교해보고 그 중에서 가장 큰수를 출력해주면 될듯 하다!

#행과열을 공백을 기준으로 입력
n,m=map(int,input().split())

res=0
#한 줄씩입력받아 확인
for i in range(n):
    data=list(map(int,input().split()))
    #현재 줄에서 가장 작은 수 찾기
    min_value=min(data)
    #가장 작은 수들중에서 가장 큰 수 찾기
    res=max(res,min_value)

print(res)  
'''
#이중 for문으로 구현
n,m=map(int,input().split())
res=0
for i in range (n):
    data=list(map(int,input().split()))
    min_value=10001
    for a in data:
        min_value=min(min_value,a)
    res=max(res,min_value)

print(res)
   



