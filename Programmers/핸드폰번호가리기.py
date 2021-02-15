def solution(phone_number):
    answer = ''
    star=len(phone_number[0:-4])
    number=phone_number[-4:]
    answer+='*'*star
    answer+=number
    print(answer)
    return answer