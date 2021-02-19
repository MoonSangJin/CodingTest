def solution(num):
    answer = ''
    while num:
        num,nam=divmod(num,3)
        answer='412'[nam]+answer;
        if nam == 0:
            num-=1
    
    return answer