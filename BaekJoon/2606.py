#dfs (입력 두개씩 들어오는것)
n=int(input())
pair=int(input())
graph=[[] for _ in range(n+1)]

for _ in range(pair):
    a,b=map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)
 
visited=[False]*(n+1)
answer=[]

def dfs(graph,v,visited):
    visited[v]=True
    answer.append(v)
    for i in graph[v]:
        if not visited[i]:
            dfs(graph,i,visited)

dfs(graph,1,visited)            
print(len(answer)-1)