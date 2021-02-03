def solution(a, b):
    answer = 0
    for i in range(len(a)):
        answer+=a[i]*b[i]
    return answer

#zip함수를 이용하면 더 간단해진다.
a=[1,2,3,4]
b=[-3,-1,0,2]
answer=[]
for i,j in zip(a,b):
    answer.append(i*j)
print(sum(answer))    