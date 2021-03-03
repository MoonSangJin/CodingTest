x,y,w,h=map(int,input().split())
data=[]
data.append(x)
data.append(y)
data.append(w-x)
data.append(h-y)

print(min(data))