#그리디
def solution(people, limit):
    answer = 0
    people.sort()
    a=0
    b=len(people)-1  
    cnt=0
    while a<=b:
        cnt+=1
        if people[a]+people[b]<=limit:
            a+=1
            b-=1
        else:
            b-=1
    answer=cnt
    return answer