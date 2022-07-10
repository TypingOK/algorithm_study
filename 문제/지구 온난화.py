import sys

input = sys.stdin.readline

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


N, M = map(int, input().split(" "))


def check(x, y):
    count = 0
    for i in range(4):
        nx = x+dx[i]
        ny = y+dy[i]
        if nx < N and ny < M and nx >= 0 and ny >= 0:
            if map[nx][ny] == '.':
                count += 1
        else:
            count += 1
    return count


map = []

for i in range(N):
    temp = list(input().rstrip("\n"))
    map.append(temp)

remove = []
for i in range(N):
    for j in range(M):
        if(map[i][j] == 'X' and check(i, j) >= 3):
            remove.append([i, j])

for i, j in remove:
    map[i][j] = '.'

minH = 10
maxH = 0
minW = 10
maxW = 0
for i in range(N):
    for j in range(M):
        if(map[i][j] == 'X'):
            minH = min(i, minH)
            maxH = max(i, maxH)
            minW = min(j, minW)
            maxW = max(j, maxW)

for i in range(minH, maxH+1):
    for j in range(minW, maxW+1):
        print(map[i][j], end="")
    print()
