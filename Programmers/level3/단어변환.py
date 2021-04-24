#dfs
begin='hit'
target='cog'
words=["hot", "dot", "dog", "lot", "log", "cog"]
# def solution(begin, target, words):
#     answer = 0
#     stacks=[begin]
#     visited={i:0 for i in words} #visited 역할
#     if target not in words:
#         return 0
#     while stacks:
#         stack=stacks.pop()
#         if stack==target:
#             return answer
#         for word in words:
#             for i in range(len(word)):
#                 copy=list(word)
#                 copy_front=list(stack)
#                 copy[i]=0
#                 copy_front[i]=0
#                 if copy==copy_front:
#                     if visited[word]!=0:
#                         continue
#                     visited[word]=1
#                     stacks.append(word)
#                     break
#         answer+=1
#     return answer


def solution(begin, target, words): #dfs이용한 풀이
    answer = 0
    visit=[0]*len(words)
    answer_list=[]
    def dfs(word,depth):
        if word==target:
            answer_list.append(depth)
            return
        else:
            for i in range(len(visit)):
                if visit[i]==1:
                    continue
                co=0
                for j in range(len(word)):
                    if word[j]!=words[i][j]:
                        co+=1
                if co==1:
                    visit[i]=1
                    dfs(words[i],depth+1)
                    visit[i]=0
    
    dfs(begin,0)
    if len(answer_list)!=0:
        answer=min(answer_list)
    return answer
    
solution(begin,target,words)