import sys
from copy import deepcopy
input = sys.stdin.readline

# f = open("새파일.txt", 'w')

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

N = int(input())
graph = [list(map(int, input().split())) for _ in range(N)]
max_block = -sys.maxsize


def move(dir, g, comb, x, y):
    # f.write(str(x)+" "+str(y)+"\n")
    if dir == 0:
        for i in range(N-1, x, -1):
            if g[i][y] == 0:
                g[i][y] = g[x][y]
                g[x][y] = 0
                x = i
                break
        if x+1 < N and g[x+1][y] == g[x][y] and not comb[x+1][y]:
            comb[x+1][y] = True
            g[x+1][y] = g[x][y] + g[x+1][y]
            g[x][y] = 0
    elif dir == 2:
        for i in range(0, x):
            if g[i][y] == 0:
                g[i][y] = g[x][y]
                g[x][y] = 0
                x = i
                break
        if x-1 >= 0 and g[x-1][y] == g[x][y] and not comb[x-1][y]:
            comb[x-1][y] = True
            g[x-1][y] = g[x][y] + g[x-1][y]
            g[x][y] = 0

    elif dir == 1:
        for i in range(N-1, y, -1):
            if g[x][i] == 0:
                g[x][i] = g[x][y]
                g[x][y] = 0
                y = i
                break
        if y+1 < N and g[x][y+1] == g[x][y] and not comb[x][y+1]:
            comb[x][y+1] = True
            g[x][y+1] = g[x][y] + g[x][y+1]
            g[x][y] = 0
    else:
        for i in range(0, y):
            if g[x][i] == 0:
                g[x][i] = g[x][y]
                g[x][y] = 0
                y = i
                break
        if y-1 >= 0 and g[x][y-1] == g[x][y] and not comb[x][y-1]:
            comb[x][y-1] = True
            g[x][y-1] = g[x][y] + g[x][y-1]
            g[x][y] = 0
    return g


def re(depth: int, g: list):
    global max_block
    if depth == 5:
        for i in range(N):
            for j in range(N):
                max_block = max(g[i][j], max_block)
        return
    # f.write(str(depth) + " ----------------------------------------- \n")
    # for i in range(N):
    #     for j in range(N):
    #         f.write(str(g[i][j])+" ")
    #     f.write("\n")
    # f.write("\n")
    comb = [[False for _ in range(N)] for _ in range(N)]

    # 위에서 아래로
    copy_g = deepcopy(g)
    for i in range(N):
        for j in range(N-1, -1, -1):
            if copy_g[j][i] != 0:
                copy_g = move(0, copy_g, comb, j, i)
    re(depth+1, copy_g)

    # 왼쪽에서 오른쪽으로
    comb = [[False for _ in range(N)] for _ in range(N)]
    copy_g = deepcopy(g)
    for i in range(N):
        for j in range(N-1, -1, -1):
            if copy_g[i][j] != 0:
                copy_g = move(1, copy_g, comb, i, j)
    re(depth+1, copy_g)

    # 아래에서 위로
    comb = [[False for _ in range(N)] for _ in range(N)]
    copy_g = deepcopy(g)
    for i in range(N):
        for j in range(N):
            if copy_g[j][i] != 0:
                copy_g = move(2, copy_g, comb, j, i)
    re(depth+1, copy_g)

    # 오른쪽에서 왼쪽으로
    comb = [[False for _ in range(N)] for _ in range(N)]
    copy_g = deepcopy(g)
    for i in range(N):
        for j in range(N):
            if copy_g[i][j] != 0:
                copy_g = move(3, copy_g, comb, i, j)
    re(depth+1, copy_g)


re(0, graph)

print(max_block)


# f.close()
