#bfs
from collections import deque

n,k=map(int,input().split())

q=deque()
check=[-1 for i in range(100001)]
q.append((n,0))   #튜플로 tree의 깊이 까지 넣어준다.
check[n]=0
while q:
    data,cnt=q.popleft()
    for next in (data-1,data+1,data*2):
        if 0<=next<=100000 and check[next]==-1:
            q.append((next,cnt+1))
            check[next] = cnt+1

print(check[k])            


