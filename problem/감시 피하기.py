from sys import stdin
from copy import deepcopy


def check(x, y, copy_maps):
    for i in range(4):
        index = 1
        while (True):
            nx = x + (index * dx[i])
            ny = y + (index * dy[i])
            if 0 <= nx < N and 0 <= ny < N and (copy_maps[nx][ny] == 'X' or copy_maps[nx][ny] == 'T'):
                index += 1
                continue
            elif 0 <= nx < N and 0 <= ny < N and copy_maps[nx][ny] == "O":
                break
            elif 0 <= nx < N and 0 <= ny < N and copy_maps[nx][ny] == "S":
                return False
            else:
                break
    return True


def perm(idx, teachs_count, copy_map):
    if (idx == 3):
        # print(copy_map)
        flag = True
        for i in teachers:
            if not check(i[0], i[1], copy_map):
                flag = False
        if (flag):
            print("YES")
            exit()
        return
    copy_maps = deepcopy(copy_map)
    for i in range(N):
        for j in range(N):
            if copy_maps[i][j] == "X":
                copy_maps[i][j] = "O"
                perm(idx+1, teachs_count, copy_maps)
                copy_maps[i][j] = "X"


dx = [0, -1, 0, 1]
dy = [-1, 0, 1, 0]

N = int(stdin.readline())
cctv = []
teachers = []
for i in range(N):
    temp = list(stdin.readline().split())
    for j in range(N):
        if temp[j] == 'T':
            teachers.append([i, j])
    cctv.append(temp)

if (len(teachers) == 0):
    print("YES")
    exit()
perm(0, len(teachers), cctv)
print("NO")
