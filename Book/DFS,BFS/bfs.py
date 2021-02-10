from collections import deque

def bfs(graph,start,visited):
  queue=deque([start])
  visited[start]=True #현재 노드 방문처리
  while queue: #큐가 빌때까지 반복
    v=queue.popleft()
    print(v,end=' ')
    for i in graph[v]:
      if not visited[i]:
        queue.append(i)
        visited[i]=True

graph=[
  [], #0번째 노드는 없고 노드는 1번째부터 시작하니까
  [2,3,8],
  [1,7],
  [1,4,5],
  [3,5],
  [3,4],
  [7],
  [2,6,8],
  [1,7]
]        

visited=[False]*9

bfs(graph,1,visited)