import sys
from collections import deque
input = sys.stdin.readline
N, M = map(int, input().split())

graph = [[sys.maxsize for _ in range(N+1)] for _ in range(N+1)]

for i in range(1, N+1):
    for j in range(1, N+1):
        if i == j:
            graph[i][j] = 0

for i in range(M):
    a, b = map(int, input().split())
    graph[a][b] = 1

for k in range(1, N+1):
    for i in range(1, N+1):
        for j in range(1, N+1):
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])
result = 0
for i in range(1, N+1):
    count = 0
    for j in range(1, N+1):
        if graph[i][j] != sys.maxsize or graph[j][i] != sys.maxsize:
            count += 1
    if count >= N:
        result += 1
print(result)
