from collections import deque
import sys
input = sys.stdin.readline
dx = [-1, -1, -1, 0, 0, 1, 1, 1]
dy = [-1, 0, 1, -1, 1, -1, 0, 1]

N, M, K = map(int, input().split())
A = []
for i in range(N):
    A.append(list(map(int, input().split())))

graph = [[5] * N for _ in range(N)]
tree = [[deque() for _ in range(N)] for _ in range(N)]

for i in range(M):
    x, y, z = map(int, input().split())
    tree[x-1][y-1].append(z)  # 나이, x, y 좌표

for _ in range(K):

    for i in range(N):
        for j in range(N):
            size = len(tree[i][j])
            for k in range(size):
                if graph[i][j] >= tree[i][j][k]:
                    graph[i][j] -= tree[i][j][k]
                    tree[i][j][k] += 1
                else:
                    for _ in range(k, size):
                        graph[i][j] += (tree[i][j].pop()//2)
                    break

    for i in range(N):
        for j in range(N):
            size = len(tree[i][j])
            for k in range(size):
                if tree[i][j][k] % 5 == 0:
                    for l in range(8):
                        nx = i+dx[l]
                        ny = j+dy[l]
                        if 0 <= nx < N and 0 <= ny < N:
                            tree[nx][ny].appendleft(1)
            graph[i][j] += A[i][j]

answer = 0
for i in range(N):
    for j in range(N):
        answer += len(tree[i][j])

print(answer)
