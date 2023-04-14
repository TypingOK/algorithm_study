import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

grid = []
start = []

for i in range(N):
    temp = list(input().rstrip("\n"))
    for j in range(M):
        if temp[j] == "o":
            start.append((i, j))
    grid.append(temp)


def bfs(start, N, M, grid):
    q = deque()
    q.append((start[0][0], start[0][1], start[1][0], start[1][1], 0))

    while q:
        x, y, m, z, count = q.popleft()
        if count >= 10:
            return -1
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            nm = m+dx[i]
            nz = z + dy[i]

            if 0 <= nx < N and 0 <= ny < M and 0 <= nm < N and 0 <= nz < M:
                if grid[nx][ny] == "#":
                    nx = x
                    ny = y
                if grid[nm][nz] == "#":
                    nm = m
                    nz = z
                q.append((nx, ny, nm, nz, count+1))
            elif 0 <= nx < N and 0 <= ny < M:
                return count+1
            elif 0 <= nm < N and 0 <= nz < M:
                return count+1
    return -1


answer = bfs(start, N, M, grid)
print(answer)
