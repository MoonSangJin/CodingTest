def solution(a, b):
    answer = 0
    if a==b:
        answer=a
    
    if a<b:
        for i in range(b-a+1):
            answer+=a+i
    elif b<a:
        for i in range(a-b+1):
            answer+=b+i
    return answer