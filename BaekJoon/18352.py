#bfs
#그래프에서 모든 간선의 비용이 동일하면 BFS 사용한다.
# 입력 값에 따라 visited 사용 유무 결정 
from collections import deque

n,m,k,x=map(int,input().split())
graph=[[] for _ in range(n+1)]

for _ in range(m):
    a,b=map(int,input().split())
    graph[a].append(b)

distance=[-1]*(n+1)
distance[x]=0

q=deque([x]) #이부분 중요, 첫 시작 점을 queue에 넣는다.

while q:
    now=q.popleft()
    for next_node in graph[now]:
        if distance[next_node]==-1: #-1이면 아직 방문안 한 것
            distance[next_node]=distance[now]+1 #한번만 이동한게 최소길이다.
            q.append(next_node)

check=False
for i in range(1,n+1):
    if distance[i]==k:
        print(i)
        check=True
if check==False:
    print(-1)                  

