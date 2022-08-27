from math import dist
import sys

#n,m은 각각 노드의 수와 간선의 수이다.
n,m=map(int,sys.stdin.readline().strip().split())
INF=int(1e9)
start=int(sys.stdin.readline().strip())
#노드의 상황을 그래프로 표현
graph=[[] for _ in range(n)]
#최단 거리 테이블
distance=[INF]*(n+1)
#방문했는지 확인하는 테이블
visited=[False]*(n+1)

for i in range(m+1):
    a,b,c=map(int,sys.stdin.readline().strip().split())
    graph[a].append((b,c))

def get_smallest_node():
    min_value=INF
    index=0
    
    for i in range(1,n+1):
        if distance[i]<min_value and not visited[i]:
            min_value=distance[i]
            index=i
    return index


def dijkstra(start):
    distance[start]=0
    visited[start]=True
    for i in graph[start]:
        distance[i[0]]=i[1]

    for j in range(n-1):
        now=get_smallest_node()
        visited[now]=True
        for i in graph[now]:
            cost=distance[now]+graph[i[1]]
            if cost<distance[i[0]]:
                distance[i[0]]=cost

        