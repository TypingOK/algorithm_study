import sys
input = sys.stdin.readline

T = int(input())

d = [[[0, 0], [1, 0], [0, 1]],
     [[0, 0], [0, 1], [1, 1]],
     [[0, 0], [1, 0], [1, 1]],
     [[0, 0], [1, 0], [1, -1]]]


def cover(di, x, y, number, H, W, board):
    flag = True
    for i in range(3):
        nx = x + d[di][i][0]
        ny = y + d[di][i][1]

        if 0 > nx or nx >= H or 0 > ny or ny >= W:
            flag = False
        elif board[nx][ny] + number > 1:
            board[nx][ny] += number
            flag = False
        else:
            board[nx][ny] += number
    return flag


def first(board, H, W):
    x, y = -1, -1
    for i in range(H):
        for j in range(W):
            if board[i][j] == 0:
                x = i
                y = j
                break
        if y != -1:
            break

    # 탈출 조건
    if x == -1:
        return 1
    answer = 0

    for i in range(4):
        if cover(i, x, y, 1, H, W, board):

            answer += first(board, H, W)
            # print(board)
        cover(i, x, y, -1, H, W, board)

    return answer


for _ in range(T):
    H, W = map(int, input().split())
    board = []
    count = H * W

    for i in range(H):
        temp = input().rstrip("\n")
        board_temp = []
        for j in temp:
            if j == "#":
                count -= 1
                board_temp.append(1)
            elif j == ".":
                board_temp.append(0)
        board.append(board_temp)
    print(board)
    if count % 3 != 0:
        print(0)
    else:
        answer = first(board, H, W)
        print(answer)
