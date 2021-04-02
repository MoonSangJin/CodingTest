def solution(s):
    answer = True
    stack=[]
    for i in s:
        if i=='(': # (가 들어올때
            stack.append(i)
        else:       # )가 들어올때
            if len(stack)==0:
                return False
            if stack[-1]=='(':
                stack.pop()
    if len(stack):
        return False
    return True