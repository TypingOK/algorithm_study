import sys
from collections import deque

input = sys.stdin.readline
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

N = int(input())
gird = [[0 for _ in range(N)] for _ in range(N)]

K = int(input())

for i in range(K):
    x, y = map(int, input().split())
    gird[x-1][y-1] = 1

L = int(input())
directions = deque()
for i in range(L):
    temp = list(input().split(" "))
    temp[1] = temp[1].rstrip("\n")
    dir = -1
    if temp[1] == "D":
        dir = 1
    else:
        dir = -1
    directions.append((int(temp[0]), dir))


def turn(dir, now_d):

    now_d += dir
    if now_d >= 4:
        now_d %= 4
    elif now_d <= -1:
        now_d = 3
    return now_d


visited = [[False for _ in range(N)] for _ in range(N)]
visited[0][0] = True

snake = deque()
snake.append((0, 0))

q = deque()
q.append((0, 0, 0))

answer = 0

for time in range(0, (N*N)):
    x, y, now_d = q.popleft()

    if directions and time == directions[0][0]:
        dir = directions.popleft()
        now_d = turn(dir[1], now_d)
    nx = x + dx[now_d]
    ny = y + dy[now_d]

    if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny]:
        visited[nx][ny] = True
        snake.append((nx, ny))
        if gird[nx][ny] != 1:
            cur = snake.popleft()
            visited[cur[0]][cur[1]] = False
        q.append((nx, ny, now_d))
        gird[nx][ny] = 0
    else:
        answer = time
        break
print(answer + 1)
