a = int(input())
result = 1


def solution(a, result):
    if(a == 0):
        return result
    result = result*a
    return solution(a-1, result)


print(solution(a, result))
