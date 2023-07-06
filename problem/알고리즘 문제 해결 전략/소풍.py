import sys

input = sys.stdin.readline
T = int(input())


def comb(visited):
    first = -1
    count = 0

    for i in range(N):
        if not visited[i]:
            first = i
            break

    if first == -1:
        return 1

    for i in range(first+1, N):
        if not visited[i] and friends[first][i]:
            visited[first], visited[i] = True, True
            count += dfs(visited)
            visited[first], visited[i] = False, False

    return count


for _ in range(T):
    N, M = map(int, input().split())
    visited = [False for _ in range(N)]
    temp = list(map(int, input().split()))
    peoples = [i for i in range(N)]

    friends = [[0 for _ in range(N)] for _ in range(N)]

    for i in range(0, len(temp), 2):
        A, B = temp[i], temp[i+1]
        friends[A][B] = 1
        friends[B][A] = 1

    print(comb(visited))
