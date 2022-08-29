import sys
import heapq

INF=int(1e9)

v,e=map(int,sys.stdin.readline().strip().split())
start=int(sys.stdin.readline().strip())
graph=[[] for i in range(v+1)]

distance=[INF]*(v+1)
for _ in range(e):
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

dijkstra(start)
for i in range(1,v+1):
    if distance[i]==INF:
        print("INF")
    else:
        print(distance[i])           