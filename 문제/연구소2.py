from copy import deepcopy
import sys
from itertools import combinations
from collections import deque


def BFS(position, visited, copy):
    q = deque()
    for i in range(len(position)):
        q.append(position[i])
        visited[position[i][0]][position[i][1]] = True
    maxNum = 0
    while q:
        x, y = q.popleft()
        maxNum = max(copy[x][y], maxNum)
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny] and copy[nx][ny] != '-':
                visited[nx][ny] = True
                copy[nx][ny] = copy[x][y]+1
                q.append([nx, ny])
    return maxNum


input = sys.stdin.readline

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

N, M = map(int, input().split())

virus = []

e = []
for i in range(N):
    temp = list(map(int, input().split()))
    for j in range(N):
        if(temp[j] == 2):
            virus.append([i, j])
            temp[j] = 0
        if(temp[j] == 1):
            temp[j] = "-"
    e.append(temp)
temp = list(combinations(virus, M))


minNum = 99999999999

flag = 0
index = 0
for i in temp:
    index += 1
    visited = [[False for _ in range(N)] for _ in range(N)]
    copy = deepcopy(e)
    result = BFS(i, visited, copy)
    count = 0
    for i in range(N):
        for j in range(N):
            if (copy[i][j] == 0):
                count += 1
    if count > M:
        flag += 1
    else:
        minNum = min(result, minNum)

if flag >= len(temp):
    print(-1)
else:
    print(minNum)
