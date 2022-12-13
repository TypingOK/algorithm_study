import sys

input = sys.stdin.readline

N = int(input())
M = int(input())

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

slug = [[0 for i in range(N)] for i in range(N)]
x = 0
y = 0
answer_x = 0
answer_y = 0
count = (N*N)-1
slug[0][0] = N*N
d = 0
while(count > 0):
    d %= 4
    nx = x+dx[d]
    ny = y+dy[d]
    if(0 <= nx < N and 0 <= ny < N and slug[nx][ny] == 0):

        x = nx
        y = ny
        slug[nx][ny] = count
        if(count == M):
            answer_x = nx
            answer_y = ny
        count -= 1
    else:
        d += 1
for i in range(N):
    answer = " ".join(map(str, slug[i]))
    print(answer)
print(answer_x+1, answer_y+1)
