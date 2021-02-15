def solution(x):
    data=list(str(x))
    data=sum(list(map(int,data)))
    if x%data==0:
        answer=True
    else:
        answer=False
    return answer