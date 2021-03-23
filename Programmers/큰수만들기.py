#combinations 이용하면 시간초과
# from itertools import combinations
# def solution(number, k):
#     answer = ''
#     n=len(number)-k
#     tmp=list(combinations(number,n))
#     data=[]
#     for i in tmp:
#         data.append(''.join(i))
#     answer=max(data)    
#     return answer

#그리디, 예제를 보며 천천히 분기지점을 찾아간다.
def solution(number, k):
    answer = []
    for i in number:
        if len(answer)==0 or answer[-1]>=i or k==0:
            answer.append(i)
        else:
            while  len(answer)!=0 and answer[-1]<i and k>0:
                answer.pop()
                k-=1
            answer.append(i)
    if k>0:
        answer=answer[:-k]
    answer=''.join(answer)      
    return answer