def solution(a, b):
    answer = ''
    month=[31,29,31,30,31,30,31,31,30,31,30,31]
    data=sum(month[:a-1])
    data+=b
    
    day=['THU','FRI','SAT','SUN','MON','TUE','WED',]
    answer=day[data%7]
    return answer