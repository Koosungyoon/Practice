import sys
INF=int(1e9)

#노드의 개수, 간선의 개수를 입력 받기
n,m=map(int,sys.stdin.readline().strip().split())
#시작 노드 번호를 입력 받기
start=int(sys.stdin.readline().strip())
#각 노드에 연결되어 있는 노드에 대한 정보를 담는 리스트를 만들기
graph=[[] for i in range(n+1)]
#방문한 적이 있는지 체크하는 목적의 리스트를 만들기
visited=[False]*(n+1)
#최단 거리 테이블을 모두 무한으로 초기화
distance=[INF]*(n+1)

for _ in range(m):
    a,b,c=map(int,sys.stdin.readline().strip().split())
    # a번 노드에서 b번 노드로 가는 비용이 c라는 의미
    graph[a].append((b,c))

# 방문하지 않은 노드 중에서, 가장 최단 거리가 짧은 노드의 번호를 반환
def get_smallest_node():
    min_value=INF
    index=0 #가장 최단 거리가 짧은 노드(인덱스)
    for i in range(1,n+1):
        if distance[i]<min_value and not visited[i]:
            min_value=distance[i]
            index=i
    return index