import sys
input = sys.stdin.readline

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def scan(R, C):
    bomb = []
    for i in range(R):
        for j in range(C):
            if map[i][j] == 'O':
                bomb.append([i, j])
    return bomb


def boom(bomb):
    for i, j in bomb:
        map[i][j] = '.'
        for k in range(4):
            nx = i+dx[k]
            ny = j+dy[k]

            if nx >= 0 and nx < R and ny >= 0 and ny < C:
                map[nx][ny] = '.'


def full(R, C):
    for i in range(R):
        for j in range(C):
            map[i][j] = 'O'


R, C, N = map(int, input().split(" "))

map = []

for i in range(R):

    temp = list(input().rstrip("\n"))
    map.append(temp)

index = 1
bomb = scan(R, C)

while(index <= N):
    if(index == N):
        break
    full(R, C)
    index += 1
    if(index == N):
        break
    boom(bomb)
    index += 1
    if(index == N):
        break
    bomb = scan(R, C)
#     for i in range(R):
#         for j in range(C):

#             print(map[i][j], end="")
#         print()
#     print("-------------------------------")
# print()
# print("------------------------------end")
for i in range(R):
    for j in range(C):

        print(map[i][j], end="")
    print()
