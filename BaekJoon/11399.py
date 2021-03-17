#그리디,정렬
n=int(input())
data=list(map(int,input().split()))
data.sort()
answer=0
for i in range(0,1):
    for j in range(len(data)):
        answer+=sum(data[i:j+1])
print(answer)        