from sys import stdin

n,m=map(int,stdin.readline().split())

answer = []
min=min(n,m) #최대 공약수 : 둘중 작은거 부터 1씩 줄어가며 두수 다 나머지 0으로 만드는 숫자찾기
for i in range(min,0,-1):
    if n%i==0 and m%i==0:
        answer.append(i)
        break
    
max=max(n,m) #최소 공배수 : 둘중 큰거부터 1씩 키워가며 두수로 나눴을때 나머지 0되는거
for i in range(max,n*m+1):
    if i%n==0 and i%m==0:
        answer.append(i)
        break

for i in answer:
    print(i)

