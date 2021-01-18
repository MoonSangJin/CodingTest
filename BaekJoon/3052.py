arry = []
for i in range(10):
    a = int(input())
    a = a % 42
    if a not in arry:
        arry.append(a)
print(len(arry))
