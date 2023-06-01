import sys
from collections import deque

input = sys.stdin.readline

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
M, N = map(int, input().split())
wall = []
for i in range(N):
    temp = list(input().rstrip())
    wall.append(list(map(int, temp)))


def bfs(wall, N, M):
    q = deque()
    q.append((0, 0, 0))
    visited = [[False for _ in range(M)] for _ in range(N)]
    while q:
        x, y, count = q.popleft()
        if x == (N-1) and y == (M-1):
            print(count)
            return

        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if 0 <= nx < N and 0 <= ny < M:
                if not visited[nx][ny]:
                    if wall[nx][ny] == 0:
                        q.appendleft((nx, ny, count))
                    elif wall[nx][ny] == 1:
                        q.append((nx, ny, count+1))
                    visited[nx][ny] = True


bfs(wall, N, M)
