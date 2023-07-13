import sys
from collections import deque
input = sys.stdin.readline
N = int(input())

graph = [[] for i in range(N+1)]
indegree = [0 for _ in range(N+1)]
times = [0]
for i in range(1, N+1):
    temp = list(map(int, input().split()))
    times.append(temp[0])
    for j in range(1, len(temp)):
        if temp[j] != -1:
            graph[temp[j]].append(i)
            indegree[i] += 1
        else:
            break
dp = [0 for _ in range(N+1)]
q = deque()

for i in range(1, N+1):
    if indegree[i] == 0:
        dp[i] += times[i]
        q.append(i)

while q:
    size = len(q)
    for _ in range(size):
        x = q.popleft()
        for i in graph[x]:

            dp[i] = max(dp[i], dp[x] + times[i])
            indegree[i] -= 1

            if indegree[i] == 0:
                q.append(i)

for i in range(1, (N+1)):
    print(dp[i])
