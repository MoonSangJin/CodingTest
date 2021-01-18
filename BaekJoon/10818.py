n = int(input())
arry = list(map(int, input().split()))
maximum = -1000000
minimum = 1000000
for i in range(len(arry)):
    cmp = arry[i]
    if(maximum < cmp):
        maximum = cmp
    if(minimum > cmp):
        minimum = cmp
print(minimum, end=" ")
print(maximum)
