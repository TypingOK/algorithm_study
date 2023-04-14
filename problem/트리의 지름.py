import sys
sys.setrecursionlimit(10**9)

input = sys.stdin.readline
N = int(input())
graph = [[] for _ in range(N+1)]


def dfs(x, weight):
    for i in graph[x]:
        a, b = i
        if dist[a] == -1:
            dist[a] = weight+b
            dfs(a, weight+b)


for i in range(N-1):
    A, B, C = map(int, input().split())
    graph[A].append([B, C])
    graph[B].append([A, C])

dist = [-1] * (N+1)
dist[1] = 0
dfs(1, 0)

start = dist.index(max(dist))
dist = [-1] * (N+1)
dist[start] = 0
dfs(start, 0)

print(max(dist))
