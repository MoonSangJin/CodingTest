import math
def solution(n):
    answer = 0
    data=math.sqrt(n)
    if data==int(data):
        answer=(data+1)**2
    else:
        answer=-1
    return answer