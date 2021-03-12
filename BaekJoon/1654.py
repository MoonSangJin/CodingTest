from sys import stdin
#이분탐색
input=stdin.readline
k,n=map(int,input().split())
data=[]

for _ in range(k):
    data.append(int(input().rstrip()))
start=1
data.sort(reverse=True)
end=data[0]
answer=[]
while start<=end:
    mid=(start+end)//2
    temp=[]
    for i in data:
        temp.append(i//mid)
    if sum(temp)>=n:
        start=mid+1
        answer.append(mid)
    elif sum(temp)<n:
        end=mid-1

print(max(answer))