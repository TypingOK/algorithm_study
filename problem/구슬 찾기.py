import sys

N, M = map(int, sys.stdin.readline().split())

mid = (N+1)//2

big = [[] for _ in range(N+1)]
small = [[] for _ in range(N+1)]

for _ in range(M):
    a, b = map(int, sys.stdin.readline().split())
    big[a].append(b)
    small[b].append(a)


def dfs(a, n):
    global count

    for i in a[n]:
        if not visited[i]:
            visited[i] = True
            count += 1
            dfs(a, i)


answer = 0
for i in range(1, N+1):
    visited = [False] * (N+1)

    count = 0
    dfs(big, i)
    if count >= mid:
        answer += 1
    count = 0
    dfs(small, i)
    if count >= mid:
        answer += 1
print(answer)
