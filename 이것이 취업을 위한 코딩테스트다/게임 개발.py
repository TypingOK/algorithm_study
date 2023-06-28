import sys
input = sys.stdin.readline
dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]

N, M = map(int, input().split())
x, y, d = map(int, input().split())
visited = [[False for _ in range(M)] for _ in range(N)]

grid = []
for i in range(N):
    temp = list(map(int, input().split()))
    grid.append(temp)

visited[x][y] = True


def turn_left(d):
    d -= 1
    if d < 0:
        d = 3
    return d


count = 1
turn_time = 0

while True:
    d = turn_left(d)
    nx = x + dx[d]
    ny = y + dy[d]

    if 0 <= nx < N and 0 <= ny < M and grid[nx][ny] == 0 and not visited[nx][ny]:
        visited[nx][ny] = True
        x = nx
        y = ny
        count += 1
        turn_time = 0
        continue
    else:
        turn_time += 1

    if turn_time == 4:
        nx = x - dx[d]
        ny = y - dy[d]

        if 0 <= nx < N and 0 <= ny < M and grid[nx][ny] == 0:
            x = nx
            y = ny
        else:
            break
        turn_time = 0

print(count)
