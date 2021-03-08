#dfs,bfs 개념
from collections import deque

n,m,v=map(int,input().split())
graph=[[] for _ in range(n+1)]

for _ in range(m):
    a,b=map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(len(graph)):
    graph[i].sort()     #정점 번호가 작은 것을 먼저 방문하므로 sort해준다

visited_dfs=[False]*(n+1)
visited_bfs=[False]*(n+1)

def dfs(graph,v,visited_dfs):
    visited_dfs[v]=True
    print(v,end=' ')

    for i in graph[v]:
        if not visited_dfs[i]:
            dfs(graph,i,visited_dfs)

def bfs(graph,v,visited_bfs):
    queue=deque([v])
    visited_bfs[v]=True

    while queue:
        a=queue.popleft()
        print(a,end=' ')
        for i in graph[a]:
            if not visited_bfs[i]:
                queue.append(i)
                visited_bfs[i]=True

dfs(graph,v,visited_dfs)
print()
bfs(graph,v,visited_bfs)            

    