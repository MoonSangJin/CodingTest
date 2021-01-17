n = int(input())
result = []
for i in range(0, n):
    a = int(input())
    if(a != 0):
        result.append(a)
    else:
        result.pop()
real = 0
for j in range(len(result)):
    real = real+result[j]

print(real)
