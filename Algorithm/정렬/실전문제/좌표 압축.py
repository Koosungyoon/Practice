import sys
n=int(sys.stdin.readline())
arr=list(map(int,sys.stdin.readline().split()))
#집합으로 중복됨을 피하고 정렬하기!
arr1=list(sorted(set(arr)))
#딕셔너리로 표현{Key값은 실제 값:Value값은 압축 값} 
dic1={arr1[i]:i for i in range(len(arr1))}

for i in arr:
    print(dic1[i],end=' ')