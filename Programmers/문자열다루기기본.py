def solution(s):
    answer = True
    if len(s)==4 or len(s)==6:
        for i in range(len(s)):
            if not s[i].isdigit(): #숫자인지 아닌지 체크해주는 함수
                answer=False
    else:
        answer=False
    return answer