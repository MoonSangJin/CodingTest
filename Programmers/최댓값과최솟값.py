def solution(s):
    answer = ''
    a=list(map(int,s.split(' ')))
    a.sort()
    answer+=str(a[0])
    answer+=' '
    answer+=str(a[len(a)-1])
    
    return answer