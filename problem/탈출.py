import sys
from collections import deque

input = sys.stdin.readline

N, T, G = map(int, input().split())


def bfs(N, T, G):
    q = deque()
    q.append((N, 0))
    visited = [False] * 100000
    visited[N] = True
    minAnswer = T+1
    while q:
        x, count = q.popleft()

        if x == G:
            minAnswer = min(minAnswer, count)
            continue
        if count > T:
            break
        temp = x+1
        if temp < 100000 and not visited[temp]:
            q.append((temp, count+1))
            visited[temp] = True
        temp = x*2
        if 0 < temp < 100000:
            temp = str(temp)
            temp = int(str(int(temp[0])-1) + temp[1:])
            if not visited[temp]:
                q.append((temp, count+1))
                visited[temp] = True
    return minAnswer


answer = bfs(N, T, G)
if answer == T+1:
    print("ANG")
else:
    print(answer)
