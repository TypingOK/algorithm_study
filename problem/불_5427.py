import sys
from collections import deque
from copy import deepcopy

input = sys.stdin.readline
inf = 999999999
T = int(input())
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]


def bfs(start, a, M, N):
    q = deque()
    visit = [([False] * N) for i in range(M)]
    for i in start:
        q.append(i)
        visit[i[0]][i[1]] = True
    a[q[0][0]][q[0][1]] = 1
    while (q):
        temp = q.popleft()
        x = temp[0]
        y = temp[1]
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if 0 <= nx < M and 0 <= ny < N and a[nx][ny] == 0 and not visit[nx][ny]:
                a[nx][ny] = a[x][y]+1
                visit[nx][ny] = True
                q.append([nx, ny])
    return a


for _ in range(T):
    N, M = map(int, input().split(" "))
    build = []
    start = []
    fire = []
    for i in range(M):
        temp = list(input())
        for j in range(len(temp)):
            if (temp[j] == "@"):
                start.append([i, j])
                temp[j] = 0
            elif (temp[j] == "*"):
                fire.append([i, j])
                temp[j] = 0
            elif (temp[j] == "."):
                temp[j] = 0
        build.append(temp)
    fire_result = deepcopy(build)
    man_result = deepcopy(build)
    if (len(fire) >= 1):
        fire_result = bfs(fire, fire_result, M, N)
        man_result = bfs(start, man_result, M, N)
        for i in range(M):
            for j in range(N):
                print(fire_result[i][j], end=" ")
            print()
        print()
        for i in range(M):
            for j in range(N):
                print(man_result[i][j], end=" ")
            print()

        result = inf
        for i in range(M):
            if man_result[i][0] != "#" and man_result[i][0] != 0 and man_result[i][0] < fire_result[i][0]:
                result = min(result, man_result[i][0])
            elif man_result[i][0] != "#" and man_result[i][0] != 0 and fire_result[i][0] == 0:
                result = min(result, man_result[i][0])
            elif man_result[i][N-1] != "#" and man_result[i][N-1] != 0 and man_result[i][N-1] < fire_result[i][N-1]:
                result = min(result, man_result[i][N-1])
            elif man_result[i][N-1] != "#" and man_result[i][N-1] != 0 and fire_result[i][N-1] == 0:
                result = min(result, man_result[i][N-1])
        for i in range(N):
            if man_result[0][i] != "#" and man_result[0][i] != 0 and man_result[0][i] < fire_result[0][i]:
                result = min(result, man_result[0][i])
            elif man_result[0][i] != "#" and man_result[0][i] != 0 and fire_result[0][i] == 0:
                result = min(result, man_result[0][i])
            elif man_result[M-1][i] != "#" and man_result[M-1][i] != 0 and man_result[M-1][i] < fire_result[M-1][i]:
                result = min(result, man_result[M-1][i])
            elif man_result[M-1][i] != '#' and man_result[M-1][i] != 0 and fire_result[M-1][i] == 0:
                result = min(result, man_result[M-1][i])
        if (result == inf):
            print("IMPOSSIBLE")
        else:
            print(result)
    else:
        man_result = bfs(start, man_result, M, N)
        result = inf
        for i in range(M):
            for j in range(N):
                print(man_result[i][j], end=" ")
            print()
        for i in range(M):
            if man_result[i][0] != "#":
                result = min(result, man_result[i][0])
            elif man_result[i][N-1] != "#":
                result = min(result, man_result[i][N-1])
        for i in range(N):
            if man_result[0][i] != "#":
                result = min(result, man_result[0][i])
            elif man_result[M-1][i] != "#":
                result = min(result, man_result[M-1][i])
        if (result == inf):
            print("IMPOSSIBLE")
        else:
            print(result)
