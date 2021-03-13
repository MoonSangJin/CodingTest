#소수구하기 m이상 n이하 처럼 특정범위면 에라토스테네스의 체 사용
m,n=map(int,input().split())

a = [False,False] + [True]*(n-1)
primes=[]

for i in range(2,n+1):
  if a[i]:
    primes.append(i)
    for j in range(2*i, n+1, i):
        a[j] = False

for i in primes:
    if m<=i<=n:
        print(i)