import sys
import heapq

INF=int(1e9)

v,e=map(int,sys.stdin.readline().strip().split())
#start=int(sys.stdin.readline().strip())
graph=[[] for i in range(v+1)]

for _ in range(e):
    a,b,c=map(int,sys.stdin.readline().strip().split())
    graph[a].append((b,c))
    graph[b].append((a,c))

v1,v2=map(int,sys.stdin.readline().strip().split())

def dijkstra(start,a):
    dp=[INF for i in range(v+1)]
    q=[]
    heapq.heappush(q,(0,start))
    dp[start]=0
    while q:
        dist,now=heapq.heappop(q)
        if dp[now]<dist:
            continue
        for i in graph[now]:
            cost=dist+i[1]
            if cost<dp[i[0]]:
                dp[i[0]]=cost
                heapq.heappush(q,(cost,i[0]))
    
    return dp[a]

a_val=dijkstra(1,v1)+dijkstra(v1,v2)+dijkstra(v2,v)

b_val=dijkstra(1,v2)+dijkstra(v2,v1)+dijkstra(v1,v)
res=min(a_val,b_val)

if res<INF:
    print(res)
else:
    print(-1)
          