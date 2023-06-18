import sys
input = sys.stdin.readline

N, M, k = map(int, input().split())

A = [0] + list(map(int, input().split()))

answer = 0
root = [i for i in range(N+1)]


def find(x):
    if x != root[x]:
        root[x] = find(root[x])
    return root[x]


def union(x, y):
    nx = find(x)
    ny = find(y)

    if A[nx] > A[ny]:
        root[nx] = ny
    else:
        root[ny] = nx


for i in range(M):
    a, b = map(int, input().split())
    union(a, b)

f = set()

for i in range(1, N+1):
    if find(i) not in f:
        answer += A[root[i]]
        f.add(root[i])

if answer > k:
    print("Oh no")
else:
    print(answer)
