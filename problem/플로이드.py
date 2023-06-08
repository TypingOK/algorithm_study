import sys
input = sys.stdin.readline

INF = 987654321
N = int(input())
M = int(input())

graph = [[INF for _ in range(N+1)] for _ in range(N+1)]

for i in range(M):
    a, b, w = map(int, input().split())

    graph[a][b] = min(graph[a][b], w)

for k in range(1, N+1):
    for i in range(1, N+1):
        for j in range(1, N+1):
            if i != j:
                graph[i][j] = min(graph[i][j], graph[i][k]+graph[k][j])

for i in range(1, N+1):
    for j in range(1, N+1):
        if graph[i][j] != INF:
            print(graph[i][j], end=" ")
        else:
            print(0, end=" ")
    print()
