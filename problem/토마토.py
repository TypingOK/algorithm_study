import sys
from collections import deque
input = sys.stdin.readline

M, N, H = map(int, input().split())
dx = [1, 0, -1, 0, 0, 0]
dy = [0, 1, 0, -1, 0, 0]
dh = [0, 0, 0, 0, 1, -1]

grid = []
start = []
for i in range(H):
    temp = []
    for j in range(N):
        t = list(map(int, input().split()))
        for k in range(M):
            if t[k] == 1:
                start.append([i, j, k])
        temp.append(t)
    grid.append(temp)
visited = [[[False for _ in range(M)] for _ in range(N)] for _ in range(H)]


def bfs():
    q = deque()
    for i in start:
        q.append((i[0], i[1], i[2]))
    count = 0
    while q:
        size = len(q)
        for _ in range(size):
            h, x, y = q.popleft()

            for i in range(6):
                nx = dx[i] + x
                ny = dy[i] + y
                nh = dh[i] + h

                if 0 <= nx < N and 0 <= ny < M and 0 <= nh < H and not visited[nh][nx][ny] and grid[nh][nx][ny] == 0:
                    q.append((nh, nx, ny))
                    visited[nh][nx][ny] = True
                    grid[nh][nx][ny] = 1
        count += 1

    return count - 1


answer = bfs()
for i in range(H):
    for j in range(N):
        for k in range(M):
            if grid[i][j][k] == 0:
                print(-1)
                exit()

print(answer)
