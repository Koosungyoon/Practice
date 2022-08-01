#스택 자료구조를 기초하여 DFS구현

def dfs(graph,v,visited):
    #현재노드 방문 처리
    visited[v]=True
    #인접한 노드의 방문 확인하려고!
    for i in graph[v]:
        if not visited[i]:
            dfs(graph,i,visited)