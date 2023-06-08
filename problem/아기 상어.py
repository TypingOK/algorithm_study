import sys
from collections import deque
input = sys.stdin.readline

# 위 왼쪽 아래 오른쪽
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

N = int(input())
graph = []
x, y = 0, 0
for i in range(N):
    temp = list(map(int, input().split()))
    for j in range(N):
        if temp[j] == 9:
            x = i
            y = j
            temp[j] = 0
    graph.append(temp)
shark = [x, y, 2, 0, 0]

# 큐를 돌려서 물고기를 찾기
def search():
    q = deque()
    x, y, size, exp, count = shark
    visited = [[False for _ in range(N)] for _ in range(N)]
    visited[x][y] = True
    q.append((x, y, size, exp, count))
    # 같은 거리에 있는지 판별 하기 위해 먹이 배열을 생성
    feed = []

    while q:
        x, y, size, exp, count = q.popleft()

        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            # 상어가 갈 수 있는지 체크
            if 0 <= nx < N and 0 <= ny < N and graph[nx][ny] <= size and not visited[nx][ny]:
                # 먹을 수 있으면 먹이 리스트에 넣음
                if 0 < graph[nx][ny] < size:
                    feed.append([nx, ny, count+1])
                # 아니면 이동만
                else:
                    q.append((nx, ny, size, exp, count+1))
                visited[nx][ny] = True
    # 이동한 횟수를 기준으로 정렬, 이동한 횟수가 같으면 세로 가로 순으로 올림차순 정렬
    if (len(feed) > 0):
        feed.sort(key=lambda x: (x[2], x[0], x[1]))
    if feed:
        shark[3] += 1
        if shark[3] == shark[2]:
            shark[3] = 0
            shark[2] += 1
        graph[feed[0][0]][feed[0][1]] = 9
        graph[shark[0]][shark[1]] = 0
        shark[0], shark[1], shark[4] = feed[0][0], feed[0][1], feed[0][2]

        return True

    return False


while True:
    result = search()
    if not result:
        break
print(shark[4])
