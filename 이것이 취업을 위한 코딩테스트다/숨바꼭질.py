import sys
from heapq import heappop, heappush

input = sys.stdin.readline
N, M = map(int, input().split())

graph = [[] for _ in range(N+1)]
distance = [sys.maxsize for _ in range(N+1)]

for i in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

distance[1] = 0
q = [(0, 1)]

while q:
    dist, x = heappop(q)

    if distance[x] < dist:
        continue

    for i in graph[x]:
        if distance[i] > 1 + dist:
            distance[i] = dist+1
            heappush(q, (dist+1, i))

answer = 0
for i in range(1, N+1):
    if distance[i] != sys.maxsize:
        answer = max(answer, distance[i])
index = distance.index(answer)
count = distance.count(answer)

print(index, answer, count)
