import sys

input = sys.stdin.readline
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
N, e, w, s, n = list(map(int, input().split()))
temp = [e, w, s, n]
visited = [[False] * (2 * N+1) for i in range(2 * (N+1))]


def DFS(depth, x, y, count):
    global answer

    if (depth == N):
        # print(count)
        answer += count
        return
    visited[x][y] = True
    for i in range(4):
        nx = x+dx[i]
        ny = y+dy[i]
        if (0 <= nx < 2*N+1 and 0 <= ny < 2*N+1):
            if not visited[nx][ny]:
                DFS(depth+1, nx, ny, count * (temp[i]/100))
                visited[nx][ny] = False


answer = 0
DFS(0, N, N, 1.0)
print(answer)
