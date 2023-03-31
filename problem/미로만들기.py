import sys
from collections import deque

input = sys.stdin.readline
grid = []
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

N = int(input())

for i in range(N):
    grid.append(list(map(int, list(input().strip()))))
INF = sys.maxsize


def bfs(N):
    q = deque()
    visited = [[INF] * N for _ in range(N)]
    q.append((0, 0, 0))
    visited[0][0] = 0

    while q:
        x, y, count = q.popleft()

        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]

            if 0 <= nx < N and 0 <= ny < N:
                if grid[nx][ny] == 0 and visited[nx][ny] > count + 1:
                    visited[nx][ny] = count+1
                    q.append((nx, ny, count+1))
                elif grid[nx][ny] == 1 and visited[nx][ny] > count:
                    visited[nx][ny] = count
                    q.append((nx, ny, count))
    return visited[N-1][N-1]


answer = bfs(N)
print(answer)
