import sys
from heapq import heappop, heappush
INF = 1e9

N, M, X = map(int, input().split())
graph = [[] for _ in range(N+1)]


for i in range(M):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))


def dijkstra(start):
    heap = []
    distance = [INF for _ in range(N+1)]

    distance[start] = 0

    heappush(heap, (0, start))

    while heap:
        cost, now = heappop(heap)

        if cost > distance[now]:
            continue

        for index, dist in graph[now]:
            cost_sum = cost+dist
            if distance[index] > cost_sum:
                distance[index] = cost_sum
                heappush(heap, (cost_sum, index))
    return distance


end_result = dijkstra(X)
answer = 0
for i in range(1, N+1):
    start_result = dijkstra(i)

    answer = max(answer, start_result[X]+end_result[i])
print(answer)
