import sys
from heapq import heappop, heappush
input = sys.stdin.readline
INF = int(1e9)

N, M, R = map(int, input().split())
answer = 0
items = [0] + list(map(int, input().split()))
graph = [[] for _ in range(N+1)]

for i in range(R):
    a, b, l = map(int, input().split())
    graph[a].append((b, l))
    graph[b].append((a, l))


def dijkstra(start):
    distance = [INF for _ in range(N+1)]
    heap = []
    heappush(heap, (0, start))
    distance[start] = 0
    cost = items[start]
    while heap:
        cost, now = heappop(heap)

        if distance[now] < cost:
            continue
        for index, dist in graph[now]:
            cost_sum = cost + dist
            if distance[index] >= cost_sum:
                if cost_sum >= M:
                    cost += items[index]
                distance[index] = cost_sum
                heappush(heap, (cost_sum, index))
    return distance


for i in range(1, N+1):
    result = dijkstra(i)
    count = 0
    for j in range(1, N+1):
        if result[j] <= M:
            count += items[j]
    answer = max(answer, count)

print(answer)
