import sys
input = sys.stdin.readline

N, M = map(int, input().split())


def find(parents, x):
    if x != parents[x]:
        parents[x] = find(parents, parents[x])
    return parents[x]


def union(parents, x, y):
    root_x = find(parents, x)
    root_y = find(parents, y)

    if root_x == root_y:
        return
    elif root_x > root_y:
        parents[x] = root_y
    else:
        parents[y] = parents[x]


parents = [i for i in range(N+1)]

for i in range(N):
    temp = list(map(int, input().split()))
    for j in range(N):
        if temp[j] == 1:
            union(parents, i+1, j+1)


move = list(map(int, input().split()))

flag = False
for i in range(M-1):
    if find(parents, move[i]) != find(parents, move[i+1]):
        flag = True
        break

if flag:
    print("NO")
else:
    print("YES")
