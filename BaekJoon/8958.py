n = int(input())
for i in range(n):
    data = list(input())
    result = 0
    count = 0
    for j in data:
        if j == 'O':
            count += 1
            result += count
        else:
            count = 0
    print(result)
