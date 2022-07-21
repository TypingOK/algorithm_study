import sys
import heapq
INF = 9999999999999

input = sys.stdin.readline

n = int(input())
m = int(input())

city = [[] for _ in range(n+1)]

for i in range(m):
    start, end, weight = map(int, input().split(" "))
    city[start].append([end, weight])

start, end = map(int, input().split())

q = []
dist = [INF] * (n+1)
dist[start] = 0
heapq.heappush(q, [0, start])

parent = [0] * (n+1)

while(q):
    cost, cur = heapq.heappop(q)

    if cost > dist[cur]:
        continue

    for nextCur, nextCost in city[cur]:
        distance = nextCost+cost

        if(distance < dist[nextCur]):
            dist[nextCur] = distance
            parent[nextCur] = cur
            heapq.heappush(q, [distance, nextCur])

answer = [end]
temp = end
while(parent[temp] != 0):
    answer.append(parent[temp])
    temp = parent[temp]
print(dist[end])
print(len(answer))
answer.reverse()
print(*answer)
