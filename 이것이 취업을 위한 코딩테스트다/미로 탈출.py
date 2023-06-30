import sys
from collections import deque

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


def BFS():
    q = deque()
    q.append((0, 0, 1))

    while q:
        x, y, count = q.popleft()
        if x == N-1 and y == M-1:
            return count
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]

            if 0 <= nx < N and 0 <= ny < M and grid[nx][ny] == 1:
                grid[nx][ny] = 0
                q.append((nx, ny, count+1))
    return -1


answer = BFS()
if answer != -1:
    print(answer)
else:
    print("불가능")
