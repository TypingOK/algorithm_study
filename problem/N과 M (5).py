import sys
input = sys.stdin.readline

N, M = map(int, input().split())

numbers = list(map(int, input().split()))
visited = [False] * N
select = []


def perm(idx):
    if idx == M:
        if len(select) == M:
            answer = " ".join(map(str, select))
            print(answer)
        return

    for i in range(N):
        if not visited[i]:
            visited[i] = True
            select.append(numbers[i])
            perm(idx+1)
            select.pop()
            visited[i] = False


numbers.sort()
perm(0)
