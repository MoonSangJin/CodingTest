#정규표현식
import re
def solution(dartResult):
    bonus = {'S' : 1, 'D' : 2, 'T' : 3}
    option = {'' : 1, '*' : 2, '#' : -1}

    p = re.compile('([0-9]+)([SDT]{1})([*#]?)')
    a = re.compile('[0-9]+[SDT]{1}[*#]?')
    dart = p.findall(dartResult)     
    b=a.findall(dartResult)
    print(dart,b)

    for i in range(len(dart)):
        if dart[i][2] == '*' and i > 0:
            dart[i-1] *= 2
        dart[i] = int(dart[i][0]) ** bonus[dart[i][1]] * option[dart[i][2]]

    answer = sum(dart)
    return answer