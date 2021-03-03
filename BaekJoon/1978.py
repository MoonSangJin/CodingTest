import math

n=int(input())
data=list(map(int,input().split()))
answer=0

def checkPrime(n):
    if n==1:
        return False

    for i in range(2,int(math.sqrt(n))+1): #소수는 루트 자기자신까지만 범위다
        if n%i==0:
            return False
    return True

for i in data:
    if checkPrime(i):
        answer+=1
print(answer)        
