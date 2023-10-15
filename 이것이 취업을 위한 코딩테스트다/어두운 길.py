import sys
input = sys.stdin.readline

N, M = map(int, input().split())
road = []

for i in range(M):
    temp = list(map(int, input().split()))
    road.append(temp)

road.sort(key=lambda x: x[:][2])


def find(root, x):
    if root[x] != x:
        root[x] = find(root, root[x])
    return root[x]


def uinon(root, x, y):
    a = find(root, x)
    b = find(root, y)
    if a > b:
        root[a] = b
    else:
        root[b] = a


root = [i for i in range(N)]
count = 0
result = 0
for a, b, c in road:
    result += c
    if find(root, a) != find(root, b):
        uinon(root, a, b)
        count += c


print(result - count)
