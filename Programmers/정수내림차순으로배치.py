def solution(n):
    answer = 0
    data=sorted(list(str(n)),reverse=True)
    answer=int(''.join(data))
    return answer