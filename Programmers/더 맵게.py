#heap,힙,최소힙
from heapq import heappop,heappush
def solution(scoville, K):
    answer = 0
    cnt=0
    heap=[]
    for i in scoville:
        heappush(heap,i)
    while True:
        if len(heap)==2 and heap[0]+(heap[1]*2)<K:
                return -1
        minimum1=heappop(heap)
        minimum2=heappop(heap)
        heappush(heap,minimum1+(minimum2*2))
        cnt+=1
        for i in range(len(heap)):
            if heap[i]>=K:
                check=True
                if i==len(heap)-1 and check:
                    answer=cnt
                    return answer
            else:
                check=False
                break
    return answer