import sys
from copy import deepcopy
input = sys.stdin.readline
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]


N, M = map(int, input().split())

graph = []
for i in range(N):
    temp = list(map(int, input().split()))
    graph.append(temp)
result = 0


def move(x, y, temp):
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < N and 0 <= ny < M and temp[nx][ny] == 0:
            temp[nx][ny] = 2
            move(nx, ny, temp)


def dfs(count):
    global result
    if count == 3:
        temp = deepcopy(graph)
        zero = 0
        for i in range(N):
            for j in range(M):
                if temp[i][j] == 2:
                    move(i, j, temp)
        for i in range(N):
            for j in range(M):
                if temp[i][j] == 0:
                    zero += 1
        result = max(result, zero)
        return

    for i in range(N):
        for j in range(M):
            if graph[i][j] == 0:
                graph[i][j] = 1
                dfs(count + 1)
                graph[i][j] = 0


dfs(0)
print(result)
