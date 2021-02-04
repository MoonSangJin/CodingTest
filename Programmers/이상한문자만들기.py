def solution(s):
    answer = ''
    data=[]
    word_list=s.split(' ')    
    for word in word_list:
        new_words=''
        for i in range(len(word)):
            if i%2==0:
                new_words+=word[i].upper()
            else:
                new_words+=word[i].lower()
        data.append(new_words)
        
    answer=' '.join(data)
        
    return answer