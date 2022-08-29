#플로이드 워셜 알고리즘으로 풀이하자!
import sys

INF=int(1e9)
n,m=map(int,sys.stdin.readline().strip().split())

graph=[[INF]*(n+1) for _ in range(n+1)]
for a in range(n+1):
    for b in range(n+1):
        if a==b:
            graph[a][b]=0
#연결되어 있는 두 회사의 정보를 그래프에 갱신
for _ in range(m):
    a,b=map(int,sys.stdin.readline().strip().split())
    graph[a][b]=1
    graph[b][a]=1
x,k=map(int,sys.stdin.readline().strip().split())

for i in range(1,n+1):
    for a in range(1,n+1):
        for b in range(1,n+1):
            graph[a][b]=min(graph[a][b],graph[a][i]+graph[i][b])

distance=graph[1][k]+graph[k][x]

if distance>=INF:
    print(-1)
else:
    print(distance) 