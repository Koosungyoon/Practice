# import sys
# import heapq

# input = sys.stdin
#time out
# n = int(input.readline().strip())
# res = []
# for i in range(n):
#     num = int(input.readline().strip())
#     res.append(num)
#     res.sort()
#     print(res[i//2])
# n = int(input.readline().strip())

# leftheap = []
# rightheap = []
# res = []
# for i in range(n):
#     num = int(input.readline().strip())

#     if len(leftheap) == len(rightheap):
#         heapq.heappush(leftheap,(-num,num))
#     else:
#         heapq.heappush(rightheap,(num,num))
    
#     if rightheap and leftheap[0][1] > rightheap[0][0]:
#         min = heapq.heappop(rightheap)[0]
#         max = heapq.heappop(leftheap)[1]
#         heapq.heappop(leftheap,(-min,min))
#         heapq.heappop(rightheap,(max,max))
    
#     res.append(leftheap[0][1])

# for j in res:
#     print(j)
    
'''
최대 힙 만들기

파이썬의 heapq 모듈은 최소 힙으로 구현되어 있기 때문에 최대 힙 구현을 위해서는 트릭이 필요하다.

IDEA: y = -x 변환을 하면 최솟값 정렬이 최댓값 정렬로 바뀐다.

힙에 원소를 추가할 때 (-item, item)의 튜플 형태로 넣어주면 튜플의 첫 번째 원소를 우선순위로 힙을 구성하게 된다.  이때 원소 값의 부호를 바꿨기 때문에, 최소 힙으로 구현된 heapq 모듈을 최대 힙 구현에 활용하게 되는 것이다.

아래의 예시는 리스트 heap_items에 있는 원소들을 max_heap이라는 최대 힙 자료구조로 만드는 코드이다.

'''

import heapq
import sys

n = int(sys.stdin.readline())

leftHeap = []
rightHeap = []
for i in range(n):
    num = int(sys.stdin.readline())

    if len(leftHeap) == len(rightHeap):
        heapq.heappush(leftHeap, -num)
    else:
        heapq.heappush(rightHeap, num)

    if rightHeap and rightHeap[0] < -leftHeap[0]:
        leftValue = heapq.heappop(leftHeap)
        rightValue = heapq.heappop(rightHeap)

        heapq.heappush(leftHeap, -rightValue)
        heapq.heappush(rightHeap, -leftValue)

    print(-leftHeap[0])