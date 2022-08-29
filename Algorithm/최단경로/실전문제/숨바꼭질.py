'''
#다이나믹 프로그래밍?->BFS(너비 우선 탐색)

import sys
from collections import deque

n,k=map(int,sys.stdin.readline().strip().split())
q=deque()
q.append(n)

visited=[-1 for i in range(100001)]
visited[n]=0

while q:
    s=q.popleft()

    if s==k:
        print(visited[s])
        break
    if 0<=s-1<100001 and visited[s-1]==-1:
        visited[s-1]=visited[s]+1
        q.append(s-1)
    if 0<s*2<100001 and visited[s*2]==-1:
        visited[s*2]=visited[s]
        q.appendleft(s*2)
    if 0<=s+1<100001 and visited[s+1]==-1:
        visited[s+1]=visited[s]+1
        q.append(s+1)
    
'''

'''
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
'''
'''
BFS+우선순위 큐-> 다익스트라 
그래프의 형태는 아니지만 정점이 10만개 있는 다익스트라라고 생각하면 될 것 같다.
visited 라는 방문 체크 배열을 만들어두고, n부터 탐색을 진행한다.
탐색은 3방향으로, n-1, n+1, n*2 이다. 
visited의 인덱스 범위 배열을 넘어가지 않게 조건을 주고, 만약 정점 k에 도달했다면 시간을 출력하고 종료한다.

import sys
import heapq

n,k=map(int,sys.stdin.readline().strip().split())
visited=[False]*(100001)
visited[n]=True
hq=[(0,n)]

while hq:
    time,now=heapq.heappop(hq)
    if now==k:
        print(now)
        break
    dx=now*2
    if dx<100001 and not visited[dx]:
        visited[dx]=True
        heapq.heappush(hq,(time,dx))
    for i in (now+1,now-1):
        if 0<=i<100001 and not visited[i]:
            visited[i]=True
            heapq.heappush(hq,(time+1,i))
'''
#스스로 구현한 소스코드!
#핵심은 -> 100000개의 노드가 있다고 생각하고 간선은 i*2,i+1,i-1로 3개 있다고 생각하기
import sys,heapq
INF=int(1e9)
#수빈이와 수빈이 동생의 위치 입력
n,k=map(int,sys.stdin.readline().strip().split())
#최단 거리 테이블을 무한대로 초기화 
distance=[INF]*(100001)
#우선 순위 큐를 이용하기
q=[]
#시작 노드의 시간 0으로 하고 q에 삽입
distance[n]=0
heapq.heappush(q,(0,n))
while q:#q가 비어있지 않다면
    #시간,현재 노드 큐에서 빠짐-> 우선 순위 큐에서 원소가 빠져나온다.
    time,now=heapq.heappop(q)
    #만약 현재노드와 동생의 위치가 같다면->time을 출력하고 반복문을 빠져나온다.
    if now==k:
        print(time)
        break
    #방문한 노드라면 넘어가기
    if distance[now]<time:
        continue
    #우선적으로 0초가 걸리는 now*2 부터 확인하기-> now*2가 100000이하이고 방문한적이 없다면
    if now*2<100001 and distance[now*2]==INF:
        distance[now*2]=time
        heapq.heappush(q,(time,now*2))
    #나머지 now+1,now-1 간선을 살펴본다.
    for i in (now+1,now-1):
        if 0<=i<100001 and distance[i]==INF:
            distance[i]=time+1
            heapq.heappush(q,(time+1,i))
    

        


