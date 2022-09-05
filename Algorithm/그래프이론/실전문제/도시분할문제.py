import sys

def find_parent(parent,x):
    if parent[x]!=x:
        parent[x]=find_parent(parent,parent[x])
    return parent[x]

def union_parent(parent,a,b):
    a=find_parent(parent,a)
    b=find_parent(parent,b)
    if a<b:
        parent[b]=a
    else:
        parent[a]=b

edges=[]
result=0

n,m=map(int,sys.stdin.readline().strip().split())
parent=[0]*(n+1)
for i in range(1,n+1):
    parent[i]=i

for _ in range(m):
    a,b,c=map(int,sys.stdin.readline().strip().split())
    edges.append((c,a,b))

edges.sort()
last=0
for edge in edges:
    c,a,b=edge
    if find_parent(parent,a)!=find_parent(parent,b):
        union_parent(parent,a,b)
        result+=c
        last=c

print(result-last)
