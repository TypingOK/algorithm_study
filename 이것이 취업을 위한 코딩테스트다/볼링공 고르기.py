import sys
input = sys.stdin.readline

N, M = map(int, input().split())
balls = list(map(int, input().split()))


def comb(depth, index, balls, N, select, visited):
    if depth == 2:
        select.sort()
        visited.add((select[0], select[1]))
        return
    if index == N:
        return

    if index == 0 and len(select) == 0:
        select.append(0)
        comb(depth+1, index, balls, N, select, visited)
        select.pop()
    for i in range(index+1, N):
        if balls[index] != balls[i]:
            select.append(i)
            comb(depth+1, i, balls, N, select, visited)
            select.pop()


visited = set()
comb(0, 0, balls, N, [], visited)
print(len(visited))
