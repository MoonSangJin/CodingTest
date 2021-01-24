n = int(input())
group_word = 0
for i in range(n):
    word = input()
    error = 0
    for index in range(len(word)-1):
        # 현재 단어랑 다음 인덱스에 해당하는 단어가 다르면 <같은 경우는 그냥 넘기고> ex) ab =>a는 b 뒤에 나오면 그룹 단어가 안되네
        if word[index] != word[index+1]:
            # 그럼 b로 시작하는 새로운 단어에서 a가 나오는지를 체크하자
            new_word = word[index+1:len(word)]
            # a가 b뒤에 나오면 find 했을때 해당 index가 나오겠지, 안나오면 -1일테고
            if new_word.find(word[index]) != -1:
                error += 1  # 원래는 그냥 n-1했는데 오류 케이스가 한 단어에서 한번만 나오는게 아닐 수 도 있으니까=> 여러번 오류 나더라도 그 한 단어내에서 일어나는 일이고 결론적으로는 그 단어가 그룹단어가 안되는 경우는 최종 딱 한번
    if error == 0:
        group_word += 1
print(group_word)
