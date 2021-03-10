#해쉬
from sys import stdin

n,m=map(int,stdin.readline().split())
dic={}

for i in range(1,n+1):
    key=stdin.readline().rstrip()
    dic[key]=i
    dic[i]=key

for j in range(m):
    data=stdin.readline().rstrip()
    if data.isdigit():
        print(dic[int(data)])
    elif data.isalpha():
        print(dic[data])    
