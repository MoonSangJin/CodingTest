def solution(n, lost, reserve):
    answer = 0
    set_reserve=set(reserve)-set(lost) #여벌이 있는 학생이 도난당하면 빌려줄 수 없으므로 그 처리 부터 해야한다.
    set_lost=set(lost)-set(reserve)     #도난당한사람중에 여벌이 있는 학생이 속해있으면 빌려줄수 없다.
    for i in set_reserve:
        if i-1 in set_lost:
            set_lost.remove(i-1)
        elif i+1 in set_lost:
            set_lost.remove(i+1)
    answer=n-len(set_lost)        
    
    return answer