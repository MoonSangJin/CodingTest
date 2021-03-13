#stack
no_message=False
stack=[]
answer=[]
cnt=0
n=int(input())
for _ in range(n):
    x=int(input())
    while cnt<x:
        cnt+=1
        stack.append(cnt)
        answer.append('+')
    if stack[-1]==x:
        answer.append('-')
        stack.pop()
    else:
        no_message=True
        break

if no_message==True:
    print('NO')
else:
    for i in answer:
        print(i)   
