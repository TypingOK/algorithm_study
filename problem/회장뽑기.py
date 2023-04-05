import sys
from collections import deque

input = sys.stdin.readline
N = int(input())
INF = sys.maxsize

graph = [[INF for _ in range(N+1)] for _ in range(N+1)]
for i in range(N+1):
    graph[i][i] = 0

while True:
    a, b = map(int, input().split())
    if a == -1 and b == -1:
        break
    else:
        graph[a][b] = 1
        graph[b][a] = 1

for k in range(1, N+1):
    for i in range(1, N+1):
        for j in range(1, N+1):
            if graph[i][j] == 1 or graph[i][j] == 0:
                continue
            elif graph[i][j] > graph[i][k] + graph[k][j]:
                graph[i][j] = graph[i][k]+graph[k][j]

answer_count = 0
temp = []
for i in range(1, N+1):
    temp.append(max(graph[i][1:]))

answer = min(temp)
print(answer, temp.count(answer))
for i in range(N):
    if answer == temp[i]:
        print(i+1, end=" ")
