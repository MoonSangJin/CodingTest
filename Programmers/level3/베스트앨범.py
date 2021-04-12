#해쉬
def solution(genres, plays):
    answer = []
    dict={}
    dict_sum={}
    for i in genres:
        dict[i]=[]
        dict_sum[i]=0
    for i in range(len(genres)):
        dict[genres[i]].append((plays[i],i))
        dict_sum[genres[i]]+=plays[i]
    for i in dict:
        dict[i].sort(key=lambda x:(-x[0],x[1]))
    order=sorted(dict_sum.items(),key=lambda x:-x[1])
    
    for i in order:
        for j in range(2):
            if len(dict[i[0]])==1:
                answer.append(dict[i[0]][0][1])
                break
            else:
                answer.append(dict[i[0]][j][1])
                
    return answer