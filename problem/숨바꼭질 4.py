import sys
from collections import deque

input = sys.stdin.readline
N, K = map(int, input().split())


def bfs(N, K):
    q = deque()
    q.append(N)
    visited = [False] * 100001
    path = [0] * 100001

    count = 0
    while q:
        size = len(q)
        count += 1
        for _ in range(size):

            x = q.popleft()
            if x == K:
                print(count - 1)
                temp = x
                arr = []
                for i in range(count):
                    arr.append(temp)
                    temp = path[temp]
                print(" ".join(map(str, arr[::-1])))
                return

            for i in (x-1, x+1, 2*x):
                if 0 <= i < 100001 and not visited[i]:
                    q.append(i)

                    visited[i] = True
                    path[i] = x


bfs(N, K)
