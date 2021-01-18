data = list(map(int, input().split()))
for i in range(len(data)):
    if data[i] % 2 == 0:
        print('even')
    else:
        print('odd')
