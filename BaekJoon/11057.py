n=int(input())
dp=[[0]*10 for _ in range(n+1)]
answer,mod=0,10007

for i in range(10):
    dp[1][i]=1
for i in range(2,n+1):
    dp[i][0]
