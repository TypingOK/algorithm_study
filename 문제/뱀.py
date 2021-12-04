N = int(input())
K = int(input())
board = [[0] * (N+1) for _ in range(N+1)]
for i in range(K):
    a, b = map(int, input().split())
    board[a][b] = 1

L = int(input())
move = []
for i in range(L):
    x, c = input().split()
    move.append((int(x), c))

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]


def turn(direction, c):
    if c == "L":
        direction = (direction-1) % 4
    else:
        direction = (direction+1) % 4
    return direction


def simulation():
    x, y = 1, 1
    q = [(x, y)]
    board[x][y] = 2
    direction = 0
    time = 0
    index = 0
    while True:
        nx = x+dx[direction]
        ny = y+dy[direction]

        if 1 <= nx and nx <= N and 1 <= ny and ny <= N and board[nx][ny] != 2:
            if board[nx][ny] == 1:
                board[nx][ny] = 2
                q.append((nx, ny))
            if board[nx][ny] == 0:
                board[nx][ny] = 2
                q.append((nx, ny))
                px, py = q.pop(0)
                board[px][py] = 0
        else:
            time += 1
            break
        x, y = nx, ny
        time += 1
        if index < L and time == move[index][0]:
            direction = turn(direction, move[index][1])
            index += 1
    return time


print(simulation())
