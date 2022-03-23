# 10개의 자연수를 받고 42로 나누어 나머지가 몇가지인지 출력 하자
# 나머지 리스트에 존재하지 않는 수라면 추가   해주기로 조건 추가!
import sys
a=[]
b=[]

for i in range(10):
    a.append(int(sys.stdin.readline().strip()))
    #b.append(a[i]%42)  # 나머지 리스트에 존재하지 않는 수라면 추가   해주기로 조건 추가!
    if (a[i]%42) not in b:
        b.append(a[i]%42)


''' 
for j in range(len(b)): #문제점 : 중복해서 더하는중!
    for s in range(j):
        if b[j]!=b[s]:
            k+=1
        else:
            break
'''

print(b)
print(len(b))
