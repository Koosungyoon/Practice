#선택 정렬 


from operator import le


arr=[2,6,5,4,7,1,0,9,3,8]

for i in range(len(arr)):
    min_index=i #가장 작은수의 인덱스
    for j in range(i,len(arr)): # 좌측을 제외한 나머지중 가장 작은수의 인덱스를 min_index에 업데이트
        if arr[min_index]>arr[j]:
            min_index=j
    arr[min_index],arr[i]=arr[i],arr[min_index]
        
print(arr)

#삽입 정렬
 # 특정데이터를 적절한 위치에 삽입한다. 단 첫 번째 데이터는 이미 정렬  되었다고 판단하고 시작 

arr=[2,6,5,4,7,1,0,9,3,8]

for i in range(1,len(arr)):
    for j in range(i,0,-1):
        if arr[j]<arr[j-1]:  #좌측 정렬에서 하나하나 비교하면서 적절한 위치로 이동
            arr[j],arr[j-1]=arr[j-1],arr[j]
print(arr)

#퀵 정렬
    #피벗을 기준으로 좌측 우측 나누어짐 결국 파티션에 원소가 한개 남으면 정렬 끝
arr=[2,6,5,4,7,1,0,9,3,8]

def quick_sort(arr,start,end):
    if start>=end: #원소의 개수가 1개이면 종료
       return
    
    pivot=start
    left=start+1
    right=end

    while left<=right:
        #피벗보다 큰 데이터를 찾을 때까지 반복
        while left<=end and arr[left]<=arr[pivot]:
            left+=1
        #피벗보다 작은 데이터를 찾을 때까지 반복
        while right>start and arr[right]>=arr[pivot]:
            right-=1
        #엇갈렸다면 작은데이터와 피벗데이터 교환
        if left>right:
            arr[right],arr[pivot]=arr[pivot],arr[right]
        #그렇지 않다면 좌우 데이터 교환
        else:
            arr[left],arr[right]=arr[right],arr[left]
    #분할된 나머지들도 퀵 정렬로 정렬    
    quick_sort(arr,start,right-1)
    quick_sort(arr,right+1,end)

quick_sort(arr,0,len(arr)-1)
print(arr)






arr=[5,6,7,4,2,3,1,0,9,8]

def quick_sort(arr):
    if len(arr)<=1:
        return arr

    pivot=arr[0]
    tail=arr[1:]

    left_side=[x for x in tail if x<=pivot]
    right_side=[x for x in tail if x>pivot]

    return quick_sort(left_side)+pivot+quick_sort(right_side)

# 계수 정렬 구현

array=[5,7,9,0,3,1,6,2,4,8]
#모든 범위를 포함하는 리스트 선언(리스트 값은 0으로 초기화)
count=[0]*(max(array)+1) 

for i in range(len(array)):
    count[array[i]]+=1

for i in range(len(count)):
    for j in range(count[i]):
        print(i,end=' ')
    