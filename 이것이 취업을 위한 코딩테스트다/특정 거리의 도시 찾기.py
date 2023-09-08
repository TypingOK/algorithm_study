import sys
from heapq import heappush, heappop
input = sys.stdin.readline
INF = 1e9

N, M, K, X = map(int, input().split())

distance = [INF for _ in range(N+1)]
graph = [[] for _ in range(N+1)]

for i in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)

heap = []
distance[X] = 0
heappush(heap, (0, X))

while heap:
    dist, now = heappop(heap)

    if distance[now] < dist:
        continue

    for index in graph[now]:
        if distance[index] > dist + 1:
            distance[index] = dist + 1
            heappush(heap, (dist+1, index))

flag = False
for i in range(1, N+1):
    if distance[i] == K:
        print(i)
        if not flag:
            flag = True

if not flag:
    print(-1)
