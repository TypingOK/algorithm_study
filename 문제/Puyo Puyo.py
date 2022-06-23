import sys

input = sys.stdin.readline

dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]

result = []
for i in range(12):
    temp = list(input())
    temp.pop()
    result.append(temp)
    # print(result[i])


def BFS(x, y, c):
    count = 1
    q = []
    q.append([x, y])
    visit = [[False for _ in range(6)] for _ in range(12)]

    visit[x][y] = True
    while(q):
        temp = q.pop()

        for i in range(4):
            nx = dx[i]+temp[0]
            ny = dy[i]+temp[1]

            if 0 <= nx < 12 and 0 <= ny < 6 and not visit[nx][ny] and result[nx][ny] == c:
                # print("result : ", result[nx][ny])
                visit[nx][ny] = True
                q.append([nx, ny])
                count += 1
    if count >= 4:
        # print("---------visit----------------")
        for r in range(12):
            for c in range(6):
                # print(visit[r][c], end=" ")
                if(visit[r][c]):
                    result[r][c] = '.'
            # print()
        return True

    return False


def down():
    # print()
    # for r in range(12):
    #     for c in range(6):

    #         print(result[r][c], end="")
    #     print()
    # print()
    for i in range(6):
        count = 0
        for j in range(11, -1, -1):
            if(result[j][i] != '.'):
                count += 1
        # print(count)
        if(count > 0):
            while(True):
                flag = False
                for j in range(11, 11-count, -1):
                    # if(i == 4):
                    # print(result[j][i])
                    if(result[j][i] == '.'):
                        flag = True
                        break
                # print(flag)
                if(flag):
                    for k in range(11, 0, -1):
                        if(result[k][i] == '.'):
                            result[k][i] = result[k-1][i]
                            result[k-1][i] = '.'
                else:
                    break

    return


def check():
    flag = False
    for i in range(12):
        for j in range(6):
            if(result[i][j] != '.'):

                if(BFS(i, j, result[i][j])):
                    flag = True
    # print("flag "+str(flag))
    if(flag):
        down()

    return flag


# visit = [[False for _ in range(6)] for _ in range(12)]
count = 0
while(True):
    if(not check()):
        break
    else:
        count += 1
print(count)
