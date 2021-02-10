n, m = map(int, input().split())  # 몇 행 몇열인지 입력받기

graph = []
for i in range(n):
    graph.append(list(map(int, input())))  # 2차원 리스트의 맵 정보 입력받기


def dfs(x, y):
    if x <= -1 or x >= n or y <= -1 or y >= m:  # 재귀적 호출이니까 종료조건 필요
        return False
    if graph[x][y] == 0:  # 방문 안했으면
        graph[x][y] = 1  # 방문 처리후
        dfs(x-1, y)  # 상하좌우로 dfs 재귀호출
        dfs(x+1, y)
        dfs(x, y-1)
        dfs(x, y+1)
        return True  # 첫 시발점이 True되는게 dfs 끝났다는 뜻
    else:
        return False


result = 0
for i in range(n):
    for j in range(m):
        if dfs(i, j) == True:  # 모든 맵의 각각에 대해서 dfs 돌린다.
            result += 1

print(result)
