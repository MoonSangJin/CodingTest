#이중우선순위큐,최대힙,최소힙
from heapq import heappop,heappush,nlargest,nsmallest
from sys import stdin
input=stdin.readline

t=int(input())

def sync(h,visited):
    while h and not visited[h[0][1]]:
        heappop(h)

for _ in range(t):        
    visited=[False]*1000000
    max_heap,min_heap=[],[]

    k=int(input())
    for key in range(k):
        cal,num=input().split()
        num=int(num)
        if cal=='I':
            heappush(max_heap,(-1*num,key))
            heappush(min_heap,(num,key))
            visited[key]=True
        elif cal=='D':
            if num==1:
                sync(max_heap,visited)
                if max_heap:
                    visited[max_heap[0][1]]=False
                    heappop(max_heap)
            else:
                sync(min_heap,visited)
                if min_heap:
                    visited[min_heap[0][1]]=False
                    heappop(min_heap)        
    sync(max_heap,visited)
    sync(min_heap,visited)

    if max_heap:
        print(-1*max_heap[0][0], min_heap[0][0])
    else:
        print("EMPTY")




# for _ in range(t):
#     heap=[]
#     k=int(input())
#     for _ in range(k):
#         cal,num=input().split()
#         num=int(num)
#         if cal=='I':
#             heappush(heap,num)
#         elif cal=='D':
#             if len(heap)==0:
#                 continue
#             else:
#                 if num==1:
#                     heap.pop(heap.index(nlargest(1,heap)[0]))
#                 else:
#                     heappop(heap)

#     if len(heap)==0:
#         print('EMPTY')
#     else:
#         print(nlargest(1,heap)[0],nsmallest(1,heap)[0])                   

