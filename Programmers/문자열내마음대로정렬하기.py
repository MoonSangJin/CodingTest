def solution(strings, n):
    answer = []
    strings.sort()
    answer=sorted(strings,key=lambda alphabet:alphabet[n])
    
    return answer