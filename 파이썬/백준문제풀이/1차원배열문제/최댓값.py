#입력 -> 9개의 자연수가 줄단위로 입력됨 
'''
import sys
a=[]
for i in range(9):
    a.append(sys.stdin.readline().strip())

print(max(a))
print(a.find(max(a)))#find 함수는 문자열함수이다
'''

import sys
a= []
max_value=0
index=0

for i in range(9):
    a.append(int(sys.stdin.readline().strip()))
    if max_value<a[i]: #왜 max(a)하면 되는데 이렇게 하는가? ->  index를 출력하기 위해서
        max_value=a[i]
        index=i+1 #index는 0부터 시작이므로 몇번째를 나타내려면 +1

print(max_value) 
print(index)