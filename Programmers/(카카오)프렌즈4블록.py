def check(x,y,graph):
    if graph[x][y]==graph[x][y+1]==graph[x+1][y+1]==graph[x+1][y]:
        if graph[x][y]!='-':
            return True
        else:
            return False
    else:
        return False

def deldown(graph):
    for i in range(len(graph)-2,-1,-1):
        for j in range(len(graph[0])):
            a,b=i,j
            while graph[a+1][b]=='-':
                graph[a+1][b]=graph[a][b]
                graph[a][b]='-'
                a+=1
                if a==len(graph)-1:
                    break
        
def solution(m, n, board):
    answer = 0
    temp=[]
    graph=[[] for _ in range(m)]
    
    for i in range(m):
        for j in range(n):
            graph[i].append(board[i][j])
                
    end=False
    while end==False:
        for i in range(m-1):
            for j in range(n-1):
                if check(i,j,graph):
                    temp.append((i,j))
                    temp.append((i,j+1))
                    temp.append((i+1,j+1))
                    temp.append((i+1,j))
                    
        for a,b in list(set(temp)):
            graph[a][b]='-'
        temp=[]
        deldown(graph)
        end=True
        for i in range(m-1):
            for j in range(n-1):
                if check(i,j,graph):
                    end=False
                    break
            if end==False:
                break
                
    for i in range(len(graph)):
        for j in range(len(graph[0])):
            if graph[i][j]=='-':
                answer+=1
    return answer