def solution(arr):
    answer = []
    for i in range(len(arr)):
        if i==0:
            answer.append(arr[0]) #처음거는 그냥 넣고
        elif arr[i-1]!=arr[i]: #이전거랑 지금거랑 다르면 추가
            answer.append(arr[i])
    return answer