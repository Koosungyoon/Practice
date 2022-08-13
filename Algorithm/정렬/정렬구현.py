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

def quick_sort(arr,start,end):
    if start>=end:
        return 
    
    pivot=start
    left=start+1
    right=end

    while right>=left:
        while left<=end and arr[left]<=arr[pivot]:
            left+=1
        while right>start and arr[right]>=arr[pivot]:
            right-=1
        if left>right:
            arr[right],arr[pivot]=arr[pivot],arr[right]
        else:
            arr[left],arr[right]=arr[right],arr[left]
    
    quick_sort(arr,start,right-1)
    quick_sort(arr,right+1,end)

quick_sort(array,0,len(array)-1)
print(array)

#파이썬의 장점을 살린 퀵 정렬

array=[5,7,9,0,3,1,6,2,4,8]

def quick_sort(arr):
    if len(arr)<=1:
        return arr
    
    pivot=arr[0]
    tail=arr[1:]

    left_side=[x for x in tail if x<=pivot] # 분할된 왼쪽 부분
    right_side=[x for x in tail if x>pivot] # 분할된 오른쪽 부분

    #분할 이후 왼쪽 부분과 오른쪽 부분에서 각각 정렬을 수행하고, 전체 리스트를 변환
    return quick_sort(left_side)+[pivot]+quick_sort(right_side)

print(quick_sort(array))