import sys

input = sys.stdin.readline

n, m = map(int, input().split())
root = [i for i in range(n)]

answer = 0


def find(x):
    if x != root[x]:
        root[x] = find(root[x])
    return root[x]


def union(x, y):
    nx = find(x)
    ny = find(y)

    if nx == ny:
        return True

    elif nx > ny:
        root[nx] = ny
    elif ny > nx:
        root[ny] = nx
    return False


for i in range(1, m+1):
    a, b = map(int, input().split())
    result = union(a, b)

    if result and answer == 0:
        answer = i

print(answer)
