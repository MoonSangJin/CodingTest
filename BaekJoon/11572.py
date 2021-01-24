word = input()
word = word.upper()

word_list = list(set(word))
word_count = []
count = 0
for i in word_list:
    for j in word:
        if i == j:
            count += 1
    word_count.append(count)
    count = 0

word_maxcount = max(word_count)
count2 = 0
for i in word_count:
    if i == word_maxcount:
        count2 += 1
if count2 > 1:
    print('?')
else:
    word_index = word_count.index(max(word_count))
    print(word_list[word_index])
