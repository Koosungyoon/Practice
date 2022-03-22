#A,B,C의 곱의 결과를 보고 0~9까지 각각 몇개인지 출력하는 문제
'''
import sys

A=int(sys.stdin.readline().strip())
B=int(sys.stdin.readline().strip())
C=int(sys.stdin.readline().strip())

cnt=[0,0,0,0,0,0,0,0,0,0]
res=str(A*B*C)

for i in range(10):
    if str(i) in res:
        cnt[i]+=1

for j in range(10):
    print(cnt[j])
#17037300
'''
import sys 

A=int(sys.stdin.readline().strip())
B=int(sys.stdin.readline().strip())
C=int(sys.stdin.readline().strip())

res =list(str(A*B*C))#리스트로 변환하고 0~9까지의 수 갯수 세준다!
for i in range(10):
    print(res.count(str(i)))
