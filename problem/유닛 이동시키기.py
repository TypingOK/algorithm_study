import sys
from collections import deque

input = sys.stdin.readline
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

N, M, A, B, K = map(int, input().split())

grid = [[0] * M for _ in range(N)]
for _ in range(K):
    a, b = map(int, input().split())
    grid[a-1][b-1] = 1
sx, sy = map(int, input().split())
ex, ey = map(int, input().split())
sx, sy = sx - 1, sy - 1
ex, ey = ex-1, ey-1


def check(grid, A, B, nx, ny):
    for i in range(nx, nx+A):
        for j in range(ny, ny+B):
            if (grid[i][j] == 1):
                return False
    return True


def bfs(sx, sy, ex, ey, grid, A, B):
    q = deque()
    q.append((sx, sy, 0))
    visited = [[False] * M for _ in range(N)]
    visited[sx][sy] = True
    while q:
        x, y, count = q.popleft()
        # print(x, y)
        if x == ex and y == ey:
            return count
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if 0 <=nx and nx+A-1 < N and 0 <=ny and ny+B-1 < M and not visited[nx][ny] and check(grid, A, B, nx, ny):
                q.append((nx, ny, count+1))
                visited[nx][ny] = True
    return -1


result = 0
for i in range(sx, sx+A):
    for j in range(sy, sy+B):
        if grid[i][j] == 1:
            result = -1
if result == 0:
    answer = bfs(sx, sy, ex, ey, grid, A, B)
    print(answer)
else:
    print(-1)
