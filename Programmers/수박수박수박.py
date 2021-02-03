def solution(n):
    answer = ''
    data=[0]*(n+1)
    for i in range(len(data)):
        if i == 0:
            continue
        else:
            if i%2!=0:
                answer+='수'
            else:
                answer+='박'
    return answer