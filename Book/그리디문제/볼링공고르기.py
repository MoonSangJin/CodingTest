n,m=map(int,input().split())
data=list(map(int,input().split()))
answer=0

# for i in range(len(data)-1):
#     for j in range(i+1,len(data)):
#         if data[i]!=data[j]:
#             answer+=1           
array=[0]*11
for i in data:
    array[i]+=1
    
result=0
for i in range(1, m+1):
    n-=array[i]
    result+=array[i]*n