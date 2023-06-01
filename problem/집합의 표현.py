import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

N, M = map(int, input().split())

root = [i for i in range(N+1)]
rank = [0 for _ in range(N+1)]


def find(x):
    if root[x] == x:
        return x
    else:
        root[x] = find(root[x])
        return root[x]


def union(x, y):
    nx = find(x)
    ny = find(y)
    if nx == ny:
        return

    if rank[nx] < rank[ny]:
        root[nx] = ny
    else:

        root[ny] = nx
        if rank[nx] == rank[ny]:
            rank[nx] += 1


for i in range(M):
    a, b, c = map(int, input().split())
    if a == 0:
        union(b, c)
    elif a == 1:
        result_b = find(b)
        result_c = find(c)
        if result_b == result_c:
            print("YES")
        else:
            print("NO")
