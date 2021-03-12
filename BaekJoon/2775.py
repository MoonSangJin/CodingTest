#bottom-up
from sys import stdin
input=stdin.readline

t=int(input())

def get(k,n):
    data=[[0]*15 for _ in range(k+1)]
    for i in range(1,15):
        data[0][i]=i

    for i in range(1,k+1):
        for j in range(1,15):
            data[i][j]=sum(data[i-1][1:j+1])

    return data[k][n]        

for _ in range(t):
    k=int(input())
    n=int(input())
    print(get(k,n))