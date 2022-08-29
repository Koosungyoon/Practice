#최단 거리를 구하는 문제로 치환해서 풀면 간단하다.
#자료의 양이 많으므로 힙 자료구조를 사용하여 다익스트라 알고리즘으로 풀이한다.
import sys
import heapq
INF=int(1e9)

#n,m,c는 차례대로 도시의 개수 통로의 개수 메시지를 보내고자 하는 도시
n,m,c=map(int,sys.stdin.readline().strip().split())
#각 노드에 연결되어 있는 간선을 저장하기 위함
graph=[[] for i in range(n+1)]
#c라는 노드에서 출발하여 다른 노드로의 시간을 저장하는 거리 테이블 초기화
distance=[INF]*(n+1)

for i in range(m):
    #x에서 y로 가는데 걸리는 시간 z라 표현
    x,y,z=map(int,sys.stdin.readline().strip().split())
    graph[x].append((y,z))

def dijkstra(start):
    q=[]
    heapq.heappush(q,(0,start))
    distance[start]=0
    while q:
        #가장 최단 거리가 짧은 노드에 대한 정보를 꺼내기
        dist,now=heapq.heappop(q)
        if distance[now]<dist:
            continue
        #now와 연결되어있는 간선을 확인한다.
        for i in graph[now]:
            cost=dist+i[1]
            if cost<distance[i[0]]:
                distance[i[0]]=cost
                heapq.heappush(q,(cost,i[0]))
    
dijkstra(c)
'''
help=(len(distance)-distance.count(INF))
time=0
for i in range(1,n+1):
    if distance[i]!=INF and time<=distance[i]:
        time=distance[i]
print(help,time)
'''
count=0
max_distance=0
for d in distance:
    if d!=INF:
        count+=1
        max_distance=max(max_distance,d)
print(count-1,max_distance)