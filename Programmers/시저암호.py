def solution(s, n):
    answer = ''
    large='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    small='abcdefghijklmnopqrstuvwxyz'
    for i in range(len(s)):
        if s[i].isupper():
            answer+=large[((large.index(s[i]))+n)%26]
        elif s[i].islower():
            answer+=small[((small.index(s[i]))+n)%26]
        else:
            answer+=' '
    
    return answer