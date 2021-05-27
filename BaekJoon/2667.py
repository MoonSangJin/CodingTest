#bfs
from collections import deque
n=int(input())
graph=[]
queue=deque()

for i in range(n):
    graph.append(list(map(int,list(input()))))

visited=[[False]*n for _ in range(n)]

def bfs(i,j):
    dx=[-1,1,0,0]
    dy=[0,0,-1,1]
    cnt=0

    queue.append((i,j))
    visited[i][j]=True

    while queue:
        a,b=queue.popleft()
        cnt+=1
        for i in range(4):
            nx=a+dx[i]
            ny=b+dy[i]
            if nx<0 or ny<0 or nx>=n or ny>=n:
                continue
            if graph[nx][ny]==1 and not visited[nx][ny]:
                visited[nx][ny]=True
                queue.append((nx,ny))
                graph[nx][ny]=0
    return cnt

temp=[]
total=0

for i in range(n):
    for j in range(n):
        if graph[i][j]==1:
            bfs_count=bfs(i,j)
            total+=1
            temp.append(bfs_count)
temp.sort()

#정답 출력
print(total)
for i in temp:
    print(i)