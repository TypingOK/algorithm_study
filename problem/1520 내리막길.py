import sys
input = sys.stdin.readline

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

max_number = sys.maxsize

N, M = map(int, input().split())
graph = []
for i in range(N):
    temp = list(map(int, input().split()))
    graph.append(temp)

dp = [[-1 for _ in range(M)] for _ in range(N)]
dp[N-1][M-1] = 1

def dfs(dp,graph, x, y, N, M):
    if dp[x][y] != -1:
        return dp[x][y]

    count = 0
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < N and 0 <= ny < M and graph[x][y] > graph[nx][ny]:
            count += dfs(dp,graph, nx, ny, N, M)
    dp[x][y] = count
    print(dp)
    return dp[x][y]
print(dfs(dp, graph, 0, 0, N, M))

