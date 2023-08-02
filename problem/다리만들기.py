import sys
from collections import deque
input = sys.stdin.readline

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

N = int(input())
visited = [[False for _ in range(N)] for _ in range(N)]
answer = sys.maxsize


def first_bfs(c, startX, startY):
    q = deque()
    q.append((startX, startY))
    visited[startX][startY] = True
    grid[startX][startY] = c
    while (q):
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny] and grid[nx][ny] == 1:
                grid[nx][ny] = c
                visited[nx][ny] = True
                q.append((nx, ny))
    return


def second_bfs(startX, startY):
    q = deque()
    q.append((startX, startY, 0))
    visit = [[False for _ in range(N)] for _ in range(N)]

    while (q):
        x, y, count = q.popleft()
        # print(x, y, count)
        # for i in range(N):
        #     for j in range(N):
        #         print(visit[i][j], end=" ")
        #     print()
        # print()
        if count > answer:
            continue
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < N and not visit[nx][ny] and grid[nx][ny] == 0:
                visit[nx][ny] = True
                q.append((nx, ny, count+1))
            elif 0 <= nx < N and 0 <= ny < N and not visit[nx][ny] and grid[nx][ny] != 0 and grid[nx][ny] != grid[startX][startY]:
                return count
    return sys.maxsize


grid = []
for i in range(N):
    temp = list(map(int, input().split()))
    grid.append(temp)
count = 1
for i in range(N):
    for j in range(N):
        if not visited[i][j] and grid[i][j] == 1:
            first_bfs(count, i, j)
            count += 1
            # print(count)
# for i in range(N):
#     for j in range(N):
#         print(visited[i][j], end=" ")
#     print()

for i in range(N):
    for j in range(N):
        if grid[i][j] != 0:
            result = second_bfs(i, j)
            answer = min(result, answer)

# for i in range(N):
#     for j in range(N):
#         print(grid[i][j], end=" ")
#     print()

print(answer)
