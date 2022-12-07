import sys
input = sys.stdin.readline

N, M = map(int, input().split())

numbers = list(map(int, input().split()))
selected = []


def perm(idx):
    if idx == M:
        answer = " ".join(map(str, selected))
        print(answer)
        return

    for i in range(N):
        selected.append(numbers[i])
        perm(idx+1)
        selected.pop()


numbers.sort()

perm(0)
