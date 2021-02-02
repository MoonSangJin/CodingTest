def solution(n):
    answer = 0
    data=[]
    while n>0:
        data.append(n%3)
        n=n//3
    
    data.reverse()
    
    for i in range(len(data)):
        answer+=data[i]*3**i
        
    return answer