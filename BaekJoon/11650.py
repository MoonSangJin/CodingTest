n=int(input())
data=[]
for _ in range(n):
    a,b=map(int,input().split())
    data.append((a,b))

data.sort(key=lambda x:x[1])
data.sort(key=lambda x:x[0])

for i in data:
    print(i[0],i[1])
    