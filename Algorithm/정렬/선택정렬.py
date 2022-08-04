#선택 정렬 구현
'''
!!매번 가장 작은 것을 선택한다.!!
'''
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
