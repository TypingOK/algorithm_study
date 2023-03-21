import sys
from collections import deque

input = sys.stdin.readline

dx = [1, 0, -1, 0, 0, 0]
dy = [0, 1, 0, -1, 0, 0]
up = [0, 0, 0, 0, 1, -1]


def bfs(start, end):
    q = deque()
    q.append((start[0], start[1], start[2], 0))
    visited = [[[False for _ in range(C)] for _ in range(R)] for _ in range(L)]
    visited[start[0]][start[1]][start[2]] = True

    while q:
        z, x, y, count = q.popleft()
        if z == end[0] and x == end[1] and y == end[2]:
            return count

        for i in range(6):
            nx = x + dx[i]
            ny = y + dy[i]
            nz = z + up[i]

            if (0 <= nx < R and 0 <= ny < C and 0 <= nz < L and not visited[nz][nx][ny] and grid[nz][nx][ny] != "#"):
                q.append((nz, nx, ny, count+1))
                visited[nz][nx][ny] = True

    return -1


while True:
    L, R, C = map(int, input().split())
    if (L == 0 and R == 0 and C == 0):
        break

    grid = []
    start = [0, 0, 0]
    end = [0, 0, 0]
    for i in range(L):
        temp = []
        for j in range(R):
            a = list(input().rstrip("\n"))
            for k in range(C):
                if (a[k] == "S"):
                    start[0] = i
                    start[1] = j
                    start[2] = k
                elif (a[k] == "E"):
                    end[0] = i
                    end[1] = j
                    end[2] = k

            temp.append(a)

        grid.append(temp)
        gabage = input()
    answer = bfs(start, end)
    if (answer > 0):
        print("Escaped in", answer, "minute(s).")
    else:
        print("Trapped!")
