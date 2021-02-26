n=int(input())
temp=[]
cnt=0
a=666
while True:
    if '666' in str(a):
        temp.append(a)
        cnt+=1
        a+=1
        if cnt==n:
            break
    else:
        a+=1
        if cnt==n:
            break     
print(temp[n-1])           