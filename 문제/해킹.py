import sys
import heapq
input = sys.stdin.readline

tc = int(input())
INF = 1e9 + 1
for i in range(tc):
    N, D, C = map(int, input().split(" "))
    graph = [[] for _ in range(N+1)]
    for i in range(D):
        end, start, weight = map(int, input().split(" "))
        graph[start].append([end, weight])

    dist = [INF] * (N+1)
    q = []
    dist[C] = 0
    heapq.heappush(q, [0, C])
    count = 0
    while(q):

        cost, cur = heapq.heappop(q)

        if(cost > dist[cur]):
            continue

        for nextCur, nextCost in graph[cur]:
            distance = nextCost+cost

            if(distance < dist[nextCur]):
                dist[nextCur] = distance
                heapq.heappush(q, [distance, nextCur])
    max_dist = 0
    for i in dist:
        if i != INF:
            if max_dist < i:
                max_dist = i
            count += 1

    print(count, max_dist)
