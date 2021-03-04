data=list(map(int,input().split()))
answer=list(map(lambda x:x**2,data))
print(sum(answer)%10)