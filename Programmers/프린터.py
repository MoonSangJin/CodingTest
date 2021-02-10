def solution(priorities, location):
    answer = 0
    from collections import deque
    
    d=deque([(v,i) for i,v in enumerate(priorities)])
    print(max(d))
    while len(d):
        item=d.popleft() #가장 왼쪽에서 뽑아낸게 아이템
        if d and max(d)[0]>item[0]: #리스트에 1개만 있으면 뽑는순간 d가 0이 되니까 안돌아감
            d.append(item)
        else:
            answer+=1   #순서하나씩 증가
            if item[1]==location: #인덱스가 찾으려는 인덱스와 같은거면
                break
    return answer