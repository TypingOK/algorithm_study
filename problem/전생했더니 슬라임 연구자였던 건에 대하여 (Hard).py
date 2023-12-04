import sys
from heapq import heappop, heappush, heapify

input = sys.stdin.readline
T = int(input())

for _ in range(T):
    N = int(input())
    s = list(map(int, input().split()))
    heapify(s)

    count = 0
    while len(s) > 1:
        x1 = heappop(s)
        x2 = heappop(s)
        y = x1 * x2
        if (count > 0):
            count *= y
        else:
            count += y
        heappush(s, y)
    if count > 1:
        print(count % 1000000007)
    else:
        print(1)
