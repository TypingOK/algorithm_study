import sys
input = sys.stdin.readline


def find(parents, x):
    if parents[x] != x:
        parents[x] = find(parents, parents[x])

    return parents[x]


def union(x, y, parents):
    root_x = find(parents, x)
    root_y = find(parents, y)

    if root_x < root_y:
        parents[root_y] = root_x
    else:
        parents[root_x] = root_y


N, M = map(int, input().split())
edges = []
parents = [i for i in range(N+1)]

for i in range(M):
    a, b, c = map(int, input().split())
    edges.append((c, a, b))

edges.sort()

answer = 0
last = 0
for edge in edges:
    c, a, b = edge
    if find(parents, a) != find(parents, b):
        union(a, b, parents)
        answer += c
        last = c
print(answer-last)
