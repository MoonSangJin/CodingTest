n=int(input())
data=[]
for _ in range(n):
    age,name=input().split()
    data.append((int(age),name))
answer=sorted(data,key=lambda x:x[0])

for i in answer:
    print(i[0],i[1])    