import sys
input = sys.stdin.readline
N, M = map(int, input().split())
graph = []

for i in range(N):
    temp = list(map(int, input().split()))
    graph.append(temp)


def calcIdx(x, y):
    return x * M + y


def solve(idx, count):
    if idx == N * M:
        global answer
        answer = (max(answer, count))
        return

    if visited[idx]:
        return

    x = idx // M
    y = idx % M

    eIdx = calcIdx(x, y+1)
    wIdx = calcIdx(x, y-1)
    sIdx = calcIdx(x+1, y)
    nIdx = calcIdx(x-1, y)

    if (x+1 < N and not visited[sIdx] and (y+1 < M and not visited[eIdx])):
        visited[idx] = True
        visited[sIdx] = True
        visited[eIdx] = True
        for i in range(idx+1, N*M+1):
            solve(i, count + (graph[x][y] * 2 + graph[x+1][y] + graph[x][y+1]))
        visited[idx] = False
        visited[sIdx] = False
        visited[eIdx] = False

    if (y-1 >= 0 and not visited[wIdx] and (x+1 < N and not visited[sIdx])):
        visited[idx] = True
        visited[wIdx] = True
        visited[sIdx] = True
        for i in range(idx+1, N*M+1):
            solve(i, count + (graph[x][y] * 2 +
                  graph[x][y-1] + graph[x+1][y]))
        visited[idx] = False
        visited[wIdx] = False
        visited[sIdx] = False

    if (y-1 >= 0 and not visited[wIdx] and (x-1 >= 0 and not visited[nIdx])):
        visited[idx] = True
        visited[wIdx] = True
        visited[nIdx] = True
        for i in range(idx+1, N*M+1):
            solve(i, count + (graph[x][y] * 2 + graph[x][y-1] + graph[x-1][y]))
        visited[idx] = False
        visited[wIdx] = False
        visited[nIdx] = False

    if (x-1 >= 0 and not visited[nIdx] and (y+1 < M and not visited[eIdx])):
        visited[idx] = True
        visited[nIdx] = True
        visited[eIdx] = True
        for i in range(idx+1, N*M+1):
            solve(i, count + (graph[x][y] * 2 + graph[x-1][y] + graph[x][y+1]))
        visited[idx] = False
        visited[nIdx] = False
        visited[eIdx] = False


if N < 2 or M < 2:
    print(0)
else:
    visited = [False for _ in range(N*M)]
    answer = 0

    for i in range(N*M):
        solve(i, 0)
    print(answer)
