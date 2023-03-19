import sys
input = sys.stdin.readline

A, B, C = map(int, input().split())
visited = [[False for _ in range(201)] for _ in range(201)]
answer = [False] * 201


def dfs(a, b, c):
    if (visited[a][b]):
        return
    if a == 0:
        answer[c] = True

    visited[a][b] = True
    # A -> B
    if (a+b) > B:
        dfs((a+b)-B, B, c)
    else:
        dfs(0, (a+b), c)
    # B -> A
    if (a+b) > A:
        dfs(A, (a+b)-A, c)
    else:
        dfs((a+b), 0, c)
    # C -> A
    if (c+a) > A:
        dfs(A, b, (a+c)-A)
    else:
        dfs((a+c), b, 0)
    # C -> B
    if (c+b) > B:
        dfs(a, B, (c+b)-B)
    else:
        dfs(a, (c+b), 0)
    # A -> C
    dfs(0, b, (a+c))
    # B -> C
    dfs(a, 0, (b+c))


dfs(0, 0, C)
for i in range(201):
    if answer[i]:
        print(i, end=" ")
