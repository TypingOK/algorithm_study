import sys
from collections import deque

input = sys.stdin.readline
N, M = map(int, input().split())

graph = [[] for _ in range(N+1)]
indegree = [0 for _ in range(N+1)]

for i in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    indegree[b] += 1


def topology_sort():
    result = []
    q = deque()

    # 진입 차수가 0인 녀석만 큐에 집어넣기
    for i in range(1, N+1):
        if indegree[i] == 0:
            q.append(i)

    while q:
        x = q.popleft()
        result.append(x)

        for i in graph[x]:
            indegree[i] -= 1
            if indegree[i] == 0:
                q.append(i)
    return result


answer = topology_sort()
print(" ".join(map(str, answer)))
