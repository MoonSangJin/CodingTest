
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
