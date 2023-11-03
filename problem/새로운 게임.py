import sys

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
    for i in range(1, K+1):
        if root[i] == 0:
            nx = position[i][0] + dx[di[i]]
            ny = position[i][1] + dy[di[i]]

            if 0 <= nx < N and 0 <= ny < N and graph[nx][ny] != 2:
                if board[nx][ny] == 0:
                    board[nx][ny] = i

                    board[position[i][0]][position[i][1]] = 0
                    position[i] = (nx, ny)
                    if graph[nx][ny] == 1:
                        box[i].reverse()
                        temp = box[i][0]
                        if temp != i:
                            board[nx][ny] = temp
                            root[temp] = 0
                            root[box[i][-1]] = 1
                            box[temp] = box[i]
                            position[temp] = (nx, ny)
                        if len(box[i]) >= 4:
                            flag = True
                            break
                elif board[nx][ny] != 0:
                    if graph[nx][ny] == 1:
                        box[board[nx][ny]] += box[i][::-1]
                        if len(box[board[nx][ny]]) >= 4:
                            flag = True
                            break
                    else:
                        box[board[nx][ny]] += box[i][:]
                        if len(box[board[nx][ny]]) >= 4:
                            flag = True
                            break
                    board[position[i][0]][position[i][1]] = 0
                    root[i] = 1

            else:
                if di[i] == 0:
                    di[i] = 1
                elif di[i] == 1:
                    di[i] = 0
                elif di[i] == 2:
                    di[i] = 3
                elif di[i] == 3:
                    di[i] = 2
                nx = position[i][0] + dx[di[i]]
                ny = position[i][1] + dy[di[i]]
                if 0 <= nx < N and 0 <= ny < N:
                    if graph[nx][ny] != 2:
                        if board[nx][ny] == 0:
                            board[nx][ny] = i
                            board[position[i][0]][position[i][1]] = 0
                            position[i] = (nx, ny)
                            if graph[nx][ny] == 1:
                                box[i].reverse()
                                temp = box[i][0]
                                if temp != i:
                                    board[nx][ny] = temp
                                    root[temp] = 0
                                    root[box[i][-1]] = 1
                                    box[temp] = box[i]
                                    position[temp] = (nx, ny)

                                if len(box[i]) >= 4:
                                    flag = True
                                    break

                        elif board[nx][ny] != 0:

                            if graph[nx][ny] == 1:
                                box[board[nx][ny]] += box[i][::-1]
                                if len(box[board[nx][ny]]) >= 4:
                                    flag = True
                                    break
                            else:
                                box[board[nx][ny]] += box[i][:]
                                if len(box[board[nx][ny]]) >= 4:
                                    flag = True
                                    break
                            board[position[i][0]][position[i][1]] = 0
                            root[i] = 1
    count += 1

    if flag:
        break
if count > 1000:
    print(-1)
else:
    print(count)
