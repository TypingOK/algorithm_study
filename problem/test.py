import sys
from collections import deque

input = sys.stdin.readline
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

N, K = map(int, input().split())
graph = []
for i in range(N):
    temp = list(map(int, input().split()))
    graph.append(temp)

board = [[0 for _ in range(N)] for _ in range(N)]
root = [0 for _ in range(K+1)]
di = [0 for _ in range(K+1)]
position = [()]
box = {}

for i in range(1, K+1):
    a, b, c = map(int, input().split())
    board[a-1][b-1] = i
    di[i] = c-1
    position.append((a-1, b-1))
    box[i] = [i]


count = 0

while count <= 1000:
    flag = False
    print(f"Turn {count}:")
    for i in range(1, K+1):
        if root[i] == 0:
            nx = position[i][0] + dx[di[i]]
            ny = position[i][1] + dy[di[i]]

            if 0 <= nx < N and 0 <= ny < N:
                if graph[nx][ny] != 2:
                    if board[nx][ny] == 0:
                        board[nx][ny] = i
                        position[i] = (nx, ny)
                        board[position[i][0]][position[i][1]] = 0
                        if graph[nx][ny] == 1:
                            box[i].reverse()
                            if len(box[i]) == K:
                                flag = True
                                break
                    elif board[nx][ny] != 0:
                        if graph[nx][ny] == 1:
                            box[board[nx][ny]] += box[i][::-1]
                            if len(box[board[nx][ny]]) == K:
                                flag = True
                                break
                        else:
                            box[board[nx][ny]] += box[i][:]
                            if len(box[board[nx][ny]]) == K:
                                flag = True
                                break
                        board[position[i][0]][position[i][1]] = 0
                        root[i] = 1

    for i in range(N):
        for j in range(N):
            print(board[i][j], end=" ")
        print()
    print(position)
    print(f"box: {box}")
    print("--------------------------------------------")

    if flag:
        break

    count += 1

if count > 1000:
    print(-1)
else:
    print(count)
