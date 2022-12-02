import sys

input = sys.stdin.readline
V, E = map(int, input().split(" "))
graph = []
parent = [i for i in range(V+1)]


def find(v):
    if v != parent[v]:
        parent[v] = find(parent[v])
    return parent[v]


for i in range(E):
    start, end, weight = map(int, input().split(" "))
    graph.append([start, end, weight])

answer = 0

graph.sort(key=lambda x: x[2])

for start, end, weight in graph:
    s = find(start)
    e = find(end)
    if s != e:
        if s > e:
            parent[s] = e
        else:
            parent[e] = s
        answer += weight


print(answer)
