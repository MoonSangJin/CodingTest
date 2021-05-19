from collections import deque
def solution(cacheSize, cities):
    answer = 0
    queue=deque([])
    new_city=[]
    for i in cities:
        new_city.append(i.lower())

    for i in range(len(new_city)):
        if cacheSize==0:
            return len(new_city)*5

        if cacheSize==len(queue):
            if new_city[i] in queue:
                answer+=1
                temp=new_city[i]
                queue.remove(temp)
                queue.append(temp)
            else:
                answer+=5
                queue.popleft()
                queue.append(new_city[i])
        else:
            if new_city[i] in queue:
                answer+=1
                temp=new_city[i]
                queue.remove(temp)
                queue.append(temp)
            else:
                answer+=5
                queue.append(new_city[i])
    return answer


#모범풀이 deque의 maxlen을 지정해버리면 초과시 자동으로 맨 앞에꺼 삭제함
def solution(cacheSize, cities):
    cache = deque(maxlen=cacheSize)
    time = 0
    for i in cities:
        s = i.lower()
        if s in cache:
            cache.remove(s)
            cache.append(s)
            time += 1
        else:
            cache.append(s)
            time += 5
    return time