#dfs
def solution(numbers, target):
    answer = []
    def dfs(index,target,sum):
        if index==len(numbers):
            if target==sum:
                answer.append(1)
                return
            else:
                return
        else:
            dfs(index+1,target,sum-numbers[index])
            dfs(index+1,target,sum+numbers[index])
    dfs(0,target,0)
    answer=len(answer)
    return answer