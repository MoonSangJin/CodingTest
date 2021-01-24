data = input()
alphabet = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']
sum = 0
for i in data:
    for j in range(len(alphabet)):
        if i in alphabet[j]:
            plus = j+3
    sum += plus
    plus = 0
print(sum)
