#순차 탐색 소스코드 구현   
import sys
def sequnential_search(n,target,arr):
    for i in range(n):
        if target==arr[i]:
            return i+1

#생설할 원소의 개수를 입력하고, 찾을 데이터를 받기
input_data=sys.stdin.readline().split()
n=int(input_data[0])
targe_data=input_data[1]

#원소의 개수 만큼 데이터 입력
arr=sys.stdin.readline().split()

print(sequnential_search(n,targe_data,arr))

