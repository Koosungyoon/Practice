#크루스칼 알고리즘을 이용하여 최소 신장 트리 구하기
'''
1.간선들을 모두 오름차순으로 정렬
2.간선을 하나 하나 확인하며 -> 특정 노드의 집합이 같은지 확인하는데 같으면 -> 사이클을 발생할 수있으닌 포함시키지 않는다.
                                                                다르면 -> 포함시킨다.
'''
import sys

#특정 원소가 속한 집합을 찾기
def find_parent(parent,x):
    #루트 노드가 아니라면, 루트 노드를 찾을 때까지 재귀적으로 호출
    if parent[x]!=x:
        #단순하게 parent테이블은 노드의 부모노드를 기록하는 것이므로->재귀적으로 부모 노드의 부모 노드를 찾는다고 생각하자!
        parent[x]=find_parent(parent,parent[x])
    return parent[x]
#두 원소가 속한 집합을 합치기
def union_parent(parent,a,b):
    a=find_parent(parent,a)
    b=find_parent(parent,b)
    if a<b:
        parent[b]=a
    else:
        parent[a]=b
    
#노드의 개수와 간선(union 연산)의 개수 입력 받기
v,e=map(int,sys.stdin.readline().strip().split())
parent=[0]*(v+1)

#모든 간선을 담을 리스트와 최종 비용을 담을 변수
edges=[]
result=0

#부모 테이블 각각 자기 자신으로 초기화
for i in range(1,v+1):
    parent[i]=i

#모든 간선에 대한 정보를 입력 받기
for _ in range(e):
    a,b,cost=map(int,sys.stdin.readline().strip().split())
    #비용순으로 정렬하기 위해서 튜플의 첫 번째 원소를 비용으로 설정
    edges.append((cost,a,b))

#간서늘 비용순으로 정렬
edges.sort()

#간선을 하나씩 확인하며
for edge in edges:
    cost,a,b = edge
    #사이클이 발생하지 않는 경우만 집합에 포함
    if find_parent(parent,a)!=find_parent(parent,b):
        union_parent(parent,a,b)
        result+=cost
    
print(result)