#bfs (동시에 여러 위치에서 bfs돌릴수 있는 구조)
from collections import deque

m,n=map(int,input().split())
graph=[]
queue=deque()

for i in range(n):
    graph.append(list(map(int, input().split())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs():
    days=0    
    while queue:
        days+=1 #한번 퍼져나갈때마다 하루씩 증가
        for _ in range(len(queue)): #이 for문 의미 => bfs를 동시에 돌려야됨
            x,y=queue.popleft() 
            for i in range(4):
                nx = x+dx[i]
                ny = y+dy[i]
                if nx < 0 or ny < 0 or nx >= n or ny >= m: #범위 벗어나는거면 무시
                    continue
                if graph[nx][ny] == 0: #익을 수 있는 부분이면
                    graph[nx][ny]=1 #익혀
                    queue.append((nx,ny))
    return days


all_check=True
for i in range(n):
    for j in range(m):
        if graph[i][j]==0:
            all_check=False

if all_check:
    print(0)
    exit()

for i in range(n):
        for j in range(m):
            if graph[i][j]==1:
                queue.append((i,j))
result=bfs()-1

all_check=True
for i in range(n):
    for j in range(m):
        if graph[i][j]==0:
            all_check=False

if not all_check:
    print(-1)
else:
    print(result)

