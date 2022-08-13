import sys
from collections import Counter #카운터 해주는 라이브러리 이용

n=int(sys.stdin.readline())

arr=[]
for _ in range(n):
    arr.append(int(sys.stdin.readline()))

print(round(sum(arr)/n)) # 산술평균
arr.sort()
print((arr[(n//2)])) #중앙값
#최빈값!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
arr_cnt=Counter(arr).most_common() #카운터는 딕셔너리의 확장
if len(arr_cnt)>1 and arr_cnt[0][1]==arr_cnt[1][1]:
    print(arr_cnt[1][0])
else:
    print(arr_cnt[0][0])
#범위 
print(max(arr)-min(arr))