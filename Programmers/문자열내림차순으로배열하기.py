def solution(s):
    answer = ''
    a=sorted(s)
    a.reverse()
    for i in a:
        answer+=i
    
    return answer