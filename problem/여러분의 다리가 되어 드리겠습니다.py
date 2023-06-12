import sys

input = sys.stdin.readline

N = int(input())


def find(x):
    if x != root[x]:
        root[x] = find(root[x])
    return root[x]


def union(x, y):
    nx = find(x)
    ny = find(y)

    if nx == ny:
        return
    elif nx > ny:
        root[nx] = ny
    elif nx < ny:
        root[ny] = nx


if N == 2:
    print("1 2")

else:
    bri = []
    root = [i for i in range(N+1)]
    for _ in range(N-2):
        a, b = map(int, input().split())
        union(a, b)
        bri.append([a, b])

    for i in range(1, N):
        nx = find(i)
        ny = find(i+1)

        if nx != ny:
            print(nx, ny)
            break
