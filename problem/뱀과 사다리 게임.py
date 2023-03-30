import sys
from collections import deque

input = sys.stdin.readline
visited = [False] * 101
radder = {}
snake = {}
N, M = map(int, input().split())

for i in range(N):
    temp = list(map(int, input().split()))
    radder[temp[0]] = temp[1]

for i in range(M):
    temp = list(map(int, input().split()))
    snake[temp[0]] = temp[1]


def bfs():
    q = deque()
    q.append(1)
    visited[1] = True

    count = 0

    while q:
        size = len(q)
        count += 1
        for _ in range(size):
            x = q.popleft()
            for i in range(1, 7):
                nx = x+i
                if nx >= 100:
                    return count
                elif 0 < nx < 100 and not visited[nx]:
                    if nx in radder:
                        temp = radder[nx]
                        q.append(temp)
                        visited[nx] = True
                        visited[temp] = True
                    elif nx in snake:
                        temp = snake[nx]
                        q.append(temp)
                        visited[nx] = True
                        visited[temp] = True
                    else:
                        q.append(nx)
                        visited[nx] = True
    return 0


count = bfs()
print(count)
