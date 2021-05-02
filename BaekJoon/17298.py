
# n = int(input())  이중포문 돌리면 바로 시간초과다...
# array = list(map(int, input().split()))

# result = []
# for i in range(len(array)):
#     nge = 0
#     cmp = 0
#     if(i == len(array)-1):
#         result.append(-1)
#         break
#     nge = array[i]
#     for j in range(i+1, len(array)):
#         cmp = array[j]
#         if(nge < cmp):
#             nge = cmp
#             result.append(nge)
#             break
#         else:
#             if(j == len(array)-1):
#                 result.append(-1)
#                 continue
#             else:
#                 continue
# for k in result:
#     print(k, end=' ')

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