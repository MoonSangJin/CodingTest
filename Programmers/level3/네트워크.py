#dfs
def solution(n, computers):
    answer = 0
    graph=[[] for _ in range(n)]
    visited=[False]*n
    print(graph,visited)
    for i in range(n):
        for j in range(n):
            if i!=j and computers[i][j]==1:
                graph[i].append(j)
    def dfs(graph,v,visited):
        visited[v]=True
        for i in graph[v]:
            if not visited[i]:
                dfs(graph,i,visited)

    for i in range(n):
        if visited[i]==False:
            dfs(graph,i,visited)
            answer+=1
        
    return answer