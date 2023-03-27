import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split())

q = deque()
visited = [False] * 100001
q.append((N, 0))
visited[N] = True
while q:
    x, count = q.popleft()
    if x == M:
        print(count)
        break

    for i in (x*2, x-1, x+1):
        if 0 <= i < 100001 and not visited[i]:
            if i == (x*2):
                q.appendleft((i, count))
                visited[i] = True
            if i == x-1 or i == x+1:
                q.append((i, count+1))
                visited[i] = True
