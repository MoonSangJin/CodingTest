def solution(s):
    answer = ''
    s=s.lower()
    a=s.split(' ')
    for i in a:
        i=i.capitalize()
        answer+=i+' '
        
    answer=answer[:-1]
    return answer