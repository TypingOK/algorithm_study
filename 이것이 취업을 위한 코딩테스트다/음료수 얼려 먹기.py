import sys
input = sys.stdin.readline

N, M = map(int, input().split())
grid = []

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

for i in range(N):
    temp = list(input().rstrip("\n"))
    a = []
    for j in temp:
        a.append(int(j))
    grid.append(a)
print(grid)


def DFS(x, y, grid, visited, N, M):
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny] and grid[nx][ny] == 0:
            visited[nx][ny] = True
            DFS(nx, ny, grid, visited, N, M)


visited = [[False for _ in range(M)] for _ in range(N)]
answer = 0
for i in range(N):
    for j in range(M):
        if grid[i][j] == 0 and not visited[i][j]:
            answer += 1
            DFS(i, j, grid, visited, N, M)

print(answer)
