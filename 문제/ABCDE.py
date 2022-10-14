import sys
input = sys.stdin.readline

N, M = map(int, input().split())

graph = [[] for _ in range(N)]
visited = [False] * N


def DFS(count, graph, cur, M, visited):
    if(count >= 4):
        print(1)
        exit(0)

    for i in graph[cur]:
        if(not visited[i]):
            visited[i] = True
            DFS(count+1, graph, i, M, visited)
            visited[i] = False


for _ in range(M):
    a, b = map(int, input().split())

    graph[a].append(b)
    graph[b].append(a)

test = False
for i in range(N):
    visited[i] = True
    DFS(0, graph, i, M, visited)
    visited[i] = False
print(0)
