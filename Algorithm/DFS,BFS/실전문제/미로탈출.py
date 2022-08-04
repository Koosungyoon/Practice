#미로 탈출 
#BFS를 이용하여 괴물을 피해서 최단거리를 구한다.

'''
sol)바로 주변의 상황을 판단해야 하므로 너비 우선 탐색을 이용하여 해결할 것이다. 
    시작 위치의 4방향(상하좌우)를 살펴볼 것이다. 큐에서 현재 위치(x,y)를 꺼내고 주변 노드를 살핀다.
    1)공간을 넘어간다.-> 무시한다.(continue)
    2)0인경우-> 무시한다.(continue)
    3)1인경우-> graph[nx][ny]=grpah[x][y]+1 해주고 큐에(nx,ny)를 삽입해준다.

    큐가 빌때 까지 반복한다.(while문을 통해서) 

'''
from collections import deque

#n,m크기를 받는다.
n,m=map(int,input().split())
#미로의 정보를 그래프로 담는다.
graph=[]
for i in range(n):
    graph.append(list(map(int,input())))

#상하좌우 표현
dx=[-1,1,0,0]
dy=[0,0,-1,1]

def bfs(x,y):
    queue=deque()
    queue.append((x,y))
    #큐가 빌 때까지
    while queue:
        x,y=queue.popleft()
        #현재위치에서 상 하 좌 우 살펴보기!
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            #미로 찾기 공간을 벗어난 경우 무시
            if nx<0 or ny<0 or nx>=n or ny>=m:
                continue
            # 괴물이 있는 경우 무시
            if graph[nx][ny]==0:
                continue
            # 해당 노드를 처음 방문하는 경우에만 최단 거리 기록
            if graph[nx][ny]==1:
                graph[nx][ny]=graph[x][y]+1
                queue.append((nx,ny))
    #가장 오른쪽 아래까지의 최단 거리 반환 
    return graph[n-1][m-1]

#BFS를 수행한 결과 출력 
print(bfs(0,0))


