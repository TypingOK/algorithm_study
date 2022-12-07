import sys
input = sys.stdin.readline

N, M = map(int, input().split())

visited = [False] * N

numbers = list(map(int, input().split()))
selected = []


def comb(idx, depth):
    if(idx == M):
        answer = " ".join(map(str, selected))
        print(answer)
        return
    if(depth == N):
        return

    visited[depth] = True
    selected.append(numbers[depth])
    comb(idx+1, depth+1)

    visited[depth] = False
    selected.pop()
    comb(idx, depth+1)

numbers.sort()
comb(0, 0)
