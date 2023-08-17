import sys
input = sys.stdin.readline


def find(parents, x):
    if parents[x] != x:
        return find(parents, parents[x])
    else:
        return parents[x]


def union(x, y, parents):
    root_x = find(parents, x)
    root_y = find(parents, y)

    if root_x > root_y:
        parents[x] = root_y
    else:
        parents[y] = root_x


N, M = map(int, input().split())
parents = [i for i in range(0, N+1)]

for i in range(M):
    o, a, b = map(int, input().split())
    if (o == 0):
        union(a, b, parents)
    else:
        if (find(parents, a) == find(parents, b)):
            print("YES")
        else:
            print("NO")
