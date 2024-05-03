import sys
from collections import deque

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]


def bfs(i, j, visited, out_air):
    q = deque()
    q.append((i, j))

    visited[i][j] = True
    stack = [[0 for _ in range(M)] for _ in range(N)]

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]

            if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny]:
                if graph[nx][ny] == 0 and out_air[nx][ny]:
                    stack[x][y] += 1
                elif graph[nx][ny] == 1:
                    visited[nx][ny] = True
                    q.append((nx, ny))
    for i in range(N):
        for j in range(M):
            if stack[i][j] >= 2:
                graph[i][j] = 0


input = sys.stdin.readline
N, M = map(int, input().split())

graph = []
for i in range(N):
    temp = list(map(int, input().split()))
    graph.append(temp)

count = 0
while True:
    out_air = [[False for _ in range(M)] for _ in range(N)]
    q = deque()
    # 가장자리는 반드시 치즈가 없음
    q.append((0, 0))

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < M and graph[nx][ny] == 0 and not out_air[nx][ny]:
                out_air[nx][ny] = True
                q.append((nx, ny))

    exit_flag = False
    visited = [[False for _ in range(M)] for _ in range(N)]

    for i in range(N):
        for j in range(M):
            if graph[i][j] == 1 and not visited[i][j]:
                exit_flag = True
                bfs(i, j, visited, out_air)

    # print(count, "--------------------------------------------")
    # for i in range(N):
    #     for j in range(M):
    #         print(graph[i][j], end=" ")
    #     print()
    # print()
    if not exit_flag:
        break
    count += 1

print(count)
