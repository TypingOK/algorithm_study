import sys

input = sys.stdin.readline

N, M = map(int, input().split())

select = []
numbers = [i for i in range(1, N+1)]


def perm(idx):
    if idx == M:
        answer = " ".join(map(str, select))
        print(answer)
        return
    for i in range(N):
        select.append(numbers[i])
        perm(idx+1)
        select.pop()


perm(0)
