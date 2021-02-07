def solution(n, m):
    answer = []
    if n<m: #최대공약수
        min=n
    else:
        min=m
    for i in range(min,0,-1):
        if n%i==0 and m%i==0:
            answer.append(i)
            break
    
    if n<m: #최소공배수
        max=m
    else:
        max=n
    for i in range(max,n*m+1):
        if i%n==0 and i%m==0:
            answer.append(i)
            break
    return answer