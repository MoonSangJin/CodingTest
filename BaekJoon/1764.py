from sys import stdin

n,m=map(int,stdin.readline().split())

not_listened = [stdin.readline().strip() for i in range(n)]
not_seen = [stdin.readline().strip() for i in range(m)]

answer = list(set(not_listened) & set(not_seen))

print(len(answer))

for i in sorted(answer):
    print(i)