import sys
from collections import deque
input = sys.stdin.readline

N, L, R = map(int, input().split())
graph = []

for i in range(N):
    graph.append(list(map(int, input().split())))


dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]


def bfs(x, y, N):
    q = deque()
    temp = []
    sum_result = 0

    q.append((x, y))

    while q:
        x, y = q.popleft()
        if visited[x][y]:
            continue

        visited[x][y] = True
        sum_result += graph[x][y]
        temp.append((x, y))
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]

            if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny] and L <= abs(graph[nx][ny] - graph[x][y]) <= R:
                q.append((nx, ny))

    if len(temp) <= 1:
        return False
    for i, j in temp:
        result = sum_result // len(temp)
        graph[i][j] = result

    return True


count = 0
while True:
    flag = False
    visited = [[False for _ in range(N)] for _ in range(N)]
    for i in range(N):
        for j in range(N):
            result = bfs(i, j, N)
            if result:
                flag = True
    if not flag:
        break
    count += 1
print(count)
