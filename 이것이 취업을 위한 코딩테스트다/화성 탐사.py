from heapq import heappop, heappush
import sys
from collections import deque

input = sys.stdin.readline
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

T = int(input())
for _ in range(T):
    N = int(input())
    graph = []
    for i in range(N):
        temp = list(map(int, input().split()))
        graph.append(temp)

    q = deque()
    d = [[sys.maxsize for _ in range(N)] for _ in range(N)]
    d[0][0] = graph[0][0]
    q.append((0, 0))
    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]

            if 0 <= nx < N and 0 <= ny < N:
                if d[nx][ny] > d[x][y] + graph[nx][ny]:
                    q.append((nx, ny))
                    d[nx][ny] = d[x][y] + graph[nx][ny]

    print(d[N-1][N-1])


# input = sys.stdin.readline
# dx = [-1, 0, 1, 0]
# dy = [0, -1, 0, 1]

# T = int(input())
# for _ in range(T):
#     N = int(input())
#     graph = []
#     for i in range(N):
#         temp = list(map(int, input().split()))
#         graph.append(temp)

#     d = [[sys.maxsize for _ in range(N)] for _ in range(N)]
#     d[0][0] = graph[0][0]
#     q = [(d[0][0], 0, 0)]
#     while q:
#         dist, x, y = heappop(q)
#         if dist > d[x][y]:
#             continue

#         for i in range(4):
#             nx = x+dx[i]
#             ny = y+dy[i]

#             if 0 <= nx < N and 0 <= ny < N:
#                 if d[nx][ny] > dist + graph[nx][ny]:
#                     d[nx][ny] = dist + graph[nx][ny]
#                     heappush(q, (dist + graph[nx][ny], nx, ny))
#     for i in range(N):
#         for j in range(N):
#             print(d[i][j], end=" ")
#         print()
#     print()
#     print(d[N-1][N-1])
