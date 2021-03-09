#hash
from sys import stdin
n=int(stdin.readline())
data=list(map(int,stdin.readline().split()))

m=int(stdin.readline())
find=list(map(int,stdin.readline().split()))

answer=[]

dic={}

for i in data:
    if i in dic:
        dic[i]+=1
    else:
        dic[i]=1


for i in find:
     print(dic[i],end=' ') if i in dic else print(0,end=' ')
       