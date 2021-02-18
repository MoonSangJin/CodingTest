def solution(clothes):
    answer = 0
    data={}
    for i in clothes:
        if i[1] in data:
            data[i[1]]+=1
        else:
            data[i[1]]=1
    cnt=1
    for value in data.values():
        cnt*=value+1  #안입은 경우도 생각해서 +1 더한걸 곱한다.
    answer=cnt-1    
    return answer