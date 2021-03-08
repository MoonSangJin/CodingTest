from sys import stdin

n,m=map(int,stdin.readline().split())
#투포인터
data=list(map(int,stdin.readline().split()))

answer=0
start,end=0,0
sum=0

while not start==end==n :
    if sum==m:
        answer+=1
    if sum<m and end<n:
        sum+=data[end]
        end+=1
    else:
        sum-=data[start]
        start+=1        

print(answer)            