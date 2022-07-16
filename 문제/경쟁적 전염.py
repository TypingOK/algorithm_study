import sys

input = sys.stdin.readline
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def scan(m):
    dic = dict()
    for i in range(N):
        for j in range(N):
            if(m[i][j] != 0):
                if(m[i][j] not in dic):
                    dic[m[i][j]] = [[i, j]]
                else:
                    dic[m[i][j]].append([i, j])
    # return dict(sorted(dic.items(), key=lambda x: x[0]))
    return dic


def move(m, key, N, dic):

    for i in range(len(dic[key])):
        x, y = dic[key].pop(0)
        for j in range(4):
            nx = x+dx[j]
            ny = y+dy[j]
            if 0 <= nx < N and 0 <= ny < N and m[nx][ny] == 0:
                m[nx][ny] = key
                dic[key].append([nx, ny])
    return m


N, K = map(int, input().split(" "))


m = []
for i in range(N):
    temp = list(map(int, input().split(" ")))
    m.append(temp)

S, X, Y = map(int, input().split(" "))

dic = scan(m)
keys = sorted(list(dic.keys()))
for i in range(S):
    # print(list(dic.keys()))
    for key in keys:
        m = move(m, key, N, dic)

print(m[X-1][Y-1])
