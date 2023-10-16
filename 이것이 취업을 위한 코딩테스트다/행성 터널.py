import sys
sys.setrecursionlimit(1000000)
input = sys.stdin.readline

N = int(input())

x = []
y = []
z = []
for i in range(N):
    temp = list(map(int, input().split()))
    x.append((temp[0], i))
    y.append((temp[1], i))
    z.append((temp[2], i))

x.sort()
y.sort()
z.sort()

edges = []
for i in range(N-1):
    edges.append((x[i+1][0]-x[i][0], x[i][1], x[i+1][1]))
    edges.append((y[i+1][0]-y[i][0], y[i][1], y[i+1][1]))
    edges.append((z[i+1][0]-z[i][0], z[i][1], z[i+1][1]))

edges.sort()


root = [i for i in range(N)]


def find(root, x):
    if root[x] != x:
        root[x] = find(root, root[x])
    return root[x]


def union(root, x, y):
    a = find(root, x)
    b = find(root, y)

    if a == b:
        return False
    elif a > b:
        root[a] = b
    else:
        root[b] = a
    return True


answer = 0
for k, x, y in edges:
    if union(root, x, y):
        answer += k

print(answer)
