#bfs
from collections import deque
n=int(input())
graph=[[] for _ in range(n+1)]

for i in range(n):
    data=list(map(int,input().split()))
    index=data[0]
    data=data[1:-1]
    for i in range(0,len(data),2):
        graph[index].append((data[i],data[i+1]))

def bfs(start):
    q = deque()
    q.append((start,0))
    dis = [-1] * (n + 1) # -1은 아직 방문하지 않은 곳
    dis[start] = 0
    while q:
        v,now_cost = q.popleft()
        for to,new_cost in graph[v]:
            if dis[to] == -1:  # 방문하지 않은 곳 거리값으로 수정
                dis[to] = now_cost + new_cost
                q.append((to,dis[to]))
    ans = max(dis) # start로부터 최대 거리에 있는 노드와의 거리
    idx = dis.index(ans) # start로부터 최대 거리에 있는 노드 번호
    print(dis,idx)
    return ans, idx
    
ans = bfs(1)[1] # 임의의 노드에서 최대 거리에 있는 노드 v 찾기
ans = bfs(ans)[0] # v와 u사이의 거리

print(ans)