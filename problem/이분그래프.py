import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

tc = int(input())


def dfs(idx):
    global result

    for i in graph[idx]:
        if colors[i] == -1:
            if (colors[idx] == 1):
                colors[i] = 2
            else:
                colors[i] = 1
            dfs(i)
        else:
            if (colors[i] == colors[idx]):
                result = False
                return


for i in range(tc):
    V, E = map(int, input().split())

    graph = [[] for i in range(V+1)]
    for i in range(E):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)
    colors = [-1] * (V+1)
    result = True

    for i in range(1, V+1):
        if colors[i] == -1:
            colors[i] = 1

            dfs(i)

            if (not result):
                break
    if (not result):
        print("NO")
    else:
        print("YES")
