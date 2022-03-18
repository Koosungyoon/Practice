#입력 -> 수열을 이루는 갯수(N), X보다 작은 수들을 걸러 내려함!
'''
import sys

N,X=map(int,sys.stdin.readline().split())
list=[]
result=[]
for i in range(N):
    list[i]=sys.stdin.readline().strip() #이것은 조금더 생각해보자
    
for j in list:
    if X>j:
        result.append(j)

print(result)
'''
import sys

result=[]
N ,X = map(int,sys.stdin.readline().strip().split())
A = list(map(int,sys.stdin.readline().strip().split()))#정수를 한줄 입력 받을 떄는 이와 같이한다. !!!!!!!!!!!!기억하기!!!!!!!!!!!

for i in range(N):
    if A[i]<X:
        result.append(A[i])

print(result)
