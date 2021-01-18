c = int(input())
for i in range(c):
    data = list(map(int, (input().split())))
    avg = sum(data[1:len(data)])/data[0]
    count = 0
    for i in range(1, len(data)):
        if data[i] > avg:
            count += 1
    p = count/data[0]*100
    p = round(p, 3)
    print("%.3f" % p + "%")
