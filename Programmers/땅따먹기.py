#dp
#dp는 보통 모든 경우에 대해 구하게됨
def solution(land):
    answer = 0
    for i in range(1,len(land)):
        for j in range(4):
            land[i][j]+=max(land[i-1][:j]+land[i-1][j+1:]) #배열끼리 합치는 방법 (j에 해당하는 열만 빼놓고)
    answer=max(land[-1])     
    return answer