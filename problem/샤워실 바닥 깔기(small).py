import sys

def solution(x, y, k, area):
    global num

    if k <= 1:
        count = 3
        if area == 0 or area == 4:
            for i in range(x, x+2):
                for j in range(y, y+2):
                    if not board[i][j] and count:
                        board[i][j] = num
                        count -= 1
        elif area == 1:
            for i in range(x, x+2):
                for j in range(y+1, y-1, -1):
                    if not board[i][j] and count:
                        board[i][j] = num
                        count -= 1
        elif area == 2:
            for i in range(x+1, x-1, -1):
                for j in range(y, y+2):
                    if not board[i][j] and count:
                        board[i][j] = num
                        count -= 1
        else:
            for i in range(x+1, x-1, -1):
                for j in range(y+1, y-1, -1):
                    if not board[i][j] and count:
                        board[i][j] = num
                        count -= 1
        num += 1
        return

    solution(x, y, k-1, 0)
    solution(x, y + 2 ** (k-1), k-1, 1)
    solution(x + 2 ** (k-1), y, k-1, 2)
    solution(x + 2 ** (k-1), y + 2 ** (k-1), k-1, 3)
    solution(x + 2 ** k//4, y + 2 ** k//4, k-1, 4)


input = sys.stdin.readline

K = int(input())
position = list(map(int, input().split()))

t = 2 ** K

board = [[0] * t for _ in range(t)]
board[t - position[1]][position[0]-1] = -1

num = 1

solution(0, 0, K, 0)

for x in board:
    for y in x:
        print(y, end=" ")
    print()
