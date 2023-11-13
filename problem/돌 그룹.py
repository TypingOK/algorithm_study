from collections import deque
import sys
input = sys.stdin.readline


def bfs(X, Y, Z):
    q = deque()
    q.append((X, Y))
    visited[X][Y] = True
    total = X+Y+Z
    while q:
        x, y = q.popleft()
        z = total - x - y
        if x == y == z:
            print(1)
            return

        for a, b in (x, y), (x, z), (y, z):
            if a < b:
                b -= a
                a += a
            elif a > b:
                a -= b
                b += b
            else:
                continue

            c = total - a - b
            x = min(a, b, c)
            y = max(a, b, c)

            if not visited[x][y]:
                q.append((x, y))
                visited[x][y] = True
    print(0)


X, Y, Z = map(int, input().split())
total = X+Y+Z
if total % 3 != 0:
    print(0)
else:
    visited = [[False] * (total + 1) for _ in range(total+1)]
    bfs(X, Y, Z)
