import sys
from collections import deque

F, S, G, U, D = map(int, sys.stdin.readline().split())

visited = [False] * (F+1)


def bfs(F, S, G, U, D):
    q = deque()
    q.append((S, 0))
    visited[S] = True

    while q:
        x, count = q.popleft()
        if x == G:
            return count

        if 0 < x+U <= F and not visited[x+U]:
            q.append((x+U, count+1))
            visited[x+U] = True
        if 0 < x-D <= F and not visited[x-D]:
            q.append((x-D, count+1))
            visited[x-D] = True

    return -1


answer = bfs(F, S, G, U, D)
if answer == -1:
    print("use the stairs")
else:
    print(answer)
