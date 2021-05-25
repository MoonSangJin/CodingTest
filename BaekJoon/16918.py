from collections import deque

r,c,n=map(int,input().split())
dx=[1,-1,0,0]
dy=[0,0,1,-1]
queue=deque()
graph=[]

def install():
    for i in range(r):
        for j in range(c):
            if graph[i][j]=='.':
                graph[i][j]='O'
            elif graph[i][j]=='O':
                queue.append((i,j))

def bomb():
    while queue:
        a,b=queue.popleft()
        graph[a][b]='.'
        for i in range(4):
            nx=a+dx[i]
            ny=b+dy[i]
            if nx<0 or ny<0 or nx>=r or ny>=c:
                continue
            else:
                graph[nx][ny]='.'

for i in range(r):
    graph.append(list(input()))

for i in range(r):
    for j in range(c):
        if graph[i][j]=='O':
            queue.append((i,j))
n-=1

while n:
    n-=1
    install()
    if n==0:
        break
    n-=1
    bomb()
    

for i in range(r):
    for j in range(c):
        print(graph[i][j],end='')
    print()