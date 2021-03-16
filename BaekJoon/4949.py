while True:
    message=input().rstrip()
    if message=='.':
        break
    stack=[]
    check=True
    for i in message:
        if i=='(' or i=='[':
            stack.append(i)
        elif i==')':
            if stack and stack[-1]=='(':
                stack.pop()
            else:
                check=False
                break
        elif i==']':
            if stack and stack[-1]=='[':
                stack.pop()
            else:
                check=False
                break
        
    print('yes') if check and not stack else print('no')                        