import sys
input = sys.stdin.readline

imino = [[[0, 0], [1, 0], [2, 0], [3, 0]], [[0, 0], [0, 1], [0, 2], [0, 3]]]
omino = [[0, 0], [0, 1], [1, 0], [1, 1]]
lmino = [[[0, 0], [1, 0], [2, 0], [2, 1]], [[0, 0], [0, 1], [0, 2], [1, 0]], [
    [0, 0], [0, 1], [1, 1], [2, 1]], [[0, 0], [0, 1], [-1, 2], [0, 2]]]
rmino = [[[0, 0], [0, 1], [-1, 1], [-2, 1]], [[0, 0], [1, 0], [1, 1], [1, 2]],
         [[0, 0], [0, 1], [1, 0], [2, 0]], [[0, 0], [0, 1], [0, 2], [1, 2]]]
zmino = [[[0, 0], [1, 0], [1, 1], [2, 1]], [[0, 0], [0, 1], [-1, 1], [-1, 2]],
         [[0, 0], [0, 1], [1, 1], [1, 2]], [[0, 0], [-1, 0], [-1, 1], [-2, 1]]]
tmino = [[[0, 0], [0, 1], [0, 2], [1, 1]], [[0, 0], [0, 1], [-1, 1], [1, 1]],
         [[0, 0], [0, 1], [-1, 1], [0, 2]], [[0, 0], [-1, 0], [1, 0], [0, 1]]]

N, M = map(int, input().split(" "))


def ical(x, y):
    maxNum = 0
    for i in imino:
        count = 0
        for k in i:
            nx = x+k[0]
            ny = y+k[1]

            if 0 <= nx < N and 0 <= ny < M:
                count += arr[nx][ny]
            else:
                count = 0
                break
        maxNum = max(count, maxNum)
    return maxNum


def ocal(x, y):
    maxNum = 0
    for i in range(4):
        nx = x+omino[i][0]
        ny = y+omino[i][1]
        if 0 <= nx < N and 0 <= ny < M:
            maxNum += arr[nx][ny]
        else:
            return 0
    return maxNum


def lcal(x, y):
    maxNum = 0
    for i in lmino:
        count = 0
        for k in i:
            nx = x+k[0]
            ny = y+k[1]
            if 0 <= nx < N and 0 <= ny < M:
                count += arr[nx][ny]
            else:
                count = 0
                break
        maxNum = max(count, maxNum)
    return maxNum


def rcal(x, y):
    maxNum = 0
    for i in rmino:
        count = 0
        for k in i:
            nx = x+k[0]
            ny = y+k[1]
            if 0 <= nx < N and 0 <= ny < M:
                count += arr[nx][ny]
            else:
                count = 0
                break
        maxNum = max(count, maxNum)
    return maxNum


def tcal(x, y):
    maxNum = 0
    for i in tmino:
        count = 0
        for k in i:
            nx = x+k[0]
            ny = y+k[1]
            if 0 <= nx < N and 0 <= ny < M:
                count += arr[nx][ny]
            else:
                break
        maxNum = max(count, maxNum)
    return maxNum


def zcal(x, y):
    maxNum = 0
    for i in zmino:
        count = 0
        for k in i:
            nx = x+k[0]
            ny = y+k[1]
            if 0 <= nx < N and 0 <= ny < M:
                count += arr[nx][ny]
            else:
                break
        maxNum = max(count, maxNum)
    return maxNum


arr = []

for i in range(N):
    arr.append(list(map(int, input().split(" "))))

answer = 0
for i in range(N):
    for j in range(M):
        answer = max(ical(i, j), answer)
        answer = max(ocal(i, j), answer)
        answer = max(lcal(i, j), answer)
        answer = max(rcal(i, j), answer)
        answer = max(tcal(i, j), answer)
        answer = max(zcal(i, j), answer)
print(answer)
