#구현
def check(p):
    stack=[]
    for i in p:
        if i in ('(','[','{'):
            stack.append(i)
        else:
            if len(stack)==0:
                return False
            x=stack.pop()
            if i==')' and x!='(':
                return False
            if i==']' and x!='[':
                return False
            if i=='}' and x!='{':
                return False
    if stack:
        return False
    return True
    
def solution(s):
    answer = 0
    for i in range(len(s)):
        s=s[1:]+s[0]
        if check(s):
            answer+=1
    return answer