n, m = map(int, input().split())
card = list(map(int, input().split()))
result = 0
for i in range(len(card)):
    for j in range(i+1, len(card)):
        for k in range(j+1, len(card)):
            if(result < card[i]+card[j]+card[k] | card[i]+card[j]+card[k] <= m):
                result = card[i]+card[j]+card[k]
print(result)
