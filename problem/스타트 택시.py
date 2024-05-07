import sys
from collections import deque
input = sys.stdin.readline
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

N, M, F = map(int, input().split())
graph = []
S = [[0 for _ in range(N)]for _ in range(N)]
E = dict()

for i in range(N):
    temp = list(map(int, input().split()))
    graph.append(temp)

taxi = list(map(int, input().split()))
taxi[0] -= 1
taxi[1] -= 1

for i in range(M):
    temp = list(map(int, input().split()))
    S[temp[0]-1][temp[1]-1] = i+1
    E[i+1] = (temp[2]-1, temp[3]-1)

for _ in range(M):
    number = 0
    if S[taxi[0]][taxi[1]] != 0:
        number = S[taxi[0]][taxi[1]]
        S[taxi[0]][taxi[1]] = 0
    else:
        q = deque()
        q.append((taxi[0], taxi[1], F, 0))
        visited = [[False for _ in range(N)] for _ in range(N)]
        visited[taxi[0]][taxi[1]] = True
        H = []
        while q:
            x, y, f, c = q.popleft()
            if f <= 0:
                continue
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]

                if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny] and graph[nx][ny] != 1:
                    if graph[nx][ny] == 0 and S[nx][ny] != 0:
                        visited[nx][ny] = True
                        H.append((c+1, nx, ny, f-1))
                        q.append((nx, ny, f-1, c+1))
                    elif graph[nx][ny] == 0:
                        q.append((nx, ny, f-1, c+1))
                        visited[nx][ny] = True
        if H:
            H.sort(key=lambda x: (x[0], x[1], x[2]))

            co, sx, sy, sf = H[0]
            taxi[0] = sx
            taxi[1] = sy

            number = S[sx][sy]
            F = sf
            S[sx][sy] = 0

    count = 0
    q = deque()
    q.append((taxi[0], taxi[1], F, count))
    visited = [[False for _ in range(N)] for _ in range(N)]
    visited[taxi[0]][taxi[1]] = True
    if (number in E):
        ex, ey = E[number]
        while q:
            flag = False
            x, y, f, c = q.popleft()
            if f <= 0:
                continue

            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]

                if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny] and graph[nx][ny] != 1:
                    if graph[nx][ny] == 0 and nx == ex and ny == ey:
                        del E[number]
                        taxi[0] = nx
                        taxi[1] = ny
                        F = f-1 + ((c+1) * 2)
                        flag = True
                        break
                    elif graph[nx][ny] == 0:
                        q.append((nx, ny, f-1, c+1))
                        visited[nx][ny] = True
            if flag:
                break
    else:
        break


if len(E) > 0:
    print(-1)
    exit()
for i in range(N):
    for j in range(N):
        if S[i][j] != 0:
            print(-1)
            exit()

print(F)
