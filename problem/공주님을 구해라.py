import sys
from collections import deque
input = sys.stdin.readline

N, M, T = map(int, input().split())
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
grid = []
for i in range(N):
    temp = list(map(int, input().split()))
    grid.append(temp)
visited = [[[False for _ in range(2)] for _ in range(M)] for _ in range(N)]


def bfs():
    q = deque()
    q.append((0, 0, 0, 0))

    visited[0][0][0] = True

    while q:
        x, y, count, g = q.popleft()

        if (x == N-1 and y == M-1):
            return count
        for i in range(4):
            nx = x+dx[i]
            ny = y + dy[i]

            if 0 <= nx < N and 0 <= ny < M:
                if visited[nx][ny][g]:
                    continue
                elif grid[nx][ny] == 2:
                    q.append((nx, ny, count+1, 1))
                    visited[nx][ny][0] = True
                elif g == 1:
                    q.append((nx, ny, count+1, 1))
                    visited[nx][ny][1] = True
                elif grid[nx][ny] == 0 and g == 0:
                    q.append((nx, ny, count+1, 0))
                    visited[nx][ny][0] = True

    return -1


answer = bfs()
if (answer == -1 or answer > T):
    print("Fail")
else:
    print(answer)
