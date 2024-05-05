import sys
from collections import OrderedDict
from copy import deepcopy

input = sys.stdin.readline
dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, -1, -1, -1, 0, 1, 1, 1]

answer = 0
fishes = OrderedDict()
shark = []

for i in range(4):
    a1, b1, a2, b2, a3, b3, a4, b4 = map(int, input().split())
    fishes[a1] = [b1-1, i, 0]
    fishes[a2] = [b2-1, i, 1]
    fishes[a3] = [b3-1, i, 2]
    fishes[a4] = [b4-1, i, 3]
    if (i == 0):
        shark = [0, 0, a1, b1-1]
        del fishes[a1]
fishes = OrderedDict(sorted(fishes.items()))


def fish_recur(fishes: OrderedDict, x, y):
    items = fishes.items()

    for key, value in items:
        dir, fish_x, fish_y = map(int, value)
        index = 0
        while index <= 7:
            nx = fish_x + dx[dir]
            ny = fish_y + dy[dir]
            if 0 <= nx < 4 and 0 <= ny < 4 and (nx != x or ny != y):
                flag = False
                for find_key, find_value in items:
                    if find_key == key:
                        continue
                    if nx == find_value[1] and ny == find_value[2]:
                        flag = True
                        fishes[find_key] = [find_value[0], fish_x, fish_y]
                        fishes[key] = [dir, nx, ny]
                        break
                if not flag:
                    fishes[key] = [dir, nx, ny]
                break
            elif nx < 0 or nx >= 4 or ny < 0 or ny >= 4 or (nx == x and ny == y):
                dir = (dir + 1) % 8
                fishes[key] = [dir, fish_x, fish_y]

            index += 1
    return


def recur(shark: list, original_fishes: OrderedDict):
    global answer
    x = shark[0]
    y = shark[1]
    fishes = OrderedDict(sorted(deepcopy(original_fishes).items()))
    fish_recur(fishes, shark[0], shark[1])
    for i in range(1, 4):
        nx = x + (i * dx[shark[3]])
        ny = y + (i * dy[shark[3]])
        if i == 1 and (nx < 0 or nx > 3 or ny < 0 or ny > 3):
            answer = max(answer, shark[2])
            return
        elif 0 <= nx < 4 and 0 <= ny < 4:
            for key, value in fishes.items():
                if value[1] == nx and value[2] == ny:
                    copied_fishes = deepcopy(fishes)
                    del copied_fishes[key]
                    recur([nx, ny, shark[2]+key, value[0]], copied_fishes)
                    break

    answer = max(answer, shark[2])
    return


recur(shark, fishes)
print(answer)
