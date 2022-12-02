import sys
from collections import deque

input = sys.stdin.readline

dx = [-2, -2, 0, 0, 2, 2]
dy = [-1, 1, -2, 2, -1, 1]


def BFS(x, y, N, end):
    q = deque()
    q.append([x, y])
    visited = [[False for _ in range(N)] for _ in range(N)]
    visited[x][y] = True
    count = 0
    while q:
        size = len(q)
        for _ in range(size):
            x, y = q.popleft()
            if(x == end[0] and y == end[1]):
                return count
            for i in range(6):
                nx = x+dx[i]
                ny = y+dy[i]
                if(0 <= nx < N and 0 <= ny < N and not visited[nx][ny]):
                    visited[nx][ny] = True
                    q.append([nx, ny])
        count += 1
    return -1


N = int(input())


point = list(map(int, input().split()))

start = [point[0], point[1]]
end = [point[2], point[3]]
answer = BFS(start[0], start[1], N, end)

print(answer)
