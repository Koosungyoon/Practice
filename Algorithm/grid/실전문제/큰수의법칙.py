#큰수의 법칙 
'''
우선N,M,K는 각각 배열의 크기,숫자가 더해지는 횟수, 연속해서 더해질 수 있는 최대
그러나 다른 인덱스의 수가 같아도 다른 숫자로 인정됨
예)5,8,3
  2 4 5 4 6    이면 6+6+6+5+6+6+6+5=46 이 된다
'''
#내 풀이
'''
import sys

n,m,k= map(int,sys.stdin.readline().strip().split())
data=list(map(int,sys.stdin.readline().strip().split()))
data.sort()
sum=0 
count=0

for i in range(m):
    if count<k:
        sum+=data[-1]
        count+=1
    else:
        sum+=data[-2]
        count=0
print(sum)
'''
'''
#문제 풀이
#가장 큰수와 두 번쨰로 큰수 저장 하여-> 가장 큰 수 K번 더하고 두 번째로 큰 수 한번 더하는 것을 반복하면 됨!
#N M K를 공백으로 구분하여 입력받기
n,m,k=map(int,input().split())
#N개의 수를 공백으로 구분하여 입력받기
data=list(map(int,input().split()))

data.sort() #입력받은 수들 정렬
first=data[n-1]
second=data[n-2]

result=0

while True:
    for i in range(k): #가장 큰 수를 K번 더하기
        if m==0: # m이 0이면 반복문 탈출 
            break
        result+=first
        m-=1
    if m==0:
        break
    result+=second# 두 번째로 큰 수를 한 번 더하기
    m-=1
print(result)
'''

#만약 M의 숫자가 엄청나게 큰수로 커진다면=> 시간초과가 된다
#수열을 이용하여 코드를 수정하자면-> (M//(K+1))*K+ M % (k+1) =>  first의 등장횟수를 구함
#                              ->   (M-first등장횟수)*second
n,m,k=map(int,input().split())
data=list(map(int,input().split()))

data.sort()
first=data[n-1]
second=data[n-2]

count=(m//(k+1))*k + m%(k+1)
result=0
result=count*first + (m-count)*second

print(result)