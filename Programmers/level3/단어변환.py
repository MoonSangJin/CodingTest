#dfs
begin='hit'
target='cog'
words=["hot", "dot", "dog", "lot", "log", "cog"]
def solution(begin, target, words):
    answer = 0
    stacks=[begin]
    visited={i:0 for i in words} #visited 역할
    if target not in words:
        return 0
    while stacks:
        stack=stacks.pop()
        if stack==target:
            return answer
        for word in words:
            for i in range(len(word)):
                copy=list(word)
                copy_front=list(stack)
                copy[i]=0
                copy_front[i]=0
                if copy==copy_front:
                    if visited[word]!=0:
                        continue
                    visited[word]=1
                    stacks.append(word)
                    break
        answer+=1
    return answer

solution(begin,target,words)