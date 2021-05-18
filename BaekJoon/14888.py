n=int(input())
number=list(map(int,input().split()))
plus,minus,multiple,divide=map(int,input().split())

min_value=1e9
max_value=-1e9

def dfs(i,now):
    global min_value,max_value,plus,minus,multiple,divide
    
    if i==n: #number를 다썼다는 소리 dfs는 재귀니까 종료조건이 있어야되자나
        min_value=min(min_value,now)
        max_value=max(max_value,now)
    else:
        if plus>0:
            plus-=1
            dfs(i+1,now+number[i])
            plus+=1
        if minus>0:
            minus-=1
            dfs(i+1,now-number[i])
            minus+=1
        if multiple>0:
            multiple-=1
            dfs(i+1,now*number[i])
            multiple+=1
        if divide>0:
            divide-=1
            dfs(i+1,int(now/number[i]))
            divide+=1
        

dfs(1,number[0]) #now를 처음숫자 주고, i를 그 다음숫자로 줌

print(max_value)
print(min_value)