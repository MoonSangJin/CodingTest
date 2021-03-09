from collections import deque

n,k=map(int,input().split())

data=deque(list(range(1,n+1)))

i=0
answer=[]
while len(data)!=0:
    i+=1
    if i==k:
        answer.append(data.popleft())
        i=0
    else:
        data.append(data.popleft())

print('<',end='')
for i in range(len(answer)-1):
    print(answer[i],end=', ')
print(answer[-1],end='')    
print('>')    