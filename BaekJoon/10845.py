from collections import deque
from sys import stdin

q=deque([])

n=int(stdin.readline())

for _ in range(n):
    order=list(stdin.readline().split())
    if order[0]=='push':
        q.append(order[1])
    elif order[0]=='pop':
        print(q.popleft()) if len(q)!=0 else print(-1)
    elif order[0]=='size':
        print(len(q))
    elif order[0]=='empty':
        print(1) if len(q)==0 else print(0)
    elif order[0]=='front':
        print(q[0]) if len(q)!=0 else print(-1)
    elif order[0]=='back':
        print(q[len(q)-1]) if len(q)!=0 else print(-1)
        
    