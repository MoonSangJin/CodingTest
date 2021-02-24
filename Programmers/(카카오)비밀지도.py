def solution(n, arr1, arr2):
    answer = []
    bin1=[]
    bin2=[]
    for i in arr1:
        bin=[]
        for _ in range(n):
            bin.append(i%2)
            i=i//2
        bin.reverse()
        bin1.append(bin)
        
    for i in arr2:
        bin=[]
        for _ in range(n):
            bin.append(i%2)
            i=i//2
        bin.reverse()
        bin2.append(bin)    
    
    for i in range(len(bin1)):
        temp=[]
        for j in range(len(bin1[i])):
            if bin1[i][j]==0 and bin2[i][j]==0:
                temp.append(' ')
            else:
                temp.append('#')
        answer.append(''.join(temp))                        
    return answer