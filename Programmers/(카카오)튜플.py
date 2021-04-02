def solution(s):
    answer = []
    s=s[1:-1]
    s=s.replace('},{','/')
    s=s[1:-1]
    s=s.split('/')
    thing=''
    s.sort(key=lambda x:len(x))
    for i in s:
        if len(i)==1:
            answer.append(int(i))
            continue
        for j in i:
            if j!=',':
                thing+=j
            elif j==',':
                if int(thing) not in answer:
                    answer.append(int(thing))
                    thing=''
                else:
                    thing=''
        if len(thing) and int(thing) not in answer:
            answer.append(int(thing))
        thing=''
    return answer

#다른이 풀이
def solution(s):
    answer = []

    s1 = s.strip('{}').split('},{') #lstrip('{')은 왼쪽부터 {의 조합을 없앰 {아닌거 만나면 멈춤, strip은 양쪽에서부터 {}의 조합을 없앰

    new_s = []
    for i in s1:
        new_s.append(i.split(','))

    new_s.sort(key = len)

    for i in new_s:
        for j in range(len(i)):
            if int(i[j]) not in answer:
                answer.append(int(i[j]))

    return answer
