n=int(input())
data = list(map(int,input().split()))
data.sort() #오름차순으로 sort를 해서 그룹화 하면 간단하다

result=0
count=0
for i in data:
    count+=1
    if count>=i:
        result+=1
        count=0
print(result)    