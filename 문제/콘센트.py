import sys
import heapq
input = sys.stdin.readline

N, M = map(int, input().split(" "))

divice = list(map(int, input().split(" ")))


divice.sort(reverse=True)

q = []
for i in divice:
    if len(q) < M:
        heapq.heappush(q, i)
    else:
        temp = heapq.heappop(q)
        heapq.heappush(q, temp+i)
print(max(q))
