#그리디,정렬,우선순위큐,힙
from heapq import heappop,heappush
n=int(input())
data=[]
for _ in range(n):
    heappush(data,int(input()))
result=0
while len(data)!=1:
    a=heappop(data)
    b=heappop(data)
    result+=a+b
    heappush(data,a+b)
print(result)