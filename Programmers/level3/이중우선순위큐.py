from heapq import heappush,heappop
def solution(operations):
    min_heap=[]
    max_heap=[]
    for i in operations:
        command,data=i.split(' ')
        if command == 'I':
            data=int(data)
            heappush(min_heap,data)
            heappush(max_heap,(data*-1,data))
        elif command == 'D':
            if len(min_heap)==0:
                pass
            elif data=='1':
                max_value=heappop(max_heap)[1]
                min_heap.remove(max_value)
            elif data=='-1':
                min_value=heappop(min_heap)
                max_heap.remove((min_value*-1,min_value))
                
    if min_heap:
        return [heappop(max_heap)[1],heappop(min_heap)]
    else:
        return [0,0]