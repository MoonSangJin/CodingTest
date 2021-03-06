n=int(input())
data=[]
for _ in range(n):
    data.append(input())

for i in data:
    cnt=0
    for j in i:
        if j=='(':
            cnt+=1 
        if j==')':
            cnt-=1
        if cnt<0:
            break    
    if cnt==0:
        print('YES')
    else:
        print('NO')            