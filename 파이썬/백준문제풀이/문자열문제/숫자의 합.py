'''
import sys
#숫자의 개수
m=int(sys.stdin.readline().strip())
sum=0
n=int(sys.stdin.readline().strip())
for i in str(n):
    sum+=int(i)
print(sum)
'''

#sum 함수를 이용
import sys
n = sys.stdin.readline().strip()

print(sum(map(int,sys.stdin.readline().strip())))