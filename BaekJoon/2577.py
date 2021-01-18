a, b, c = int(input()), int(input()), int(input())
result = list(str(a*b*c))

for i in range(0, 10):
    print(result.count(str(i)))
