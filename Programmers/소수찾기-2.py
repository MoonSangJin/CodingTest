#에라토스테네스의 체, 순열
import itertools

def solution(numbers):
    data=[]
    for i in range(1,len(numbers)+1):
        tmp=itertools.permutations(numbers,i) #순열 이용 17과 71은 다르니까 순열이용
        for n in tmp:
            tmp_str=''.join(n)
            data.append(int(tmp_str))
    data=list(set(data))
    #에라토스테네스의 체 이용
    n=max(data)
    a=[False,False]+[True]*(n-1)
    primes=[]
    answer=[]
    for i in range(2,n+1):
        if a[i]:
            primes.append(i)
            for j in range(i,n+1,i):
                a[j]=False
    for i in data:
        if i in primes:
            answer.append(i)
        
    answer=len(answer)
    return answer