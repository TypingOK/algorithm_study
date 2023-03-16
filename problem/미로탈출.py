import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())
x, y = map(int, input().split())
ex, ey = map(int, input().split())
x, y, ex, ey = x-1, y-1, ex-1, ey-1
grid = []
for i in range(N):
    grid.append(list(map(int, input().split())))

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]


def bfs(x, y):
    q = deque()
    q.append((x, y, 0, 1))
    visited = [[[False for _ in range(2)] for i in range(M)] for _ in range(N)]
    visited[x][y][1] = True

    while (q):
        tx, ty, count, magic = q.popleft()

        if (tx) == ex and ty == ey:
            return count
        else:
            for i in range(4):
                nx = tx + dx[i]
                ny = ty + dy[i]
                if (0 <= nx < N and 0 <= ny < M):
                    if visited[nx][ny][magic]:
                        continue
                    if grid[nx][ny] == 1 and magic == 1:
                        q.append((nx, ny, count+1, magic-1))
                        visited[nx][ny][0] = True
                    elif grid[nx][ny] == 0:
                        q.append((nx, ny, count+1, magic))
                        visited[nx][ny][magic] = True
    return -1


answer = bfs(x, y)
print(answer)
