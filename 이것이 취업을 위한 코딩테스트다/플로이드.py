import sys
input = sys.stdin.readline
N = int(input())
M = int(input())

graph = [[sys.maxsize for _ in range(N)] for _ in range(N)]

for i in range(M):
    a, b, c = map(int, input().split())
    graph[a-1][b-1] = min(graph[a-1][b-1], c)

for k in range(N):
    for i in range(N):
        for j in range(N):
            if i != j:
                graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

for i in range(N):
    for j in range(N):
        if graph[i][j] != sys.maxsize:
            print(graph[i][j], end=" ")
        else:
            print(0, end=" ")
    print()
