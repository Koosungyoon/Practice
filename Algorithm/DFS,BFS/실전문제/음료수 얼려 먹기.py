#N*M크기의 얼음 틀이 주어진다. 0은 구멍이 뚫려 있는 부분이고, 1은 칸막이가 존재하는 부분이다. 
#상하좌우로 붙어 있는 경우 서로 연결되어 있는 것으로 간주한다. 
#이때 얼음 틀의 모양이 주어질 떄 생성되는 총 아이스크림의 개수를 구하라.

 #아무리 0이어도 이미 방문한 곳은 False이므로 카운트 되지 않는다. 이 점을 유의하고 코드를 작성 하자.

n,m=map(int,input().split())

graph=[]
for i in range(n):
    graph.append(list(map(int,input()))) #append 함수에는 한 가지 요소만 들어갈 수 있으니까 split()함수를 사용하지 않구나!

#DFS로 특정한 노드를 방문한 뒤에 연결된 모든 노드들도 방문
def dfs(x,y):
    if x<=-1 or x>=n or y<=-1 or y>=m:
        return False
    if graph[x][y]==0:
        #해당 노드 방문 처리
        graph[x][y]=1
        #해당 노드의 상, 하, 좌, 우의 위치도 모두 재귀적으로 호출
        dfs(x-1,y)
        dfs(x+1,y)
        dfs(x,y-1)
        dfs(x,y+1)
        return True
    return False

result=0
for i in range(n):
    for j in range(m):
        if dfs(i,j)==True:
            result+=1
            print(i,j,"=",dfs(i,j))

print(result)