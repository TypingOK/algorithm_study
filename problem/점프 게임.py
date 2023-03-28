import sys
from collections import deque
input = sys.stdin.readline

N, K = map(int, input().split())

grid = [[0]*(200001) for _ in range(2)]
for i in range(2):
    temp = list(input().rstrip("\n"))
    for j in range(N):
        grid[i][j] = int(temp[j])


def bfs(N, K):
    index_y = 0
    visited = [[False] * (200001) for _ in range(2)]
    board = [[False] * (200001) for _ in range(2)]
    visited[0][0] = True
    q = deque()
    q.append((0, 0))

    while q:
        size = len(q)
        for _ in range(size):
            x, y = q.popleft()
            # print(x, y)
            if board[x][y]:
                continue
            for i in (y-1, y+1):
                if (i > N or (i == N and grid[x][i] == 1)):
                    return 1
                if 0 <= i < 200001 and grid[x][i] == 1 and not visited[x][i]:
                    q.append((x, i))
                    visited[x][i] = True
            for i in (x-1, x+1):
                if 0 <= i < 2 and (y+K > N):
                    return 1
                if 0 <= i < 2 and 0 <= y+K < 200001 and grid[i][y+K] == 1 and not visited[i][y+K]:
                    q.append((i, y+K))
                    visited[i][y+K] = True
        board[0][index_y] = True
        board[1][index_y] = True
        index_y += 1

    return 0


answer = bfs(N-1, K)
print(answer)
