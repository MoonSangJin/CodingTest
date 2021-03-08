s=int(input())
n=0
answer=[]
while True:
    n+=1
    s-=n
    if s>=0:
        answer.append(n)
    else:
        break    
print(len(answer))    