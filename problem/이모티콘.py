import sys
from collections import deque


N = int(sys.stdin.readline())

dx = [0, 1, 2]
visited = [[-1] * (N+1) for i in range(N+1)]
visited[1][0] = 0  # 화면에 하나, 클립보드엔 없음

q = deque()
q.append((1, 0))  # 현재 화면에 나와있는 이모티콘, 클립보드에 있는 모든 이모티콘
answer = 0

while q:
    now, clip = q.popleft()

    if now == N:
        answer = visited[now][clip]
        break

    for i in dx:
        if i == 0 and visited[now][now] == -1:
            visited[now][now] = visited[now][clip] + 1
            q.append((now, now))
        elif i == 1 and clip != 0 and now+clip <= N and visited[now+clip][clip] == -1:
            visited[now+clip][clip] = visited[now][clip] + 1
            q.append((now+clip, clip))
        elif i == 2 and now-1 > 0 and visited[now-1][clip] == -1:
            visited[now-1][clip] = visited[now][clip] + 1
            q.append((now-1, clip))
print(answer)
