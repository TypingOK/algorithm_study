import sys
from collections import deque
input = sys.stdin.readline

s, t = map(int, input().split())


def bfs(s, t):
    q = deque()
    visited = set()
    q.append((s, ""))
    visited.add(s)
    max_num = 1000000001

    while q:
        x, y = q.popleft()

        if x == t:
            return y

        if 0 <= x*x <= max_num and x*x not in visited:
            q.append((x*x, y+"*"))
            visited.add(x*x)

        if 0 <= x+x <= max_num and x+x not in visited:
            q.append((x+x, y+"+"))
            visited.add(x+x)

        if x != 0 and 0 <= x//x <= max_num and x//x not in visited:
            q.append((x//x, y+"/"))
            visited.add(x//x)

    return -1


if s == t:
    print(0)
else:
    answer = bfs(s, t)
    print(answer)
