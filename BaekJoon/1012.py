#dfs (입력 두개씩 들어오는것)
import sys
sys.setrecursionlimit(10**6)

n=int(input())

def dfs(row,column):
    if row<=-1 or row>=n or column<=-1 or column>=m:
        return False
    if graph[row][column]==1:
        graph[row][column]=9
        dfs(row-1,column)
        dfs(row,column+1)
        dfs(row+1,column)
        dfs(row,column-1)
        return True
    return False

for _ in range(n):
    m,n,k=map(int,input().split())
    graph=[ [0]*m for _ in range(n)]
    result=0
    for _ in range(k):
        column,row=map(int,input().split())
        graph[row][column]=1

    for i in range(n):
        for j in range(m):
            if dfs(i,j)==True:
                result+=1
    print(result)            