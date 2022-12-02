import sys
import heapq

input = sys.stdin.readline

N = int(input())
M = int(input())

graph = [[] for _ in range(N+1)]
visited = [False] * (N+1)

for i in range(M):
    start, end, weight = map(int, input().split(" "))
    graph[start].append([end, weight])
    graph[end].append([start, weight])

q = [[0, 1]]

count = 0
answer = 0

while(q):

    if(count == N):
        break

    cost, cur = heapq.heappop(q)

    if not visited[cur]:
        answer += cost
        visited[cur] = True
        count += 1

        for nextCur, nextCost in graph[cur]:
            heapq.heappush(q, [nextCost, nextCur])
print(answer)
