# 입력 -> 과목수(N), 각 교과 점수 
import sys

N = int(sys.stdin.readline().strip())
A = list(map(int,sys.stdin.readline().strip().split()))
res = 0
max_value = max(A)
B=[]
#B = list(map(lambda x,y: (x/y) *100,A,max_value)) #int(정수)==max_value는 반복가능하지 않다 
for j in range(N):
    B.append((A[j]/max_value)*100)
for i in range(len(B)):
    res+=B[i]

print("%f"%(res/N))
print(f'{res/N:.2f}') #소수점 2자리수 나타내는 방식 