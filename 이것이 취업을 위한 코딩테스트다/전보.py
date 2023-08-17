import sys
from heapq import heappop, heappush
INF = int(1e9)
input = sys.stdin.readline

N, M, C = map(int, input().split())

graph = [[] for _ in range(N+1)]

for i in range(M):
    x, y, z = map(int, input().split())
    graph[x].append((z, y))

distance = [INF for _ in range(N+1)]
heap = []
heappush(heap, (0, C))
distance[C] = 0

while heap:
    dist, now = heappop(heap)
    if distance[now] < dist:
        continue

    for cost, node in graph[now]:
        if distance[node] > cost + dist:
            distance[node] = cost + dist
            heappush(heap, (cost+dist, node))
count = 0
answer = 0
for i in range(1, N+1):
    if distance[i] != INF and distance[i] != 0:
        count += 1
        answer = max(answer, distance[i])

print(count, answer)
