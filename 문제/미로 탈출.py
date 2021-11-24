# 최소 칸의 개수를 구하기 => bfs 문제.
from collections import deque

# 입력
n, m = map(int, input().split())
graph = []
for i in range(n):
    graph.append(list(map(int, input())))

# 상 하 좌 우로 움직일 때 사용
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(x, y):
    queue = deque()
    queue.append((x, y))
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            # 범위 밖으로 나간 경우 무시
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            # 갈 수 없는 경우 무시
            if graph[nx][ny] == 0:
                continue
            # 처음 방문인 경우 최단 거리 기록
            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y]+1
                queue.append((nx, ny))
    # 가장 오른쪽 아래까지의 최단 거리 반환
    return graph[n-1][m-1]


print(bfs(0, 0))
