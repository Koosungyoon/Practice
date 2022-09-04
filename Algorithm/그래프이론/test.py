#서로소 집합 자료구조 구현

import sys
sys.stdin.readline().strip()
#특정 원소가 속한 집합을 찾기
def find_parent(preant,x):
    if parent[x]!=x:
        return find_parent(parent,parent[x])
    return x
#union 연산 
def union_parent(parent,a,b):
    a=find_parent(parent,a)
    b=find_parent(parent,b)
    if a<b:
        parent[b]=a
    else:
        parent[a]=b

v,e=map(int,sys.stdin.readline().strip().split())
parent=[0]*(v+1)
#루트노드를 자기 자신으로 우선 초기화
for i in range(1,v+1):
    parent[i]=i
#union 연산 입력 받기
for i in range(e):
    a,b=map(int,sys.stdin.readline().strip().split())
    union_parent(parent,a,b)

#각 원소가 속한 집합 출력
print("각 원소가 속한 집합",end='')
for i in range(1,v+1):
    print(find_parent[i],end=' ')
print()
print("부모 테이블: ",end='')
for i in range(1,v+1):
    print(parent[i],end=' ')