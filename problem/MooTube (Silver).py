import sys
from collections import deque, defaultdict
input = sys.stdin.readline
N, Q = map(int, input().split())

graph = defaultdict(list)
for i in range(N-1):
    p, q, r = map(int, input().split())
    graph[p].append((q, r))
    graph[q].append((p, r))

for _ in range(Q):
    k, v = map(int, input().split())

    count = 0
    q = deque()
    q.append(v)
    visited = [False] * (N+1)
    visited[v] = True
    while q:
        x = q.popleft()

        for i in graph[x]:
            if i[1] >= k and not visited[i[0]]:
                visited[i[0]] = True
                count += 1
                q.append(i[0])

    print(count)
