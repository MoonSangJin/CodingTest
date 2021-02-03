#효율성 탈락한 코드
def solution(n):
    answer = 0
    s=0
    for i in range(2,n+1):
        for j in range(2,i):
            if i%j==0:
                s=1
        if s!=1:
            answer+=1
        else:
            s=0          
    return answer

#에라토스테네스의 체를 이용해서 소수를 찾는방법 (통과)
n=10    
a = [False,False] + [True]*(n-1) #0은 상관없고 1은 모든 수의 약수니까 필요없다
primes=[]
for i in range(2,n+1):   #2부터 n까지 중에서
    if a[i]:             #2부터 시작해서 배수들을 지워나간다.(false처리)
        primes.append(i) #true였던 거는 배수들을 지워가는 과정에서 살아남은 놈이므로 약수가 1과 자기자신밖에 없는놈
        for j in range(i,n+1,i):
            a[j]=False  #배수들을 지워가는 과정
print(primes)                
