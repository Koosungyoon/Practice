#input() 함수 대신 -> sys.stdin.readline()으로 대체!
#여기서 sys은 모듈이다 
#sys 를 이용해서 더 input()함수보다 더 빠르게 입력 받을 수 있다.
#readline()함수는 공백을 기준으로 줄단위로 읽어주는 함수
import sys

N = int(sys.stdin.readline()) 
list =[]

for i in range(N):
    a,b=map(int,sys.stdin.readline().split())
    list.append(a+b)

for j in range(N):
    print(list[j])
