#최대힙
from heapq import heappop,heappush
from sys import stdin
input=stdin.readline
x=int(input())
heap=[]
for _ in range(x):
    num=int(input())
    if num!=0:
        heappush(heap,(-num))
    else:
        if len(heap)==0:
            print(0)
        else:
           print(-1*heappop(heap))      


