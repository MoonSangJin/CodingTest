#stack
n=int(input())
nums=list(map(int,input().split()))

stack=[]
result=[-1 for _ in range(n)]

stack.append(0)
i=1

while stack and i<n:
    while stack and nums[stack[-1]]<nums[i]:
        result[stack[-1]]=nums[i]
        stack.pop()
    stack.append(i)
    i+=1

for i in result:
    print(i, end=' ')