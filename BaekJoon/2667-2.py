#dfs로 바꿔 풀이
n=int(input())
graph=[]

for i in range(n):
    graph.append(list(map(int,list(input()))))

visited=[[False]*n for _ in range(n)]
cnt=0

def dfs(i,j):
    global cnt
    if i<0 or j<0 or i>=n or j>=n:
        return False
    if graph[i][j]==1 and not visited[i][j]:
        visited[i][j]=True
        graph[i][j]=0
        cnt+=1
        dfs(i-1,j)
        dfs(i+1,j)
        dfs(i,j-1)
        dfs(i,j+1)
        return True
    return False

temp=[]
total=0

for i in range(n):
    for j in range(n):
        if dfs(i,j):
            total+=1
            temp.append(cnt)
            cnt=0
temp.sort()

#정답 출력
print(total)
for i in temp:
    print(i)