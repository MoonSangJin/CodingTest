#dp
n=int(input())
data=[]
for _ in range(n):
    t,p=map(int,input().split())
    data.append((t,p))
temp=[]

for i in range(len(data)):
    nextday=0
    cost=0
    day=0
    while nextday<=n:
        nextday+=data[nextday][0]
        cost+=data[nextday][1]
    temp.append(cost)
print(temp)