def solution(n):
    answer = []
    n=str(n)
    for i in range(len(n)-1,-1,-1):
        answer.append(int(n[i]))
        
        
    return answer

#파이썬적으로 다시
def solution(n):
    answer = []
    answer=list(str(n))
    answer.reverse()
    answer=list(map(int,answer))
        
        
    return answer