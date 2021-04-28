#hash
n=int(input())
temp=list(map(int,input().split()))
sorted_temp=sorted(list(set(temp)))
answer={sorted_temp[i]:i for i in range(len(sorted_temp))}

for i in temp:
    print(answer[i],end=' ')