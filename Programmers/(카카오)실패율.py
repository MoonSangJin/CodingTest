def solution(N, stages):
    answer = []
    count=[]
    temp=[]
    temp2=[]
    user=len(stages)
    stages.sort()
    for i in stages:
        i=str(i)
    for i in range(1,N+2):
        count.append(stages.count(i))
    for i in count:
        if i != 0:
            temp.append(i/user)
        else:
            temp.append(0)
        user-=i
    for i in range(len(temp)):
        temp2.append((i+1,temp[i]))
        
    result = sorted(temp2,key=lambda x:x[1],reverse=True)   
    for i in result:
        if i[0]!=N+1:
            answer.append(i[0])
            
    return answer