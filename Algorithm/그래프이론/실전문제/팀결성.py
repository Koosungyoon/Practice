import sys

n,m=map(int,sys.stdin.readline().strip().split())
#특정원소가 속한 집합
def find_parent(parent,x):
    if parent[x]!=x:
        parent[x]=find_parent(parent,parent[x])
    return parent[x]

#팀 합치기 
def union_parent(parent,a,b):
    a=find_parent(parent,a)
    b=find_parent(parent,b)
    if a<b:
        parent[b]=a
    else:
        parent[a]=b

parent=[0]*(n+1)
#부모 테이블 자기 자신으로 초기화
for i in range(1,n+1):
    parent[i]=i

for _ in range(m):
    x,y,z=map(int,sys.stdin.readline().strip().split())
    if x==0:
        union_parent(parent,y,z)
    else:
        if find_parent(parent,y)==find_parent(parent,z):
            print("yes")
        else:
            print("no")
