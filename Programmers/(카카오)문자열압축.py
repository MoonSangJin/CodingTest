def solution(s):
    cand=[]
    if len(s)==1:
        return len(s)
    for size in range(1,len(s)):
        count=1
        compressed=''
        splited=[]
        for i in range(0,len(s),size):
            splited.append(s[i:i+size])
        for j in range(1,len(splited)):
            if splited[j-1]==splited[j]:
                count+=1
            else:
                compressed+=str(count)+splited[j-1] if count>1 else splited[j-1]
                count=1
        compressed+=str(count)+splited[-1] if count>1 else splited[-1] #맨 마지막거 처리 위해서       
        cand.append(len(compressed))
        
    return min(cand)