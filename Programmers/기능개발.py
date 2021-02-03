#실패한 코드
def solution(progresses, speeds):
    answer = []
    temp=[]
    count=1
    while len(progresses)>0:
        while progresses[0]+speeds[0]*count<100:
            count+=1
        temp.append(count)
        progresses.pop(0)
        speeds.pop(0)
    
    print(temp)
    temp2=[]
    for i in range(len(temp)):
        temp2.append(temp.count(temp[i]))
    print(temp2)    
    for i in range(len(temp2)):
        if i ==0:
            answer.append(temp2[i])
        elif temp2[i-1]!=temp2[i]:
            answer.append(temp2[i])
            
    print(answer)    
    return answer

#맞는코드
def solution(progresses, speeds):
    answer = []
    time=0
    count=0
    while len(progresses)>0: #progresses 빌때까지
        if (progresses[0]+speeds[0]*time)>=100: #100퍼센트이상이면
            progresses.pop(0) #다음꺼진행
            speeds.pop(0)
            count+=1            #한번 배포할때 어디까지 작업이 끝나있는지 체크
        else:
            if count>0:
                answer.append(count)
                count=0
            time+=1
    answer.append(count)         
    return answer    