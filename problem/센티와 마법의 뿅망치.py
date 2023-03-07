import sys
from heapq import heappush, heappop

input = sys.stdin.readline

N, H, T = map(int, input().split())

heap = []

for _ in range(N):
    i = int(input())
    heappush(heap, (-i, i))

count = 0
for i in range(T):
    temp = heappop(heap)[1]
    if (temp < H or temp == 1):
        heappush(heap, (-temp, temp))
        break
    count += 1
    heappush(heap, (-(temp//2), temp//2))

answer = heappop(heap)[1]
if (answer >= H):
    print("NO")
    print(answer)
else:
    print("YES")
    print(count)
