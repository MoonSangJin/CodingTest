t=int(input())
for _ in range(t):
    h,w,n=map(int,input().split())
    left=n%h
    right=n//h
    if left==0:
        answer=h*100
        ho=right
    else:
        answer=left*100
        ho=right+1
    print(answer+ho)    
   
