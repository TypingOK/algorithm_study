import heapq
import sys

input = sys.stdin.readline

V, E = map(int, input().split(" "))

start = int(input())

graph = [[] for _ in range(V+1)]

for i in range(E):
    a, b, w = map(int, input().split(" "))
    graph[a].append([b, w])

dist = [(int(1e9))] * (V+1)
dist[start] = 0

q = []
heapq.heappush(q, [0, start])

while q:
    cost, current = heapq.heappop(q)

    if(cost > dist[current]):
        continue

    for nextCur, nextCost in graph[current]:
        distance = cost+nextCost

        if(distance < dist[nextCur]):
            dist[nextCur] = distance
            heapq.heappush(q, [distance, nextCur])

for i in range(1, V+1):
    if(dist[i] != int(1e9)):
        print(dist[i])
    else:
        print("INF")
