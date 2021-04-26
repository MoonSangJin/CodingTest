#dfs 기본 
import sys
sys.setrecursionlimit(10000)

n,m=map(int,input().split())
graph=[[] for _ in range(n+1)]
visited=[False]*(n+1)
for i in range(m):
    a,b=map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)
cnt=0

def dfs(graph,v,vistied):
    vistied[v]=True
    for i in graph[v]:
        if not visited[i]:
            dfs(graph,i,visited)
    
for i in range(1,n+1):
    if visited[i]==False:
        dfs(graph,i,visited)
        cnt+=1

print(cnt)