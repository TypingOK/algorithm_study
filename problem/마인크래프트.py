import sys
input = sys.stdin.readline
N, M, B = map(int, input().split(" "))

# block = [list(map(int, input().split(" "))) for _ in range(N)]
block = []
# avg = 0
for i in range(N):
    temp = list(map(int, input().split(" ")))

    block.append(temp)

answer = sys.maxsize
floor = 0

for t in range(257):
    max_t, min_t = 0, 0

    for i in range(N):
        for j in range(M):

            if(block[i][j] >= t):
                max_t += block[i][j] - t

            else:
                min_t += t - block[i][j]

    if max_t+B >= min_t:
        if min_t + (max_t * 2) <= answer:
            answer = min_t+(max_t * 2)
            floor = t

print(answer, floor)
