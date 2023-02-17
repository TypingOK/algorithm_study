import sys
from collections import deque

M, N = map(int, input().split())

maze = []
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]


def bfs(x, y, maze, fire):
    global answer
    q = deque()
    q.append([x, y])
    fire_q = deque(fire)
    while (q):
        size = len(q)
        answer += 1
        for _ in range(size):
            temp = q.popleft()
            x = temp[0]
            y = temp[1]
            if (maze[x][y] == 'F'):
                continue
            for i in range(4):
                nx = x+dx[i]
                ny = y+dy[i]
                if 0 <= nx < M and 0 <= ny < N and maze[nx][ny] != 'F' and maze[nx][ny] != "#" and not visit[nx][ny]:
                    maze[nx][ny] = 'J'
                    visit[nx][ny] = True
                    q.append([nx, ny])
                elif 0 > nx or nx >= M or 0 > ny or ny >= N:
                    return True

        fire_size = len(fire_q)
        for _ in range(fire_size):
            temp = fire_q.popleft()
            x = temp[0]
            y = temp[1]
            for i in range(4):
                nx = x+dx[i]
                ny = y+dy[i]

                if 0 <= nx < M and 0 <= ny < N and maze[nx][ny] != 'F' and maze[nx][ny] != "#":
                    maze[nx][ny] = 'F'
                    fire_q.append([nx, ny])

    return False


start = []
fire = []
for i in range(M):
    line = list(input().rstrip("\n"))
    maze.append(line)
    for j in range(N):
        if line[j] == "J":
            start = [i, j]
        elif line[j] == "F":
            fire.append([i, j])
answer = 0
visit = [[False] * N for i in range(M)]
if (bfs(start[0], start[1], maze, fire)):
    print(answer)
else:
    print("IMPOSSIBLE")
