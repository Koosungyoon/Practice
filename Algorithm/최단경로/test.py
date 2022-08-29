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


#개선된 다익스트라 최단 경로 알고리즘 소스코드
import sys
import heapq
INF=int(1e9)

n,m=map(int,sys.stdin.readline().strip().split())
start=int(sys.stdin.readline().strip())

graph=[[] for i in range(n+1)]
distance=[INF]*(n+1)
visited=[False]*(n+1)

for _ in range(m+1):
    a,b,c=map(int,sys.stdin.readline().strip().split())
    graph[a].append((b,c))

def dijkstra(start):
    q=[]
    heapq.heappush(q,(0,start))
    distance[start]=0
    while q:
        dist,now=heapq.heappop(q)
        if distance[now]<dist:
            continue
        for i in graph[now]:
            cost=dist+i[1]
            if cost<distance[i[0]]:
                distance[i[0]]=cost
                heapq.heappush(q,(cost,i[0]))











from collections import deque

n, k = map(int, input().split())  # n: 수빈이가 있는 위치, k: 동생이 있는 위치
q = deque()
q.append(n) 
visited = [-1 for _ in range(100001)]
visited[n] = 0

while q:
    s = q.popleft()
    if s == k:
        print(visited[s])
        break
    if 0 <= s-1 < 100001 and visited[s-1] == -1:
        visited[s-1] = visited[s] + 1
        q.append(s-1)
    if 0 < s*2 < 100001 and visited[s*2] == -1:
        visited[s*2] = visited[s]
        q.appendleft(s*2)  # 2*s 가 다른 연산보다 더 높은 우선순위를 가지기 위함
    if 0 <= s+1 < 100001 and visited[s+1] == -1:
        visited[s+1] = visited[s] + 1
        q.append(s+1)
