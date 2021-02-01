def solution(s):
    answer = ''
    if len(s)%2==0:
        index=len(s)//2
        answer=s[index-1]+s[index]
    else:
        index=len(s)//2
        answer=s[index]
    return answer