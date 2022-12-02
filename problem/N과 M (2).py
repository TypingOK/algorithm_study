import sys

input = sys.stdin.readline

N, M = map(int, input().split(" "))

numbers = [i+1 for i in range(N)]
visited = [False] * N
select = []


def comb(idx, depth):
    if(idx == M):
        answer = " ".join(map(str, select))
        print(answer)
        return
    if(depth == N):
        return

    select.append(numbers[depth])
    comb(idx+1, depth+1)

    select.pop()
    comb(idx, depth+1)


comb(0, 0)
