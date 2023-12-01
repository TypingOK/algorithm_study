import sys
from heapq import heappush, heappop, heapify
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    K = int(input())
    chapters = list(map(int, input().split()))

    heapify(chapters)
    count = 0

    while len(chapters) > 1:
        x1 = heappop(chapters)
        x2 = heappop(chapters)
        y = x1+x2
        count += y
        heappush(chapters, y)
    print(count)
