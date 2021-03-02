def solution(numbers):
    answer = ''
    numbers=list(map(str,numbers))
    data=sorted(numbers,key=lambda x:(x[0],x[1%len(x)],x[2%len(x)],x[3%len(x)]),reverse=True)
    answer=''.join(data)
    if int(answer)==0:
        answer='0'
    return answer