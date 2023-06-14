import sys

input = sys.stdin.readline
N = int(input())
M = int(input())

root = [i for i in range(N+1)]


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
    elif ny > nx:
        root[ny] = nx


for i in range(1, N+1):
    temp = list(map(int, input().split()))

    for j in range(1, N+1):
        if i != j and temp[j-1] == 1:
            union(i, j)
visit = [0]
visit += list(map(int, input().split()))
flag = True
for i in range(1, M):
    x = find(visit[i+1])
    y = find(visit[i])
    if x != y:
        print("NO")
        flag = False
        break
if flag:
    print("YES")
