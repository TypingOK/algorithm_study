import sys

input = sys.stdin.readline

N, M = map(int, input().split(" "))

numbers = [i+1 for i in range(N)]
visited = [False] * N
select = []


def comb(idx, start):
    if(idx == M):
        answer = " ".join(map(str, select))
        print(answer)
        return
    # if(depth == N):
    #     return

    # select.append(numbers[depth])
    # comb(idx+1, depth+1)

    # select.pop()
    # comb(idx, depth+1)
    for i in range(start, N):
        visited[i] = True
        select.append(numbers[i])
        comb(idx+1, i+1)
        visited[i] = False
        select.pop()


comb(0, 0)
