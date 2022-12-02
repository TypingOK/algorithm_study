from collections import deque
import sys

input = sys.stdin.readline

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

N, M = map(int, input().split())

paper = []

for i in range(N):
    temp = list(map(int, input().split()))
    paper.append(temp)

count = 0
max_size = 0

visited = [[False for _ in range(M)] for _ in range(N)]


def bfs(x, y):
    cnt = 1
    q = deque()
    q.append([x, y])
    visited[x][y] = True
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]

            if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny] and paper[nx][ny] == 1:
                cnt += 1
                q.append([nx, ny])
                visited[nx][ny] = True
    return cnt


for i in range(N):
    for j in range(M):
        if(not visited[i][j] and paper[i][j] == 1):
            visited[i][j] = True
            count += 1
            max_size = max(max_size, bfs(i, j))


print(count)
print(max_size)
