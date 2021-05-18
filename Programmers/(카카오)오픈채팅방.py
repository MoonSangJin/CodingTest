def solution(record):
    answer = []
    real=[]
    dict={}
    for i in range(len(record)):
        a=record[i].split(' ')
        if a[0]=='Enter':
            dict[a[1]]=a[2]
            answer.append(a[1]+'님이 들어왔습니다.')
        elif a[0]=='Leave':
            answer.append(a[1]+'님이 나갔습니다.')
        elif a[0]=='Change':
            dict[a[1]]=a[2]
    
    for i in answer:
        a=i.split(' ')
        b=a[0].split('님이')
        change_id=dict[b[0]]
        real.append(i.replace(b[0],change_id))
        
    return real