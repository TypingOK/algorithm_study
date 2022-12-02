import sys
sys.setrecursionlimit(1000000)

input = sys.stdin.readline

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

ori = []

N, M = map(int, input().split())

V = 0
O = 0
for i in range(N):
    temp = list(input())
    ori.append(temp[:-1])
    for j in range(M):
        if temp[j] == 'v':
            V += 1
        elif temp[j] == 'o':
            O += 1

visited = [[False for _ in range(M)] for _ in range(N)]

a = 0
b = 0


def DFS(x, y):
    global a
    global b
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if(0 <= nx < N and 0 <= ny < M and not visited[nx][ny] and ori[nx][ny] != '#'):
            visited[nx][ny] = True
            if ori[nx][ny] == 'v':
                a += 1
            elif ori[nx][ny] == 'o':
                b += 1
            DFS(nx, ny)


for i in range(N):
    for j in range(M):
        if(not visited[i][j] and ori[i][j] != '#'):
            visited[i][j] = True
            a = 0
            b = 0
            if(ori[i][j] == 'v'):
                a += 1
            elif(ori[i][j] == 'o'):
                b += 1
            DFS(i, j)
            if(a >= b):
                O -= b
            elif(a < b):
                V -= a

print(O, V)
