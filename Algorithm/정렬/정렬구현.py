#선택 정렬 구현
'''
!!매번 가장 작은 것을 선택한다.!!
'''
from operator import le


array=[7,5,9,0,3,1,6,2,4,8]

for i in range(len(array)):
    min_index=i #가장 작은 원소의 인덱스
    for j in range(i+1,len(array)):
        if array[min_index]>array[j]:
            min_index=j
    array[i],array[min_index]=array[min_index],array[i]

print(array)

#삽입 정렬 구현
'''
데이터를 하나씩 확인하며, 각 데이터를 적절한 위치에 삽입한다.
    삽입 정렬은 특정한 데이터가 적절한 위치에 들어가기 이전에, 그 앞까지의 데이터는 이미 정렬되어 있다고 가정한다.
'''
array=[7,5,9,0,3,1,6,2,4,8]

for i in range(1,len(array)):
    for j in range(i,0,-1):
        if array[j]<array[j-1]: #한 칸씩 왼쪽으로 이동 
            array[j],array[j-1]=array[j-1],array[j]
        else: #자기보다 작은 데이터를 만나면 그 위치에서 멈춤!
            break
print(array)

#퀵 정렬 구현
'''
기준 데이터를 설정하고 그 기준보다 큰 데이터와 작은 데이터의 위치를 바꾼다.
'''

array=[5,7,9,0,3,1,6,2,4,8]

def quick_sort(array,start,end):
    if start>=end: #원소가 1개인 경우 종료
        return 
    pivot=start # 피벗은 첫 번쨰 원소
    left=start+1
    right=end
    while left<=right:
        #피벗보다 큰 데이터를 찾을 때까지 반복
        while left<=end and array[left]<=array[pivot]:
            left+=1
        #피벗보다 작은 데이터를 찾을 떄까지 반복
        while right>start and array[right]>=array[pivot]:
            right-=1
        if left>right: #엇갈렸다면 작은 데이터와 피벗을 교체
            array[right],array[pivot]=array[pivot],array[right]
        else: #엇갈리지 않았다면 작은 데이터와 큰 데이터를 교체
            array[left],array[right]=array[right],array[left]
        
    #분할 이후 왼쪽 부분과 오른쪽 부분에서 각각 정렬 수행
    quick_sort(array,start,right-1)
    quick_sort(array,right+1,end)

quick_sort(array,0,len(array)-1)
print(array)