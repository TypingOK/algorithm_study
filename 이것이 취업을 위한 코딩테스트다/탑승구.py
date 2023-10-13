import sys
input = sys.stdin.readline

G = int(input())
P = int(input())

root = [i for i in range(G+1)]
exit = []
for i in range(P):
    exit.append(int(input()))


def find(parents, x):
    if parents[x] != x:
        parents[x] = find(parents, parents[x])
    return parents[x]


def union(parents, x, y):
    a = find(parents, x)
    b = find(parents, y)

    if a < b:
        parents[b] = a
    else:
        parents[a] = b


count = 0
for temp in exit:
    data = find(root, temp)
    if data != 0:
        union(root, data, data-1)
        count += 1
    else:
        break

print(count)
