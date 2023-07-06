import sys
input = sys.stdin.readline

N = int(input())

answer = 0


def dfs(board, x, y, d):

    if x == N-1 and y == N-1:
        return 1
    count = 0
    if d == 0 or d == 2:
        nx = x + 0
        ny = y + 1
        if 0 <= nx < N and 0 <= ny < N and board[nx][ny] != 1:
            count += dfs(board, nx, ny, 0)

    if d == 1 or d == 2:
        nx = x + 1
        ny = y + 0
        if 0 <= nx < N and 0 <= ny < N and board[nx][ny] != 1:
            count += dfs(board, nx, ny, 1)
    nx2 = x + 1
    ny2 = y + 1
    if 0 <= nx2 < N and 0 <= ny2 < N and board[nx2-1][ny2] != 1 and board[nx2][ny2 - 1] != 1 and board[nx2][ny2] != 1:
        count += dfs(board, nx2, ny2, 2)
    return count


board = []
for i in range(N):
    temp = list(map(int, input().split()))
    board.append(temp)

board[0][0] = 1
board[0][1] = 1

# 0 == 가로, 1== 세로, 2 == 대각선
if board[N-1][N-1] == 1:
    print(0)
else:
    answer = dfs(board, 0, 1, 0)
    print(answer)
