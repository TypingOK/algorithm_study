import sys
from collections import deque
from copy import deepcopy
input = sys.stdin.readline
N = int(input())
graph = [[] for i in range(N+1)]
times = [0 for i in range(N+1)]
indegree = [0 for i in range(N+1)]

for i in range(1, N+1):
    temp = list(map(int, input().split()))
    times[i] = temp[0]
    for j in range(1, len(temp)-1):
        graph[temp[j]].append(i)
        indegree[i] += 1
result = deepcopy(times)

q = deque()

for i in range(1, N+1):
    if indegree[i] == 0:
        q.append(i)

while q:
    now = q.popleft()
    for i in graph[now]:
        indegree[i] -= 1

        result[i] = max(result[i], result[now] + times[i])
        if indegree[i] == 0:
            q.append(i)
for i in range(1, N+1):
    print(result[i])
