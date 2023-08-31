import sys

input = sys.stdin.readline

N, M = map(int, input().split())
chickens = []
houses = []

for i in range(N):
    temp = list(map(int, input().split()))
    for j in range(N):
        if temp[j] == 1:
            houses.append((i, j))
        elif temp[j] == 2:
            chickens.append((i, j))

answer = sys.maxsize


def comb(depth, index, select, M, len_chicken, chickens):
    global answer
    if len(select) == M:
        count = 0
        for j in houses:
            local_min = sys.maxsize
            for i in select:
                local_min = min(local_min, abs(j[0]-i[0])+abs(j[1]-i[1]))
            count += local_min
        answer = min(count, answer)
        return

    for i in range(index, len_chicken):
        select.append(chickens[i])
        comb(depth+1, i+1, select, M, len_chicken, chickens)
        select.pop()


comb(0, 0, [], M, len(chickens), chickens)
print(answer)
