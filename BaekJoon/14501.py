#dp
n=int(input())
t=[]
p=[]
dp=[]
for _ in range(n):
    a,b=map(int,input().split())
    t.append(a)
    p.append(b)
    dp.append(b)
dp.append(0)
for i in range(n - 1, -1, -1):
    if t[i] + i > n:
        dp[i] = dp[i + 1]
    else:
        dp[i] = max(dp[i + 1], p[i] + dp[i + t[i]])  #i번째 상담을 하면 t[i]동안 다른 상담 못함, 대신 보수 p[i]가져감
                                                    #i번째 상담을 안하면 dp[i+1]임 i번째는 건너뛰므로 
print(dp[0])
