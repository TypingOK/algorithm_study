import sys
from collections import deque
input = sys.stdin.readline

T = int(input())


def topology_sort():

    q = deque()

    for i in range(1, N+1):
        if indegree[i] == 0:
            q.append(i)
            dp[i] += build_time[i]

    # print(result)
    while q:
        size = len(q)

        for s in range(size):
            x = q.popleft()

            for i in graph[x]:
                indegree[i] -= 1
                dp[i] = max(dp[i], build_time[i] + dp[x])

                if indegree[i] == 0:
                    q.append(i)

        # print(x, max_build_time, result)``


for _ in range(T):

    N, K = map(int, input().split())
    build_time = [0]+list(map(int, input().split()))
    dp = [0 for _ in range(N+1)]
    graph = [[] for _ in range(N+1)]
    indegree = [0 for _ in range(N+1)]
    for i in range(K):
        a, b = map(int, input().split())
        graph[a].append(b)
        indegree[b] += 1

    victory_tower = int(input())

    topology_sort()
    print(dp[victory_tower])
