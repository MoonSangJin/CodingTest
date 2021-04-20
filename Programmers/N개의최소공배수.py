def solution(arr):
    answer = 0
    min_number=min(arr)
    max_number=1
    for i in arr:
        max_number*=i
    for i in range(min_number,max_number+1):
        cnt=0
        for j in arr:
            if i%j==0:
                cnt+=1
        if cnt==len(arr):
                answer=i
                break
    return answer