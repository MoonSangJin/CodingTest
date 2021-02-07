def solution(num):
    answer = 0
    count=0
    if num==1:
        return 0
    while(count!=500):
        count+=1
        if num%2==0:
            num=num/2
        else:
            num=num*3+1
        if num==1:
            answer=count
            break
    if(count==500):
        answer=-1
        
        
    return answer