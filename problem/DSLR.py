import sys
from collections import deque

input = sys.stdin.readline
T = int(input())


def bfs(a, b):
    q = deque()
    visited = [False] * 10000
    q.append((a, ""))
    visited[a] = True

    while q:
        x, y = q.popleft()

        if x == b:
            return y

        temp = (x*2) % 10000
        if not visited[temp]:
            q.append((temp, y+"D"))
            visited[temp] = True
        temp = (x-1) % 10000
        if not visited[temp]:
            q.append((temp, y+"S"))
            visited[temp] = True
        temp = (10*x+(x//1000)) % 10000
        if not visited[temp]:
            visited[temp] = True
            q.append((temp, y+"L"))
        temp = (x//10+(x % 10)*1000) % 10000
        if not visited[temp]:
            visited[temp] = True
            q.append((temp, y+"R"))


for _ in range(T):
    A, B = map(int, input().split())
    answer = bfs(A, B)
    print(answer)
