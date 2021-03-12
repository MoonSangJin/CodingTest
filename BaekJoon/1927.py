#우선순위큐, 힙
from heapq import heappop,heappush
from sys import stdin
input=stdin.readline
n=int(input())
data=[]
for _ in range(n):
    a=int(input())
    if a==0:
        if len(data)==0:
            print(0)
        else:
            print(data[0])
            heappop(data)     
    else:
        heappush(data,a)

