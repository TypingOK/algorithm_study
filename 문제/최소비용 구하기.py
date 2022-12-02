import heapq
import sys

input = sys.stdin.readline

N = int(input())
M = int(input())

graph = [[] for _ in range(N+1)]

for i in range(M):
    start, end, weight = map(int, input().split(" "))
    graph[start].append([end, weight])

start, end = map(int, input().split(" "))

q = []
dist = [int(1e9)]*(N+1)
dist[start] = 0

heapq.heappush(q, [0, start])

while(q):
    cost, current = heapq.heappop(q)
    # print(cost, current)
    if(cost > dist[current]):
        continue

    for nextCur, nextCost in graph[current]:
        distance = cost + nextCost

        if distance < dist[nextCur]:
            dist[nextCur] = distance
            heapq.heappush(q, [distance, nextCur])

print(dist[end])
